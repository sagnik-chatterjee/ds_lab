import pandas as pd
 
dict1 = {
 "Name":["lambda","beta","alpha"],
 "Height":["180","195","210"],
 "Qualification":["Btech","BArch","BSc"]
}
 
new = pd.DataFrame.from_dict(dict1)
 
print(new)
 
address = ["omega","alpha","zeta"]
dict1.update({"Address":address})
 
print("updated dictionary is:",dict1)
new2 = pd.DataFrame.from_dict(dict1)
 
print(new2)