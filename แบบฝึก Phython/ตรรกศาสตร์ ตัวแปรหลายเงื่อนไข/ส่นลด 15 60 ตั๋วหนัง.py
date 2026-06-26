print("ระบบขายตั๋วหนังโปรโมชั่น (No Loop)")

ticket_price = 200
popcorn_price = 120
total = ticket_price

age = int(input('กรุณาใส่อายุลูกค้า: '))
is_popcorn = int(input('รับป๊อปคอร์นไหม (1=รับ, 0=ไม่): '))


if age < 15 or age > 60:
    total = total - 50
    
if is_popcorn == 1:
    total = total + popcorn_price
print('ยอดรวมสุทธิที่ต้องจ่ายคือ:', total, 'บาท')