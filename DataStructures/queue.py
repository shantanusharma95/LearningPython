import sys

class node:
    def __init__(self,data):
        self.data=data
        self.next=None

class queue:
    def __init__(self):
        self.Head=self.Tail=None
        self.queueSize=0

    #adds a new value to the head
    def enqueue(self,data):
        temp=node(data)
        if self.Head==None:
            self.Head=temp
            self.Tail=temp
        else:
            self.Head.next=temp
            self.Head=temp 
        self.queueSize+=1

    #removes the most oldest inserted value
    def dequeue(self):
        if self.queueSize==0:
            print("Queue is empty!\n")
            return
        temp=self.Tail
        self.Tail=temp.next
        del(temp)
        self.queueSize-=1

    def sizeCheck(self):
        print("Size of queue is ",self.queueSize)

    def display(self):
        print("The queue contains...\n")
        temp=self.Tail
        while(temp!=None):
            print(temp.data,"  ")
            temp=temp.next
def main():
    queueObj=queue()
    while(True):
        #add a new element at head of queue
        print("1. Enqueue")
        
        #remove element from tail of queue
        print("2. Dequeue")

        #display size of stack
        print("3. Size Check")

        #display size of stack
        print("4. Display Queue")

        print("5. Exit")
        user_choice=input("Enter your Choice!\n")
        user_choice=int(user_choice)
        if user_choice == 1:
            data=input("Enter data")
            queueObj.enqueue(data)
            print("Updated Queue : \n")
            queueObj.display()
        elif user_choice == 2:
            print("Removing from queue...")
            queueObj.dequeue()
        elif user_choice == 3:
            queueObj.sizeCheck()
        elif user_choice == 4:
            queueObj.display()
        elif user_choice == 5:
            sys.exit(0)
        else:
            print("Please enter a valid choice!")

if __name__=='__main__':
    main()
