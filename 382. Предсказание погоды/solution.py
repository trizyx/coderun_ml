data = []
n = int(input())
for i in range(n):
    data.append(float(input()))

m = int(input())

for i in range(m):
    alpha = 0.95
    betta = 0.9
    temp = data[-1] * alpha + (1 - alpha) * data[-2]
    temp = betta * temp + (1 - betta) * data[i]
    print(temp)
    temp = float(input())
    data.append(temp)
