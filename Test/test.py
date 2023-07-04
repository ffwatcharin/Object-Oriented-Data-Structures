def highlight_text(text, keyword):
    highlighted_text = text.replace(keyword, f"[{keyword}]")
    return highlighted_text

# รับข้อความ
text = input("กรุณากรอกข้อความ: ")

# รับคำที่ต้องการ Auto Highlight
keyword = input("กรุณากรอกคำที่ต้องการ Auto Highlight: ")

# แสดงผลลัพธ์
highlighted_text = highlight_text(text, keyword)
print("ผลลัพธ์:")
print(highlighted_text)
