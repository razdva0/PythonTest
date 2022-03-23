num = int(input())
m_list = list(input().split())
for x in range(1, num):
	if (num - 1) % x == 0 and m_list[:-x] == m_list[x:]:
		print(x)
		break
