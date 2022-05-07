def get_strings(n):
    return [bin(x)[2:].rjust(n,'0') for x in range(2**n)]

def bruteforce(wt,B, W):
    n = len(B) 
    bit_strings = get_strings(n) 
    maximum_benefit = 0 
    best_choice = ''
    for c in bit_strings: 
        benefit = sum([int(c[i]) * B[i] for i in range(n)]) 
        weight = sum([int(c[i]) * wt[i] for i in range(n)])
        if weight <=W and benefit > maximum_benefit:
            maximum_benefit = benefit 
            best_choice = c
    return (best_choice, maximum_benefit)

if __name__== '__main__':
    benefit_value = [45, 30, 45,10]
    weight = [3, 5, 9, 5]
    weight_of_knapsack = 16
    print(bruteforce( weight, benefit_value, weight_of_knapsack))