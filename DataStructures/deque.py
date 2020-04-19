"""
insertFront(): Adds an item at the front of Deque.
insertEnd(): Adds an item at the rear of Deque.
removeFront(): Deletes an item from front of Deque.
removeEnd(): Deletes an item from rear of Deque.
displayFront(): Gets the front item from queue.
displayEnd(): Gets the last item from queue.
displayQueue(): Display all elements in the queue
"""
import sys

class node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None

class doubleQueue:
    def __init__(self):
        self.Head=None
        self.Tail=None
        self.queueSize=0

    def insertFront(self,data):
        if self.Head==None:
            tmp=node(data)
            self.Head=self.Tail=tmp
            del(tmp)
        else:
            tmp=node(data)
            tmp.next=self.Head
            tmp.prev=None
            self.Head=tmp
        self.queueSize+=1
        
    def insertEnd(self,data):
        if self.Head==None:
            tmp=node(data)
            self.Head=self.Tail=tmp
            del(tmp)
        else:
            tmp=node(data)
            tmp.next=None
            tmp.prev=self.Tail
            self.Tail.next=tmp
            self.Tail=tmp
        self.queueSize+=1

    def removeFront(self):
        if self.queueSize==0:
            print("Queue empty!")
        else:
            tmp=self.Head
            self.Head=self.Head.next
            del(tmp)
            self.queueSize-=1

    def removeEnd(self):
        if self.queueSize==0:
            print("Queue empty!")
        else:
            tmp=self.Tail
            self.Tail=self.Tail.prev
            del(tmp)
            self.queueSize-=1

    def displayFront(self):
        if self.queueSize==0:
            print("Queue empty!")
        else:
            print(self.Head.data)

    def displayEnd(self):
        if self.queueSize==0:
            print("Queue empty!")
        else:
            print(self.Tail.data)

    def displayQueue(self):
        if self.queueSize==0:
            print("Queue empty!")
        else:
            tmp=self.Head
            while tmp!=None:
                print(tmp.data,"\n")
                tmp=tmp.next

def main():
    queue=doubleQueue()
    while(True):
        print("1. Insert at front")
        print("2. Insert at end")
        print("3. Delete at front")
        print("4. Delete at end")
        print("5. Display value at front")
        print("6. Display value at end")
        print("7. Display all elements")
        print("8. Exit")
        user_choice=input("Enter your Choice!\n")
        user_choice=int(user_choice)
        if user_choice == 1:
            data=input("Enter value")
            queue.insertFront(data)
        elif user_choice == 2:
            data=input("Enter value")
            queue.insertEnd(data)
        elif user_choice == 3:
            queue.removeFront()
        elif user_choice == 4:
            queue.removeEnd()
        elif user_choice == 5:
            queue.displayFront()
        elif user_choice == 6:
            queue.displayEnd()
        elif user_choice == 7:
            queue.displayQueue()
        elif user_choice == 8:
            sys.exit(0)
        else:
            print("Please enter a valid choice!")

if __name__=='__main__':
    main()
