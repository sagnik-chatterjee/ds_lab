import fileinput

total_value = 0
old_key = None

# readin lines from stdin
for line in fileinput.input():
    data = line.strip().split("\t")
    if len(data) != 2:
        continue

    # extracting country along with cases being displayed
    current_key, current_value = data

    # if the country is cahnged then print the country with the cases
    if old_key and old_key != current_key:
        print(f"{old_key} --> {float(total_value)}")
        old_key = current_key
        total_value = 0
    # else keep the country same , these will be printed at last
    old_key = current_key

    total_value = total_value + float(current_value)

# print the cases per country
if old_key != None:
    print(f"{old_key} --> {float(total_value)}")
