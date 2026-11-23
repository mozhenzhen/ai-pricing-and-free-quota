# LLM API Relay Identity Verification: Methodology & Macro Statistics
# 大模型 API 中转站真假验真：方法说明与宏观公开统计

> **Snapshot Updated / 更新时间**: `2026-11-23`  
> **Live Verification Tool / 在线免费验真入口**: <https://mozhenzhen.com/verify>  
> **Public Reports Directory / 公开验真报告库**: <https://mozhenzhen.com/providers>

---

## 1. Why Third-Party Relays Need Identity Checks / 为什么要验真？

When developers buy discounted API access from third-party LLM relays, the nominal model name in the response payload (`model: "claude-opus-5.5"`) is trivial to spoof. Common real-world anomalies include:
- Routing a flagship model name to a cheaper sibling or older version during peak hours;
- Serving a self-hosted or third-party re-quantized deployment of an open-weights model whose behavior diverges from the vendor's official endpoint;
- Continuing to sell a model that the official vendor has already deprecated or retired.

在第三方 API 中转站购买大模型接口时，接口返回的模型名字段可以被任意改写。常见风险包括：把高价旗舰模型路由到低价或旧版模型、用与官方表现不一致的第三方量化/自部署版本冒充官方接口，或者继续售卖官方已经停服的模型。

---

## 2. How MoZhenZhen Verifies Model Identity / 模真真的官方基准比对方法

Since **2026-09-24**, MoZhenZhen's primary text-model verification uses **multi-round independent sampling against official vendor reference baselines**:

1. **Official Baselines Only / 只认官方基准**：Reference baselines are collected exclusively from the model vendor's own official API or vendor-authorized cloud endpoints. Third-party relays and unofficial hosts are never used as ground truth.
2. **Multi-Round Independent Sampling / 多轮独立采样**：When a user submits an API base URL and key at [mozhenzhen.com/verify](https://mozhenzhen.com/verify), the test runs multiple independent rounds against the target endpoint and compares behavioral distributions against the official reference bank.
3. **Three Clear Outcomes / 三种明确结论**：
   - **身份一致 (`Identity Matched`)**：Behavior aligns with the claimed official model within verified thresholds.
   - **身份不符 (`Identity Mismatched`)**：Behavior diverges significantly from the claimed official model. Note: we report only that it does not match the claimed official model — we do not speculate which other model it might be.
   - **无法判定 (`Inconclusive`)**：Two official sibling models are too close in behavior or boundary conditions prevented a definitive call.

> **Scope Boundary / 边界说明**：To prevent relays from gaming or memorizing verification prompts, prompt formats and sample counts are intentionally not published. Verification checks model identity only — it does not represent long-term uptime or network latency, and MoZhenZhen does not publish latency or stability scores.

---

## 3. Macro Statistics (Official Fingerprint Era: 2026-09-24 – 2026-11-23)

> Note: Historical quick-check reports collected before `2026-09-24` used earlier methods and are counted separately from official fingerprint verification reports below.

| Metric / 统计维度 | Count / 数值 | Share / 占比 |
| --- | --- | --- |
| Total public official-fingerprint reports (`2026-09-24` – `2026-11-23`) | **8,902** | 100% |
| — Identity Matched / 身份一致 | **5,704** | **64.1%** (`5,704/8,902`) |
| — Identity Mismatched / 身份不符 | **2,549** | **28.6%** (`2,549/8,902`) |
| — Inconclusive / 无法判定 | **649** | **7.3%** (`649/8,902`) |
| Last 30 days (`2026-10-24` – `2026-11-23`) total public reports | **5,545** | 100% |
| — Last 30 days Identity Matched / 近 30 天身份一致 | **3,775** | **68.1%** (`3,775/5,545`) |
| — Last 30 days Identity Mismatched / 近 30 天身份不符 | **1,378** | **24.9%** (`1,378/5,545`) |
| Unique third-party relays covered by fingerprint checks | **888** | — |
| Relays with ≥ 5 public fingerprint reports | **335** | 100% |
| — Relays with **0** mismatch records (≥ 5 reports) | **62** | **18.5%** (`62/335`) |
| — Relays with ≥ 1 mismatch record (≥ 5 reports) | **273** | **81.5%** (`273/335`) |
| — Relays with ≥ 50% mismatch rate (≥ 5 reports) | **79** | **23.6%** (`79/335`) |

---

## 4. Last 30 Days Pass Rate by Popular Models (`2026-10-24` – `2026-11-23`)

Only models with at least 40 public fingerprint reports in the past 30 days are listed below:

| Model / 模型 | Pass Rate (Matched / Total) / 通过率 | Mismatched / 不符份数 | Inconclusive / 无法判定 | Live Model Page / 模真真实时页 |
| --- | --- | --- | --- | --- |
| **Claude Opus 5.5** | **66.2%** · `626/946 份` | 273 | 47 | [View](https://mozhenzhen.com/models/claude-opus-5-5-2922) |
| **GPT-6.1 Sol** | **76.7%** · `710/926 份` | 197 | 19 | [View](https://mozhenzhen.com/models/gpt-6-1-sol-2969) |
| **DeepSeek V4.1 Flash** | **82.7%** · `511/618 份` | 37 | 70 | [View](https://mozhenzhen.com/models/deepseek-v4-1-flash-2056) |
| **GPT-6 Astra** | **88.3%** · `385/436 份` | 47 | 4 | [View](https://mozhenzhen.com/models/gpt-6-astra-2053) |
| **GPT-6.2 Sol** | **86.6%** · `207/239 份` | 32 | 0 | [View](https://mozhenzhen.com/models/gpt-6-2-sol-3107) |
| **Claude Sonnet 5.5** | **58.5%** · `114/195 份` | 75 | 6 | [View](https://mozhenzhen.com/models/claude-sonnet-5-5-2945) |
| **GPT-6.1 Terra** | **53.1%** · `86/162 份` | 75 | 1 | [View](https://mozhenzhen.com/models/gpt-6-1-terra-3052) |
| **GLM-5.3** | **76.2%** · `115/151 份` | 31 | 5 | [View](https://mozhenzhen.com/models/glm-5-3-1889) |
| **GPT-6.2 Astra** | **85.6%** · `113/132 份` | 17 | 2 | [View](https://mozhenzhen.com/models/gpt-6-2-astra-3106) |
| **Gemini 4 Argon** | **73.7%** · `84/114 份` | 23 | 7 | [View](https://mozhenzhen.com/models/gemini-4-argon-3012) |
| **DeepSeek V4 Pro** | **44.2%** · `46/104 份` | 49 | 9 | [View](https://mozhenzhen.com/models/deepseek-v4-pro-73) |
| **Claude Haiku 5.5** | **83.5%** · `86/103 份` | 14 | 3 | [View](https://mozhenzhen.com/models/claude-haiku-5-5-3009) |
| **Claude Fable 5.2** | **60.2%** · `62/103 份` | 31 | 10 | [View](https://mozhenzhen.com/models/claude-fable-5-2-3075) |
| **GLM-5.3-Flash** | **64.8%** · `59/91 份` | 9 | 23 | [View](https://mozhenzhen.com/models/glm-5-3-flash-2050) |
| **Kimi K3** | **57.8%** · `52/90 份` | 26 | 12 | [View](https://mozhenzhen.com/models/kimi-k3-1861) |
| **Kimi K3.1 Pro** | **59.5%** · `47/79 份` | 20 | 12 | [View](https://mozhenzhen.com/models/kimi-k3-1-pro-3041) |
| **GPT-6 Sol** | **23.2%** · `16/69 份` | 43 | 10 | [View](https://mozhenzhen.com/models/gpt-6-sol-2924) |
| **Claude Fable 5.1** | **8.8%** · `6/68 份` | 52 | 10 | [View](https://mozhenzhen.com/models/claude-fable-5-1-2047) |
| **Grok 4.7** | **71.2%** · `42/59 份` | 0 | 17 | [View](https://mozhenzhen.com/models/grok-4-7-2918) |
| **Gemini 4 Carbon** | **86.0%** · `43/50 份` | 4 | 3 | [View](https://mozhenzhen.com/models/gemini-4-carbon-3077) |

> **Important Caution / 重要说明**：Public reports reflect endpoints that users actively chose to test (often because they already suspected an anomaly). Therefore, these numbers illustrate real-world risk across tested endpoints — they do not represent a random census of all relays, nor should price alone be used to infer authenticity.

---

## 5. Pre-Purchase Self-Check Checklist / 买前自查 4 步

1. **Check the provider's history first / 先查站方历史记录**：Search the relay domain on [mozhenzhen.com/providers](https://mozhenzhen.com/providers) to see whether it is actively operating, its actual-paid price (after recharge exchange rate & multiplier), and past public verification reports.
2. **Test the exact group/channel you plan to use / 按具体分组实测**：Many relays sell multiple groups (e.g., official enterprise channel vs. discounted reverse channel) under the same domain; a pass on one group does not guarantee another group.
3. **Top up small and verify before scaling / 小额充值先验真**：Run a verification check at [mozhenzhen.com/verify](https://mozhenzhen.com/verify) on a minimal deposit before committing larger balance, and watch for official model deprecation notices.
4. **Re-check periodically / 定期复测**：Relays can switch upstream routing after you recharge; schedule periodic re-checks or inspect recent public reports for your model.
