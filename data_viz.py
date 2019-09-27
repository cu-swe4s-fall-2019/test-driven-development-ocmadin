
def boxplot(L, out_file_name='boxplot.png'):
    if L is None:
        raise TypeError('boxplot: No input to L')
    if not isinstance(L,list):
        raise TypeError('boxplot: must pass a list to L')
        
    valid_types = [isinstance(value,(int,float,complex)) for value in L]
    
    if not any(valid_types):
        raise TypeError("boxplot: Invalid types in list")
    pass

def histogram(L, out_file_name):
    pass

def combo(L, out_file_name):
    pass
