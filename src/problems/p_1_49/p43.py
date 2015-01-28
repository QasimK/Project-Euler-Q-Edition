"""
Triangle, pentagonal, and hexagonal numbers are generated by the following
formulae:

Triangle           Tn=n(n+1)/2          1, 3, 6, 10, 15, ...
Pentagonal         Pn=n(3n-1)/2         1, 5, 12, 22, 35, ...
Hexagonal          Hn=n(2n-1)           1, 6, 15, 28, 45, ...
It can be verified that T(285) = P(165) = H(143) = 40755.

Find the next triangle number that is also pentagonal and hexagonal.
"""

"""
Not done:
Realise all hexagonal numbers are triangle numbers.
Therefore if hexagonal number == pentagonal number, we know it is also a triangle
number

Also, we do not need to generate pentagonal numbers but just check if, given
the n, the n is an integer when reversed from the hexagonal number to produce
the pentagonal base number.
"""

import utility.start as start
import utility.integers as integers


def p43():
    def get_pentagonal_number(n):
        return 0.5*n*(3*n-1)
    def get_hexagonal_number(n):
        return n*(2*n-1)
    
    h = 143 #143 is 1st triplet
    while True:
        h += 1
        h_num = get_hexagonal_number(h)
        
        p37a = h #p37a is larger than h
        while True:
            p37a += 1
            p_num = get_pentagonal_number(p37a)
            
            if p_num == h_num:
                t = p37a #t is larger than p37a
                while True:
                    t += 1
                    t_num = integers.get_triangle_number(t)
                    
                    if t_num == p_num:
                        return (t_num, t, p37a, h)
                    elif t_num > p_num:
                        break
            elif p_num > h_num:
                break
                
    
    
    for n, t_num in enumerate(integers.get_triangle_numbers()):
        x = 166 #x=165 is the first one
        p_num = get_pentagonal_number(x)
        while p_num < t_num:
            x += 1
            p_num = get_pentagonal_number(x)
        
        if p_num == t_num:
            y = 144 #y=143 is the first one
            h_num = get_hexagonal_number(y)
            while h_num < t_num:
                y += 1
                h_num = get_hexagonal_number(y)
            
            if h_num == t_num:
                return (t_num, n+1, x, y) #n starts from 0


if __name__ == '__main__':
    start.time_functions(p43)
