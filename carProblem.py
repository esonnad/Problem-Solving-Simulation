from featurecost import Problem, uniformCostSearch, Node


carTree = Node("A")
carTree.add_child(Node("B", [1, 3, 6, 8]))
b = carTree.children[0]
carTree.add_child(Node("C", [2, 9, 6, 4]))
c = carTree.children[1]
carTree.add_child(Node("D", [4, 4, 7, 1]))
d = carTree.children[2]
c.add_child(d)
print("A's children", carTree.children)

b.add_child(Node("E", [10, 9, 8, 7]))
b.add_child(Node("F", [3, 2, 2, 8]))
b.add_child(Node("G", [5, 0, 10, 2]))
e = b.children[0]
f = b.children[1]
g = b.children[2]
e.add_child(f)

e.add_child(Node("I", [3, 1, 9, 4]))
i = e.children[1]
f.add_child(i)

i.add_child(Node("GOAL", [5, 2, 9, 6]))
goal = i.children[0]

d.add_child(Node("H", [6, 1, 2, 4]))
d.add_child(Node("L", [1, 10, 8, -10]))
h = d.children[0]
l = d.children[1]
l.add_child(h)

h.add_child(Node("J", [10, 10, 1, 3]))
h.add_child(Node("K", [2, 2, 4, 0]))
j = h.children[0]
k = h.children[1]
k.add_child(j)

g.add_child(j)
g.add_child(goal)
j.add_child(goal)


weights1 = [.25, .25, .25 ,.25]
weights2 = [.5, .23, .1, .1]
weights3 = [.1, .2 ,.2 ,.5]
weights4 = [0, 0, 0, 1]

carProblem = Problem(carTree, "GOAL")
print "Path for weights1:", (uniformCostSearch(carProblem, weights1))
print "Path for weights2:", (uniformCostSearch(carProblem, weights2))
print "Path for weights3:", (uniformCostSearch(carProblem, weights3))
print "Path for weights4:", (uniformCostSearch(carProblem, weights4))