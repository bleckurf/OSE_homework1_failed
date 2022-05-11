# First homework for OSE. Deadline 15 of May
# To do: - select functions that can be called
#        - push to git (or check if they are already pushed?) into right folder
#        - create tests
#        - push tests?

def midpoint(a, b, f):
    """
    Calculate mid-point approximation of integral in the interval (a,b) of function f
    :param a: float
        lower limit of integral
    :param b: float
        upper limit of integral
    :param f: anonymous function
        function of which the integral is to be approximated
    :return: float
        integral value approximated with mid-point rule
    """
    m = 0.5 * (a + b)
    return f(m) * (b - a)


def trapezoidal(a, b, f):
    """
        Calculate trapezoidal approximation of integral in the interval (a,b) of function f
        :param a: float
            lower limit of integral
        :param b: float
            upper limit of integral
        :param f: anonymous function
            function of which the integral is to be approximated
        :return: float
            integral value approximated with trapezoidal rule
        """
    return 0.5 * (f(a) + f(b)) * (b - a)