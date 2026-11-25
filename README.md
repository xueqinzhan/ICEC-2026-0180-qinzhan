# ICEC-2026-0180-qinzhan

「智能·创造者」选拔考核 · 过程数据仓库

## 介绍与选题说明

选题方向：**智能体**。

本人所学为「人工智能技术应用」专业，后续主攻方向是 AI Agent（智能体）的搭建与落地。本次考核以智能体为长期方向，阶段二先以「校园真实痛点的轻量化实用工具」作为切入点，完成了校园 WiFi 信号地图（`02-20Days-Challenge/Campus-WiFi-Map/`），跑通了从实测数据采集、工具实现、部署到用户反馈迭代的完整链路，为后续把智能体能力接入校园场景（如自动采集与录入测量数据、信号问题诊断问答）打下数据与工程基础。

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
├── 01-Field-Discovery/              阶段一：实地测评
│   ├── README.md                    ← 课题索引（2 个课题、数据量、选做说明）
│   ├── 课题02-手机发热与掉电实测/    报告 + 56 组数据 + 现场照片
│   ├── 课题03-WiFi信号盲区测绘/      报告 + 24 组数据 + 6 张现场照片
│   └── report.md                    两课题合并的原始提交版
├── 02-20Days-Challenge/             阶段二：作品与过程数据
│   ├── Campus-WiFi-Map/             作品源码（src/）+ 线上站点（docs/）
│   │   └── process_logs/            ← 12 份遥测日志 JSON 原始文件（417 条）
│   ├── P2-Data-Cleaning/            数据清洗管道（Python）+ CSV + 质量报告
│   ├── process-logs/README.md       ← 日志统计分析与结论
│   └── iterations/                  ← 3 次迭代的 Git diff（.patch）与说明
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
