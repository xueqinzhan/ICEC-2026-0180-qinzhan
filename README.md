# ICEC-2026-0180-qinzhan

「智能·创造者」选拔考核 · 过程数据仓库

## 三阶段选题一览

| 阶段 | 规则 | 我的选择 | 产出位置 |
|-----|------|---------|---------|
| 阶段一 · 基础素养实地测评 | **10 选 2**（20 分） | **课题02** 手机多工况发热与掉电实测<br>**课题03** 教学楼与宿舍无线信号盲区测绘 | [`01-Field-Discovery/`](01-Field-Discovery/README.md) |
| 阶段二 · 工坊开放式项目挑战 | **8 选 1**（60 分） | **项目四** 解决校园真实痛点的轻量化实用程序研发与日常运行日志验证 | [`02-20Days-Challenge/`](02-20Days-Challenge/README.md) |
| 阶段三 · 12 分钟 AI 结构化面试 | 20 分 | — | 面试题库出处 <https://icec.openkub.com/assessment.html> |

阶段二的作品是 **校园 WiFi 信号地图**，已上线：<https://xueqinzhan.github.io/ICEC-2026-0180-qinzhan/>

选题官方出处：[ICEC 2026 选拔考核大纲](https://icec.openkub.com/assessment.html)

## 介绍与选题说明

选题方向：**智能体**。

本人所学为「人工智能技术应用」专业，后续主攻方向是 AI Agent（智能体）的搭建与落地。本次考核以智能体为长期方向，阶段二选定的**项目四**，官方英文名即为 *Campus Utility Software / **Agent** & 7-Day Telemetry Verification*，交付形态本身包含 Agent。

阶段二先以「校园真实痛点的轻量化实用工具」作为切入点，完成了校园 WiFi 信号地图（`02-20Days-Challenge/Campus-WiFi-Map/`），跑通了从实测数据采集、工具实现、部署到用户反馈迭代的完整链路，为后续把智能体能力接入校园场景（如自动采集与录入测量数据、信号问题诊断问答）打下数据与工程基础。

**关于数据复用**：阶段二作品使用的 24 组数据，就是阶段一课题03 的实测结果。这是刻意延续——课题03 的交付要求止步于"提交数据表与衰减分析"，产出是一张没人打开的 Excel；阶段二解决的是它的下游问题：让数据变成同学手机上能用的工具，并用 7 天日志验证有没有人用。两阶段考核的能力项不同（数据本身 vs 工具与使用验证），新增工作量清单见 [`02-20Days-Challenge/README.md`](02-20Days-Challenge/README.md)。

整个过程的显著特点是**以 AI Agent 作为主要开发协作方式**：需求拆解、代码生成、排障与部署均由我与 AI 协作完成，关键对话与排障记录保存在 `03-AI-Collaboration/`。过程中持续记录从选题调研、动手实现到迭代优化的完整过程数据。

## 个人简介

- 姓名：薛钦展
- 学校：深圳城市职业学院
- 专业：人工智能技术应用（C3 班）
- 年级：大一
- 兴趣：小游戏、视频剪辑、烹饪

## 目录结构

```
ICEC-2026-0180-qinzhan/
├── 01-Field-Discovery/              阶段一（10 选 2）：课题02 + 课题03
│   ├── README.md                    ← 课题索引（选做哪两个、数据量）
│   ├── 课题02-手机发热与掉电实测/    报告 + 56 组数据 + 现场照片
│   ├── 课题03-WiFi信号盲区测绘/      报告 + 24 组数据 + 6 张现场照片
│   └── report.md                    两课题合并的原始提交版
├── 02-20Days-Challenge/             阶段二（8 选 1，选中项目四）
│   ├── README.md                    ← 选题声明 + 评分项证据对照 + 数据复用说明
│   ├── 提交材料.md                   考核表单正文原文（998 字）与附件清单
│   ├── Campus-WiFi-Map/             ★ 作品本体：源码 src/ + 417 条日志
│   ├── P2-Data-Cleaning/            数据清洗管道（Python）+ CSV + 质量报告
│   ├── process-logs/README.md       ← 评分项① 日志统计分析与结论
│   └── iterations/                  ← 评分项② 3 次迭代的 Git diff 与说明
├── docs/                            GitHub Pages 部署目录（与 src/ 同步）
└── 03-AI-Collaboration/             关键 AI 提问与排障对话记录（6 篇）
```

## 线上地址

| 用途 | 地址 |
|-----|------|
| 主应用 | <https://xueqinzhan.github.io/ICEC-2026-0180-qinzhan/> |
| 反馈表 | <https://xueqinzhan.github.io/ICEC-2026-0180-qinzhan/feedback.html> |

国内网络可直接访问，无需代理。

## 快速查阅路径

- 想看**实测原始数据** → [`01-Field-Discovery/`](01-Field-Discovery/README.md)（表格已内嵌在 README，GitHub 直接可读）
- 想看**迭代改了什么** → [`02-20Days-Challenge/iterations/`](02-20Days-Challenge/iterations/README.md)
- 想看**有没有人真在用** → [`02-20Days-Challenge/process-logs/`](02-20Days-Challenge/process-logs/README.md)
- 想看**怎么和 AI 协作排障** → [`03-AI-Collaboration/`](03-AI-Collaboration/README.md)
