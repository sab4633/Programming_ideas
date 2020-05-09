
def main():
    a = 30
    n = 17
    ar = []
    i=1
    for i in range(a):
        ar.append(i)
    print("~",*ar, sep="   ")
    j = 1
    while(j<=n):
        ar2 = []
        k = 1
        for k in range(a):
            k+=1
            #print("k: ",k)
            #3 situation
            #sit. 1 a = b mod n
            #val = k**((j-1)/2)%j
#adding comment


                ar2.append(-1)
            else:
                ar2.append(int(j%k))
        print(j,*ar2, sep="   ")
        j+=2



if __name__ == "__main__":
    main()


