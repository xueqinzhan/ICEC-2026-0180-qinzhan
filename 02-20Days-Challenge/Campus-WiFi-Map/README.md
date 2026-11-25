# 校园WiFi信号地图

> **ICEC 2026 第二阶段 · 工坊开放式项目挑战（8 选 1 · 60 分）— 选用「项目四」**
> 项目四全名：解决校园真实痛点的轻量化实用程序研发与日常运行日志验证
> 官方英文名：*Campus Utility Software / Agent & 7-Day Telemetry Verification*
> 选题声明与 8 个项目的完整对照见 [`../README.md`](../README.md)

## 在线地址

| | |
|---|---|
| 主应用 | <https://xueqinzhan.github.io/ICEC-2026-0180-qinzhan/> |
| 用户反馈表单 | <https://xueqinzhan.github.io/ICEC-2026-0180-qinzhan/feedback.html> |

已部署 GitHub Pages（从仓库根 `docs/` 发布），国内网络手机直接打开，无需代理、无需安装。

## 项目简介

校园WiFi信号地图是一个面向全校师生的实用工具，帮助快速了解校园各区域的WiFi信号覆盖质量，定位信号盲区。基于8个典型点位的24组实测数据构建，支持持续添加新测量点。

## 解决的痛点

- 新生入学不了解校园WiFi覆盖情况，选座/学习找不到好信号区域
- 校园网络故障时无法快速定位是局部盲区还是全局问题
- 缺乏可视化的信号质量参考工具

## 功能特性

### 核心功能
- **多建筑切换**：支持实训楼4F、食堂/图书馆、楼梯间三个区域
- **交互式信号地图**：SVG楼层平面图 + 8个WiFi信号点，点击查看详情
- **信号热力图**：Canvas渲染的信号覆盖热力分布
- **数据管理**：添加/删除/搜索/筛选测量点
- **数据导出**：支持 CSV 和 JSON 格式导出
- **数据导入**：支持从 CSV/JSON 文件导入数据

### 运行日志系统（Telemetry）
- 自动记录所有用户操作（页面切换、数据查看、功能使用等）
- 每条日志含时间戳、会话ID、操作类型和详情
- 日志自动保存到 localStorage
- 支持导出运行日志（JSON格式），满足连续7天日志提交要求
- 实时显示日志统计（总条数、今日条数、会话时长）

### 用户反馈系统
- 独立反馈表单页面（feedback.html）
- 收集满意度评分、功能偏好、改进建议
- 反馈数据自动保存并导出

### 离线支持（PWA）
- Service Worker 缓存核心文件
- 支持离线访问
- 可安装到手机桌面

## 迭代记录

| 版本 | 日期 | 更新内容 | commit |
|------|------|----------|--------|
| v1.0 | 2026-10-24 | 初始版本：SVG地图 + 信号图表 + 详情弹窗 | `dab988b` |
| v1.1 | 2026-10-24 | 添加多建筑切换、热力图、数据管理功能 | `182b6aa` |
| v1.2 | 2026-10-24 | 添加遥测日志系统、用户反馈表单、PWA离线支持 | `e64a7da` |
| **v1.3** | 2026-11 | **深色模式**：CSS 变量主题 + localStorage 记忆，响应用户"晚上躺着看太刺眼" | `86772c0` |
| **v1.4** | 2026-11 | **信号趋势折线图**：Canvas 绘制各点位信号变化，响应日志中点位对比需求 | `86772c0` |
| **v1.5** | 2026-11 | **一键分享应用**：Web Share API + 剪贴板降级，响应"反馈链接传不到别人手机" | `86772c0` |

v1.3–v1.5 是满足考核"≥3 次 Git 迭代 Diff"要求的三次迭代，逐项 diff 已导出：[`../iterations/`](../iterations/README.md)

## 运行日志（评分项① 证据）

- 原始 JSON：[`process_logs/`](process_logs/) — 12 份文件，417 条事件
- 统计分析与结论：[`../process-logs/README.md`](../process-logs/README.md)
- 覆盖范围：开发者侧 10-24 ~ 10-31 共 7 天（10-27 漏记，如实保留）+ 5 位同学侧日志

## 数据来源

初始数据来自 **2026-10-22 的实地测量**：
- 测试设备：iPhone 15 Pro + Wi-Fi Analyzer
- 测试点位：8个（覆盖教学楼、走廊、楼梯、机房、食堂等）
- 每点位测量：3轮，共24组数据
- 采集指标：信号强度(dBm)、延迟(ms)、下载速度(Mbps)、上传速度(Mbps)

原始数据：[data/wifi_signal_raw.csv](data/wifi_signal_raw.csv)

**与阶段一课题03 同源，但不是同一件工作。** 这批 24 组数据就是阶段一课题03 的实测结果——课题03 的考核要求止步于"提交数据表 + 照片 + 衰减分析"，产出是一张没人打开的 Excel。本作品解决的是它的下游问题：让数据变成同学手机上能用的工具，并用 7 天日志验证有没有人用。

| | 阶段一 课题03 | 本作品（阶段二 项目四） |
|---|---|---|
| 数据角色 | 数据本身即交付物 | 数据只是输入 |
| 考察能力 | 实地采样与数据分析 | 工具研发与真实使用验证 |
| 是否写代码 | 不要求 | 核心要求 |

完整的选题声明、8 个项目对照与新增工作量清单见 [`../README.md`](../README.md)。

## 使用方式

**推荐：直接访问线上地址**（手机可打开，这是收集 8 人反馈的唯一可行方式）
<https://xueqinzhan.github.io/ICEC-2026-0180-qinzhan/>

本地运行（仅本机有效，`file://` 路径发到手机上是打不开的——这正是阶段二最大的卡点，见 [`../../03-AI-Collaboration/04_手机打不开file协议.md`](../../03-AI-Collaboration/04_手机打不开file协议.md)）：

```bash
# 直接双击打开 src/index.html
# 或使用本地服务器
cd src
python -m http.server 8080
# 访问 http://localhost:8080
```

用户反馈页面：`src/feedback.html`（线上版在 `/feedback.html`）

## 项目结构

```
Campus-WiFi-Map/
├── src/                       开发版源码（改动从这里开始）
│   ├── index.html             # 主应用（含遥测日志系统）
│   ├── feedback.html          # 用户反馈表单
│   ├── sw.js                  # Service Worker（离线缓存）
│   ├── manifest.json          # PWA 配置
│   └── telemetry_logs_*.json  # ⚠️ 误放入 src 的一份日志副本，正式版已归档 process_logs/
├── data/
│   └── wifi_signal_raw.csv    # 原始测量数据（24组）
├── process_logs/              ★ 评分项① 12 份遥测日志 JSON 原始文件（417 条）
├── docs/                      空占位（实际部署目录是仓库根 ../docs/）
├── output/                    空占位
└── README.md
```

> **部署注意**：GitHub Pages 从**仓库根部的 `docs/`** 发布，不是这个目录下的 `docs/`。改完 `src/index.html` 必须复制到 `../../docs/index.html` 再推送，线上才会更新。

## 技术栈

- 纯 HTML + CSS + JavaScript（零依赖）
- SVG 楼层平面图
- Canvas 热力图渲染（IDW 插值算法）
- localStorage 数据持久化
- Service Worker 离线缓存
- TelemetryLogger 类（运行日志系统）
- Web Share API（v1.5 分享，含剪贴板降级）
- CSS 自定义属性 + `[data-theme]`（v1.3 深色模式）

## 作者

- **考生**：qinzhan
- **学号后四位**：0180
- **学校**：深圳城市职业学院
- **GitHub**：[ICEC-2026-0180-qinzhan](https://github.com/xueqinzhan/ICEC-2026-0180-qinzhan)
