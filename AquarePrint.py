n = int(input())
m = ""
for i in range (1,n+1):
    if i==1 or i==n:
        m += n*"*"+"\n"
    else:
        m += "*"+(n-2)*" "+"*"+"\n"
print(m);