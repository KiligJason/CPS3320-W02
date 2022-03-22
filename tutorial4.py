#tutorial 4
#Ziyiyang Wang 1098529
#Zhaoze Wang 1098471

step=0
class Node:
    
    def __init__(self, data):
      self.left = None
      self.right = None
      self.data = data
# Insert method to create nodes
    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif (data > self.data):
                if self.right is None:
                  self.right = Node(data)
                else:
                  self.right.insert(data)
        else:
            self.data = data

# findval method to compare the value with nodes
    def findval(self, lkpval):
        global step
        if lkpval < self.data:
            step=step+1
            if self.left is None:
                return str(lkpval)+" Not Found. Search steps are: "+str(step)
            return self.left.findval(lkpval)
        elif lkpval > self.data:
            step=step+1
            if self.right is None:
               return str(lkpval)+" Not Found. Search steps are: "+str(step)
            return self.right.findval(lkpval)
        else:
            print(str(self.data) + ' is found. Search steps are: '+str(step))

# Print the tree
    def PrintTree(self):
      if self.left:
         self.left.PrintTree()
      print( self.data),
      if self.right:
         self.right.PrintTree()
root = Node(12)
root.insert(6)
root.insert(14)
root.insert(3)
root.insert(5)
root.insert(1)
root.insert(20)
root.insert(32)

#print search result
print(root.findval(7))
print(root.findval(14))
print(root.findval(32))