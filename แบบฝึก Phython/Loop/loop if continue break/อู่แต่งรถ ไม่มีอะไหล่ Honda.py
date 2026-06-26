#อู่แต่งรถ ไม่มีอะไหล่ Honda
print('---ยินดีต้อนรับเข้าสู่อู่ไปเรื่อย---')
stock = 3
while True:
    brand = input('กรอก brand รถที่ขับมาแต่ง: ')
    if brand == "honda":
        print('ขออภัย Honda อะไหล่หมดครับพี่!!!')
        continue
    stock -=1
    print(f'{brand} ปรับแต่งอะไหล่เรียบร้อย')
    print(f'stock ที่เหลือ: {stock}')
    if stock == 0:
        print('อะไหล่หมดแล้ว รอของมาส่งง')
        break
print('----ปิดอู่แล้วจ้าาา---')