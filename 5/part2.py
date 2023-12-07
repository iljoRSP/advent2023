'''
so... part 1's current implementation is no bueno. at all
i have exactly one (1) idea that __might__ just work for part 2:


consider each map as a piecewise function, below is simple example

seed-to-soil(x) = f(x) =
{
  x E [98, 98 + 2)  : x - (98 - 50)
  x E [50, 50 + 48) : x - (50 - 52)
  otherwise         : x
}


soil-to-fertilizer(x) = g(x) =
{
  x E [15, 15 + 37) : x - (15 -  0)
  x E [52, 52 +  2) : x - (52 - 37)
  x E [ 0,  0 + 15) : x - ( 0 - 39)
  otherwise         : x
}

... and so on

a seed-to-fertilizer map is equivalent to gf(x): and so a seed-to-location map is equivalent to lkjihgf(x).


the most significant bump in the road is that when chaining f(x) into g(x), when they are piecewise, is that you have to also chain the x in the condition...
take the following simple examples

f(x) =
{
 x E [ 0, 10) : x + 1
 otherwise    : x
}

g(x) =
{
 x E [ 5, 15) : x + 5
 otherwise    : x
}


to most easily chain these functions we should split the ranges up for every digit in all ranges (0, 5, 10, 15)
then we replicate all ranges in both functions

f(x) =
{
 x E [ 0,  5) : x + 1
 x E [ 5, 10) : x + 1
 x E [10, 15) : x
 otherwise    : x
}

g(x) =
{
 x E [ 0,  5) : x
 x E [ 5, 10) : x + 5
 x E [10, 15) : x + 5
 otherwise    : x
}


now, its easy to chain f into g

(g again, but for the ranges, replace x with what f(x) calls for)

g(f(x)) =
{
 y E [ 0,  5) : y               <--- f(x) dictates y -> x + 1
 y E [ 5, 10) : y + 5           <--- f(x) dictates y -> x + 1
 y E [10, 15) : y + 5           <--- f(x) dictates y -> x
 otherwise    : y               <--- f(x) dictates y -> x
}


(replace y for x+1)


g(f(x)) =
{
 (x + 1) E [ 0,  5) : x + 1
 (x + 1) E [ 5, 10) : x + 1 + 5
 x       E [10, 15) : x + 5
 otherwise          : x
}


(flatten the ranges, and we can clamp negative numbers to 0)
(if upper bound is zero, we can safely drop that range)


gf(x) =
{
 x E [ 0,  4) : x + 1
 x E [ 4,  9) : x + 6
 x E [10, 15) : x + 5
 otherwise    : x
}



now, suppose our seed ranges were [0, 3), [6, 12)


we consider this as its own piecewise function

e(x) =
{
 x E [ 0,  3) : x
 x E [ 6, 12) : x
}

we apply the same overlapping method to get a gfe(x)
(ranges = 0, 3, 4, 6, 9, 10, 12, 15)
we can also drop the ranges not subset to the seed ranges

gfe(x) =
{
 x E [ 0,  3) : x + 1
/x E [ 3,  4) : x + 1
/x E [ 4,  6) : x + 6
 x E [ 6,  9) : x + 5
 x E [ 9, 10) : x
 x E [10, 12) : x + 5
/x E [12, 15) : x + 5
 otherwise    : x
}


gfe(x) =
{
 x E [ 0,  3) : x + 1
 x E [ 6,  9) : x + 5
 x E [ 9, 10) : x
 x E [10, 12) : x + 5
 otherwise    : x
}

now, we take the minimum from each range and input it into the formula to get

gfe( 0) =  0 +  1 =  1
gfe( 6) =  6 +  5 = 11
gfe( 9) =  9      =  9
gfe(10) = 10 +  5 = 15


and there we have it! the smallest possible output from seeds E [0, 3), [6, 12) is 1!


~~~

this approach scales with the number of pieces/range boundaries, rather than the size of the ranges. in other words, should work well.


now, as for implementing it... I will save it for another day.
'''


