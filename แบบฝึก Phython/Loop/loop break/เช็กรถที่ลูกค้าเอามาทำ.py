stock = 4
while True:
    car_model = input('รถที่ลูกค้าเอาทำ: ')
    stock -= 1
    print(f'Stock คงเหลือ: {stock}')
    if stock == 0:
        print('stock เต็มแล้วว')
        break
print("ปิดร้านนน")