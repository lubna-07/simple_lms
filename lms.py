class library:
    def __init__(self,list,name):
        self.booklist=list
        self.libname=name
        self.lenddict={}

    def dis(self):
        print("We have the following books in : {self.libname}")
        for book in self.booklist:
            print(book)
    def add(self,book):
        self.booklist.append(book)
        print("Book have been added")
    def lend(self,user,book):
        if book not in self.lenddict.keys():
            self.lenddict.update({book:user})
            print("Book is available..you can take your book now")
        else:
            print(f"Book is already taken by {self.lenddict[book]}")

    def returnbook(self,book):
         self.lenddict.pop(book)

if __name__ == '__main__':
    lubna=library(["python","c++","java","c","c#","swift"],"lms")
    print(f"Welcome to {lubna.libname}... ")
    while True:
        print("Do u want to \n1.Display\n2.Lend\n3.Add\n4.Return\n")
        print("Enter your choice")
        user_choice=input()
        if user_choice not in ['1','2','3','4']:
            print("Please enter a valid option")
            continue
        else :
            user_choice=int(user_choice)
        if user_choice==1:
            lubna.dis()
        elif user_choice==2:
            name=input("Enter your name")
            book = input("Enter the name of the book you want to issue")
            lubna.lend(name,book)
        elif user_choice==3:
            add_book = input("Enter the name of the book you want to add")
            lubna.add(add_book)
        elif user_choice==4:
            ret_book=input("Enter the name of the book you want to return")
            lubna.returnbook(ret_book)
        else:
            print("Invalid option")

        print("Enter q to quit or c to continue")
        user_choice2 = ""
        while user_choice2!='c' and user_choice2!='q' :
            user_choice2 = input()
            if(user_choice2=="q"):
                exit()
            else:
                continue
           # print("Enter q to quit or c to continue")
