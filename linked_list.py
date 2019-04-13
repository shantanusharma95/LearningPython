import sys
class node:
    def __init__(self,data):
        self.data = data
        self.next = None

class linked_list:
    def __init__(self):
        self.Head=None

    #add new node to linked list
    def new_node(self,data):
        print("Inserting ",data,"...")
        if self.Head==None:
            self.create_head(data)  #create head node if linked list empty
        else:
            temp=self.Head
            while(temp.next!=None):
                temp=temp.next
            temp.next=node(data)

    #create new head node
    def create_head(self,data):
        temp=node(data)
        self.Head=temp

    #remove the first occurrence of node if matching data is found
    #can be improved by asking user to delete a specific occurrence or all occurrences
    def remove_node(self,data):
        if self.Head==None:
            print("List is empty!")
            return
        if int(self.Head.data)==data:
            temp=self.Head
            self.Head=self.Head.next
            del(temp)
            print("Deleted ",data)
            return
        temp=self.Head
        tempNext=temp.next
        while(tempNext!=None):
            print("data is ",data," and tempNext data is ",tempNext.data)
            if int(tempNext.data)==data:
                temp.next=tempNext.next
                del(tempNext)
                print("Deleted ", data)
                return
            temp=temp.next
            tempNext=tempNext.next
        print("Data Not Found!")

    #display the entire linked list
    def display(self):
        temp=self.Head
        if temp==None:
            print("List is empty!")
            return
        while(temp!=None):
            print(temp.data)
            temp=temp.next

    #count and display total nodes
    def node_count(self):
        temp=self.Head
        count=0
        while temp!=None:
            count+=1
            temp=temp.next
        print("\nTotal nodes = ",count)

def main():
    link=linked_list()
    while(True):
        print("1. Enter New Node")
        print("2. Remove A Node")
        print("3. Node count")
        print("4. Display List")
        print("5. Exit")
        user_choice=input("Enter your Choice!\n")
        user_choice=int(user_choice)
        if user_choice == 1:
            data=input("Enter data")
            link.new_node(data)
            print("Updated Linked List : ")
            link.display()
        elif user_choice == 2:
            data=input("Enter data to remove : ")
            data=int(data)
            link.remove_node(data)
        elif user_choice == 3:
            link.node_count()
        elif user_choice == 4:
            link.display()
        elif user_choice == 5:
            sys.exit(0)
        else:
            print("Please enter a valid choice!")

if __name__=='__main__':
    main()