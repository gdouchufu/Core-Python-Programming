def pay():
    balance = float(raw_input('Enter opening balance: '))
    balance = round(balance, 2)
    payment = float(raw_input('Enter monthly payment: '))
    payment = round(payment, 2)

    print '     \tAmount\tRemaining'
    print 'Pymt#\tPaid\tBalance'
    print '------\t------\t------'

    print '0\t$0.00\t$%s' % balance
    i = 1
    while balance > payment:
        balance -= payment
        balance = round(balance, 2)
        print '%d\t$%s\t$%s' % (i, payment, balance)
    print '%d\t$%s\t$0.00' % (i, balance)

pay()