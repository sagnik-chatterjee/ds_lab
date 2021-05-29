import fileinput
max_value = -1
old_key = None

for line in fileinput.input():
    data = line.strip().split("\t")
    if len(data) == 2:
        current_key, current_value = data
        if old_key == current_key:
            if float(current_value) > float(max_value):
                max_value = float(current_value)
        else:
            if old_key != None:
                print(old_key, "-->", max_value, end="\n")
            old_key = current_key
            max_value = current_value
