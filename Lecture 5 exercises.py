def recurPower(base, exp):
    if exp == 1:
        return base
    elif exp == 0:
        return 1
    elif exp % 2 == 0:
        return base *  recurPower(base, exp/2)
    elif exp % 2 == 1:
        return base * recurPower(base, exp - 1)
        
        
def recurPowerNew(base, exp):
    if exp == 1:
        return base
    elif exp == 0:
        return 1
    elif exp % 2 == 0:
        return recurPowerNew(base*base, exp/2)
    elif exp % 2 == 1:
        return base * recurPowerNew(base, exp - 1)



def gcdIter(a, b):
    value = 0
    if a > b:
        value = b
    else: 
        value = a
    while (a % value > 0) or (b % value > 0):
        #print value
        value -= 1
    return value

  
    
def gcdRecur(a,b):
    if b == 0:
        return a
    else:
        return gcdRecur(b, a%b)
      

def fib(x):
    assert type(x) == int and x >= 0
    if x == 0 or x == 1:
        return 1
    else:
        print fib(x-1), " + ", fib(x-2)
        return fib (x-1) + fib (x-2)       


def isPalidrome(s):
    
      def toChar(s):
          s = s.lower()
          ans = ''
          for c in s:
              if c in 'abcdefghijklmnopqrstuvwxyz':
                  ans = ans + c
          return ans  
          
      def isPal(s):
          if len(s) <= 1:
              return True
          else:
              return s[0] == s[-1] and isPal(s[1:-1]) 
      
      return isPal(toChar(s))
              
#print isPalidrome('gag')



def lenIter(aStr):
    ans = 0
    for c in aStr:
        ans += 1
    return ans

def lenRecur(aStr):
    if aStr == '':
        return 0
    else:
        return 1 + lenRecur(aStr[1:])

#print lenRecur('a')


def isIn(char, aStr):
    mid = len(aStr)/2
    if aStr == '' or (len(aStr) == 1 and aStr != char):
        return False
    elif aStr[mid] == char:
        return True
    elif char > aStr[mid]:
        return isIn(char,aStr[mid:])
    elif char < aStr[mid]:
        return isIn(char,aStr[:mid])


#print isIn('a','acdegijlllnopuuvww')


def semordnilap(str1, str2):
     if str1 != '' and str2 != '':
        if len(str1) == 1 and len(str2) == 1:
            return str1 == str2
        elif str1[0] == str2[-1]:
            #print str1[0], str2[-1]
            return semordnilap(str1[1:],str2[:-1])
        else:
            return False
     else:
         return False
    

#print semordnilap('dog','tgod')


def fibMetered(x):
    global numCalls
    numCalls += 1
    if x == 0 or x == 1:
        return 1
    else:
        return fibMetered(x-1) + fibMetered(x-2)

def testFib(n):
    global numCalls    
    for i in range(n+1):
        numCalls = 0
        print('fib of ' + str(i) + ' = ' + str(fibMetered(i)))
        print ('fib called ' + str(numCalls) + ' times')

testFib(10)

