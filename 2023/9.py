import sys
import re
from math import gcd
from collections import defaultdict, Counter
D = open(sys.argv[1]).read().strip()
L = D.split('\n')

def f(xs,part2):
  D = []
  for i in range(len(xs)-1):
    D.append(xs[i+1]-xs[i])
  if all(y==0 for y in D):
    return 0
  else:
    return xs[0 if part2 else -1] + (-1 if part2 else 1)*f(D,part2)

for part2 in [False,True]:
  ans = 0
  for line in L:
    xs = [int(x) for x in line.split()]
    ans += f(xs,part2)
  print(ans)
