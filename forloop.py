# user=int(input("enter the number:"))
# for i in range(1,11):
# print(user,"*",i,"=",i*user)
name=input("enter a name to be reversed:")
rev=""
for i in range(len (name)-1,-1,-1):
    rev+=name[i]
print(rev)

