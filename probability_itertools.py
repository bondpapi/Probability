import itertools


def probability_of_a(N, letters, K):
    # Generate all combinations of K indices from N elements
    all_combinations = list(itertools.combinations(range(N), K))

    # Count how many combinations contain at least one 'a'
    count_with_a = 0
    for combination in all_combinations:
        if any(letters[i] == "a" for i in combination):
            count_with_a += 1

    # Total number of combinations
    total_combinations = len(all_combinations)

    # Probability of selecting at least one 'a'
    prob_at_least_one_a = count_with_a / total_combinations

    # Return the result rounded to 4 decimal places
    return round(prob_at_least_one_a, 4)


def main():
    # Input
    N = int(
        input("Enter the number of elements (N): ")
    )  # Number of elements in the list
    letters = input(
        "Enter the letters separated by spaces: "
    ).split()  # List of letters
    K = int(
        input("Enter the number of indices to select (K): ")
    )  # Number of indices to be selected

    # Ensure inputs are valid
    if K > N:
        print("Invalid input: K cannot be greater than N")
        return

    # Output the probability
    result = probability_of_a(N, letters, K)
    print(result)


# Call the main function to execute the program
if __name__ == "__main__":
    main()
