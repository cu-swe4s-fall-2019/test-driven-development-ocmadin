import sys


def read_stdin_col(col_num):
    """
    Function that reads an input file from stdin, takes a column number and
    converts the numbers in the column to a list
    
    Arguments
    ---------
    col_num : int
        Column number to read from stdin and convert to list
    
    Returns
    -------
    column : list
        The list of values in the specified column
    """
    
    if col_num is None:
        raise TypeError('read_stdin_col: No column number supplied to function')
    
    if not isinstance(col_num,int):
        raise TypeError('read_stdin_col: Column number must be an integer')
        
    stdin = sys.stdin.readlines()
    if len(stdin[0].rstrip().split(' ')) < col_num:
        raise IndexError('read_stdin_col: Column number is out of range')
    return None
