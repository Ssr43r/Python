print('---เครื่องคิดเงินและทวงตังค์---')
price = int(input('ใส่ราคาสินค้า'))
cash = int(input('เงินที่รับมา'))
if cash >= price:
    change = cash - price
    print ('เงินทอน: ', change)
else: missing = price - cash
print('เงินไม่พอขาดอีก: '  , missing)