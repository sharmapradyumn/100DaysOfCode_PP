if __name__ == '__main__':
    s = input()
    a = 0
    b = 0
    c = 0
    d = 0
    e = 0
    #main function
    for i in s :
        if i.isalnum() == True :
            e += 1
            if i.isalpha() == True :
                a += 1
                if i.islower() == True :
                    b += 1
                else :
                    c += 1
            else :
                d += 1
    #any alphanum
    if e > 0 :
        print(True)
    else :
        print(False)
    #any alpha
    if a > 0 :
        print(True)
    else :
        print(False)
    #any digit
    if d > 0 :
        print(True)
    else :
        print(False)
    #any lowercase
    if b > 0 :
        print(True)
    else :
        print(False)
    #any uppercase
    if c > 0 :
        print(True)
    else :
        print(False)
        
#optimal solution
#if __name__ == '__main__':
#    s = input()
#    print(any(i.isalnum() for i in s))
#    print(any(i.isalpha() for i in s))
#    print(any(i.isdigit() for i in s))
#    print(any(i.islower() for i in s))
#    print(any(i.isupper() for i in s))