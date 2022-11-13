import List1
import date

def borrow_Book():
    borrowed = False
    
    while(True):
        firstname = input("Enter the first name of the borrower: ")
        if firstname.isalpha():
            break
        print("*----------------------------*")
        print("Please input alphabet from A-Z")
        
    while(True):
        lastname = input("Enter the last name of the borrower: ")
        if lastname.isalpha():
            break
        print("*----------------------------*")
        print("Please input alphabet from A-Z")
            
    bfile = "Borrowed by-"+firstname+".txt"
    
    with open(bfile,"w") as File:
        File.write("Shibuya Library"+"\n")
        File.write("Borrowed By: "+firstname+" "+lastname+"\n")
        # File.write("Date: " + dt.getDate()+"Time:"+ dt.getTime())
        File.write("S.N. \t\t Bookname \t      Authorname \n" )
    
    while borrowed == False:
        print()
        print("Please select the book you want to borrow:")
        for i in range(len(List1.bookname)):
            print("Enter",i,"to borrow book", List1.bookname[i])
            print("*----------------------------*")
     
        try:   
            a = int(input("Enter the number of book you want to borrow: "))
            if (a<0):
                print("Please Input positive value")
            else:
                try:
                    if(int(List1.quantity[a])>0):
                        print("The required book is available")
                        with open(bfile,"a") as File:
                            File.write("1. \t\t"+ List1.bookname[a]+"\t\t "+List1.authorname[a]+"\n")

                        List1.quantity[a]=int(List1.quantity[a])-1
                        with open("Stock.txt","w") as File:
                            for i in range(len(List1.lines)):
                                File.write(List1.bookname[i]+","+List1.authorname[i]+","+str(List1.quantity[i])+","+"$"+List1.cost[i]+"\n")

                        # for multiple book borrowing 
                        loop = True
                        count = 1  
                        while loop == True:

                            more_borrow = input("Do you want to borrow more books? However you cannot borrow same book twice. Press Y for Yes and N for No.")
                            if(more_borrow.upper() == "Y"):
                                count = count+1
                                print("Please select an option below: ")
                            
                                for i in range(len(List1.bookname)):
                                    print("Enter", i, "to borrow book", List1.bookname[i])
                                    print("*----------------------------*")
                                a = int(input("Enter the number of books you want to borrow: "))

                                if(int(List1.quantity[a])>0):
                                    print("The required book is available")
                                    with open(bfile,"a") as File:
                                        File.write(str(count) +". \t\t"+ List1.bookname[a]+"\t\t  "+List1.authorname[a]+"\n")

                                    List1.quantity[a]=int(List1.quantity[a])-1
                                    with open("Stock.txt","w") as File:
                                        for i in range(len(List1.lines)):
                                            File.write(List1.bookname[i]+","+List1.authorname[i]+","+str(List1.quantity[i])+","+"$"+List1.cost[i]+"\n")
                                            borrowed = False
                                else:
                                    loop = False
                                    break
                            elif (more_borrow.upper() == "N"):
                                print ("Thank you for borrowing book. ")
                                print("*----------------------------*")
                                loop = False
                                borrowed = True
                            else:
                                print("Please choose as instructed")
                        
                    else:
                        print("Book is not available")
                        borrow_Book()
                        borrowed = False
                except IndexError:
                    print("*----------------------------*")
                    print("Please choose book according to their number.")
        except ValueError:
                print("*----------------------------*")
                print("Please choose as suggested.")
