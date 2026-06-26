car_list = []
print('---ระบบบันทึกรถเข้าอู่---')
while True:
    brand = input('รถแบรนด์ไหนขับเข้ามาไหนอู่: ')
    print('พิมพ์ stop เพื่อหยุดโปรแกรม')
    if brand == 'stop':
        break
    car_list.append(brand)
    print(f"บันทึก {brand} ลงระบบเรียบร้อย")
    print(f'ตอนนี้มีรถในอู่มี: {len(car_list)} คัน \nได้แก่: {car_list}')
print("---สรุปยอดวันนี้---")
print(f"วันนี้แต่งรถไปทั้งหมด: {len(car_list)} คัน\nได้แก่: {car_list}")