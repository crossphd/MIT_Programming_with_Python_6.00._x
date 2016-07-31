balance = 5000
annualInterestRate = .2


maxpayments = 12
error = .01
monthlyInterestRate = (annualInterestRate) / 12
minp = balance/12.0
maxp = (balance * (1 + monthlyInterestRate)**12) / 12
p = (maxp+minp)/2

nbal = balance

while abs(0-nbal) > error:
    nbal = balance
    for mp in range(maxpayments):
        nbal = (nbal - p) + ((nbal - p) * monthlyInterestRate)
    if nbal > 0:
        minp = p
    elif nbal < 0:
        maxp = p  
    p = (maxp+minp)/2
   
      
print "Lowest payment:", round(p,2)


#Monthly interest rate = (Annual interest rate) / 12.0
#Monthly payment lower bound = Balance / 12
#Monthly payment upper bound = (Balance x (1 + Monthly interest rate)12) / 12.0

