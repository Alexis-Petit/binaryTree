from pprint import pprint 

class Tree:
	def __init__(self):
		self.root = None;

	def addValue(self, value):
		node = Node(value)
		if (self.root == None):
			self.root = node
		else:
			self.root.addNode(node)

	def traverse(self):
		self.root.visit()

	def search(self, val):
		found = self.root.search(val)
		if(found!=None):
			print("Found : %d" % found)
		else:
			print("Not found")

class Node:
	def __init__(self, value):
		self.val = value
		self.left = None
		self.right = None

	#def __repr__(self):
	#	print ("value : %d" % self.val)

	def getVal(self):
		return self.val

	def addNode(self, node):
		if(node.val<self.val):
			if(self.left == None):
				self.left = node
			else:
				self.left.addNode(node)
		elif(node.val>self.val):
			if(self.right == None):
				self.right = node
			else:
				self.right.addNode(node)
			
	def visit(self):
		if(self.left != None):
			self.left.visit()
		print(self.getVal())
		if(self.right != None):
			self.right.visit()

	def search(self, val):
		if(self.val == val):
			return self.val
		elif(val<self.val and self.left!=None):
			return self.left.search(val)
		elif(val>self.val and self.right!=None):
			return self.right.search(val)
		return None

tree = Tree()
tree.addValue(30)
tree.addValue(40)
tree.addValue(20)
tree.addValue(60)
tree.addValue(10)
tree.addValue(90)

# pprint(vars(tree.root.left))

tree.traverse()

tree.search(40)
