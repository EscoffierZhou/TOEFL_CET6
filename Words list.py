def create_html_word_row():
    """
    循环接收用户输入的单词信息，并生成HTML表格行代码。
    """
    print("--- HTML单词行生成器 ---")
    print("输入 'q' 并回车即可随时退出程序。")
    print("-" * 25)

    while True:
        # 接收用户输入
        word = input("请输入单词: ")
        if word.lower() == 'q':
            break

        phonetic = input("请输入音标: ")
        if phonetic.lower() == 'q':
            break

        definition = input("请输入释义: ")
        if definition.lower() == 'q':
            break

        example_en = input("请输入英文例句: ")
        if example_en.lower() == 'q':
            break

        example_zh = input("请输入中文例句: ")
        if example_zh.lower() == 'q':
            break

        # 使用 f-string 格式化生成 HTML 代码
        # 使用 .replace() 方法将例句中的单词和释义突出显示
        html_row = f"""
    <tr>
      <td><strong>{word}</strong></td>
      <td>/{phonetic}/</td>
      <td>{definition}</td>
      <td>
        <details>
          <summary>点击查看例句</summary>
          <p> </p>
          <p>{example_en.replace(word, f'<b>{word}</b>')}</p>
          <p>{example_zh.replace(definition, f'<b>{definition}</b>')}</p>
        </details>
      </td>
    </tr>
"""

        print("\n" + "=" * 10 + " 生成的HTML代码 " + "=" * 10)
        print(html_row.strip())
        print("=" * 35 + "\n")


if __name__ == "__main__":
    create_html_word_row()
"""
<table>
  <thead>
    <tr>
      <th>单词</th>
      <th>音标</th>
      <th>释义</th>
      <th>例句</th>
    </tr>
  </thead>
  <tbody>
  
  <tr>生成的代码<tr>
  
  </tbody>
</table>
  """