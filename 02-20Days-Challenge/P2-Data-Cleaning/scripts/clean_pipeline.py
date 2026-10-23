"""
P2 数据清洗管道
处理 ICEC 课题02（手机发热）和课题03（WiFi信号）的原始测量数据

清洗步骤：
1. 缺失值检测与处理
2. 异常值识别（IQR方法）
3. 数据类型标准化
4. 重复值检查
5. 数据质量评分
"""

import csv
import os
import sys
from datetime import datetime
from collections import defaultdict

# 添加项目根目录到路径
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


class DataCleaner:
    """数据清洗器"""

    def __init__(self, input_file, output_file, data_type):
        self.input_file = input_file
        self.output_file = output_file
        self.data_type = data_type  # 'phone' or 'wifi'
        self.raw_data = []
        self.clean_data = []
        self.headers = []
        self.quality_report = {
            'total_rows': 0,
            'missing_values': 0,
            'outliers': 0,
            'duplicates': 0,
            'quality_score': 0,
            'issues': []
        }

    def load_data(self):
        """加载原始数据"""
        with open(self.input_file, 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            self.headers = next(reader)
            self.raw_data = [row for row in reader]
        self.quality_report['total_rows'] = len(self.raw_data)
        print(f"加载数据：{len(self.raw_data)} 行")

    def check_missing_values(self):
        """检查缺失值"""
        missing_count = 0
        for row in self.raw_data:
            for val in row:
                if val.strip() == '' or val is None:
                    missing_count += 1

        self.quality_report['missing_values'] = missing_count
        if missing_count > 0:
            self.quality_report['issues'].append(f"发现 {missing_count} 个缺失值")
        print(f"缺失值：{missing_count}")

    def check_duplicates(self):
        """检查重复值"""
        seen = set()
        duplicates = 0
        for row in self.raw_data:
            row_tuple = tuple(row)
            if row_tuple in seen:
                duplicates += 1
            seen.add(row_tuple)

        self.quality_report['duplicates'] = duplicates
        if duplicates > 0:
            self.quality_report['issues'].append(f"发现 {duplicates} 个重复行")
        print(f"重复值：{duplicates}")

    def detect_outliers_iqr(self, column_idx):
        """使用IQR方法检测异常值"""
        values = []
        for row in self.raw_data:
            try:
                val = float(row[column_idx])
                values.append(val)
            except (ValueError, IndexError):
                continue

        if len(values) < 4:
            return []

        values.sort()
        q1 = values[len(values) // 4]
        q3 = values[3 * len(values) // 4]
        iqr = q3 - q1
        lower_bound = q1 - 1.5 * iqr
        upper_bound = q3 + 1.5 * iqr

        outliers = []
        for i, row in enumerate(self.raw_data):
            try:
                val = float(row[column_idx])
                if val < lower_bound or val > upper_bound:
                    outliers.append((i, val))
            except (ValueError, IndexError):
                continue

        return outliers

    def clean_phone_data(self):
        """清洗手机发热数据"""
        self.clean_data = []
        outlier_count = 0

        # 电量列索引：3，电池温度列索引：4
        battery_outliers = self.detect_outliers_iqr(3)
        temp_outliers = self.detect_outliers_iqr(4)

        for i, row in enumerate(self.raw_data):
            # 检查是否为异常值
            is_outlier = False
            if i in [x[0] for x in battery_outliers]:
                is_outlier = True
            if i in [x[0] for x in temp_outliers]:
                is_outlier = True

            if is_outlier:
                outlier_count += 1
                row.append('[异常值]')
            else:
                row.append('')

            self.clean_data.append(row)

        self.quality_report['outliers'] = outlier_count
        if outlier_count > 0:
            self.quality_report['issues'].append(f"发现 {outlier_count} 个异常值")

    def clean_wifi_data(self):
        """清洗WiFi信号数据"""
        self.clean_data = []
        outlier_count = 0

        # 信号强度列索引：4，延迟列索引：5
        signal_outliers = self.detect_outliers_iqr(4)
        latency_outliers = self.detect_outliers_iqr(5)

        for i, row in enumerate(self.raw_data):
            is_outlier = False
            if i in [x[0] for x in signal_outliers]:
                is_outlier = True
            if i in [x[0] for x in latency_outliers]:
                is_outlier = True

            if is_outlier:
                outlier_count += 1
                row.append('[异常值]')
            else:
                row.append('')

            self.clean_data.append(row)

        self.quality_report['outliers'] = outlier_count
        if outlier_count > 0:
            self.quality_report['issues'].append(f"发现 {outlier_count} 个异常值")

    def calculate_quality_score(self):
        """计算数据质量评分（0-100）"""
        total_cells = self.quality_report['total_rows'] * len(self.headers)
        missing_ratio = self.quality_report['missing_values'] / max(total_cells, 1)
        duplicate_ratio = self.quality_report['duplicates'] / max(self.quality_report['total_rows'], 1)
        outlier_ratio = self.quality_report['outliers'] / max(self.quality_report['total_rows'], 1)

        # 质量评分 = 100 - (缺失值惩罚 + 重复值惩罚 + 异常值惩罚)
        score = 100 - (missing_ratio * 30 + duplicate_ratio * 30 + outlier_ratio * 40)
        self.quality_report['quality_score'] = max(0, min(100, score))
        print(f"数据质量评分：{self.quality_report['quality_score']:.1f}/100")

    def save_clean_data(self):
        """保存清洗后的数据"""
        output_headers = self.headers + ['异常标记']
        with open(self.output_file, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(output_headers)
            writer.writerows(self.clean_data)
        print(f"清洗后数据已保存：{self.output_file}")

    def generate_report(self):
        """生成数据质量报告"""
        report_path = os.path.join(os.path.dirname(self.output_file), '..', 'docs', 'quality_report.md')
        os.makedirs(os.path.dirname(report_path), exist_ok=True)

        with open(report_path, 'w', encoding='utf-8') as f:
            f.write(f"# 数据质量评估报告\n\n")
            f.write(f"**生成时间**：{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
            f.write(f"**数据类型**：{'手机发热数据' if self.data_type == 'phone' else 'WiFi信号数据'}\n\n")
            f.write(f"## 数据概况\n\n")
            f.write(f"| 指标 | 值 |\n")
            f.write(f"|------|-----|\n")
            f.write(f"| 总行数 | {self.quality_report['total_rows']} |\n")
            f.write(f"| 缺失值数量 | {self.quality_report['missing_values']} |\n")
            f.write(f"| 重复行数 | {self.quality_report['duplicates']} |\n")
            f.write(f"| 异常值数量 | {self.quality_report['outliers']} |\n")
            f.write(f"| 数据质量评分 | {self.quality_report['quality_score']:.1f}/100 |\n\n")

            if self.quality_report['issues']:
                f.write(f"## 发现的问题\n\n")
                for issue in self.quality_report['issues']:
                    f.write(f"- {issue}\n")
                f.write(f"\n")

            f.write(f"## 清洗方法\n\n")
            f.write(f"1. **缺失值检测**：检查空值和None\n")
            f.write(f"2. **重复值检查**：基于行内容去重\n")
            f.write(f"3. **异常值识别**：使用IQR（四分位距）方法\n")
            f.write(f"   - Q1 = 第一四分位数\n")
            f.write(f"   - Q3 = 第三四分位数\n")
            f.write(f"   - IQR = Q3 - Q1\n")
            f.write(f"   - 异常值范围：< Q1 - 1.5*IQR 或 > Q3 + 1.5*IQR\n")

        print(f"质量报告已生成：{report_path}")

    def run(self):
        """执行完整清洗流程"""
        print(f"\n{'='*50}")
        print(f"开始清洗：{self.data_type} 数据")
        print(f"{'='*50}\n")

        self.load_data()
        self.check_missing_values()
        self.check_duplicates()

        if self.data_type == 'phone':
            self.clean_phone_data()
        else:
            self.clean_wifi_data()

        self.calculate_quality_score()
        self.save_clean_data()
        self.generate_report()

        print(f"\n{'='*50}")
        print(f"清洗完成！")
        print(f"{'='*50}\n")


def main():
    """主函数"""
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    data_dir = os.path.join(base_dir, 'data')
    output_dir = os.path.join(base_dir, 'output')

    os.makedirs(output_dir, exist_ok=True)

    # 清洗手机发热数据
    phone_cleaner = DataCleaner(
        input_file=os.path.join(data_dir, 'phone_heat_raw.csv'),
        output_file=os.path.join(output_dir, 'phone_heat_clean.csv'),
        data_type='phone'
    )
    phone_cleaner.run()

    # 清洗WiFi信号数据
    wifi_cleaner = DataCleaner(
        input_file=os.path.join(data_dir, 'wifi_signal_raw.csv'),
        output_file=os.path.join(output_dir, 'wifi_signal_clean.csv'),
        data_type='wifi'
    )
    wifi_cleaner.run()


if __name__ == '__main__':
    main()
