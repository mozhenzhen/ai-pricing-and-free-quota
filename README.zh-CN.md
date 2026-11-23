# AI 编程套餐比价、官方免费额度与模型验真公开数据表

**简体中文** | [English](./README.md)

面向开发者与 AI 用户的公开、脱敏、每周自动同步 Markdown 数据表，汇总 **主流 AI 编程套餐 / Token Plan 95% 缓存实测换算**、**官方免费 AI 额度实核清单** 以及 **大模型 API 中转站公开验真统计** —— 由 **[模真真（mozhenzhen.com）](https://mozhenzhen.com)** 维护（*买 AI 前，先查模真真*）。

> **为什么维护这个仓库？**  
> AI 套餐和免费活动几乎每周都在变动，只看月费标价很容易踩坑——比如有些套餐读缓存也按全量扣额度，写代码场景下实际用量比同类差十几倍；而第三方 API 中转站也频繁出现型号替换。本仓库直接从模真真公网公开数据定期同步精简 Markdown 表格，方便开发者收藏、对比，也方便 AI 助手直接读取和引用。

---

## 内容目录

| 数据文件 | 包含内容 | 更新方式 | 模真真实时页面 |
| --- | --- | --- | --- |
| **[AI 编程套餐与 Token Plan 对比表](./data/coding-plans.md)** | 覆盖 49 家主流云厂商、官方会员与编程工具的 130+ 档个人在售套餐，按 **95% 缓存写代码场景** 统一折算月可用 Token 与官方按量等值倍数 | 每周一自动同步 | [套餐比价交互页](https://mozhenzhen.com/plans) |
| **[官方免费 AI 额度与公益站清单](./data/free-ai-quotas.md)** | 近百项官方免费 AI 额度（每日刷新、每月刷新、新人首领、学生认证、免费 API）、付费会员额外签到福利，以及活跃社区公益站 | 每周一自动同步 | [每日领羊毛](https://mozhenzhen.com/wool) |
| **[中转站模型验真方法与宏观统计](./data/verification-methodology.md)** | 基于 **8,902 份** 官方基准指纹验真公开报告（覆盖 **888 家** 中转站）的脱敏统计、热门型号近 30 天通过率与买前自查清单 | 定期更新 | [模型验真入口](https://mozhenzhen.com/verify) |

---

## 核心速览（数据更新时间：2026-11-23）

### 1. 选 AI 编程套餐，先看「缓存省不省钱」
日常用 Claude Code、Codex、Cursor、Cline 等编程助手时，上下文重复命中率通常在 **90%–99%**。套餐读缓存打不打折，直接决定你花同样钱能干多少活：
- **同一家云、同一价格，用量差 16 倍**：百度千帆 ¥39/月 Lite 档里，**Token 制**读缓存也按全量扣，95% 缓存下跑 DeepSeek V4.1 Flash 仅约 **0.42 亿 Token**（按官方按量价只值 ¥7.1）；同价 ¥39/月 的 **积分制** 按官方 API 价扣分，95% 缓存下能用 **6.84 亿 Token**（等值 ¥115，约月费 **2.9 倍**）。
- **国内直买高折算梯队**：阿里·百炼 Token Plan（¥39–¥312/月，95% 缓存折算官方按量价 **5.1x–6.4x**，且每晚 22:00–次日 8:00 支持闲时 4–5 折）、MiniMax M Plan 中国版（¥49–¥469/月，**5.8x–7.3x**）、阶跃星辰 Step Plan（¥99–¥399/月，**10.9x–33.9x**）、智谱 GLM 官网（¥118–¥1,078/月，**4.0x–6.1x**）。
- **海外官方会员与 IDE**：Claude Pro（$20/月）、ChatGPT Plus（$20/月）、Google AI Pro（$19.99/月）在官方限流窗口内折算按量倍数较高；Cursor、GitHub Copilot 等更侧重编辑器集成体验。

完整 130+ 档明细见 [`data/coding-plans.md`](./data/coding-plans.md)，或直接打开 [mozhenzhen.com/plans](https://mozhenzhen.com/plans) 拖动滑杆自定义你的每月用量与缓存占比（0% / 50% / 95% / 99%）。

### 2. 值得收藏的官方免费 AI 额度
截至 **2026-11-23**，模真真在架核实 **99 项官方免费 AI 额度**（其中 **48 项可直接调用免费 API**，83 项附带官网截图与箭头步骤指引），外加 **22 项付费会员隐藏加赠福利**：
- **每日刷新免费 API**：Cloudflare Workers AI（每天 1 万算力点）、NVIDIA NIM（开发测试免费调用 Kimi / MiniMax / GLM / Mistral 等）、OpenRouter（免费模型每天 50 次，累计充值满 $10 后每天 1,000 次）、Groq（每天 1,000 次）、智谱 GLM Flash 免费系列、硅基流动免费模型、魔搭社区每日魔粒。
- **按月刷新与高校学生福利**：Zed 学生计划（免一年 Pro + 每月 $10 额度）、Kiro 学生计划（每月 1,000 积分连送一年）、阿里云百炼学生礼包（¥300 抵扣金一年有效）、Tavily 搜索 API（每月 1,000 次）、蚂蚁百灵（每月 1 日自动发 ¥10 券）。

完整分类清单与官网直达链接见 [`data/free-ai-quotas.md`](./data/free-ai-quotas.md)。

### 3. 中转站模型验真公开数据速览
自 **2026-09-24** 启用官方基准指纹比对至 **2026-11-23**，模真真累计公开 **8,902 份** 指纹验真报告，涉及 **888 家** 中转服务商：
- 全周期通过率：**64.1% · 5,704/8,902 份**（身份不符 2,549 份占 28.6%，无法判定 649 份占 7.3%）。
- 近 30 天（`2026-10-24` 至 `2026-11-23`）通过率：**68.1% · 3,775/5,545 份**（身份不符 1,378 份占 24.9%）。
- 在拥有 5 份及以上公开指纹报告的 **335 家** 中转站中，保持 0 次不符记录的仅 **62 家**（占比 18.5%）。

详细型号通过率与买前自查方法见 [`data/verification-methodology.md`](./data/verification-methodology.md)。

---

## 让你的 AI 助手直接查实时价格与验真（免登录）

除了本仓库的每周快照，开发者还可以直接在 AI 工具里读取模真真的只读公开接口（**无需注册、无需 API Key**）：

1. **公开只读 MCP 服务（Streamable HTTP）**
   - 接入地址：`https://mozhenzhen.com/api/mzz/mcp`
   - 配置教程（支持 Claude Code / Cursor / Codex / Cherry Studio）：<https://mozhenzhen.com/mcp>
   - 支持查中转站、查验真记录、查模型实付价、查今日官方免费额度、查订阅套餐 5 项工具。
2. **纯文本 Markdown 伴生页（`.md`）**
   - 站点导航：<https://mozhenzhen.com/llms.txt> 与 <https://mozhenzhen.com/llms-full.txt>
   - 支持直接读取 `.md` 路径获取干净数据：
     - 模型详情：`https://mozhenzhen.com/models/{slug}.md`（示例：[gpt-5-4-1.md](https://mozhenzhen.com/models/gpt-5-4-1.md)）
     - 中转站详情：`https://mozhenzhen.com/providers/{slug}.md`
     - 套餐详情：`https://mozhenzhen.com/plans/{slug}.md`（示例：[alibaba-token-plan-essential-plan.md](https://mozhenzhen.com/plans/alibaba-token-plan-essential-plan.md)）
     - 免费额度详情：`https://mozhenzhen.com/wool/{slug}.md`（示例：[cloudflare-workers-ai.md](https://mozhenzhen.com/wool/cloudflare-workers-ai.md)）

---

## 本地一键更新

```bash
python3 scripts/sync_public_data.py
```

脚本仅依赖 Python 标准库，只请求 `https://mozhenzhen.com` 的公网公开接口，不涉及任何密钥或私有数据。

## 许可与致谢

- 同步脚本与仓库模板采用 [MIT License](./LICENSE)。
- `data/` 目录下的结构化对比表采用 CC-BY-4.0 许可，引用请注明来源 [模真真（mozhenzhen.com）](https://mozhenzhen.com)。未公布官方用量公式的订阅档位所参考的第三方开源数据，均在对应行保留对 [codingplan.fyi](https://codingplan.fyi)（MIT）与 [realapipricing.com](https://realapipricing.com)（MIT）的原始署名。
