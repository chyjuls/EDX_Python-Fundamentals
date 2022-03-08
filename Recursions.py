def count_down2(start):
    for i in range(start, -1, -1):
        print(i)


# Below are some lines of code that will test your function.
# You can change the value of the variable(s) to test your
# function with different inputs.
#
# If your function works correctly, this will originally
# print: 5, 4, 3, 2, 1, 0, each on their own line.
count_down2(5)
print()


# Let's implement the Fibonacci function we saw in the
# previous video in Python!
#
# Like our Factorial function, our Fibonacci function
# should take as input one parameter, n, an integer. It
# should calculate the nth Fibonacci number. For example,
# fib(7) should give 13 since the 7th number in
# Fibonacci's sequence is 13.

# So, our function definition will basically be the same:

def fib(n):
    # What do we want to do inside the function? Once again,
    # there are really only two cases: either we're looking
    # for the first two Fibonacci numbers, or we're not.
    # What happens if we're looking for the first two? Well,
    # we already know that the 1st and 2nd Fibonacci numbers
    # are both 1, so if n == 1 or n == 2, we can go ahead
    # and return 1.

    if n == 1 or n == 2:
        return 1

    # What if n doesn't equal 1? For any value for n greater
    # than 2, the result should be the sum of the previous
    # two numbers. The previous Fibonacci number could then
    # be calculated with the same kind of function call,
    # decrementing n by 1 or 2.

    else:
        return fib(n - 1) + fib(n - 2)

    # If n is greater than 2, then it returns the sum of the
    # previous two fibonacci numbers, as calculated by the
    # same function.


# Now let's test it out! Run this file to see the results.
print("fib(5) is", fib(5))
print("fib(10) is", fib(10))

print()


# We've started a recursive function below called
# exponent_calc(). It takes in two integer parameters, base
# and expo. It should return the mathematical answer to
# base^expo. For example, exponent_calc(5, 3) should return
# 125: 5^3 = 125.
#
# The code is almost done - we have our base case written.
# We know to stop recursing when we've reached the simplest
# form. When the exponent is 0, we return 1, because anything
# to the 0 power is 1. But we are missing our recursive call!
#
# Fill in the marked line with the recursive call necessary
# to complete the function. Do not use the double-asterisk
# operator for exponentiation. Do not use any loops.
#
# Hint: Notice the similarity between exponentiation and
# factorial:
#  4! = 4! = 4 * 3!, 3! = 3 * 2!, 2! = 2 * 1
#  2^4 = 2 * 2^3, 2^3 = 2 * 2^2, 2^2 = 2 * 2^1, 2^1 = 2 * 2^0

def exponent_calc(base, expo):
    if expo == 0:
        return 1
    else:
        return base * exponent_calc(base, expo - 1)


# Below are some lines of code that will test your function.
# You can change the value of the variable(s) to test your
# function with different inputs.
#
# If your function works correctly, this will originally
# print: 125
print(exponent_calc(5, 3))
print()


def count_down(start):
    if start <= 0:
        print(start)
    else:
        count_down(start - 1)
        print(start)


count_down(5)
