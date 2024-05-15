for i in range(1, int(input()) + 1):
    pattern = input()
    len_pattern = 1
    while len_pattern <= 10:
        if pattern[:len_pattern] == pattern[len_pattern:2*len_pattern]:
            break
        len_pattern += 1

    print(f"#{i} {len_pattern}")