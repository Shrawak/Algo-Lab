def greedy( wt, B, W):
    n = len(B)
    index = list(range(n))

    priority = [0] * n
    for z in range(n):
        priority[z] = B[z] / wt[z]
    index.sort(key=lambda i: priority[i], reverse=True)
 
    max_profit = 0
    fractions = [0] * n
    for i in index:
        if wt[i] <= W:
            fractions[i] = 1
            max_profit += B[i]
            W -= wt[i]
        else:
            fractions[i] = round(W / wt[i],2)
            max_profit += B[i] * (W/wt[i])
            break
 
    return ( fractions, max_profit )

if __name__== '__main__':
    benefit_value = [45, 30, 45,10]
    weight = [3, 5, 9, 5]
    weight_of_knapsack = 16
    print(greedy(weight, benefit_value, weight_of_knapsack))