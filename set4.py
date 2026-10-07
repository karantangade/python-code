
import sys
set = {1,2,3,3}

min=sys.maxsize;

for m in set:
    if min>m:
        min=m

print(min)