#x = (1,2,(3,'John',4),'Hi')
x = [1, 2, [3, 'John', 4], 'Hi'] 

#print x[2][2]


def oddTuples(aTup):
    tup2 = ()
    for i in range(len(aTup)):
        if i % 2 == 0:
            tup2 += (aTup[i],)
    return tup2


#print oddTuples(('I', 'am', 'a', 'test', 'tuple'))



def biggest(aDict):
    big = 0
    bigkey = None
    for k,v in aDict.iteritems():
        if len(v) >= big:
            big = len(v)
            bigkey = k
    return bigkey


#print biggest({'C':[]})
#print biggest({'C': [6], 'b': [], 'J': [12, 13, 14, 5], 'l': [14, 5, 14, 8, 12], 'n': [19], 's': [11], 't': [], 'V': [0], 'Z': [18, 1, 20, 8, 2], 'z': [1, 5, 5, 15]})

#print len([12])

def ndigits(x):
    x = abs(x)
    if x == 0:
        return 0
    else:
        return 1 + ndigits(x/10)

#print ndigits(48567)

def f(x):
	import math
	return 200*math.e**(math.log(0.5)/14.1 * x)
   
def radiationExposure(start, stop, step):
    def rad(start, stop):
        if start >= stop:
            return 0
        else:
            return (f(start)*step) + rad((start+step), stop)
    return rad(start,stop)
    

print radiationExposure(0, 3, 0.1)

#1148.6783342153556

    



