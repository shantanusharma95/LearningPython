All files in this directory are implementation of a data structure in Python 3.

For ease of reading and record keeping, I am listing them down-
1. Linked List (All operations) - DONE
2. Stack - DONE
3. Queue - DONE
4. Priority Queue - DONE
5. Double Linked List - (Not implemented, as it is a simple variation of Single Linked List where we can add an additional 'prev'
   pointed to the node, which will maintain track of previous node as is mainted for next node under 'next' pointer. Deletion of a
   node can be either by taking index position from user, or based on a specific value of a node.)
6. Double Ended Queue - DONE
7. Circular Linked List - (Not implemented, as it is a variation of Double Linked List where tail can be connected to Head instead
   of making the last node point to null. However, there are amazing problems based on Circular Linked List which one must try!
8. Hashing for numerical and string values (Can be extended to Hash-Maps) - DONE
9. Tree with BFS and DFS - DONE


For my personal reference and future revisions, I am listing down more details about each implementation. The bullet number below follows
the bullet sequence as per the list above.

##### 2. Stack

* I implemented it using linked list, it could have been done by array also.
* Arrays would limit the size of stack, and would now allow dynamic size increase (that can be overcome by array resizing once array
 reaches the size limit, but it will waste memory if stack grows too much but is only larger marginally by the half of array size)
* Linked list can grow and shrink as per need, but additional memory is used to maintain pointers to the next nodes
* Arrays, however can provide quick access as they are indexed, unlike Linked Lists.

##### 3. Queue

* The time for insertion and deletion is O(1) and for displaying the queue elements is O(n)

##### 4. Priority Queue

* The time for insertion is O(n) as comparison is done for priority of each element, but for deletion is O(1)
* Imagine all elements with highest priority are on the left (tail) side and all with lower are towards right (head) side
* Dequeuing is done at the left(tail) side

##### 6. Double Queue

* All operations have a time complexity of O(1), except of course, displaying the entire queue.
* Implemented with a linked list

##### 8. Hash Table

* Hash table (fast, synchronous) is implemented in the way of dictionaries in Python. Hence, I have only used some basic operations to 
 depict the same.
* The keys can created by us based on user input of values, via any alogorithm of our choice. In that case, the user will not have to 
 enter the key. I have added an example of one such algorithm in the file, as pseudo code for key generation.

##### 9. Binary Search Tree

* BST including basic operations like insertion, deletion and searching of node.
* BFS (Breadth First Search) traversal is included.
* DFS (Depth First Search) traversals (Pre-order , In-order and Post-order) are included
  
