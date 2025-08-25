import sys
import pyperclip  # 用于复制到剪贴板

def create_html_word_row():
    """
    循环接收用户输入的单词信息，并生成HTML表格行代码。
    支持多个释义+词性、IO刷新、中文输入。
    """
    # 确保标准输入输出支持中文
    sys.stdin.reconfigure(encoding="utf-8")
    sys.stdout.reconfigure(encoding="utf-8")

    print("--- HTML单词行生成器 ---")
    print("输入 'q' 并回车即可随时退出程序。")
    print("-" * 25)
    sys.stdout.flush()

    while True:
        # 接收用户输入
        word = input("请输入单词: ")
        if word.lower() == 'q':
            break

        phonetic = input("请输入音标: ")
        if phonetic.lower() == 'q':
            break

        # 处理多个释义和词性
        definitions = []
        while True:
            definition = input("请输入释义 (输入d进入下一项): ")
            if definition.lower() == 'q':
                return
            if definition.lower() == 'd':
                break

            pos = input("请输入词性: ")
            if pos.lower() == 'q':
                return

            definitions.append((pos, definition))

        example_en = input("请输入英文例句: ")
        if example_en.lower() == 'q':
            break

        example_zh = input("请输入中文例句: ")
        if example_zh.lower() == 'q':
            break

        ex = input("请输入派生词: ")
        if ex.lower() == 'q':
            break

        # 构造释义HTML
        definitions_html = "<br>".join([f"<i>{pos}</i> {definition}" for pos, definition in definitions])

        # 使用 f-string 格式化生成 HTML 代码
        html_row = f"""
    <tr>
      <td><strong>{word}</strong></td>
      <td>/{phonetic}/</td>
      <td>{definitions_html}</td>
      <td>
        <details>
          <summary>点击查看例句</summary>
          <p> </p>
          <p>{example_en.replace(word, f'<b>{word}</b>')}</p>
          <p>{example_zh}</p>
        </details>
      </td>
      <td>{ex}</td>
    </tr>
"""

        # 输出到终端
        print("\n" + "=" * 10 + " 生成的HTML代码 " + "=" * 10)
        print(html_row.strip())
        print("=" * 35 + "\n")

        # 自动复制到剪贴板
        pyperclip.copy(html_row.strip())
        print("✅ 已复制到剪贴板！")

        sys.stdout.flush()


if __name__ == "__main__":
    create_html_word_row()
