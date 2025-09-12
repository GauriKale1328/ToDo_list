

# Function to check if it’s safe to place a queen at a given row and column
def is_safe(board, row, column, N):  # board = queen positions so far, row = current row, column = current column
    # ---------------- CHECK SAME COLUMN ----------------
    for i in range(row):  # Loop through all rows before the current row
        if board[i] == column:  # If another queen is already in the same column
            return False  # Not safe → conflict

    # ---------------- CHECK DIAGONALS ----------------
    for i in range(row):  # Loop through all rows before the current row
        # If column difference == row difference → they are on the same diagonal
        if abs(board[i] - column) == abs(i - row):
            return False  # Not safe → diagonal conflict

    # If no conflict found → safe position
    return True  


# Recursive function to solve the N-Queens problem
def solve_n_queens(board, row, N, solutions):
    if row == N:  # Base case: if all queens are placed
        solutions.append(board[:])  # Save the current arrangement (copy of board)

        # --------- Print the path to this solution ---------
        print("\nPath to one solution:")
        for r in range(N):  # Go through each row
            print(f"Row {r+1} -> Column {board[r]+1}")  # Show where queen is placed

        # --------- Print the final board ---------
        print("\nFinal Board:")
        for r in range(N):  # For each row
            row_str = ""  # Build a row string with queens and dots
            for c in range(N):  # For each column
                if board[r] == c:  # If queen is at this position
                    row_str += " Q "  # Place queen symbol
                else:
                    row_str += " * "  # Empty spot
            print(row_str)  # Print the row
        return  # End this path (backtrack)

    # Try placing a queen in all columns of the current row
    for column in range(N):
        if is_safe(board, row, column, N):  # Check if this spot is safe
            board[row] = column  # Place queen at (row, column)
            solve_n_queens(board, row + 1, N, solutions)  # Move to next row
            board[row] = -1   # Backtrack → remove queen and try next column


# ------------------ MAIN PROGRAM ------------------
if __name__ == "__main__":
    N = int(input("Enter the value of N (Number of Queens): "))  # Ask user for N

    board = [-1] * N  # Initialize board with -1 (means no queen placed yet)
    solutions = []  # List to store all solutions

    solve_n_queens(board, 0, N, solutions)  # Start solving from row 0

    print(f"\nTotal Solutions for {N}-Queens = {len(solutions)}")  # Print total count
