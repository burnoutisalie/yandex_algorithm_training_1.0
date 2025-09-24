def solve_root_equation():
    a = int(input())
    b = int(input())
    c = int(input())
    x = 0
    if c < 0:
        print("NO SOLUTION")
    else:
        if a == 0:
            if b < 0:
                print("NO SOLUTION")
            else:
                if c == pow(b, 1/2):
                    print("MANY SOLUTIONS")
                else:
                    print("NO SOLUTION")
        else:
            x = (c ** 2 - b) / a
            if x % 1 == 0:
                print(int(x))
            else:
                print("NO SOLUTION")

if __name__ == '__main__':
    solve_root_equation()
