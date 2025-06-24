#!/usr/bin/env python3
"""
文件扫描工具 - 扫描指定文件夹下的所有常见文件格式，将文件名和内容合并为一个txt文件
"""

import os
import argparse
from pathlib import Path
from typing import List, Set

# # 常见文件后缀列表
# COMMON_EXTENSIONS = {
#     '.txt', '.md', '.py', '.js', '.ts', '.html', '.css', '.json', 
#     '.xml', '.yaml', '.yml', '.ini', '.cfg', '.conf', '.log',
#     '.sh', '.bat', '.ps1', '.sql', '.java', '.c', '.cpp', '.h',
#     '.cs', '.php', '.rb', '.go', '.rs', '.swift', '.kt', '.scala',
#     '.r', '.m', '.pl', '.lua', '.dart', '.vue', '.jsx', '.tsx',
#     '.scss', '.sass', '.less', '.styl', '.coffee', '.toml'
# }

# 常见文件后缀列表
COMMON_EXTENSIONS = {
    '.py',  # Python 文件
    '.js',  # JavaScript 文件
    '.html', # HTML 文件
    '.css', # CSS 样式表文件
    '.md'   # Markdown 文件
}

def get_file_content(file_path: Path) -> str:
    """读取文件内容，处理编码问题"""
    encodings = ['utf-8', 'gbk', 'gb2312', 'latin1']
    
    for encoding in encodings:
        try:
            with open(file_path, 'r', encoding=encoding) as f:
                return f.read()
        except UnicodeDecodeError:
            continue
        except Exception as e:
            return f"[无法读取文件: {str(e)}]"
    
    return "[无法解码文件内容]"

def scan_directory(directory: Path, extensions: Set[str] = None) -> List[Path]:
    """扫描目录下所有指定后缀的文件"""
    if extensions is None:
        extensions = COMMON_EXTENSIONS
    
    files = []
    for root, dirs, filenames in os.walk(directory):
        for filename in filenames:
            file_path = Path(root) / filename
            if file_path.suffix.lower() in extensions:
                files.append(file_path)
    
    return sorted(files)

def create_combined_file(files: List[Path], output_path: Path, base_dir: Path):
    """将所有文件内容合并到一个txt文件中"""
    with open(output_path, 'w', encoding='utf-8') as output_file:
        output_file.write(f"文件扫描结果 - 共 {len(files)} 个文件\n")
        output_file.write("=" * 80 + "\n\n")
        
        for i, file_path in enumerate(files, 1):
            relative_path = file_path.relative_to(base_dir)
            
            output_file.write(f"[{i:04d}] 文件: {relative_path}\n")
            output_file.write("-" * 80 + "\n")
            
            content = get_file_content(file_path)
            output_file.write(content)
            
            output_file.write("\n\n" + "=" * 80 + "\n\n")

def main():
    parser = argparse.ArgumentParser(description='扫描文件夹并合并文件内容到txt文件')
    parser.add_argument('directory', help='要扫描的文件夹路径')
    parser.add_argument('-o', '--output', default='combined_files.txt', 
                       help='输出文件名 (默认: combined_files.txt)')
    parser.add_argument('-e', '--extensions', nargs='*',
                       help='指定文件后缀 (例如: .py .js .txt)')
    
    args = parser.parse_args()
    
    # 验证输入目录
    directory = Path(args.directory)
    if not directory.exists():
        print(f"错误: 目录 '{directory}' 不存在")
        return
    
    if not directory.is_dir():
        print(f"错误: '{directory}' 不是一个目录")
        return
    
    # 设置文件后缀
    extensions = COMMON_EXTENSIONS
    if args.extensions:
        extensions = {ext if ext.startswith('.') else f'.{ext}' for ext in args.extensions}
        print(f"使用指定后缀: {', '.join(sorted(extensions))}")
    else:
        print(f"使用默认后缀: {', '.join(sorted(list(extensions)[:10]))} ...")
    
    # 扫描文件
    print(f"扫描目录: {directory.absolute()}")
    files = scan_directory(directory, extensions)
    
    if not files:
        print("未找到匹配的文件")
        return
    
    print(f"找到 {len(files)} 个文件")
    
    # 生成输出文件
    output_path = Path(args.output)
    create_combined_file(files, output_path, directory)
    
    print(f"文件已保存到: {output_path.absolute()}")
    print(f"文件大小: {output_path.stat().st_size / 1024:.1f} KB")

if __name__ == '__main__':
    main()