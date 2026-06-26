#เก็บไอเทมในเกม
backpack = []
storage = 3
while True:
    take = input('ได้ของอะไรมา: ')
    if 'ระเบิด' in take:
        type_bomb = input ('ระเบิดอะไร(ระเบิดชนวน/ระเบิดมือ) :')
    if type_bomb == 'ระเบิดมือ':
        print('ปลอดภัยเก็บเข้ากระเป๋า')
        
    elif type_bomb == 'ระเบิดชนวน':
        print("ระวัง!!! เก็บระเบิดมาแล้ววว")
        print('เอาทิ้งง')
        continue
    else:
        print('ไม่รู้จัก ไม่เก็บจ้าาา')
        continue
    storage -=1
    backpack.append(take)
    print(f'เก็บ {take} เข้ากระเป๋าแล้ว')
    print(f'ของที่มีในกระเป๋า: {backpack}')
    print(f'มีของในกระเป๋าทั้งหมด: {len(backpack)} ชิ้น')
    print(f'กระเป๋าเหลือที่ว่างอีก: {storage} ช่อง')
    if storage == 0:
        print('กระเป๋าของผู้เล่นเต็มแล้วว')
        break    