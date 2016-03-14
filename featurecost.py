

import util

class Node(object):
    def __init__(self, name, features= [0,0,0,0]):
        self.name = name
        self.features = {'SD': features[0], 'T': features[1], 'F': features[2], 'S': features[3]}
        self.children = []

    def add_child(self, obj):
        self.children.append(obj)


class Problem(object):
	def __init__(self, start, goal):
		self.start = start
		self.goal = goal
	 
	def getStartState(self):
		return self.start

	def isGoalState(self, node):
		if node.name == self.goal:
			return True
		else:
			return False

	def getSuccessors(self, node):
		return node.children

	def getCost(self, node, weights):
		cost = 0
		for feature in node.features:
			cost += node.features[feature]*weights[feature]
		return cost


def uniformCostSearch(problem, weights):
    """Search the node of least total cost first."""
    fringe = util.PriorityQueue()
    explored = []
    start = problem.getStartState()
    weights = {'SD': weights[0], 'T': weights[1], 'F': weights[2], 'S': weights[3]}

    fringe.push((start, [start.name]), 0)
    if problem.isGoalState(start):
        return [start.name]
    while fringe.isEmpty() is False:
        node = fringe.pop()
        print "node popped:", node[0].name
        if node[0].name not in explored: 
            explored.append(node[0].name)
            if problem.isGoalState(node[0]):
                return node[1]
            for successor in problem.getSuccessors(node[0]):
                state = successor
                path = list(node[1])
                if state.name not in explored:
                    path.append(state.name)
                    cost = problem.getCost(state, weights)
                    fringe.push((state, path), cost)
                    print "cost:", state.name, cost



#

