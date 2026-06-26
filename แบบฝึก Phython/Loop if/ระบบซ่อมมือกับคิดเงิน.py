print('การคิดเงิน \nจอแตก: 700 THB\nแบตเสื่อม: 300 THB\nเปิดไม่ติด: 1500 THB')
queue = int(input("จำนวนลูกค้า:"))
total_money = 0
while queue > 0:
    symptom = input("ใส่อาการเสีย: ")
    if symptom == "จอแตก":
        total_money = total_money + 700
        print("เปลี่ยนจอ 700 THB")
    elif symptom == "แบตเสื่อม":
        total_money = total_money + 300
        print("เปลี่ยนแบต 300 THB")
    else:
        total_money = total_money + 1500
        print("เช็คบอร์ดอย่างละเอียด 1,500 THB")
    queue = queue - 1
    print(f"จำนวนลูกค้าที่เหลือ: {queue} ")
print("รายได้ของวันนี้คืิอ:", total_money,)
print("---ลูกค้าหมดแล้วปิดร้านน---")