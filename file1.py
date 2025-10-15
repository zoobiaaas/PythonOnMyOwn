#read a file with numbers, compute sum,av,max,min and write result to new file
fr=open("file1_num.txt","r")
num=[int(x.strip()) for x in fr.readlines()]
fr.close()

def calcsum(num):
    s=0
    for i in num:
        s+=i
    return s
def calcavg(num):
    s=0
    for i in num:
        s+=i
    av=s/len(num)
    return av
def maxi(num):
    maxnum=num[0]
    for i in num:
        if i>maxnum:
            maxnum=i
    return maxnum
def mini(num):
    minnum=num[0]
    for i in num:
        if i<minnum:
            minnum=i
    return minnum

fw=open("file1_result","w")
fw.write(f"The sum is {calcsum(num)} \n")
fw.write(f"The average is {calcavg(num)} \n")
fw.write(f"The maximum number is {maxi(num)} \n")
fw.write(f"The minimum number is {mini(num)} \n")
fw.close()