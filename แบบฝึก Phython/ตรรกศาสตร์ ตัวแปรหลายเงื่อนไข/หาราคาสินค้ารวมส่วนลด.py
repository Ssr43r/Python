print('---ยินดีต้อนรับเข้าสู่ร้านขายเสื้อผ้ามือสอง---')
print('วันนี้ร้านเรามี Promotion ซื้อครบจำนวน ราคาถึง รับส่วนจากเราไปได้เลย\n1.ถ้าซื้อครบ 3 ชิ้น ขึ้นไป "และ" ราคารวม มากกว่า 1,000 บาท -> ลดทันที 200 บาท\n2.ซื้อครบ 3 ชิ้น ขึ้นไป "และ" ราคารวม มากกว่า 500 บาท -> ลดทันที 50 บาท')
#ประกาศตัวแปร
amount = int(input('กรุณาใส่จำนวนสินค้าของท่าน'))
total_price = int(input('กรุณาใส่ราคาสินค้าของท่าน'))
#เงื่อนไข
if amount >= 3 and total_price > 1000:
    discount = 200
    final_price = total_price * amount - discount
    print('ท่านซื้อครบตามจำนวนท่านได้รับส่วนลดพิเศษจำนวน 200 บาท')
    print('ราคารวมของท่านคือ: ' , final_price, 'บาท')
    print('---ขอบคุณที่ใช้บริการครับ---')
elif total_price > 500:
    discount = 50
    final_price = total_price * amount - discount
    print('ท่านซื้อครบตามจำนวนท่านได้รับส่วนลดพิเศษจำนวน 50 บาท')
    print('ราคารวมของท่านคือ: ' , final_price, 'บาท')
    print('---ขอบคุณที่ใช้บริการครับ---')
else:
    discount = 0
    final_price = total_price * amount - discount
    print('ราคารวมของท่านคือ: ' , final_price, 'บาท')
    print('---ขอบคุณที่ใช้บริการครับ---')