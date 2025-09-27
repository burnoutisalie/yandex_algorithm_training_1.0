def get_subway_wait_time():
    a = int(input())
    b = int(input())
    an = int(input())
    bn = int(input())
    train_stop_time = 1
    track1_time_upper = an * train_stop_time + (an + 1) * a
    track1_time_lower = an * train_stop_time + (an - 1) * a
    track2_time_upper = bn * train_stop_time + (bn + 1) * b
    track2_time_lower = bn * train_stop_time + (bn - 1) * b
    intersection_lower = max(track1_time_lower, track2_time_lower)
    intersection_upper = min(track1_time_upper, track2_time_upper)
    if intersection_lower <= intersection_upper:
        print(intersection_lower, intersection_upper)
    else:
        print(-1)

if __name__ == '__main__':
    get_subway_wait_time()
