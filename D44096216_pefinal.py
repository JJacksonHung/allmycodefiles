def parse_matrix(matrix_str):
    rows = matrix_str.split('|')
    matrix = []
    for row in rows:
        matrix.append(list(map(int, row.split(','))))
    return matrix

def multiply_matrices(U, V):
    n = len(U)
    M = [[0] * n for _ in range(n)]
    
    for i in range(n):
        for j in range(n):
            for k in range(n):
                M[i][j] += U[i][k] * V[k][j]
    
    return M

def print_matrix(matrix):
    for row in matrix:
        print(row)

def main():
    # Sample input
    matrix_U_str = input("Enter matrix U: ")
    matrix_V_str = input("Enter matrix V: ")

    # Parse the matrices
    U = parse_matrix(matrix_U_str)
    V = parse_matrix(matrix_V_str)

    # Multiply the matrices
    M = multiply_matrices(U, V)

    # Output the resulting matrix
    print("M = U x V")
    print_matrix(M)

if __name__ == "__main__":
    main()
