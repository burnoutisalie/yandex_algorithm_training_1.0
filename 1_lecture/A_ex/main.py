import sys

def main():
	temps = list(map(int, input().split()))
	troom = temps[0]
	tcond = temps[1]
	tlater = troom
	mode = input()
	if mode == 'freeze':
		if troom > tcond:
			tlater = tcond
	elif mode == 'heat':
		if troom < tcond:
			tlater = tcond
	elif mode == 'auto':
		tlater = tcond
	elif mode == 'fan':
		tlater = troom
	print(tlater)

if __name__ == '__main__':
	main()
