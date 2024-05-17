'''
grade_dict = {1: 'A+', 2: 'A0', 3: 'A-', 4: 'B+', 5: 'B0', 6: 'B-', 7: 'C+', 8: 'C0', 9: 'C-', 10: 'D0'}
for i in range(1, int(input())+1):
    N, K = map(int, input().split())
    total = []
    scores = [list(map(int, input().split())) for _ in range(N)]
    for n in range(N):
        total.append(scores[n][0] * 0.35 + scores[n][1] * 0.45 + scores[n][2] * 0.2)
    
    score_rank = sorted(total, reverse=True)
    rank_key = score_rank.index(total[K-1])
    K_grade = grade_dict[(rank_key // (N//10)) + 1]
    
    print(f"#{i} {K_grade}")
'''
    
grades = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']
for i in range(1, int(input())+1):
    N, K = map(int, input().split())
    total = []
    for _ in range(N):
        scores = list(map(int, input().split()))
        total.append(scores[0] * 0.35 + scores[1] * 0.45 + scores[2] * 0.2)
        
    rank = sorted(total, reverse=True).index(total[K-1]) + 1
    ratio = rank / N
    K_grade = grades[int(ratio * 9.99)]
    
    print(f"#{i} {K_grade}")