# AI Pricing, Coding Plans & Free Quota Benchmarks

[简体中文](./README.zh-CN.md) | **English**

Open, weekly-synced Markdown reference tables for **AI Coding Plans / Token Plans** (95% prompt-cache benchmark), **verified official free AI quotas**, and **LLM API relay identity verification statistics** — maintained by **[MoZhenZhen (模真真)](https://mozhenzhen.com)** (*Before buying AI, check MoZhenZhen*).

> **Why this repo exists**: AI pricing tables change weekly, and headline monthly fees hide huge traps (such as plans that charge cached tokens at 100% rate or unofficial API relays substituting cheaper models). This repository publishes clean, verifiable, zero-hype Markdown snapshots synced directly from live public data so both developers and AI coding assistants can inspect real numbers fast.

---

## Quick Navigation

| Dataset | What's Inside | Sync Frequency | Live Interactive Page |
| --- | --- | --- | --- |
| **[AI Coding Plans & Token Plans](./data/coding-plans.md)** | 130+ personal plans across 49 providers (Alibaba Cloud, ByteDance Volcengine, Baidu Qianfan, Tencent Cloud, GLM, MiniMax, Kimi, StepFun, Claude, ChatGPT, Gemini, Cursor, GitHub Copilot, TRAE, etc.) under a **95% cache coding workload** | Weekly (Mon 02:00 UTC) | [mozhenzhen.com/plans](https://mozhenzhen.com/plans) |
| **[Official Free AI Quotas & Free Relays](./data/free-ai-quotas.md)** | ~100 verified official free AI quotas (daily refresh, monthly grants, new-user credits, student perks, free APIs) + active community free relays | Weekly (Mon 02:00 UTC) | [mozhenzhen.com/wool](https://mozhenzhen.com/wool) |
| **[LLM Relay Identity Verification Report](./data/verification-methodology.md)** | Anonymized macro statistics from **8,902** official-benchmark fingerprint checks across **888** third-party API relays, plus how to self-check before topping up | Periodic snapshot | [mozhenzhen.com/verify](https://mozhenzhen.com/verify) |

---

## Key Takeaways (Snapshot: 2026-11-23)

### 1. The Hidden "No-Cache-Savings" Trap in Coding Plans
Agentic coding tools (Claude Code, Codex, Cursor, Cline, etc.) routinely hit **90%–99% prompt cache rates**. Whether a Token Plan discounts cached reads makes a massive difference:
- **Same vendor, same price, 16x difference**: On Baidu Qianfan's ¥39/mo Lite tier, the **Token-quota mode** counts cached tokens at full rate (`0.42 亿 / 42M` tokens on DeepSeek V4.1 Flash at 95% cache, equivalent to only ¥7.1 of official pay-as-you-go API); the **Points-quota mode** at the exact same ¥39/mo reflects cache savings (`6.84 亿 / 684M` tokens, equivalent to ¥115 — **2.9x** the monthly fee).
- **High-leverage China direct-buy plans**: Alibaba Cloud Bailian Token Plan (¥39–¥312/mo, **5.1x–6.4x** official API value at 95% cache plus 40%–50% night discounts), MiniMax M Plan CN (¥49–¥469/mo, **5.8x–7.3x**), StepFun Step Plan (¥99–¥399/mo, **10.9x–33.9x**), and Zhipu GLM Plans (¥118–¥1,078/mo, **4.0x–6.1x**).
- **Global subscriptions**: Claude Pro ($20/mo), ChatGPT Plus ($20/mo), and Google AI Pro ($19.99/mo) deliver high effective token multiples for flagship models when used within official rate windows, while IDE wrappers like Cursor and GitHub Copilot trade raw token volume for integrated editor workflows.

See the complete comparison table in [`data/coding-plans.md`](./data/coding-plans.md) or test your own monthly volume and cache ratio (0% / 50% / 95% / 99%) at [mozhenzhen.com/plans](https://mozhenzhen.com/plans).

### 2. Official Free AI Quotas Worth Bookmarking
As of **2026-11-23**, MoZhenZhen tracks **99 active official free AI offers** (**48 with direct API access**) and **22 paid-member extra perks**:
- **Daily refreshing free APIs**: Cloudflare Workers AI (`10,000` neurons/day), NVIDIA NIM (developer free tier across Kimi, MiniMax, GLM, Mistral), OpenRouter (`50` req/day free, `1,000`/day after $10 lifetime balance), Groq (`1,000` req/day), Zhipu GLM Flash free models, SiliconFlow free tier, ModelScope daily credits.
- **Monthly & student grants**: Zed Student Plan (1 year free Zed Pro + $10/mo), Kiro Student Plan (1,000 credits/mo for 1 year), Alibaba Cloud Bailian Student Pack (¥300 for 1 year), Tavily (`1,000` searches/mo), Rime ($50/mo speech API), Ant Ling (¥10/mo).

See every active item with direct official links and step-by-step guides in [`data/free-ai-quotas.md`](./data/free-ai-quotas.md).

### 3. Third-Party API Relay Identity Verification Reality Check
Between **2026-09-24** and **2026-11-23**, public official-benchmark fingerprint checks on MoZhenZhen recorded **8,902 reports** across **888 third-party API relays**:
- Overall pass rate (`Identity Matched`): **64.1% · 5,704/8,902** (`28.6%` mismatched, `7.3%` inconclusive).
- Last 30 days (`2026-10-24` – `2026-11-23`): **68.1% · 3,775/5,545** matched (`24.9%` mismatched).
- Among **335** relays with ≥ 5 public fingerprint reports, only **62** (`18.5%`) maintained zero mismatch records.

Full model-by-model breakdown and pre-purchase checklist: [`data/verification-methodology.md`](./data/verification-methodology.md).

---

## Use Live Data Directly in Your AI Agent (MCP & `.md` Endpoints)

Instead of relying on static snapshots, AI coding agents and LLM tools can query MoZhenZhen's read-only public endpoints directly — **no login, no API key required**:

1. **Read-Only MCP Server (Streamable HTTP)**  
   - Endpoint: `https://mozhenzhen.com/api/mzz/mcp`  
   - Setup guide (Claude Code / Cursor / Codex / Cherry Studio): <https://mozhenzhen.com/mcp>  
   - Tools included: lookup API relays, query verification pass rates, compare model actual-paid prices, list active free AI quotas, compare coding/subscription plans.
2. **Clean Markdown Companion Pages (`.md`)**  
   - Site overview for LLMs: <https://mozhenzhen.com/llms.txt> and <https://mozhenzhen.com/llms-full.txt>
   - Append `.md` to supported detail pages for zero-HTML Markdown output:
     - Models: `https://mozhenzhen.com/models/{slug}.md` (example: [gpt-5-4-1.md](https://mozhenzhen.com/models/gpt-5-4-1.md))
     - Relays: `https://mozhenzhen.com/providers/{slug}.md`
     - Coding Plans: `https://mozhenzhen.com/plans/{slug}.md` (example: [alibaba-token-plan-essential-plan.md](https://mozhenzhen.com/plans/alibaba-token-plan-essential-plan.md))
     - Free Quotas: `https://mozhenzhen.com/wool/{slug}.md` (example: [cloudflare-workers-ai.md](https://mozhenzhen.com/wool/cloudflare-workers-ai.md))

---

## Reproducing Locally

```bash
python3 scripts/sync_public_data.py
```

The sync script uses Python's standard library only, calls only public `https://mozhenzhen.com` endpoints, and requires zero secrets.

## License & Attribution

- Sync scripts and repository templates: [MIT License](./LICENSE).
- Markdown benchmark tables in `data/`: CC-BY-4.0 with attribution to [MoZhenZhen](https://mozhenzhen.com). Where third-party open-source quota observations are used for subscriptions without published official caps, attribution to [codingplan.fyi](https://codingplan.fyi) (MIT) and [realapipricing.com](https://realapipricing.com) (MIT) is preserved row by row.
