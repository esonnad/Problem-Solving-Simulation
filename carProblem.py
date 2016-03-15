from featurecost import Problem, uniformCostSearch, Node


carTree = Node("A")

carTree.add_child(Node("B", [1, 3, 6, 8]))
carTree.add_child(Node("C", [2, 9, 6, 4]))
carTree.add_child(Node("D", [4, 4, 7, 1]))
b = carTree.children[0]
c = carTree.children[1]
d = carTree.children[2]

b.add_child(Node("E", [10, 9, 8, 7]))
b.add_child(Node("F", [3, 2, 2, 8]))
b.add_child(Node("G", [5, 0, 10, 2]))
e = b.children[0]
f = b.children[1]
g = b.children[2]

e.add_child(Node("I", [3, 1, 9, 4]))
e.add_child(Node("F2", [3, 2, 2, 8]))
i = e.children[0]
f2 = e.children[1]

i.add_child(Node("GOAL",[5, 2, 9, 6]))

f2.add_child(Node("I2", [3, 1, 9, 4]))
i2 = f2.children[0]

i2.add_child(Node("GOAL",[5, 2, 9, 6]))

f.add_child(Node("I3", [3, 1, 9, 4]))
i3 = f.children[0]

i3.add_child(Node("GOAL",[5, 2, 9, 6]))

g.add_child(Node("GOAL",[5, 2, 9, 6]))

c.add_child(Node("D2", [4, 4, 7, 1]))
d2 = c.children[0]

d2.add_child(Node("H", [6, 1, 2, 4]))
d2.add_child(Node("L2", [1, 10, 8, -10]))
h = d2.children[0]
l2 = d2.children[1]

h.add_child(Node("J", [10, 10, 1, 3]))
h.add_child(Node("K", [2, 2, 4, 0]))
j = h.children[0]
k = h.children[1]

j.add_child(Node("GOAL",[5, 2, 9, 6]))

k.add_child(Node("J2", [10, 10, 1, 3]))
j2 = k.children[0]

j2.add_child(Node("GOAL",[5, 2, 9, 6]))

l2.add_child(Node("H2", [6, 1, 2, 4]))
h2 = l2.children[0]

h2.add_child(Node("J7", [10, 10, 1, 3]))
h2.add_child(Node("K4", [2, 2, 4, 0]))
j7 = h2.children[0]
k4 = h2.children[1]

j7.add_child(Node("GOAL",[5, 2, 9, 6]))

k4.add_child(Node("J8", [10, 10, 1, 3]))
j8 = k4.children[0]

j8.add_child(Node("GOAL",[5, 2, 9, 6]))

d.add_child(Node("H3", [6, 1, 2, 4]))
d.add_child(Node("L", [1, 10, 8, -10]))
h3 = d.children[0]
l = d.children[1]

h3.add_child(Node("J3", [10, 10, 1, 3]))
h3.add_child(Node("K2", [2, 2, 4, 0]))
j3 = h3.children[0]
k2 = h3.children[1]

j3.add_child(Node("GOAL",[5, 2, 9, 6]))

k2.add_child(Node("J4", [10, 10, 1, 3]))
j4 = k2.children[0]

j4.add_child(Node("GOAL",[5, 2, 9, 6]))

l.add_child(Node("H4", [6, 1, 2, 4]))
h4 = l.children[0]

h4.add_child(Node("J5", [10, 10, 1, 3]))
h4.add_child(Node("K3", [2, 2, 4, 0]))
j5 = h4.children[0]
k3 = h4.children[1]

j5.add_child(Node("GOAL",[5, 2, 9, 6]))

k3.add_child(Node("J6", [10, 10, 1, 3]))
j6 = k3.children[0]

j6.add_child(Node("GOAL",[5, 2, 9, 6]))




weights1 = [.25, .25, .25 ,.25]
weights2 = [.5, .23, .1, .1]
weights3 = [.1, .2 ,.2 ,.5]
weights4 = [0, 0, 0, 1]

carProblem = Problem(carTree, "GOAL")
#print "Path for weights1:", (uniformCostSearch(carProblem, weights1))
#print "Path for weights2:", (uniformCostSearch(carProblem, weights2))
#print "Path for weights3:", (uniformCostSearch(carProblem, weights3))
print "Path for weights4:", (uniformCostSearch(carProblem, weights4))