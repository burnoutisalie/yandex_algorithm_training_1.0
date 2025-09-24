def check_triangle_validity():
	a = int(input())
	b = int(input())
	c = int(input())
	if ((a + b) > c) and ((a + c) > b) and ((b + c) > a):
		print("YES")
	else:
		print("NO")

if __name__ == '__main__':
	check_triangle_validity()
