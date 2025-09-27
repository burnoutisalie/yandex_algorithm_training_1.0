def get_min_area():
    laptop_sides = list(map(int, input().split()))
    areas = dict()
    for i in range(2):
        for j in range(2):
            x = laptop_sides[i] + laptop_sides[j + 2]
            y = max(laptop_sides[int(not(i))], laptop_sides[int(not(j)) + 2])
            area = x * y
            areas[area] = (x, y)
    min_area = min(areas.keys())
    print(' '.join(map(str, areas[min_area])))

if __name__ == '__main__':
    get_min_area()
