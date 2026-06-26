target = int(input('จะเอา turbo กี่ลูก: '))
good_turbo = 0
while True:
    status = input("บอกสถานะของ turbo {ดี/เสีย}: ")
    if status == "ดี":
        print("ดีเก็บไว้ก่อนน")
        good_turbo +=1
        print(f"เก็บ turbo ได้แล้ว {good_turbo} ลูก")
        
    elif status == 'เสีย':
        print("เสียก็โยนทิ้งจ้าาา")
        continue
    else:
        print("อ่านดิ กวนตีนอ่ออ")
            
    if good_turbo == target:
        print("ครบแล้วจ้าาา")
        break
print("พอพักก่อนนน")      