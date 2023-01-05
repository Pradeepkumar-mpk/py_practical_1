list=[1,2,3,4,5,6,7,8,9]
dict={"even":[],"odd":[]}
for i in range(len(list)):
    if i%2==0:
        dict["even"].append(list[i])
    else:
        dict["odd"].append(list[i])
print (dict)
        
        
 
