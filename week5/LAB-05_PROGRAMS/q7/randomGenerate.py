import random 

def main():
    with open('input.txt','w') as f:
        for i in range(1000):
            q= random.randint(0,10000)
            f.write(str(q)+"\n")
        print("Done")
    print("Exiting")
if __name__=='__main__':
    main()