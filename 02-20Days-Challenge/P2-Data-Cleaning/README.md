# P2: 数据清洗管道

## 项目概述
构建一个通用的数据清洗Python管道，处理来自ICEC课题02（手机发热）和课题03（WiFi信号）的原始测量数据。

## 交付物
1. **Python清洗管道** (`scripts/clean_pipeline.py`)
2. **数据可视化图表** (`output/` 目录)
3. **数据质量评估报告** (`docs/quality_report.md`)

## 项目结构
```
P2-Data-Cleaning/
├── data/           # 原始数据
│   ├── phone_heat_raw.csv
│   └── wifi_signal_raw.csv
├── scripts/        # 清洗脚本
│   └── clean_pipeline.py
├── output/         # 清洗后数据+图表
│   ├── phone_heat_clean.csv
│   ├── wifi_signal_clean.csv
│   └── *.png
── docs/           # 文档
│   └── quality_report.md
└── README.md
```

## 使用方法
```bash
python scripts/clean_pipeline.py
```

## 数据源
- 课题02：iPhone 15 Pro 多工况发热与掉电实测（4工况×2轮×7时间点=56组）
- 课题03：教学楼与宿舍WiFi信号盲区测绘（8点位×3轮=24组）

## 清洗步骤
1. 缺失值检测与处理
2. 异常值识别（IQR方法）
3. 数据类型标准化
4. 重复值检查
5. 数据质量评分

## 时间线
- 2026-10-23：项目启动
- 2026-11-10：完成清洗管道
- 2026-11-20：完成评估报告
- 2026-11-24：提交截止
