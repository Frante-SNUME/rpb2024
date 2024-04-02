def main():
    a = int(input("a: "))
    b = int(input("b: "))
    print('''
%d + %d = %d
%d - %d = %d
%d * %d = %d
%d / %d = %0.3f''' % (a,b,add(a,b),a,b,subtract(a,b),a,b,multiply(a,b),a,b,divide(a,b),))
    

def add(x,y):
    return x+y

def subtract(x,y):
    return x-y

def multiply(x,y):
    return x*y

def divide(x,y):
    try:
        return x/y
    except:
        print("Error: cannot divide by zero.")

if __name__ == "__main__":
    main()