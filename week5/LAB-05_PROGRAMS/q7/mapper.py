
def mapper(list1):
    dict1={}
    for word in list1:
        dict1[word]=1
    with open("mapperOut.txt","w") as f:
        f.write(str(dict1))
    return f 

def main():
    f=open('input.txt','r')
    list1=[int(i) for i in f]
    f.close()
    mapper(list1)
    print("Ok done")    

if __name__=='__main__':
    main()