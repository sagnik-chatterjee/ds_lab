import sys
for line in sys.stdin:
    line = line.strip()
    vals = line.split()
    print('%s %s %s %s %s' % (vals[14], vals[15], vals[16], vals[31], 1))
