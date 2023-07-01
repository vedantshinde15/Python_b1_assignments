def ds(roll_no,name):
    global List 
    global Tuple
    global Set
    global Dictionary
    List=[roll_no,name]
    Tuple=(roll_no,name)
    Set={roll_no,name}
    Dictionary={"Roll no.": roll_no , "Name":name}

def printds():
    print("\nList       : ",List,"\n")
    print("Tuple      : ",Tuple,"\n")
    print("Set        : ",Set,"\n")
    print("Dictionary : ",Dictionary,"\n")

#changing the values during runtime
def dsUpdate():
   print("Updating Data Structures :-\n")
   nr=int(input("Enter the roll no : "))
   nn=input("Enter the name    : ")
   ds(nr,nn)
   List.append("SYCO-A")
   Set.add("Thakur")
   Dictionary["Percentage"]="90"           
   Dictionary.update({"Grade":"A"})
ds(12,"Vedant")
printds()
dsUpdate()
printds()

#Deleting data structures
del List
del Tuple
del Set
del Dictionary