#นับหัวเทียนดี
target = int(input("จะเก็บหัวเทียนเท่าไหร่: "))
good_spark = 0
while True:
    status = input("บอกสถานะหัวเทียน {ดี} {แตก} {เก่าเกิน}:")
    if status == "แตก" or status == "เก่าเกิน":
        print("โยนทิ้งไปโลดดดดด")
        continue
    good_spark += 1
    print(f"ของดีเก็บสิฟะะ ได้หัวเทียนดี {good_spark} แล้ว")
    if good_spark == target:
        print("เก็บครบล้าาา")
        break
print("กว่าจะครบเอาซะเหนื่อยเลออ")