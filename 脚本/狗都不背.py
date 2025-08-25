import os
import time
import subprocess
import webbrowser

# 按顺序写入需要打开的文件/程序/网址
exe_paths = [
    r"F:\desktop\Work\_GitHub\TOEFL_CET6",                # 文件夹
    r"F:\desktop\Work\_GitHub\TOEFL_CET6\新东方TOEFL乱序版.pdf", # PDF
    r"F:\desktop\Work\_GitHub\TOEFL_CET6\Words list.py",   # Python 脚本
    "https://www.youdao.com/"                             # 网站
]

# 间隔秒数
delay = 0.5

for path in exe_paths:
    if path.startswith("http://") or path.startswith("https://"):
        print(f"正在打开网站: {path}")
        webbrowser.open(path)
    elif os.path.exists(path):
        print(f"正在启动: {path}")
        if path.lower().endswith(".exe"):
            subprocess.Popen(path)
        elif path.lower().endswith(".py"):
            subprocess.Popen(["python", path], shell=True)
        else:
            os.startfile(path)  # 文件夹 / pdf / txt / docx 等
    else:
        print(f"未找到文件: {path}")
    time.sleep(delay)
