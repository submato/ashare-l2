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

## 当前内容

- `data/DEMO.SZ/`：合成样例（非真实行情），用于说明目录格式

把本地数据放进 `data/` 后提交即可，例如：

```bash
cp -R ~/Documents/stockdata/300476.SZ data/
git add data/300476.SZ
git commit -m "Add 300476.SZ Level-2 history"
git push
```

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
