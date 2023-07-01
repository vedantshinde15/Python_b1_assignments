def write_data(roll_no,name,class_name,file="data_1.txt"):
    try:
        f=open("data_1.txt","a")
        f.writelines([roll_no+"\n",name+"\n",class_name+"\n"])
    except IOError:
        print("error found while writing to the file")

def read_data(file="data_1.xt"):
    try:
        f=open("data_1.txt","r")
        lines=f.readlines()
        print("Roll Number:", lines[0])
        print("Name:", lines[1])
        print("Class:", lines[2])
    except IOError:
        print("error found while reading to the file")

write_data("12", "Vedant", "SYCO")
read_data()


    






