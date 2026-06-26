print('ยินต้อนรับ')
print('ทางร้านเรามีส่่วนลดพิเศษให้แก่ผู้ที่มีความสูงต่ำกว่า 120 เซน')
ss = int(input('กรุณาใส่ส่วนสูงของท่าน '))
cash = int(input('กรุณาใส่จำนวนเงินของท่าน '))
total_price = 399
if ss <= 120:
    total_price = 199
    print('ท่านได้รับส่วนลดพิเศษจ่ายเพียง 199 บาท')

if cash >= total_price:
    change = cash - total_price
    print('เงินทอนของท่านคือ:' , change, 'บาท' )
else:
    missing = total_price - cash
    print('เงินขาดอีก: ', missing, 'บาท')
    
    