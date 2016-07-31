

balance = 3329
annualInterestRate = .2


maxpayments = 12
p = 10

nbal = balance

while nbal > 0:
    nbal = balance
    for mp in range(maxpayments):
        nbal = (nbal - p) + ((nbal - p) * (annualInterestRate / 12))
    if nbal > 0:
        p += 10   
         
print "Lowest payment:",p