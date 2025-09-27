def can_brick_fit_hole():
    A = int(input())
    B = int(input())
    C = int(input())
    D = int(input())
    E = int(input())
    brick_dims = [A, B, C]
    hole_dims = [D, E]
    brick_dims.sort()
    hole_dims.sort()
    message = "NO"
    if brick_dims[0] <= hole_dims[0] and brick_dims[1] <= hole_dims[1]:
        message = "YES"
    print(message)

if __name__ == '__main__':
    can_brick_fit_hole()
