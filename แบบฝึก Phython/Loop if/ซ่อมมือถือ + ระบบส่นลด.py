queue = int(input('จำนวนคิว: '))
total = 0
while queue > 0:
    symptom = str(input('ลูกค้าจะซ่อมอะไรบ้าง: '))
    if symptom == 'จอแตก':
        total = total + 700
        print('เปลี่ยนจอ 700 THB')
    elif symptom == 'แบตเสื่อม':
        total = total + 300
        print('เปลี่ยนแบต 300 THB')
    else:
        total = total + 1500
        print('อาการไม่ชัดเจนต้องเช็คบอร์ดอย่างละเอียด 1500 THB')
    queue = queue - 1
if total >= 1000:
    final_price = total * 0.9
    print(f'ลูกค้าใช้บริการครบตามเงื่อนไขทางร้านจึงลดราคาให้ 10% \nราคาเต็มคือ {total} THB\nราคารวมส่วนลดคือ {final_price} THB')
else:
    print(f'ลูกค้าใช้บริการไม่ครบตามเงื่อนไขจึงต้องจ่านราคาเต็ม {total} THB')
print('เคลียร์รายต่อไปมาเลยจ้าา จ้าาาา')