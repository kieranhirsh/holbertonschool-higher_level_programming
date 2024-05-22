#!/usr/bin/python3
def solve_nqueens(queens, size):
    """
    recursive function to solve the n quens problem
    
    Arguments:
        queens (list of tuples): a list of queens placed on the board
        size (int): the size of the board
    """
    row = len(queens)
    for col in range(size):
        if is_safe(queens, (row, col)):
                queens.append((row, col))
                if len(queens) == size:
                    print(queens)
                else:
                    solve_nqueens(queens, size)

                del queens[-1]

    return False

def is_safe(queens, new_queen):
    """
    function to find if a new queen is safe
    
    Arguments:
        queens (list of tuples): a list of queens placed on the board
        new_queen (tuple): location of the new queen

    Returns:
        True,  if the new queen is safe
        False, otherwise
    """
    pos_diag = new_queen[0] + new_queen[1]
    neg_diag = new_queen[0] - new_queen[1]

    for old_queen in queens:
        if (new_queen[0] == old_queen[0] or
                new_queen[1] == old_queen[1] or
                pos_diag == old_queen[0] + old_queen[1] or
                neg_diag == old_queen[0] - old_queen[1]):
            return False

    return True

if __name__ == '__main__':
    import sys
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except:
        print("N must be a number")
        sys.exit(1)
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    for col in range(n):
        solve_nqueens([(0, col)], n)