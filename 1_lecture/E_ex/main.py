def get_floor_entrance_numbers():
    input_nums = list(map(int, input().split()))
    flat1_num = input_nums[0]
    floors_per_entrance = input_nums[1]
    flat2_num = input_nums[2]
    entrance2_num = input_nums[3]
    floor2_num = input_nums[4]

    entrance1_num = 0
    floor1_num = 0

    if flat1_num == 1:
        entrance1_num = 1
        floor1_num = 1
    if floors_per_entrance == 1:
        floor1_num = 1

    flats_per_floor = 0
    flats_per_floor_upper_bound = 0
    flats_per_floor_lower_bound = 0
    if not(floor2_num == 1 and entrance2_num == 1):
        cumulative_floor2_num = floor2_num + floors_per_entrance * (entrance2_num - 1)
        flats_per_floor_upper_bound = (flat2_num - 1) / (cumulative_floor2_num - 1)
        flats_per_floor_lower_bound = flat2_num / cumulative_floor2_num
        if flats_per_floor_upper_bound - flats_per_floor_lower_bound < 1:
            flats_per_floor = int(flats_per_floor_upper_bound // 1)
        if flats_per_floor_upper_bound < 1:
            entrance1_num = -1
            floor1_num = -1
    else:
        if flat1_num <= (flat2_num * floors_per_entrance):
            entrance1_num = 1

    if flats_per_floor != 0:
        flats_per_entrance = flats_per_floor * floors_per_entrance
        if flat1_num % flats_per_entrance == 0:
            entrance1_num = flat1_num // flats_per_entrance
        else:
            entrance1_num = flat1_num // flats_per_entrance + 1
        net_flat1_num = flat1_num - flats_per_entrance * (entrance1_num - 1)
        if net_flat1_num % flats_per_floor == 0:
            floor1_num = net_flat1_num // flats_per_floor
        else:
            floor1_num = net_flat1_num // flats_per_floor + 1
    print(entrance1_num, floor1_num)

if __name__ == '__main__':
    get_floor_entrance_numbers()
