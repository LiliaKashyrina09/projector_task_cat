def cats_with_hats(rounds, cats):
    # Create an array to track the hat status of each cat, initialized to False (no hat)
    hat_status = [False] * cats
    
    # Perform rounds of visits
    for i in range(1, rounds + 1):
        for j in range(i, cats + 1, i):
            hat_status[j-1] = not hat_status[j-1]
    
    # Collect the indices of cats that have hats on after all rounds
    cats_with_hats = [index + 1 for index, has_hat in enumerate(hat_status) if has_hat]
    
    return cats_with_hats

# Example usage:
cats_with_hats_list = cats_with_hats(100, 100)
print(cats_with_hats_list)
