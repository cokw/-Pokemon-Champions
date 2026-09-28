base_HP = 90
base_DEF = 130
nature_DEF = 1
div = 40 # 1 ~ 64

best_counts = {}

start_P = 4000
end_P = 24000
total_P_count = end_P - start_P 

start_HP = max(0, div - 32)
end_HP = min(32, div)

for P in range(start_P, end_P): 
    max_S = 0     
    best_HP = 0
    best_DEF = 0

    for i in range(start_HP, end_HP + 1):
        ind_HP = i
        ind_DEF = div - i
        
        per_HP = (2 * base_HP + 31 + 2 * ind_HP) // 2 + 60
        per_DEF = int(((2 * base_DEF + 31 + 2 * ind_DEF) // 2 + 5) * nature_DEF)

        S = per_HP / ((11 * P / 25 / per_DEF) + 2)

        if S > max_S:
            max_S = S
            best_HP = ind_HP
            best_DEF = ind_DEF

    best_counts[(best_HP, best_DEF)] = best_counts.get((best_HP, best_DEF), 0) + 1


sorted_counts = sorted(best_counts.items(), key=lambda item: item[1], reverse=True)

print("=== 최적 배분 등장 비율 ===")
for (hp, df), count in sorted_counts:
    percentage = (count / total_P_count) * 100
    print(f"({hp}, {df}): {percentage:.1f}% 등장")
