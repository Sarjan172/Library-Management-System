import Borrow
import List1
import Return

class LibraryManagement():
     print("       Welcome to Shibuya Library        ")
     print("*----------------------------------------------------*")
     print()

     while(True):
       
        print("Library Management System Program Guide")
        print("*-----------------------*")
        print("Enter 1 to view all the available books")
        print("Enter 2 to borrow books from the library")
        print("Enter 3 to return the borrowed books")
        print("Enter 4 to exit the program")
        print("*----------------------------------------------------*")
        print()

        
        try:

            entered = int(input("Enter a number for a task you want to do: "))
            
            if(entered == 1):
                file = open("Stock.txt", "r")
                line = file.read()
                file.close()
                print("Books Available to borrow: ")
                print(line)
                print("*----------------------------------------------------*")
                
            elif(entered == 2):
                List1.list_()
                Borrow.borrow_Book()
                print()
                
            elif(entered == 3):
                List1.list_()
                Return.Return_book()
                print()
                
            elif(entered == 4):
                print()
                print("Thank you for your visit!!")
                print("*-----------*******-----------*******----------------*")
                break
            else:
                 print("Please input valid number")

        except:
            print()
            print("Enter the valid value")
            
            
