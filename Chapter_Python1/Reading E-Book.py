def auto_highlight_text(text, keyword):
    hl_text = text.replace(keyword, f"[{keyword}]")
    return hl_text

print("*** Reading E-Book ***")
text, keyword = input("Text , Highlight : ").split(',')

hl_text = auto_highlight_text(text, keyword)
print(hl_text)