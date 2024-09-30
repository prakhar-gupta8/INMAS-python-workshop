'''
Module to provide functions for learning Python.
This module that has a bad coding style. 
One algorithm uses a recursion, which is cute but not practical.
'''
def fibonacci (n):
    ''' This function calculates the nth Fibonacci number using recursion.'''
    if n <= 1:
        return n
    else:
        return ( fibonacci( n-1 )
                + fibonacci( n-2 )  )
def fiboSequence1 ( uppern ):
    '''   Return Fibonacci sequence. Recursion is cute, but not efficient in this case.   '''
    assert uppern>0
    seq=[]
    for  i in   range(uppern):
        seq.append(  fibonacci ( i ) )
    return(seq)

def fiboSequence2 (uppern):
    '''   Return Fibonacci sequence. Direct computation.  '''
    assert uppern>0
    seq=[0,1]
    if uppern<=2:
        return  seq[:uppern]
    for i in range(2,uppern):
        seq.append(seq[i-1]+seq[i-2])
    return seq

