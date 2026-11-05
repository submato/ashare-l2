# A 股 Level-2 历史行情数据

[![License: MIT](https://img.shields.io/badge/code%20%26%20docs-MIT-2ea44f.svg)](LICENSE)
[![Data Format](https://img.shields.io/badge/data-CSV-0969da.svg)](docs/schema.md)
[![Markets](https://img.shields.io/badge/markets-SSE%20%7C%20SZSE-d1242f.svg)](#数据集包含什么)

**ashare-l2 是中国 A 股 Level-2 历史行情数据的公开索引与格式样例**，覆盖沪深市场十档盘口快照、逐笔委托和逐笔成交 CSV，适合量化研究、市场微观结构分析、订单流研究与回测数据准备。

> English: ashare-l2 is an index and schema reference for China A-share Level-2 market data, including 10-level order book snapshots, order-by-order events and tick-by-tick trades.

[数据下载](#免费数据下载链接) · [字段说明](docs/schema.md) · [数据卡](docs/data-card.md) · [Python 读取示例](#如何读取-csv) · [常见问题](#常见问题) · [英文简介](#english-summary)

> [!IMPORTANT]
> 本 GitHub 仓库托管文档和 `DEMO.SZ` 演示样例，不托管全量历史行情。公开可下载月份以[数据表](#免费数据下载链接)为准；更长历史区间需联系作者确认。


## 免费数据下载链接

由于数据存储和持续更新成本，作者提供免费版与付费版。两个版本的数据内容一致，主要区别是更新时效：

- **免费版**：公开 2026 年至上一个完整月份的数据，例如 12 月更新至 11 月。数据会持续更新，欢迎 Star 本项目。
- **付费版**：提供 2017 年至今的历史数据和每日增量数据，每日 4–6 点更新当日数据。

下列月份均使用独立的永久分享链接，无需提取码。文件较大，建议下载后先校验目录、编码和字段，再批量导入数据库或回测系统。

| 数据月份 | 独立下载地址 | 提取码 | 链接状态 |
|---|---|---|---|
| 2026-01 | [夸克网盘下载](https://pan.quark.cn/s/1439ecef08b6) | 无 | 永久有效；2026-11-05 已验证 |
| 2026-02 | [夸克网盘下载](https://pan.quark.cn/s/116c0dfec6f8) | 无 | 永久有效；2026-11-05 已验证 |
| 2026-03 | [夸克网盘下载](https://pan.quark.cn/s/2f8a73f7a32b) | 无 | 永久有效；2026-11-05 已验证 |
| 2026-04 | [夸克网盘下载](https://pan.quark.cn/s/11c9d8e10984) | 无 | 永久有效；2026-11-05 已验证 |
| 2026-05 | [夸克网盘下载](https://pan.quark.cn/s/f72f854d5285) | 无 | 永久有效；2026-11-05 已验证 |
| 2026-06 | [夸克网盘下载](https://pan.quark.cn/s/0ca1466a2e09) | 无 | 永久有效；2026-11-05 已验证 |
| 2026-07 | [夸克网盘下载](https://pan.quark.cn/s/4bb79887578d) | 无 | 永久有效；2026-11-05 已验证 |
| 2026-08 | [夸克网盘下载](https://pan.quark.cn/s/3c0147a52fa6) | 无 | 永久有效；2026-11-05 已验证 |
| 2026-09 | [夸克网盘下载](https://pan.quark.cn/s/26f2b82e0cec) | 无 | 永久有效；2026-11-05 已验证 |
| 2026-10 | [夸克网盘下载](https://pan.quark.cn/s/b9ed1e0ba845) | 无 | 永久有效；2026-11-05 已验证 |
| 2026-11 | [夸克网盘下载](https://pan.quark.cn/s/a0ebe66949d5) | 无 | 永久有效；2026-11-05 已验证 |

需要其他日期、股票范围或更长历史区间，请联系 **lukalaoban@gmail.com**。历史 Level-2 在线获取项目正在开发中。

## 数据集包含什么？

A 股 Level-2 数据比基础 Level-1 行情提供更深的盘口和更细的事件粒度。本项目采用按证券、日期分区的 CSV 结构，每个交易日包含以下三类数据：

| 数据通道 | 文件名 | 主要内容 | 典型用途 |
|---|---|---|---|
| 十档行情快照 | `行情.csv` | 买卖各 10 档价格与数量、成交价量额、开高低前收等 | 盘口深度、价差、流动性、订单簿不平衡 |
| 逐笔委托 | `逐笔委托.csv` | 委托编号、买卖方向、委托价格、委托数量 | 订单流、挂单行为、撤单研究 |
| 逐笔成交 | `逐笔成交.csv` | 成交编号、成交价格与数量、买卖序号、成交/撤单标记 | 成交方向、冲击成本、事件级回测 |

**当前仓库样例包含 3 个 CSV、共 61 个行情字段、10 个委托字段和 12 个成交字段。** `DEMO.SZ` 是用于验证目录和解析流程的演示数据，不代表真实证券或完整交易日。完整字段表、编码和价格缩放说明见 [A-Share Level-2 Schema](docs/schema.md)。

## 数据覆盖范围

这里需要区分三个范围，避免把演示文件误认为完整数据集：

| 范围 | 覆盖情况 | 获取方式 |
|---|---|---|
| GitHub 演示样例 | `DEMO.SZ`，日期 `2025-01-02` | 直接克隆本仓库 |
| 当前公开下载 | `2026-01` 至 `2026-11`，每月独立链接 | 下方夸克网盘链接 |
| 作者维护的历史库存 | 沪深 A 股 `2017` 年至今；具体股票和交易日需确认 | 邮件联系作者 |

公开数据计划按存储条件滚动更新，实际可用月份始终以本 README 的下载表为准。

## 快速开始

### 1. 克隆演示数据

```bash
git clone https://github.com/submato/ashare-l2.git
cd ashare-l2
```

目录按证券代码和交易日组织：

```text
data/
  {SYMBOL}/                 # 例如 300476.SZ
    l2/
      YYYYMMDD/
        行情.csv            # 十档盘口快照
        逐笔委托.csv         # Order-by-order
        逐笔成交.csv         # Tick-by-tick
```

### 2. 如何读取 CSV？

仓库中的 `DEMO.SZ` 样例使用 UTF-8；历史文件常见 GBK 编码。下面的读取函数会依次尝试两种编码：

```python
from pathlib import Path

import pandas as pd


def read_l2_csv(path):
    for encoding in ("utf-8-sig", "gb18030"):
        try:
            return pd.read_csv(path, encoding=encoding)
        except UnicodeDecodeError:
            continue
    raise ValueError(f"Unsupported CSV encoding: {path}")


quotes = read_l2_csv("data/DEMO.SZ/l2/20250102/行情.csv")
orders = read_l2_csv("data/DEMO.SZ/l2/20250102/逐笔委托.csv")
trades = read_l2_csv("data/DEMO.SZ/l2/20250102/逐笔成交.csv")
```

> [!CAUTION]
> Wind 风格导出中的价格常见为整数乘以 `10000`（例如 `420900` 可能表示 `42.09`），但不同来源的单位和标记值可能不同。请先核对数据源说明和抽样记录，不要直接对所有价格字段执行固定缩放。

## 适合哪些研究场景？

- **量化交易与高频研究**：构造价差、盘口斜率、订单簿不平衡、主动买卖等因子。
- **市场微观结构分析**：研究流动性、价格发现、撤单行为和订单流毒性。
- **事件级回测**：用逐笔委托和逐笔成交重建事件序列；是否能重建完整订单簿取决于数据源字段完整性。
- **机器学习特征工程**：从十档快照和 tick 数据生成时序、深度与成交特征。
- **数据工程测试**：验证 GBK/UTF-8 CSV 解析、日分区导入、列式存储转换与质量检查流程。

本仓库不提供交易建议、收益保证或可直接用于实盘的策略。Level-2 历史数据也可能包含停牌、缺失记录、异常值、复权差异和数据源特有编码，研究前应执行质量检查。

## 数据质量与许可

- **来源与格式**：文档描述的是 Wind 风格 CSV；不同导出批次可能存在字段、编码或单位差异。
- **演示数据**：`DEMO.SZ` 仅用于展示结构和解析方式，不能用于投资研究结论。
- **代码与文档许可**：本仓库代码和文档采用 [MIT License](LICENSE)。
- **行情数据权利**：MIT License 不自动覆盖交易所或数据商提供的行情数据。下载、再分发、商用或公开展示前，请自行确认交易所、供应商和所在地区的授权要求。
- **维护与勘误**：字段解释或链接有误时，可提交 Issue；数据范围与获取问题请发送邮件。

更完整的数据来源、局限和推荐用途见 [数据卡（Data Card）](docs/data-card.md)。

## 常见问题

### 这个仓库提供免费的 A 股 Level-2 数据吗？

是。仓库免费提供可直接克隆的演示样例，并在[下载表](#免费数据怎么下载)中列出当前公开共享的数据月份。GitHub 不承载全量历史文件；其他日期和股票范围需要联系作者确认。代码与文档使用 MIT License，行情数据本身可能受独立授权条款约束。

### 数据是否覆盖上海证券交易所和深圳证券交易所？

作者维护的历史库存描述为沪深 A 股 2017 年至今，因此目标范围包括上海和深圳市场。公开下载包是否包含某只股票、某个市场或某个交易日，应以实际文件清单为准，并在使用前抽样验证。

### Level-1 和 Level-2 行情有什么区别？

Level-1 通常只提供较浅的最优买卖报价和基础成交信息；Level-2 可提供更深的多档盘口，以及逐笔委托、逐笔成交等更细粒度事件。本项目记录十档买卖盘，并分别存储行情快照、逐笔委托和逐笔成交。

### 可以直接用于实盘或商业产品吗？

不建议未经验证直接用于实盘。使用者需要检查完整性、时间排序、价格单位、异常值和授权范围。商业使用尤其需要确认行情数据的交易所与供应商许可；仓库的 MIT License 只适用于代码和文档。

### 如何引用这个数据仓库？

GitHub 会识别仓库根目录的 [`CITATION.cff`](CITATION.cff)。引用时建议注明仓库名称、URL、访问日期，以及实际使用的数据月份、股票范围和数据来源。

<a id="english-summary"></a>

<details>
<summary><strong>English summary</strong></summary>

**ashare-l2 documents and indexes historical Level-2 data for China A-shares.** The repository contains a synthetic `DEMO.SZ` sample with 10-level order book snapshots, order-by-order records and tick-by-tick trades in daily CSV partitions. The repository itself does not host the complete historical archive.

- **Markets:** Shanghai Stock Exchange (SSE) and Shenzhen Stock Exchange (SZSE), subject to archive availability.
- **Maintainer-stated coverage:** 2017 to present; confirm exact symbols and trading dates before purchase or research.
- **Public download currently listed:** January-November 2026, with one permanent link per month.
- **Formats:** Wind-style CSV; historical files are commonly GBK encoded, while the included demo is UTF-8.
- **Use cases:** quantitative finance, limit order book research, market microstructure, order flow analysis, high-frequency data engineering and event-driven backtesting.
- **Important limitation:** market-data licensing is separate from the MIT license covering repository code and documentation.

For field definitions, see the [schema reference](docs/schema.md). For provenance, intended use and limitations, see the [data card](docs/data-card.md).

</details>

## 存储建议

完整 Level-2 数据体积很大，普通 Git 仓库不适合保存全量历史。GitHub 建议单文件保持在 50 MB 以下，并拒绝大于 100 MB 的普通 Git 对象。大规模数据应使用 Git LFS、GitHub Releases 或 OSS/S3/R2 等对象存储，本仓库只维护索引、文档和小型样例。

## 贡献与联系

- 字段修正、解析示例和文档改进：提交 [Issue](https://github.com/submato/ashare-l2/issues) 或 Pull Request。
- 数据范围、下载和合作：**lukalaoban@gmail.com**
- Repository: <https://github.com/submato/ashare-l2>
