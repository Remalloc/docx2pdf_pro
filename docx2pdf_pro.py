import os
import sys

from docx2pdf import cli


def pre_print(*msg, end="\n", flush=True):
    print("->", *msg, end=end, flush=flush)


def pre_input(msg: str, type_: type):
    pre_print(msg)
    data = input()
    try:
        data = type_(data)
    except ValueError:
        pre_print("输入格式错误!")
        return None
    else:
        return data


def main():
    input_path = pre_input("请输入要转换为pdf的文件或目录:", str)
    input_path = os.path.abspath(input_path)
    output_path = os.path.join(input_path, "output")
    if not os.path.exists(input_path):
        pre_print("文件或目录不存在")
    else:
        if not os.path.exists(output_path):
            os.mkdir(output_path)
        if os.path.isfile(input_path):
            pre_print(f"转换的文件为 {input_path}")
            sys.argv.append(input_path)
            cli()
        else:
            pre_print(f"转换的目录为 {input_path}")
            argv = [sys.argv[0], None, None]
            for f in filter(lambda x: x.endswith(".docx"), os.listdir(input_path)):
                argv[1], argv[2] = os.path.join(input_path, f), output_path
                sys.argv = argv
                cli()
        pre_print(f"转换完成, 输出目录为 {output_path}")
        input("按任意键退出...")


if __name__ == "__main__":
    main()
