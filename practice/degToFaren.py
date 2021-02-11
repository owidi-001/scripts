def degToFaren(value):
    Fan=value*33.8
    return f'{Fan} Farenheight'
 
if __name__=='__main__':
    value=float(input('Enter degree value: \n'))
    degToFaren(value)
    print(degToFaren(value))
    
