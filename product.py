#def product(sum,*number):
#    #if number == ():
#    #    raise TypeError
#    #sum = 1
#    for x in number:
#        sum = sum * x
#    return sum
def product(*number):
    if len(number) < 1: 
        #print('At least one parameter')
        #return 
        raise TypeError('At least one parameter')
    sum = 1
    for x in number:
        sum = sum * x
    return sum
