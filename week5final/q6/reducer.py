import sys
from operator import itemgetter
n_males = 0
n_females = 0
curr_year = 0
year = None
t_females = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
t_males = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
print("Yearly Statistics")
for line in sys.stdin:
    line = line.strip()
    year, month, date, gender, count = line.split(' ', 4)
    try:
        count = int(count)
    except ValueError:
        continue

    if gender == 'M':
        t_males[int(month)] += 1
    else:
        t_females[int(month)] += 1
    if int(year) == curr_year:
        if gender == 'M':
            n_males += 1
        else:
            n_females += 1
    else:
        if curr_year >= 0:
            print('year %s females: %s males: %s total births: %s' %
                  (curr_year, n_females, n_males, n_males+n_females))
    curr_year = int(year)
    if gender == 'M':
        n_males = 1
    else:
        n_females = 1
if curr_year == year:
    print('year %s females: %s males: %s total births: %s' %
          (curr_year, n_females, n_males, n_males+n_females))
print("")
print("Monthly Statistics")
for i in range(0, 12):
    print('month %s males: %s females: %s total births: %s' %
          (i+1, t_males[i], t_females[i], t_males[i]+t_females[i]))
