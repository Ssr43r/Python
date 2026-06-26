print('---ระบบเติมเงิน---')

balance = 0
while balance < 100:
    topup = int(input('กรุณาใส่จำนวนเงินที่ท่านต้องการเติม: '))
    balance = balance + topup
    print('ตอนนี้คุณมีเงินสะสมจำนวน' , balance, 'THB')
print('คุณมีจำนวนเงินครบแล้ว')
print('---ขอบคุณที่ใช้บริการครับ---')
