import matplotlib.pyplot as plt
import math_lib as ml

def boxplot(L, out_file_name='boxplot.png'):
    if L is None:
        raise TypeError('boxplot: No input to L')
    if not isinstance(L,list):
        raise TypeError('boxplot: must pass a list to L')
        
    valid_types = [isinstance(value,(int,float,complex)) for value in L]
    
    if not any(valid_types):
        raise TypeError("boxplot: Invalid types in list")
        
    if not isinstance(out_file_name,str):
        raise TypeError("boxplot: File name must be str")
        
    fig = plt.figure(figsize=(3,3))
    ax = fig.add_subplot(1, 1 ,1)
    title = 'Mean: '+str(ml.list_mean(L))+ ', Stdev: ' + str(ml.list_stdev(L))
    ax.title.set_text(title)
    ax.set_ylabel('Values')
    ax.set_xlabel('')

    ax.boxplot(L)
    try:
        plt.savefig(out_file_name, bbox_inches='tight')
    except ValueError:
        raise ValueError


def histogram(L, out_file_name):
    if L is None:
        raise TypeError('boxplot: No input to L')
    if not isinstance(L,list):
        raise TypeError('boxplot: must pass a list to L')
        
    valid_types = [isinstance(value,(int,float,complex)) for value in L]
    
    if not any(valid_types):
        raise TypeError("boxplot: Invalid types in list")
        
    if not isinstance(out_file_name,str):
        raise TypeError("boxplot: File name must be str")
    pass

def combo(L, out_file_name):
    pass
