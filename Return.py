import List1
import date


def Return_book():
    name = input("Enter the name of borrower: ")
    bfile = "Borrowed by-"+name+".txt"
    try:
        with open(bfile,"r") as File:
            lines = File.readlines()
            lines = [bfile.strip("$") for bfile in lines]
    
        with open(bfile,"r") as File:
            data = File.read()
            print(data)
    except:
        print("The borrower name is incorrect")
        Return_book()

    b = "Return-"+name+".txt"
    with open(b,"w")as File:
        File.write("    Library Management System \n")
        File.write("    Returned By: "+ name+"\n")
        File.write("    Date: " + date.getDate()+"    Time:"+ date.getTime()+"\n\n")
        File.write("S.N.\t\tBookname\t\tCost\n")


    total = 0.0
    for i in range(len(List1.lines)):
        if List1.bookname[i] in data:
            with open(b,"a") as File:
                
                File.write(str(i+1)+"\t\t"+List1.bookname[i]+"\t\t$"+List1.cost[i]+"\n")
                List1.quantity[i]=int(List1.quantity[i])+1
            total += float(List1.cost[i])
            
    print("\t\t\t\t\t\t"+"Total cost: $"+str(total))
    print("Is the return date of book expired?")

    stat = input("Press Y for Yes and N for No")
    if(stat.upper()=="Y"):
        print("By how many days was the book returned late?")
        day = int(input())
        fine = 2*day
        with open(b,"a")as File:
            File.write("\t\t\t\t\tFine: $"+ str(fine)+"\n")
        total+=float(fine)
    


    print("Final Total: "+ "$"+str(total))
    with open(b,"a")as File:
        File.write("\t\t\t\t\tTotal: $"+ str(total))
        print("Thank you for returning our book to the library")
    
        
    with open("Stock.txt","w") as File:
            for i in range(len(List1.lines)):
                File.write(List1.bookname[i]+","+List1.authorname[i]+","+str(List1.quantity[i])+","+"$"+List1.cost[i]+"\n")
