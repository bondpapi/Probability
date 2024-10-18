from math import comb

def probability_of_a(N, letters, K):
    # Count how many 'a's are in the list
    num_a = letters.count('a')
    
    # If no 'a' is present in the list, return 0.000 as probability
    if num_a == 0:
        return 0.0
    
    # Count how many elements are not 'a'
    num_not_a = N - num_a
    
    # Total combinations of selecting K elements from N
    total_combinations = comb(N, K)
    
    # If we cannot select K elements from num_not_a, then combinations without 'a' is 0
    if num_not_a < K:
        combinations_without_a = 0
    else:
        combinations_without_a = comb(num_not_a, K)
    
    # Probability of not selecting 'a'
    prob_not_a = combinations_without_a / total_combinations
    
    # Probability of selecting at least one 'a'
    prob_at_least_one_a = 1 - prob_not_a
    
    # Return the result rounded to 4 decimal places
    return round(prob_at_least_one_a, 4)

# Input
N = int(input())  # Number of elements in the list
letters = input().split()  # List of letters
K = int(input())  # Number of indices to be selected

# Output the probability
print(probability_of_a(N, letters, K))
