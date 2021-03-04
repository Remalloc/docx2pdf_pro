# docx2pdf_pro
在docx2pdf基础上做了交互增强并打包为可执行文件
## 快速开始
1. 下载release版本(.exe)
2. 运行 docx2pdf_pro.exe
3. 按提示输入文件或目录
4. 成功后输出到output文件夹
## 打包
1. 安装requirements.txt中的依赖
2. 将hook-docx2pdf.py放入PyInstaller/hooks中
3. pyinstaller -i"icon.ico" -F --upx-dir="upx目录(可选)" docx2pdf_pro.py