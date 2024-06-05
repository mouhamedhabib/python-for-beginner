set = {0, "1",2,"3",4, "Iteam1", "Iteam2" , "Iteam3"}
print (set)
set.add("Iteam4" )
print (set)
set.update (["Iteam10" , 5])
print (set)
set.remove (0)
elementRemove = ["Iteam4" , 2]
for element in elementRemove :
    set.remove(element)

print(set)
