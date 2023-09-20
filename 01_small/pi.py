'''
leibniz formula posits that the following series converges to pi

pi = 4/1 - 4/3 + 4/5 - 4/7 + 4/9 - 4/11...

model this series and prove it converges to pi
'''

def pi_series(n):
    dividend: int = 4
    divisor: int = 1
    sign: int = 1
    pi: float = 0.0
    count: int = 1
    while count <= n:
        pi += sign*dividend/divisor
        sign *= -1
        count += 1
        divisor += 2
    return pi

#if __name__ == '__main__':
#    print(pi_series(100000))
