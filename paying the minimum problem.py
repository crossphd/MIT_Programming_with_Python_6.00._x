
balance = 4213
annualInterestRate = 0.2
monthlyPaymentRate = 0.04

months = range(1,13)
paid = 0.00
mp = 0.00

for m in months:
    mp = balance * monthlyPaymentRate
    paid += mp
    balance = (balance - mp)+ ((balance - mp)*(annualInterestRate / 12))
    print "Month:", m
    print "Minimum monthly payment:", round(mp, 2)
    print "Remaining balance:", round(balance, 2)
        
    
print "Total paid:", round(paid, 2)
print "Remaining balance:", round(balance, 2)

#Month: 1
#Minimum monthly payment: 96.0
#Remaining balance: 4784.0

#Total paid: 96.0
#Remaining balance: 4784.0