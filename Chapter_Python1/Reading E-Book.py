# กฤษฎากำลังอ่านหนังสืออิเล็กทรอนิกส์เพื่อเตรียมสอบอยู่ในห้องสมุดของโรงเรียนชื่อดังประจำจังหวัดแห่งหนึ่ง แล้วก็มีความคิดผุดหนึ่งขึ้น
# มาในหัวของกฤษฎา ถ้าหากสามารถ Auto Highlight คำที่ต้องการจาก Text ได้ก็คงจะดีไม่น้อย แต่กฤษฎาไม่รู้จะทำอย่างไรดี กฤษฎาจึงอยาก
# จะไหว้วานคุณให้ช่วยเขียนโปรแกรมในการ Highlight Text แบบที่กฤษฎาต้องการ

def auto_highlight_text(text, keyword):
    hl_text = text.replace(keyword, f"[{keyword}]")
    return hl_text

print("*** Reading E-Book ***")
text, keyword = input("Text , Highlight : ").split(',')

hl_text = auto_highlight_text(text, keyword)
print(hl_text)