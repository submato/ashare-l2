# ashare-l2 — China A-Share Level-2 Data

中国 A 股 Level-2 原始数据仓库：十档快照、逐笔委托、逐笔成交。

## 目录结构

```text
data/
  {SYMBOL}/                 # 例如 300476.SZ
    l2/
      YYYYMMDD/
        行情.csv            # 十档快照
        逐笔委托.csv
        逐笔成交.csv
```

字段说明见 [docs/schema.md](docs/schema.md)。

## 数据

目前有的数据 沪深2017-至今 level2 十档数据。

由于存储原因，免费共享最近2个月数据，后续将补充更多数据，需要更多数据请联系作者邮箱：lukalaoban@gmail.com。

在线获取历史level2项目也正在开发中。

| 日期 | 链接 |
|------|------|
| 202605-202606 | 夸克网盘：https://pan.quark.cn/s/8bae13aef6a9?pwd=Gxcc；提取码：Gxcc |

## 体积提醒

完整 L2 通常很大（单票一年常见数 GB～十几 GB）。GitHub 普通 git 不适合直接塞满仓历史：

| 限制 | 说明 |
|------|------|
| 单文件 | 建议 < 50MB；硬上限 100MB |
| 仓库 | 建议尽量 < 1GB |

若要上传真实全量，优先考虑：

1. **Git LFS**（仍受配额限制）
2. **GitHub Releases** 挂压缩包
3. **对象存储**（OSS / S3 / R2）+ 本仓库只放索引与说明

## License

代码与文档：MIT。行情数据本身可能另有交易所 / 数据商授权限制，公开前请自行确认。
