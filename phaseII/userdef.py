#!/usr/bin/python3



def leni(ch):
    if ch == 0:
        return 0

    ls = []
    while True:
        #n = ch / 10

        if ifint(ch) == 0:
            n = ch % 10
            ch = int(ch / 10)
            if (ch) >= 0:
                ls.append(ch)
                #print(ls)
                #print("an int")
                if ch == 0:
                    # print(len(ls))
                    return len(ls)
            elif ch == 0:
                break
        else:
            print("No longer int")
            break

def ifint(x):
    y = 0
    int(y)

    if type(x) == type(y):
        #print("Integer")
        return 0
    else:
        #print("Not integer")
        return -1
