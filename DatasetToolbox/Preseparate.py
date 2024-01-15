from itertools import combinations
import os

def save_combinations_to_files(matrix, i, output_directory='combinations'):
    if i > len(matrix[0]):
        raise ValueError("i>j error")

    column_combinations = list(combinations(matrix, i))

    # Create the output directory if it doesn't exist
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    saved_files = []
    saved_columns_indices = []

    for idx, combination in enumerate(column_combinations):
        file_name = os.path.join(output_directory, f"combination_{idx+1}.txt")
        with open(file_name, 'w') as file:
            indices = []
            for column_index, column in enumerate(zip(*combination)):
                file.write('\t'.join(map(str, column)) + '\n')
                indices.append(column_index)
            saved_files.append(file_name)
            saved_columns_indices.append(indices)

    return saved_files, saved_columns_indices

# Example usage:
input_matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

number_of_columns = 2

output_files, saved_columns_indices = save_combinations_to_files(input_matrix, number_of_columns)
print(f"Combinations saved to files: {output_files}")
print(f"Columns saved in each file: {saved_columns_indices}")
