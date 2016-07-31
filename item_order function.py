

#w = raw_input("Enter any word: ")

order = "salad water hamburger salad hamburger"

def item_order(order):
    global salad, water, hamburger
    salad = 0
    water = 0
    hamburger = 0
    s = order
    for l in range(len(s)):
        
        #salad count
        if s[l] == "s":
            if l+1 < len(s) and s[l + 1] == "a":
                if l+2 < len(s) and s[l + 2] == "l":
                    if l+3 < len(s) and s[l + 3] == "a":
                        if l+4 < len(s) and s[l + 4] == "d":
                            salad += 1
        #water count
        elif s[l] == "w":
            if l+1 < len(s) and s[l + 1] == "a":
                if l+2 < len(s) and s[l + 2] == "t":
                    if l+3 < len(s) and s[l + 3] == "e":
                        if l+4 < len(s) and s[l + 4] == "r":
                            water += 1
        #hamburger count
        elif s[l] == "h":
            if l+1 < len(s) and s[l + 1] == "a":
                if l+2 < len(s) and s[l + 2] == "m":
                    if l+3 < len(s) and s[l + 3] == "b":
                        if l+4 < len(s) and s[l + 4] == "u":
                            if l+5 < len(s) and s[l + 5] == "r":
                                if l+6 < len(s) and s[l + 6] == "g":
                                    if l+7 < len(s) and s[l + 7] == "e":
                                        if l+8 < len(s) and s[l + 8] == "r":
                                            hamburger += 1

    return "salad:" + str(salad) + " hamburger:" + str(hamburger) + " water:" +str(water)
     

a = item_order(order)
print a