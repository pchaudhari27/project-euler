# current function set up for sqrt(x) = a  <==>  x^2 = a
# should be changed for other functions
def f(x, a):
    return x**2 - a

def f_prime(x):
    return 2*x

# intial guess, precision, and update function set up for sqrt(x) = a
def newton_method(a, prec = 100):
    '''Given integer a and integer prec, and depending on what functions are setup, this function performs Newton's method up to precision prec.'''
    # this should be changed depending on relationship between x and a
    a = a * 10**(2*prec)
    x_prev = 0
    # intial x > 0
    x_curr = a // 2

    # use integer division to avoid floating point errors
    while abs(x_prev - x_curr) > 1:
        x_prev = x_curr
        # # what you would normally use for arbitrary function
        # x_curr = x_prev - (f(x_prev,a) // f_prime(x_prev))

        # specific update function for sqrt(x) = a
        x_curr = (x_prev + (a // x_prev)) // 2
    
    # put decimal place at proper place
    decimal_place = len(str(x_curr)) - prec

    # return as a string to avoid floating point issues
    return str(x_curr)[:decimal_place] + "." + str(x_curr)[decimal_place:]