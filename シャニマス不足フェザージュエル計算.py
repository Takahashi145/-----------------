print("足りない石の数を数値で入力してください")
n = input()
ne = int(n)
items = [390,780,1310,2100,3910,5880,11500]
for i in range(len(items)):
        for j in range(i + 1, len(items)):
            print(items[i],items[j])
            x=(items[i]+items[j])-ne
            print(x)