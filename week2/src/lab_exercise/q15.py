import pandas as pd
dct = {'Name':['H', 'R', 'P'], 'Height':[180, 182, 190], 'Qualification':['BTech', 'BArch', 'BSc']}
new = pd.DataFrame.from_dict(dct)
print(new)

address = ['Manipal', 'Udupi', 'Surathkal']
print("address list:", address)
#dct['address'] = address

new.insert(3, "address", address, True)
print(new)