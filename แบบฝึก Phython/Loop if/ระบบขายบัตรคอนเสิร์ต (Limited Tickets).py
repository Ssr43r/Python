print("ระบบขายบัตรคอนเสิร์ต (Limited Tickets)")
ticket = 10
while ticket >0:
    buy =int(input('กรุณาใส่จำนวนบัตรที่ท่านต้องการซื้อ'))
    if buy <= ticket:
        ticket = ticket - buy 
        print('จำนวนบัตรที่ขายไปแล้ว: ' ,buy, 'จำนวนบัตรที่เหลือ: ' ,ticket,)
    else:
        print('บัตรไม่พอ!!! บัตรที่คุณต้องการซื้อ: ' ,buy, 'บัตรที่เราเหลือ: ' ,ticket,)
print('----บัตรขายหมดแล้วนะคะ---')