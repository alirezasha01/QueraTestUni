def kmm(a, b):
        i = 1
        if a > b:
                c = a
                d = b
        else:
                c = b
                d = a
        while True:
                if ((c * i) / d).is_integer():
                        return c * i
                i += 1;
def bmm(a,b):
    if(b==0):
        return a
    else:
        return bmm(b,a%b)
num1 = input()
num2=num1.split()
print(bmm(int(num2[0]),int(num2[1])),kmm(int(num2[0]),int(num2[1])))