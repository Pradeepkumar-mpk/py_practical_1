a=int(input("enter number1"))
if a%2==0: 
    print("even")
else:
    print("odd")
if a%8==0:
    if a%14==0:
        print("true")
        
    else:
        if a%3==0:
            print ("it is odd number divisible by 3")
            if a%7==0:
                print("it is odd number divisible by 7")
                if a%11==0:
                     print("it is odd number divisible by 11")
                