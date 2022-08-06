arr = [];
for i in range(0,3):
  n = int(input());
  arr.append(n);
arr.sort();
if pow(pow(arr[0],2) + pow(arr[1],2), 1 / 2) == arr[2]:
  print("YES");
else:
  print("NO");