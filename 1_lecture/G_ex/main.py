def get_detail_cnt():
    inputs = list(map(int, input().split()))
    N = inputs[0]
    K = inputs[1]
    M = inputs[2]
    detail_cnt = 0
    details_per_blank = K // M
    leftover_per_blank = K % M
    if K >= M:
        while N >= K:
            blanks = N // K
            leftover_N = N % K
            detail_cnt += blanks * details_per_blank
            N = leftover_N + leftover_per_blank * blanks
    print(detail_cnt)

if __name__ == '__main__':
    get_detail_cnt()
