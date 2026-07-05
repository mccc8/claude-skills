# C4 SVG 视觉规范

## 颜色（C4 官方惯例）

| 元素 | 填充 | 描边 | 文字 |
|---|---|---|---|
| Person | #08427B | #052E56 | #fff |
| 本系统 System | #1168BD | #0B4884 | #fff |
| 外部系统 External | #999999 | #6B6B6B | #fff |
| Container | #438DD5 | #2E6295 | #fff |
| Component | #85BBF0 | #5D82A8 | #000 |
| 数据库/存储 | 同 Container，用圆柱形（cylinder） | | |

## 形状

- Person：圆头人形（圆 + 圆角矩形躯干）
- System/Container/Component：圆角矩形 rx=6
- 数据库：cylinder（椭圆顶 path）
- 系统边界：虚线圆角矩形包围，标签放左上角
- 关系：直线或折线 + 三角箭头 marker，标签白底衬垫避免压线

## 排版

- viewBox 建议 1200×800 起步，元素多时加高不加密
- 元素框：宽 200-240，高 90-110；框内三行文字居中：
  - 第1行 名称 font-weight:bold font-size:15
  - 第2行 类型标签 font-size:11 opacity:.8，如 `[Container: FastAPI]`
  - 第3行起 职责描述 font-size:12，最多2行，超长换行
- 字体：`font-family="-apple-system, 'PingFang SC', 'Helvetica Neue', sans-serif"`
- 布局方向：Person 在顶部，本系统居中，外部系统在两侧或底部；数据流自上而下
- 图例放右下角小框内

## 标题与图例

- 图顶部标题格式：`[C4-L2 容器图] <系统名>`，副标题一行说明范围
- 图例：颜色块 + 含义，最少覆盖图中出现的所有元素类型
