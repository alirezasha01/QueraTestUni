num = input()
x = [int(a) for a in str(num)]
for i in range (0 , len(x)):
  print(str(x[i])+": " , end = "")
  for j in range (0,x[i]):
    print(x[i], end="")
  print(" ")