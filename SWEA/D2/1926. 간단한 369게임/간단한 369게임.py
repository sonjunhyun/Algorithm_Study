N = int(input())
for n in range(1, N+1):
    if str(n).count("3") or str(n).count("6") or str(n).count("9"):
        print("-" * (str(n).count("3") + str(n).count("6") + str(n).count("9")), end=" ")
    else:
        print(n, end=" ")