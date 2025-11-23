import csv
with open ("complaint.csv", "w", newline='') as f:
    writer=csv.writer(f)
    writer.writerow(["Date","Name","Category","Amount"])
    def add_complaint():
        date=input("Enter date (DD-MM-YYYY): ")
        Name=input("Enter name : ")
        ID=input("enter identification (Like Aadhar no.): ")
        complain=input("Write complaint(limit-100 words) : ")

        with open("complaint.csv", "a", newline='') as f:
            w=csv.writer(f)
            w.writerow([date,Name,ID,complain])
            print("Complaint added successfully...")
            f.close()
            
    def view_complaint(dat):
        with open("complaint.csv", "r") as f:
            r=csv.reader(f)
            if dat=='ALL':
                for row in r:
                    print(row)
            for ro in r:
                if ro[0]==dat:
                    print(row)
                else:
                    print('Wrong date')
            f.close()

    def del_complaint(naam):
        with open("complaint.csv","r") as f:
            r=csv.reader(f)
            r1=[]
            for row in r:
                if row[1]!=naam:
                    r1.append(row)
            f.close()
        with open("complaint.csv","w") as f:
            w=csv.writer(f)
            w.writerows(r1)
            f.close()
        print("Complaint deleted successfully...")
    f.close()
       
while True:
    print("/n 1. Add complaint /n 2. View complaint(to view all , enter 'ALL') /n 3. Delete complaint /n 4. Exit")
    ch=int(input("Enter choice: "))
    if ch==1:
        add_complaint()
    elif ch==2:
        d=input('enter date-')
        view_complaint(d)
    elif ch==3:
        n=input('enter name-')
        del_complaint(n)
    elif ch==4:
        break
    else:
        print("invalid choice...")
