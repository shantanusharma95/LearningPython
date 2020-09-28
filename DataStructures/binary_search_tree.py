import sys
from queue import Queue

class node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

class binarySearchTree:
    def __init__(self):
        self.root=None
        self.queueSize=0

    def addItem(self,data):
        if not self.root:
            self.root=node(data)
        else:
            traverse=self.root
            while traverse!=None:
                if data<traverse.data:
                    if traverse.left!=None:
                        traverse=traverse.left
                    else:
                        traverse.left=node(data)
                        break
                elif data>traverse.data:
                    if traverse.right!=None:
                        traverse=traverse.right
                    else:
                        traverse.right=node(data)
                        break
                else:
                    print("Element exists, no duplicates allowed!")
                    return
        print("{} added successfully!".format(data))
        return

    def bf_traversal(self):

        q = Queue()
        if self.root==None:
            print("Empty tree!")
            return
        else:
            q.put(self.root)
            while not q.empty():                    
                tmp=q.get()
                print(tmp.data," ")
                if tmp.left!=None:
                    q.put(tmp.left)
                if tmp.right!=None:
                    q.put(tmp.right)
        del(q)

    def deleteItem(self,data):
        if self.root:
            tmp=self.root
            tmp_prev=None
            while tmp:
                if tmp.data == data:
                    #Case 1 - deletion node has no child
                    if (tmp.right==None and tmp.left==None) and tmp_prev!=None:
                        if tmp.data<tmp_prev.data:
                            tmp_prev.left=None
                        else:
                            tmp_prev.right=None
                        tmp=None

                    elif (tmp.right==None and tmp.left==None) and tmp_prev==None:
                        self.root=tmp=None

                    #Case 2 - deletion node has just one child
                    elif (tmp.right and not(tmp.left)):
                        if tmp==self.root:
                            self.root=self.root.right
                            print("Value deleted!\n")
                            return
                        tmp.data=tmp.right.data
                        tmp.right=None
                    elif (tmp.left and not(tmp.right)):
                        if tmp==self.root:
                            self.root=self.root.left
                            print("Value deleted!\n")
                            return
                        tmp.data=tmp.left.data
                        tmp.left=None

                    #Case 3 - deletion node has both left and right children
                    else:
                        tmp_root = tmp
                        tmp_prev = tmp
                        tmp = tmp.right

                        while tmp.left!=None:
                            tmp_prev = tmp
                            tmp = tmp.left
                        tmp_root.data = tmp.data
                        if tmp.right:
                            tmp_prev.left = tmp.right                                
                        else:
                            tmp_prev.left = None
                        del(tmp)
                    
                    print("Value deleted!\n")
                    return
                elif data<tmp.data:
                    tmp_prev=tmp
                    tmp=tmp.left

                elif data>tmp.data:
                    tmp_prev=tmp
                    tmp=tmp.right       

            print("Element not found!")
        print("No elements in the tree!")

    def df_preTraversal(self):
        q = []
        if self.root==None:
            print("Empty tree!")
            return
        else:
            tmp = self.root
            while True:
                while tmp!=None:
                    if tmp.right:
                        q.append(tmp.right)
                    print(tmp.data)
                    tmp=tmp.left
                if q:
                    tmp=q.pop()
                    continue
                else:
                    return

    def df_inTraversal(self):
        tmp = self.root
        q = []
        while True:
            while tmp!=None:
                q.append(tmp)
                tmp=tmp.left
            if q and tmp==None:
                tmp = q.pop()
                print(tmp.data)
                tmp = tmp.right
                continue
            elif (not q) and tmp==None:
                return
            
        # alternate solution
        # while True:
        #    while temp is not None:
        #        stk.append(temp)
        #        temp = temp.left
        #    
        #    if stk and temp==None:
        #        temp=stk.pop()
        #        print(temp.value," ")
        #        temp = temp.right

    #peek function used during post order traversal
    def peek(self, stk): 
        if len(stk) > 0: 
            return stk[-1] 
        return None

    def df_postTraversal(self):
        if self.root:
            tmp = self.root
            stack = []
            while True:
                while tmp!=None:
                    if tmp.right!=None:
                        stack.append(tmp.right)
                    stack.append(tmp)
                    tmp = tmp.left
                tmp = stack.pop()

                #if popped item has a right child and right child is on top of stack
                if tmp.right and self.peek(stack)==tmp.right:
                    tmp_pop = tmp
                    tmp = stack.pop()
                    stack.append(tmp_pop)
                else:
                    print(tmp.data)
                    tmp = None
                if len(stack)<1:
                    return
        else:
            print("No elements in the tree!")
        return

def main():
    bst=binarySearchTree()
    while(True):
        print("1. Add new element")
        print("2. Delete an element")
        print("3. BFS traversal")
        print("4. DFS Pre-Order traversal")
        print("5. DFS In-Order traversal")
        print("6. DFS Post-Order traversal")
        print("7. Exit")
        user_choice=input("Enter your Choice!\n")
        try:
            user_choice=int(user_choice)
            if user_choice == 1:
                data=int(input("Enter value"))
                bst.addItem(data)
            elif user_choice == 2:
                data=int(input("Enter value to remove"))
                bst.deleteItem(data)
            elif user_choice == 3:
                bst.bf_traversal()
            elif user_choice == 4:
                bst.df_preTraversal()
            elif user_choice == 5:
                bst.df_inTraversal()
            elif user_choice == 6:
                bst.df_postTraversal()
            elif user_choice == 7:
                sys.exit(0)
            else:
                print("Please enter a valid choice!")

        #handling error if user enters a non integral value
        except ValueError:
            print("Please enter a valid integral choice!")
            continue

if __name__=='__main__':
    main()
