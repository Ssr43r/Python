print('หาแม่สูตรคูณอัตโนมัติ')
i = int(input('กรุณาใส่แม่สูตรที่คุณอยากรู้: '))
o = 1
e = int(input('ใส่จำนวนที่ห้องการคูณ: '))
while o <= e :
    total = i * o
    print(i,'x' ,o,'=' ,total,)
    o = o + 1
print(f'ค่าที่ท่านอยากรู้คือ {i} x {e} = {total}')