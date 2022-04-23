def dynamic(wt, B, W):
    n = len(B) 
    table = [[0 for x in range(W + 1)] for x in range(n + 1)] 
    for i in range(n + 1): 
        for x in range(W + 1):
            benefit1 = B[i-1] + table[i-1][x-wt[i-1]] 
            benefit2 = table[i-1][x] 
            if i == 0 or x == 0:
                table[i][x] = 0
            elif wt[i-1] <= x:
                table[i][x] = max(benefit1, benefit2)
    maximum_benefit = table[n][W]
    return (maximum_benefit )

if __name__== '__main__':
    benefit_value = [45, 30, 45,10]
    weight = [3, 5, 9, 5]
    weight_of_knapsack = 16
    print(dynamic( weight, benefit_value, weight_of_knapsack))