from setuptools import setup

setup(
    name="file-scanner",
    version="1.0.0",
    description="扫描文件夹并合并文件内容的工具",
    py_modules=["file_scanner"],
    entry_points={
        "console_scripts": [
            "filescan=file_scanner:main",
        ],
    },
    python_requires=">=3.6",
)