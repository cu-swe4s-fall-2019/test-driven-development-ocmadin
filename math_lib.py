
def list_mean(L):
    """
    Function to compute the mean of a list
    
    Arguments
    ---------
    L : list of floats/ints
        List to compute the mean of
    
    Returns
    -------
    mean : float
        The mean of the list
    """
    if L is None:
        raise TypeError("list_mean: No input passed to function")
        
    if not isinstance(L,list):
        raise TypeError("list_mean: Wrong input type")

    if len(L) == 0:
        raise IndexError("list_mean: List is empty")
    
    return None

def list_stdev(L):
    return None
