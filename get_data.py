
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
    return None
