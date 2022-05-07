import itertools

def get_strings(n):
    return [bin(x)[2:].rjust(n,'0') for x in range(2**n)]

def bruteforce_fractional(wt, B, W):
    n = len(B)
    ratio = [0] * n
    for z in range(n):
        ratio[z] = B[z] / wt[z]
    
    temp = []
    for weight in wt:
        bit_strings = get_strings(weight)
        temp.append(bit_strings)
    combination = list(itertools.product(*temp))

    max_profit = 0
    solution = []
    
    for c in combination:
        profit = 0
        weight = 0
        for i in range(n):
            profit += sum([int(c[i][j]) * ratio[i] for j in range(wt[i])])
            weight += sum([int(c[i][j]) for j in range(wt[i])])

        if weight <=W and profit > max_profit:
            max_profit = profit
            solution = c

    ans = []
    for i in range(n):
        weight_ratio = sum([int(solution[i][j]) / wt[i] for j in range(wt[i])])
        ans.append(round(weight_ratio,2))
    return(ans, max_profit)

if __name__== '__main__':
    benefit_value = [45, 30, 45,10]
    weight = [3, 5, 9, 5]
    weight_of_knapsack = 16
    print(bruteforce_fractional( weight, benefit_value, weight_of_knapsack))