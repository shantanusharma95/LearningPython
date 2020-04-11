import sys

class node:
    def __init__(self,data):
        self.data=data
        self.next=None

class stack:
    def __init__(self):
        self.Head=None
        self.stackSize=0

    #add new node to the stack
    def push(self,data):
        print("Pushing ",data,"...")
        if self.Head==None:
            self.Head=node(data)
        else:
            temp=node(data)
            temp.next=self.Head
            self.Head=temp  
        self.stackSize+=1

    #display data at head and remove from list
    def pop(self):
        print("Value at top is ",self.Head.data)
        temp=self.Head
        if(self.Head==None):
            del(self.Head)
        else:
            self.Head=self.Head.next
            del(temp)        
        print("Popping...Done!")
        self.stackSize-=1

    def peek(self):
        print("Value at top of stack is ",self.Head.data)

    def isEmpty(self):
        if(self.Head==None):
            return True
        return False

    def stackCount(self):
        print("Size of the stack is ",self.stackSize)

    #display the entire stack 
    def display(self):
        temp=self.Head
        if temp==None:
            print("Stack is empty!")
            return
        while(temp!=None):
            print(temp.data)
            temp=temp.next

def main():
    stackObj=stack()
    while(True):
        #add a new element on the top
        print("1. Push")
        
        #display and remove top element
        print("2. Pop")

        #display the top element
        print("3. Peek")

        #return true if stack is empty
        print("4. Empty Check")

        #display size of stack
        print("5. Size Check")

        #display size of stack
        print("6. Display Stack")

        print("7. Exit")
        user_choice=input("Enter your Choice!\n")
        user_choice=int(user_choice)
        if user_choice == 1:
            data=input("Enter data")
            stackObj.push(data)
            print("Updated Stack : ")
            stackObj.display()
        elif user_choice == 2:
            print("Popping from stack...")
            stackObj.pop()
        elif user_choice == 3:
            stackObj.peek()
        elif user_choice == 4:
            print(stackObj.isEmpty())
        elif user_choice == 5:
            stackObj.stackCount()
        elif user_choice == 6:
            stackObj.display()
        elif user_choice == 7:
            sys.exit(0)
        else:
            print("Please enter a valid choice!")

if __name__=='__main__':
    main()
