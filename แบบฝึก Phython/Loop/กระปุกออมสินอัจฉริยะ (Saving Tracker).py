print("กระปุกออมสินอัจฉริยะ (Saving Tracker)")
day = 1
total = 0
while day <= 5:
    money = int(input('ใส่จำนวนเงินวันที่' + str(day) + ':'))
    total = total + money
    day = day +1
print("สรุปยอดเงินออมทั้งหมดของคุณคือ:", total, "บาท")