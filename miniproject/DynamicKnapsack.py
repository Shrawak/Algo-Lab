def dynamic(wt, B, W):
    n = len(B) 
    table = [[0 for x in range(W + 1)] for x in range(n + 1)] 
    take = [[0 for x in range(W + 1)] for x in range(n + 1)]
    for i in range(n + 1): 
        for x in range(W + 1):
            benefit1 = B[i-1] + table[i-1][x-wt[i-1]] 
            benefit2 = table[i-1][x] 
            if i == 0 or x == 0:
                table[i][x] = 0
            elif wt[i-1] <= x:
                table[i][x] = max(benefit1, benefit2)
                if (benefit1 > benefit2): 
                    take[i][x] = 1
                else: 
                    table[i][x] = benefit2
    picks = []
    K = W 
    for i in range(n,0,-1):
        if take[i][K] == 1:
            picks.append(i)
            K -= wt[i-1] 
    picks.sort() 
    picks = [x-1 for x in picks] 
    best_choice = ['0' for i in range(n)]
    for z in range(n):
        if z in picks: 
            best_choice[z] = '1' 
    best_choice = ''.join(best_choice) 
    maximum_benefit = table[n][W]
    return (best_choice,maximum_benefit )

if __name__== '__main__':
    benefit_value = [45, 30, 45,10]
    weight = [3, 5, 9, 5]
    weight_of_knapsack = 16
    print(dynamic( weight, benefit_value, weight_of_knapsack))