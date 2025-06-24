# 文件扫描工具

一个用于扫描指定文件夹下所有常见文件格式，并将文件名和内容合并为一个txt文件的Python工具。

**作者**: Venussci  
**版本**: 1.0.0  
**许可证**: MIT License

## 功能特性

- 🔍 **智能扫描**: 扫描指定目录下的所有指定格式文件
- 📁 **多格式支持**: 支持多种常见文件格式（Python、JavaScript、HTML、CSS、Markdown等）
- 🔧 **自定义后缀**: 可以指定特定的文件后缀进行扫描
- 📝 **内容合并**: 将所有文件内容合并到一个txt文件中
- 🌍 **编码兼容**: 自动处理多种编码格式（UTF-8、GBK、GB2312、Latin1）
- 📊 **统计信息**: 显示扫描结果统计和文件大小

## 安装

### 方法1: 直接运行
```bash
python file_scanner.py [参数]
```

### 方法2: 安装为命令行工具
```bash
pip install -e .
filescan [参数]
```

## 使用方法

### 基本用法
```bash
# 扫描当前目录
python file_scanner.py .

# 扫描指定目录
python file_scanner.py /path/to/directory

# 指定输出文件名
python file_scanner.py /path/to/directory -o my_output.txt
```

### 高级用法
```bash
# 指定特定文件扩展名
python file_scanner.py /path/to/directory -e .py .js .html

# 扫描多种格式
python file_scanner.py /path/to/directory -e py js html css md txt

# 完整示例
python file_scanner.py ./my_project -o project_files.txt -e .py .js .html .css
```

## 命令行参数

| 参数 | 说明 | 示例 |
|------|------|------|
| `directory` | 要扫描的文件夹路径（必需） | `./my_project` |
| `-o, --output` | 输出文件名（默认：combined_files.txt） | `-o result.txt` |
| `-e, --extensions` | 指定文件后缀（可多个） | `-e .py .js .html` |

## 默认支持的文件格式

- `.py` - Python文件
- `.js` - JavaScript文件  
- `.html` - HTML文件
- `.css` - CSS样式表文件
- `.md` - Markdown文件

## 输出格式

生成的txt文件包含：
- 文件统计信息
- 每个文件的相对路径
- 文件完整内容
- 文件分隔符

输出示例：
```
文件扫描结果 - 共 15 个文件
================================================================================

[0001] 文件: src/main.py
--------------------------------------------------------------------------------
#!/usr/bin/env python3
# 文件内容...

================================================================================

[0002] 文件: src/utils.py
--------------------------------------------------------------------------------
# 工具函数...
```

## 注意事项

1. **编码处理**: 工具会自动尝试多种编码格式读取文件
2. **大文件**: 对于大型项目，生成的txt文件可能会很大
3. **权限**: 确保有足够权限读取目标目录中的文件
4. **二进制文件**: 工具只处理文本文件，二进制文件会被跳过

## 故障排除

### 常见问题

**Q: 提示"目录不存在"**
A: 检查输入的目录路径是否正确，使用绝对路径或相对路径

**Q: 没有找到文件**
A: 检查目录下是否有指定格式的文件，或使用 `-e` 参数指定其他文件格式

**Q: 文件内容显示乱码**
A: 工具会自动尝试多种编码，如果仍有问题，可能是特殊编码格式

## 使用场景

- 📋 **代码审查**: 将项目代码合并到一个文件中便于审查
- 📖 **文档整理**: 收集项目中的所有文档文件
- 🔍 **内容分析**: 对项目文件进行统一分析
- 📦 **备份整理**: 将重要文件内容合并备份

## 系统要求

- Python 3.6+
- 支持的操作系统：Windows、macOS、Linux

## 版权信息

**作者**: Venussci  
**版权**: © 2024 Venussci. All rights reserved.  
**许可证**: MIT License

## 许可证协议

MIT License

Copyright (c) 2024 Venussci

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

## 免责声明

本软件仅供学习和研究使用。使用者需要：

1. **合法使用**: 确保扫描的文件和目录具有合法的访问权限
2. **隐私保护**: 不得扫描包含他人隐私信息的文件
3. **版权尊重**: 尊重扫描文件的版权，不得用于商业用途（除非获得授权）
4. **责任自负**: 使用本工具产生的任何后果由使用者自行承担

## 贡献指南

欢迎提交 Issue 和 Pull Request 来改进这个工具！

1. Fork 本项目
2. 创建特性分支 (`git checkout -b feature/AmazingFeature`)
3. 提交更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 开启 Pull Request

## 联系方式

如有问题或建议，请通过以下方式联系：

- **作者**: Venussci
- **创建时间**: 2025

---

*本项目遵循 MIT 开源协议，欢迎自由使用和修改。*