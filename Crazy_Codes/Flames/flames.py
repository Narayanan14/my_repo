print("Welcome to the World of Flames...")

name1=input("Enter the first name : ")
name2=input("Enter the second name : ")

list1=[i.lower() for i in name1 if i!=' ']
list2=[i.lower() for i in name2 if i!=' ']

for i in range(len(list1)):
    if list1[i] in list2:
        list2.remove(list1[i])
        list1[i]='_'

list1=[i for i in list1 if i!='_']

final_list=list1+list2

flames=['F','L','A','M','E','S']
j=0

while len(flames)>1:
    for i in range(len(final_list)):
        p=flames[j]
        j=j+1
        if j>len(flames)-1:
            j=0
    if j==0:
        flames.remove(p)
    else:
        flames.remove(p)
        j=j-1

print(flames[0])

