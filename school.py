import csv
def writefile(info):
    with open ("student_info.csv",'a',newline="") as csvfile:
        writer=csv.writer(csvfile)
        if csvfile.tell()==0:
            writer.writerow(["name","age","contact_number","mail_id"])
            
        writer.writerow(info)
if __name__ == '__main__':
    condition=True
    num=1
    while(condition):
        st_info=input("enter student information for student{} in the format (name age contact_number mail_id) :"
                      .format(num))
        list=st_info.split(" ")
        print("\nthe entered information is - \n name: {}\n age: {}\n contact_number: {}\n mail_id: {}".format(list[0],list[1],
                                                                                                            list[2],list[3]))
        check=input("is the entered information correct ? (yes/no): ")
        if check =="yes":
            writefile(list)
            cont=input("do you wanter to enter information of next student ? (yes/no) : ") 
            if cont=="yes":
                num=num+1
                condition=True
            elif cont=="no":
                condition=False
        elif check =="no":
            print("\n!!! please re enter the information !!!")
            
            
            
OUTPUT :
enter student information for student1 in the format (name age contact_number mail_id) :subhi 19 1234 subhi@gmail.com

the entered information is - 
 name: subhi
 age: 19
 contact_number: 1234
 mail_id: subhi@gmail.com
is the entered information correct ? (yes/no): yes
do you wanter to enter information of next student ? (yes/no) : yes
enter student information for student2 in the format (name age contact_number mail_id) :madhav 20 5678 mad@gmail.com

the entered information is - 
 name: madhav
 age: 20
 contact_number: 5678
 mail_id: mad@gmail.com
is the entered information correct ? (yes/no): yes
do you wanter to enter information of next student ? (yes/no) : yes
enter student information for student3 in the format (name age contact_number mail_id) :shreyas 14 64784 shre@yahoo.com

the entered information is - 
 name: shreyas
 age: 14
 contact_number: 64784
 mail_id: shre@yahoo.com
is the entered information correct ? (yes/no): yes
do you wanter to enter information of next student ? (yes/no) : no





OUTPUT IN THE EXCEL SHEET :

name	age	contact_number	mail_id
subhi	19	1234	subhi@gmail.com
madhav	20	5678	mad@gmail.com
shreyas	14	64784	shre@yahoo.com




        
