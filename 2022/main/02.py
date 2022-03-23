s = input()
mass = s.split()

n = int(mass[0])
k = int(mass[1])
m = int(mass[2])
x = 0

while m <= k <= n <= 200:
    n = (n - k) + k % m
    x = x + (k // m)

print(str(x))
