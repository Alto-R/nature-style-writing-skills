<div align="center">

# Writing Nature Papers 🧬

一个面向 **Nature Communications** 及 Nature 系研究期刊的 Claude Code 写作技能（Skill）：把多篇 Nature 子刊的真实写作经验、以及真实投稿 checklist 提炼为「逐节写作指南 + 期刊语气规则 + 投稿前机械校验」，让你写出的每一节在落笔时就已合规。

[![Claude Code](https://img.shields.io/badge/Claude%20Code-Skill-D97757?style=flat-square&logo=anthropic&logoColor=white)](#-如何使用)
[![Markdown](https://img.shields.io/badge/Format-Markdown-000000?style=flat-square&logo=markdown&logoColor=white)](#)
[![Python](https://img.shields.io/badge/Verification-Python%203.8+-3776AB?style=flat-square&logo=python&logoColor=white)](#-投稿前机械校验)
[![Journal](https://img.shields.io/badge/Target-Nature%20family-006699?style=flat-square)](#-适用范围)

**[中文](README.md)** | **[English](README-EN.md)**

</div>

<br>

## 📑 快速导航

<div align="center">

| | | |
|:---:|:---:|:---:|
| [✨ 核心理念](#-核心理念) | [🏗️ 目录结构](#️-目录结构) | [🚀 如何使用](#-如何使用) |
| [🧭 章节路由](#-章节路由) | [✅ 投稿前机械校验](#-投稿前机械校验) | [🎙️ 语气与全局规则](#️-语气与全局规则) |
| [📐 规则速查表](#-规则速查表) | [🚫 适用范围](#-适用范围) | [❓ 常见问题](#-常见问题) |

</div>

<br>

## ✨ 核心理念

> **先抛结论，量化一切，对推断保留余地、对核心主张果断——并在写作的同时就套用期刊格式规则，而不是事后补救。**

每一条编辑规则都被嵌入到它真正生效的那一节指南里：一节写对了，它就已经合规。

- **逐节模板化**：标题 / 摘要 / 引言 / 结果 / 讨论 / 方法 / 图表 / 参考文献 / 声明，每节都有逐段结构、句式模板（占位符而非真实内容）、时态语态、以及就地生效的合规规则。
- **从多篇子刊经验提炼**：基于多篇真实被 Nature 系期刊接收的手稿写作经验（含一篇 Nature Communications 一作已发表），去除主题相关内容，沉淀为话题无关的可复用模板——规则来自真正走通审稿与发表流程的一手经验，而非未经发表检验的二手归纳。
- **合规规则源自真实 checklist**：每条阈值与格式要求并非凭空设定，而是从期刊真实投稿 checklist 提炼而来，并嵌入到对应章节就地生效。
- **写作即合规**：把每个文件末尾的 "Self-check" 行转成 TodoWrite 待办项，写完即查、不漏项。
- **投稿前安全网**：可选的机械校验脚本，专门捕捉「靠写作改不掉」的工件级问题（残留修订痕迹、文件超限、过期 SI PDF、图中的红绿像素）。
- **话题无关**：任何学科的定量研究稿件都可套用同一套语气与结构。

## 🏗️ 目录结构

```text
writing-nature-papers/
├── SKILL.md                         技能入口：总览 + 章节路由 + 规则归属表
├── writing/                         逐节写作指南（落笔即合规）
│   ├── 00-voice-and-global-rules.md 全局语气与规则（所有正文通用，先读）
│   ├── 01-title.md                  标题
│   ├── 02-abstract.md               摘要（≤ ~200 词，"Here we show"）
│   ├── 03-introduction.md           引言
│   ├── 04-results.md                结果（含现象描述 / 数字 / 统计）
│   ├── 05-discussion.md             讨论
│   ├── 06-methods.md                方法（含公式 / 单位 / 货币 / 可用性标题）
│   ├── 07-figures-and-display.md    图、表、图注、配色、版式（正文 + SI）
│   ├── 08-references.md             参考文献（正文 + SI）
│   └── 09-declarations-and-availability.md  数据/代码可用性、利益声明、致谢、作者贡献
└── verification/                    投稿前机械校验（可选，仅上传前运行一次）
    ├── verification-workflow.md     校验流程说明 + 人工交叉一致性检查清单
    └── scripts/                     Python 校验脚本
        ├── check_all.py             汇总运行，输出 PASS / PARTIAL / FAIL
        ├── check_ooxml.py           修订痕迹 / 公式可编辑性 / 加粗 / 列表 / 域代码
        ├── check_figures.py         图像红绿共现 + 灰度可区分性
        ├── check_deliverables.py    文件大小 / 过期 SI PDF
        └── extract_text.py          docx→md 文本健全性扫描
```

## 🚀 如何使用

这是一个 **Claude Code 技能**，不是独立软件。在装有该技能的 Claude Code 会话中，当你着手撰写、修订或投稿前检查一篇 Nature 系期刊稿件时，它会被自动触发；你也可以直接说明意图来调用它。

写作流程：

1. **定位你正在写的部分**，打开 `writing/` 下对应的那一个文件。每个文件给出逐段结构、句式模板、应使用的时态/语态，以及就地嵌入的合规规则。
2. **始终牢记 `writing/00-voice-and-global-rules.md`**——它承载适用于所有正文的规则（不吹新颖性、软化绝对主张、稀疏使用 "we"、不做强调格式、缩写首次定义、不用项目符号、标题风格）。
3. **起草时，把该文件的 "Self-check" 行转成 TodoWrite 待办项**，确保不漏项。
4. **仅在上传前**，可选地运行 `verification/` 中的机械扫描，处理那些靠写作无法解决的工件级问题。

## 🧭 章节路由

| 你要写的部分 | 打开 |
| --- | --- |
| 适用于所有正文的全局语气 + 规则 | `writing/00-voice-and-global-rules.md` |
| 标题 | `writing/01-title.md` |
| 摘要 | `writing/02-abstract.md` |
| 引言 | `writing/03-introduction.md` |
| 结果（含如何描述现象、数字、统计） | `writing/04-results.md` |
| 讨论 | `writing/05-discussion.md` |
| 方法（含公式、单位、货币、可用性标题） | `writing/06-methods.md` |
| 图、表、图注、地图、配色、artwork（正文 + SI） | `writing/07-figures-and-display.md` |
| 参考文献（正文 + SI 参考列表） | `writing/08-references.md` |
| 数据/代码可用性、利益冲突、资助、作者贡献、单位署名 | `writing/09-declarations-and-availability.md` |
| 上传前最终机械扫描 | `verification/verification-workflow.md` |

## ✅ 投稿前机械校验

写作指南让正文在落笔时就合规；这套扫描是**工件级**问题的安全网——那些取决于成稿文件、靠写作改不掉的问题（误留的修订痕迹、文件大小、过期的导出 PDF、渲染图中的红绿像素）。**仅在上传前运行一次。**

```bash
cd verification/scripts
python check_all.py --docx ../../Final_manuscript.docx \
                    --si ../../Supplementary.docx \
                    --si-pdf "../../Supplementary Information.pdf" \
                    --figdir ../../figure
```

各脚本职责：

| 脚本 | 检查内容 | 为何必须事后做 |
| --- | --- | --- |
| `check_ooxml.py` | 残留修订痕迹；公式是 OMML（可编辑）还是图片；正文加粗；项目/编号列表；域代码（PAGE/NUMPAGES） | 取决于已保存的 .docx 内部结构 |
| `check_figures.py` | 成稿图 PNG 的红绿共现与灰度可区分性 | 取决于渲染后的图像像素 |
| `check_deliverables.py` | 文件大小对限值（上传 30 MB、图 50 MB）；过期 SI PDF | 取决于磁盘文件及其时间戳 |
| `extract_text.py` | pandoc docx→md；规整全角 `（N）`→`(N)`；标记 `kW/m` 式斜杠单位、"on request" 数据声明、摘要超长 | 对导出文本的健全性扫描 |
| `check_all.py` | 运行上述脚本并打印汇总 PASS / PARTIAL / FAIL | — |

依赖：`python-docx`、`PyMuPDF`（`fitz`）、`Pillow`，以及 PATH 中的 `pandoc`；在 Windows 上若用 `--word-com` 渲染/导出则需 `pywin32`。缺少可选依赖或输入时脚本会优雅降级（报 `SKIP`，不崩溃）。退出码：`0` PASS、`1` PARTIAL、`2` FAIL，可用于 CI。

> 这**不是**正确写作的替代品。若扫描标出了某个正文问题，请回到对应 `writing/` 指南、按它的术语修改，而不是在这里打补丁。

## 🎙️ 语气与全局规则

一篇 Nature 系研究论文读起来像一位自信、精确、略显克制、从不过度推销的专家。五个习惯造就这种语气：

1. **先抛结论，而非方法**——先陈述「什么是真的」，建立它的装置放第二位或入方法。
2. **量化一切**——用数字和单位代替形容词；给出分布（均值、中位数、范围），而非单一中心值。
3. **显式比较**——单个数字是惰性的，要锚定它（"约为参照组的 k 倍"、"占样本 x%"）。
4. **对推断保留余地、对头条主张果断**——机理与预测用 *indicate / suggest / likely*，核心结果直陈。
5. **主题句优先**——每段以陈述其要点的句子开头。

## 📐 规则速查表

| 规则 / 阈值 | 归属文件 |
| --- | --- |
| 摘要 ≤ ~200 词，无引用，无未定义缩写，"Here we show" | `02` |
| 引言末段用现在时，引出本研究 | `03` |
| 仅一级子标题；句首大写；标题末无标点 | `04`、`06`、`00` |
| 标量数学符号斜体（*β*、*p*、*R*、*R²*、*n*）；多字母函数/缩写用正体 | `04` |
| 单位用负指数（`kW m⁻¹` 而非 `kW/m`）；货币一致（USD） | `04`、`06` |
| 公式可编辑、编号 `(1)`、引用为 "equation (1)" | `06` |
| 图/表注 ≤ 350 词，自洽（定义每个缩写/符号/颜色） | `07` |
| ≤ 10 个正文展示项；每项适配单页 A4；Arial 5–7 pt；≥ 300 dpi；尽量矢量 | `07` |
| 不用红绿配对；地图标经纬度；多面板用 **a, b, c**；图例置于图内 | `07` |
| 参考文献按引用顺序、完整、Nature 格式；SI 列表自洽 | `08` |
| 数据可用性具体（绝不写 "on request"）；代码经 Zenodo DOI | `09` |
| 作者贡献用首字母缩写，绝不写 "all authors" | `09` |
| 不用新颖性/夸张词；软化绝对主张；稀疏 "we"；不做强调格式；不用项目符号 | `00` |
| 关闭修订痕迹；上传文件 ≤ 30 MB；新鲜 SI PDF；封面信 ≤ 250 字符摘要 | `verification/` |

## 🚫 适用范围

适用于 **Nature Communications** 及其他 Nature 系研究期刊的稿件撰写、修订与投稿前检查。

不适用的场景：

- **其他 house style 期刊**（IEEE、Elsevier、ACS）——结构可迁移，但这里的具体规则是 Nature 系专属的。
- **绘制图本身**——请用 **superpowers:academic-figure** 技能。
- **底层 .docx 操作机制**——请用 **document-skills:docx** 技能。

## ❓ 常见问题

### 这是程序还是文档？

是一个 Claude Code **技能**——主体是结构化的 Markdown 写作指南，外加一组可选的 Python 校验脚本。它不会替你写论文内容，而是约束 Claude 在写每一节时落笔即合规。

### 一定要运行校验脚本吗？

不必。写作指南已让正文在落笔时合规；脚本只是上传前对工件级问题的安全网，可选，且仅运行一次。

### 缺少 `pandoc` 或 `Pillow` 会怎样？

脚本优雅降级：缺少的可选依赖或输入会报 `SKIP` 而非崩溃。

### 校验标出了一个正文措辞问题，要在脚本里改吗？

不要。回到对应的 `writing/` 指南，按它的术语在原文修改。脚本只负责报告，不负责改写。
