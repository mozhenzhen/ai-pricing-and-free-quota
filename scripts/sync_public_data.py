#!/usr/bin/env python3
"""
Sync public, anonymized benchmark & free-quota Markdown tables from https://mozhenzhen.com.

Security & Scope:
- Reads ONLY publicly accessible, unauthenticated endpoints on https://mozhenzhen.com.
- Uses zero API keys, zero private credentials, and zero internal endpoints.
- Preserves data timestamps, currency units, source attributions, and canonical backlinks.
"""

from __future__ import annotations

import datetime as dt
import gzip
import json
import pathlib
import urllib.request
from collections import defaultdict
from typing import Any

BASE_URL = "https://mozhenzhen.com"
UA = "Mozilla/5.0 (compatible; MoZhenZhenOpenDataSync/1.0; +https://mozhenzhen.com)"
ROOT = pathlib.Path(__file__).resolve().parent.parent
DATA_DIR = ROOT / "data"
CST = dt.timezone(dt.timedelta(hours=8))


def fetch_json(path: str) -> Any:
    req = urllib.request.Request(
        f"{BASE_URL}{path}",
        headers={"User-Agent": UA, "Accept-Encoding": "gzip"},
    )
    with urllib.request.urlopen(req, timeout=30) as resp:
        raw = resp.read()
        if raw[:2] == b"\x1f\x8b" or "gzip" in (resp.headers.get("Content-Encoding") or "").lower():
            raw = gzip.decompress(raw)
        return json.loads(raw.decode("utf-8"))


def esc(text: Any) -> str:
    return str(text or "").replace("|", "\\|").replace("\n", " ").strip()


def fmt_cny(val: float | None) -> str:
    if val is None:
        return "—"
    if val >= 1000:
        return f"¥{val:,.0f}"
    if val >= 100:
        return f"¥{val:.0f}"
    return f"¥{val:.1f}".rstrip("0").rstrip(".")


def fmt_orig_price(currency: str, amount: Any) -> str:
    if amount is None:
        return "—"
    c = str(currency or "").upper()
    v = float(amount)
    num = f"{v:,.0f}" if v == int(v) else f"{v:,.2f}".rstrip("0").rstrip(".")
    if c == "USD":
        return f"${num}"
    if c in ("CNY", "RMB"):
        return f"¥{num}"
    return f"{c} {num}"


def src_label(model: dict[str, Any]) -> str:
    src = model.get("src")
    if src == "official":
        return "Official Formula / 官方规则"
    if src == "measured":
        return "Tested by MoZhenZhen / 实测"
    site = model.get("site") or "community"
    conf = model.get("conf") or ""
    return f"Open Data ({site}{f'·{conf}' if conf else ''})"


def is_expired(iso_str: str | None, now: dt.datetime) -> bool:
    if not iso_str:
        return False
    try:
        parsed = dt.datetime.fromisoformat(iso_str.replace("Z", "+00:00"))
        if parsed.tzinfo is None:
            parsed = parsed.replace(tzinfo=CST)
        return parsed <= now
    except ValueError:
        return False


def build_coding_plans_md(plans_data: dict[str, Any], now_str: str) -> str:
    observed = str(plans_data.get("observed_at") or now_str)[:16].replace("T", " ")
    usd_cny = plans_data.get("usd_cny")
    raw_plans = plans_data.get("plans") or []

    rows_cn = []
    rows_global = []

    for p in raw_plans:
        if p.get("paused") or p.get("team") or not p.get("has_data"):
            continue
        price_cny = p.get("price_cny")
        if not price_cny or float(price_cny) <= 0:
            continue
        ms = [m for m in (p.get("models") or []) if m.get("yis") and len(m["yis"]) >= 3 and m["yis"][2]]
        if not ms:
            continue
        top = sorted(ms, key=lambda x: ((x.get("aa") or 0), (x["yis"][2] or 0)), reverse=True)[0]
        yi95 = float(top["yis"][2])
        apis = top.get("apis") or []
        api_m95 = apis[2] if len(apis) >= 3 and apis[2] else top.get("api_per_m")
        eq_cny = (yi95 * 100.0 * float(api_m95)) if api_m95 else None
        mult = (eq_cny / float(price_cny)) if eq_cny else None

        notes = []
        if p.get("nocache") or top.get("nocache"):
            notes.append("Cache counts full / 缓存不省钱")
        if p.get("night") or top.get("night"):
            notes.append("Night discount / 夜间折")
        if p.get("promo"):
            notes.append("Promo / 限时价")

        entry = {
            "provider": p.get("provider") or "",
            "tier": p.get("tier") or "",
            "slug": p.get("slug") or "",
            "price_cny": float(price_cny),
            "orig": fmt_orig_price(p.get("currency", ""), p.get("price")),
            "top_model": top.get("name") or "",
            "yi95": yi95,
            "eq_cny": eq_cny,
            "mult": mult,
            "src": src_label(top),
            "notes": "; ".join(notes) or "—",
        }
        if p.get("domestic"):
            rows_cn.append(entry)
        else:
            rows_global.append(entry)

    rows_cn.sort(key=lambda x: (x["provider"], x["price_cny"]))
    rows_global.sort(key=lambda x: (x["provider"], x["price_cny"]))

    def render_table(rows: list[dict[str, Any]]) -> list[str]:
        out = [
            "| Provider & Tier / 渠道与档位 | Monthly Fee / 月费 | Top Included Model / 主力模型 | Est. Monthly Quota (95% Cache) / 95%缓存月可用 | Equiv. Official API Value / 等值官价 | Value Multiple / 折算倍数 | Source / 数据来源 | Notes / 关键提示 | Live Page / 实时页 |",
            "| --- | --- | --- | --- | --- | --- | --- | --- | --- |",
        ]
        for r in rows:
            fee = r["orig"] if r["orig"].startswith("¥") else f"{fmt_cny(r['price_cny'])} ({r['orig']})"
            yi_str = f"{r['yi95']:.2f}亿 ({r['yi95'] * 100:.0f}M)"
            eq_str = fmt_cny(r["eq_cny"]) if r["eq_cny"] is not None else "—"
            mult_str = f"**{r['mult']:.1f}x**" if r["mult"] is not None else "—"
            live_url = f"{BASE_URL}/plans/{r['slug']}"
            md_url = f"{BASE_URL}/plans/{r['slug']}.md"
            out.append(
                f"| **{esc(r['provider'])}** · {esc(r['tier'])} | {esc(fee)} | {esc(r['top_model'])} | {yi_str} | {eq_str} | {mult_str} | {esc(r['src'])} | {esc(r['notes'])} | [Detail]({live_url}) · [.md]({md_url}) |"
            )
        return out

    lines = [
        "# AI Coding Plans & Token Plans Benchmark (95% Cache Scenario)",
        "# 主流 AI 编程套餐与 Token Plan 横向对比表（95% 缓存场景）",
        "",
        f"> **Updated / 更新时间**: `{observed} (UTC+8)` · **FX / 参考汇率**: `1 USD = {usd_cny:.4f} CNY`  ",
        f"> **Live Interactive Calculator / 实时交互比价页**: <{BASE_URL}/plans>  ",
        "> **Scenario / 计算前提**: Typical agentic coding workload with **95% prompt cache hit rate** and **0.5% output share** (the remaining 4.5% is fresh input). Plans marked `Cache counts full / 缓存不省钱` deduct cached tokens at full rate and lose significant effective quota in long-context coding sessions.",
        "> ",
        "> **Attribution / 数据来源说明**: Official quota formulas take top priority, followed by MoZhenZhen controlled measurements, and open-source community quota observations from [codingplan.fyi](https://codingplan.fyi) (MIT) and [realapipricing.com](https://realapipricing.com) (MIT) where vendors do not disclose numeric caps.",
        "",
        f"## 1. China Direct-Buy Personal Plans / 国内可直接购买个人套餐 ({len(rows_cn)} tiers)",
        "",
        *render_table(rows_cn),
        "",
        f"## 2. Global Personal Subscriptions & IDE Plans / 海外个人会员与编程套餐 ({len(rows_global)} tiers)",
        "",
        *render_table(rows_global),
        "",
        "---",
        "",
        "### How to Query Live Data / 如何查询最新实时数据",
        "",
        f"- Web Calculator (supports 0% / 50% / 95% / 99% cache toggle, night-time pricing, multi-model filter): <{BASE_URL}/plans>",
        f"- All Plans Overview: <{BASE_URL}/plans/all>",
        f"- AI Assistant (Skill + 9 Read-Only MCP Tools, no login / no API key): <{BASE_URL}/ai-assistant>",
        f"- Universal Agent Skill (`SKILL.md`): <{BASE_URL}/SKILL.md> · GitHub: <https://github.com/mozhenzhen/mozhenzhen-skill>",
    ]
    return "\n".join(lines) + "\n"


def build_free_quotas_md(wool: dict[str, Any], relays: dict[str, Any], now: dt.datetime) -> str:
    verified = str(wool.get("verified_at") or now.strftime("%Y-%m-%d %H:%M"))[:16].replace("T", " ")
    offers = [o for o in (wool.get("offers") or []) if not is_expired(o.get("ends_at"), now)]
    paid_offers = [o for o in (wool.get("paid_offers") or []) if not is_expired(o.get("ends_at"), now)]
    community = [r for r in (relays.get("community") or []) if not r.get("closed_at")]

    by_cycle: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for o in offers:
        by_cycle[o.get("cycle") or "other"].append(o)

    def fmt_amount(o: dict[str, Any]) -> str:
        if o.get("value_yuan") is not None:
            v = float(o["value_yuan"])
            return f"≈¥{v:.2f}".rstrip("0").rstrip(".")
        amt = f"{o.get('amount') or ''}{o.get('unit') or ''}".strip()
        return amt or "Free tier / 免费额度"

    def render_offer_table(items: list[dict[str, Any]], include_end: bool = False) -> list[str]:
        cols = "| Vendor / 厂商 | Free Quota / 免费额度 | API? | Key Models & Conditions / 说明与条件 | Official Link / 官方入口 | Step-by-Step Guide / 领取指引 |"
        sep = "| --- | --- | --- | --- | --- | --- |"
        if include_end:
            cols = "| Vendor / 厂商 | Free Quota / 免费额度 | API? | Ends / 截止 | Key Models & Conditions / 说明与条件 | Official Link / 官方入口 | Step-by-Step Guide / 领取指引 |"
            sep = "| --- | --- | --- | --- | --- | --- | --- |"
        out = [cols, sep]
        for o in items:
            api_flag = "Yes / API" if o.get("api") else "Web/App"
            models = ", ".join(m.get("name", "") for m in (o.get("models") or [])[:4] if m.get("name"))
            gives = esc(o.get("gives") or "")
            if models:
                gives = f"{gives} (Models: {esc(models)})"
            claim = o.get("claim_url") or o.get("doc_url") or ""
            claim_md = f"[Official]({claim})" if claim else "—"
            guide_url = f"{BASE_URL}/wool/{o['slug']}"
            md_url = f"{BASE_URL}/wool/{o['slug']}.md"
            guide_md = f"[Guide]({guide_url}) · [.md]({md_url})"
            if include_end:
                end_str = str(o.get("ends_at") or "TBD")[:10]
                out.append(f"| **{esc(o.get('vendor'))}** | {esc(fmt_amount(o))} | {api_flag} | {end_str} | {gives} | {claim_md} | {guide_md} |")
            else:
                out.append(f"| **{esc(o.get('vendor'))}** | {esc(fmt_amount(o))} | {api_flag} | {gives} | {claim_md} | {guide_md} |")
        return out

    api_count = sum(1 for o in offers if o.get("api"))
    lines = [
        "# Verified Official Free AI Quotas & Community Free Relays",
        "# 官方免费 AI 额度与社区公益站实核清单",
        "",
        f"> **Updated / 更新时间**: `{verified} (UTC+8)`  ",
        f"> **Active Official Free Offers / 在架有效官方免费额度**: `{len(offers)}` items (`{api_count}` with free API access) + `{len(paid_offers)}` paid-member extra perks  ",
        f"> **Active Community Free Relays / 活跃社区公益站**: `{len(community)}` sites  ",
        f"> **Live Tracker with Screenshot Guides / 带官网截图指引的实时页面**: <{BASE_URL}/wool>",
        "",
        "> **Verification Policy / 核实说明**: Every official entry links directly to the vendor's primary announcement or console page. Expired promotions are automatically filtered out on sync.",
        "",
        f"## 1. Daily Refreshing Free Quotas / 每日刷新免费额度 ({len(by_cycle['day'])})",
        "",
        *render_offer_table(by_cycle["day"]),
        "",
        f"## 2. Monthly Refreshing Free Quotas & Student Grants / 每月刷新与学生认证额度 ({len(by_cycle['month'])})",
        "",
        *render_offer_table(by_cycle["month"]),
        "",
        f"## 3. New-User & One-Time Trial Credits / 新用户与一次性体验额度 ({len(by_cycle['new'])})",
        "",
        *render_offer_table(by_cycle["new"]),
        "",
        f"## 4. Active Limited-Time Official Campaigns / 当前有效限时官方活动 ({len(by_cycle['limited'])})",
        "",
        *render_offer_table(by_cycle["limited"], include_end=True),
        "",
        f"## 5. Paid-Member Extra Perks / 付费会员隐藏加赠福利 ({len(paid_offers)})",
        "",
        "| Vendor / 厂商 | Extra Perk / 额外福利 | Eligibility / 领取条件 | Details / 详情 |",
        "| --- | --- | --- | --- |",
    ]
    for o in paid_offers:
        lines.append(
            f"| **{esc(o.get('vendor'))}** | {esc(fmt_amount(o))} | {esc(o.get('payment_terms') or '—')} | {esc(o.get('gives') or '')} |"
        )

    lines.extend([
        "",
        f"## 6. Community Free Relays (Personal Testing Only) / 社区公益站精选（仅限个人测试）",
        "",
        "> **Privacy Notice / 隐私提醒**: Community free relays are operated by independent contributors; some may log prompts or route through shared quotas. **Never send proprietary code, customer data, or production traffic through community relays.** Full daily-checked list of all "
        f"{len(community)} active sites: <{BASE_URL}/free-relays>.",
        "",
        "| Site / 站点 | Type / 类型 | Access / 门槛 | Summary / 说明 | Live Status / 实时页 |",
        "| --- | --- | --- | --- | --- |",
    ])
    for r in community[:25]:
        access = " / ".join(r.get("access") or []) or "—"
        lines.append(
            f"| **{esc(r.get('name'))}** | {esc(r.get('use_kind') or 'text')} | {esc(access)} | {esc(r.get('summary') or '')} | [Check]({BASE_URL}/free-relays/{r['id']}) |"
        )

    lines.extend([
        "",
        "---",
        "",
        "### How to Query Live Data / 如何查询最新实时数据",
        "",
        f"- Live Official Free Quotas Tracker: <{BASE_URL}/wool>",
        f"- Live Community Free Relays Status: <{BASE_URL}/free-relays>",
        f"- AI Assistant (Skill + 9 Read-Only MCP Tools, no login / no API key): <{BASE_URL}/ai-assistant>",
        f"- Universal Agent Skill (`SKILL.md`): <{BASE_URL}/SKILL.md> · GitHub: <https://github.com/mozhenzhen/mozhenzhen-skill>",
    ])

    return "\n".join(lines) + "\n"


def main() -> None:
    now = dt.datetime.now(CST)
    now_str = now.strftime("%Y-%m-%d %H:%M")
    DATA_DIR.mkdir(parents=True, exist_ok=True)

    plans_data = fetch_json("/plans/data")
    wool = fetch_json("/api/mzz/wool")
    relays = fetch_json("/api/mzz/free-relays")

    coding_md = build_coding_plans_md(plans_data, now_str)
    free_md = build_free_quotas_md(wool, relays, now)

    (DATA_DIR / "coding-plans.md").write_text(coding_md, encoding="utf-8")
    (DATA_DIR / "free-ai-quotas.md").write_text(free_md, encoding="utf-8")

    print(
        f"Synced coding-plans.md ({len(coding_md):,} chars) and "
        f"free-ai-quotas.md ({len(free_md):,} chars) at {now_str} UTC+8"
    )


if __name__ == "__main__":
    main()
