import sys

for line in sys.stdin:
    line = line.strip()
    nums = line.split()
    for num in nums:
        val = int(num)
        if val % 2 == 0:
            print('%s\t%s' %("EVEN COUNT",1))
        else:
            print('%s\t%s' %("ODD  COUNT",1))
