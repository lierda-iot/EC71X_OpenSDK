# imageprocess 使用说明

`imageprocess` 是一个用于批量整理 Markdown 配图的小工具。

当前版本的处理逻辑是：

1. 选择 `.md` 文档
2. 选择图片目录
3. 填写图片名称前缀
4. 程序按图片目录中的文件名顺序，依次重命名图片
5. 同时按 Markdown 中图片标记出现的顺序，依次替换图片路径

这里特别注意：

- 不再要求 Markdown 里的原始图片链接必须和本地图片强匹配
- 即使 Markdown 中写的是远程链接 `https://...png`，也可以处理
- 只要 Markdown 里存在图片标记，就会按顺序替换

## 图片名称前缀有什么要求

要求很简单：

- 不能为空
- 建议使用简短、清晰的前缀，例如 `demo`、`step`、`device`

例如前缀填写 `demo`，重命名结果会是：

- `demo1.png`
- `demo2.jpg`
- `demo3.webp`

## 适用场景

适合下面这种情况：

- `.md` 文档里已经有一批图片标记
- 标记里的地址可能是旧路径，也可能是远程 URL
- 你本地另有一套真实图片文件
- 你希望按本地图片顺序统一重命名并替换 Markdown

例如：

```md
![image.png](https://example.com/a.png)
![image.png](https://example.com/b.png)
```

只要你选择的图片目录下有两张图片，程序就会按顺序处理。

## 支持的目录结构

图片目录支持：

- 根目录直接放图片
- 子文件夹放图片
- `_image` 或 `_images` 命名都可以

例如：

```text
_image/
  a.png
  b.jpg
```

或者：

```text
_image/
  doc_a/
    a.png
  doc_b/
    b.jpg
```

程序会递归搜索整个图片目录，并按名称自然排序处理。

## 支持的图片格式

- `.png`
- `.jpg`
- `.jpeg`
- `.bmp`
- `.gif`
- `.webp`
- `.tif`
- `.tiff`

## 当前替换规则

这是现在最重要的一条：

- 图片目录中的图片，按名称自然排序
- Markdown 中的图片标记，按从上到下顺序读取
- 两边一一对应，依次替换

例如：

图片目录里排序后是：

```text
1.png
2.png
10.png
```

Markdown 里有 3 个图片标记：

```md
![image.png](https://a.com/1.png)
![image.png](https://a.com/2.png)
![image.png](https://a.com/3.png)
```

那么会依次替换成：

```md
![](_image/demo1.png)
![](_image/demo2.png)
![](_image/demo3.png)
```

## 数量不一致时

如果出现：

- 图片目录里有 5 张图
- Markdown 中只有 3 个图片标记

或者反过来：

- Markdown 中有 5 个图片标记
- 图片目录里只有 3 张图

程序会先提示确认。

如果你继续：

- 只会按较小数量处理
- 也就是 `min(图片数量, Markdown 图片标记数量)`

## 处理结果示例

假设：

```text
demo.md
_image/
  doc_a/
    a.png
  doc_b/
    b.jpg
```

原 Markdown：

```md
![image.png](https://example.com/a.png)
![image.png](https://example.com/b.png)
```

如果前缀填写 `demo`，处理后可能变成：

```md
![](_image/doc_a/demo1.png)
![](_image/doc_b/demo2.jpg)
```

## 备份机制

在修改 Markdown 前，程序会自动生成：

```text
xxx.md.bak
```

建议正式处理前，也手动备份图片目录。

## 启动方式

### 运行 Python 源码

```powershell
python .\image_renamer_gui.py
```

### 运行 exe

```powershell
.\dist\ImageRenamerGUI.exe
```

## 当前版本重点

这版已经支持：

1. 新界面顺序：选择 `.md` -> 选择图片路径 -> 填写图片名称前缀。
2. 增加“导入图片”按钮。
3. 支持 `_image`、`_images` 以及子目录递归搜索。
4. 支持远程图片链接的 Markdown。
5. 处理逻辑改为“按顺序替换”，不再做强相关匹配。
