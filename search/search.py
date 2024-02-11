# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

    #print ("Start:"), problem.getStartState()
    #print ("Is the start a goal?"), problem.isGoalState(problem.getStartState())
    #print ("Start's successors:"), problem.getSuccessors(problem.getStartState())

def depthFirstSearch(problem):
    from util import Stack
    stack = Stack()
    visitedList = set()
    # Initial vertex start state
    stack.push((problem.getStartState(), [], 0))

    while not stack.isEmpty():
        # each layer of the stack will have the currentnode, the list of actions so far, and the cost
        node, actionslist, cost = stack.pop()
        
        # Ends the search if the pellet node has been found
        if(problem.isGoalState(node)):
            return actionslist
        
        if node not in visitedList: # if the node hasn't been visited yet...
            visitedList.add(node)

            for neighbour, action, stepCost in problem.getSuccessors(node):
                if neighbour not in visitedList:
                    newActionList = actionslist + [action]
                    newCost = cost + stepCost
                    stack.push((neighbour, newActionList, newCost))

    util.raiseNotDefined()

def breadthFirstSearch(problem):
    from util import Queue
    queue = Queue()
    visitedlist = set()

# Same implementation as depth first search but with a queue instead of a stack
    queue.push((problem.getStartState(), [], 0))

    while not queue.isEmpty():
        node, actionslist, cost = queue.pop()

        if(problem.isGoalState(node)):
            return actionslist
        
        if node not in visitedlist:
            visitedlist.add(node)
            
            for neighbour, path, stepCost in problem.getSuccessors(node):
                if neighbour not in visitedlist:
                    newActionList = actionslist + [path]
                    newCost = cost + stepCost
                    queue.push((neighbour, newActionList, newCost))
    
    util.raiseNotDefined()

def uniformCostSearch(problem):
    from util import PriorityQueue
    priorityQueue = PriorityQueue()
    visitedList = set()

    priorityQueue.push((problem.getStartState(), [], 0), 0)

    while not priorityQueue.isEmpty():
        node, actionslist, cost = priorityQueue.pop()

        if(problem.isGoalState(node)):
            return actionslist
        
        if node not in visitedList:
            visitedList.add(node)

            for neighbour, path, stepCost in problem.getSuccessors(node):
                if neighbour not in visitedList:
                    newActionList = actionslist + [path]
                    newCost = cost + stepCost
                    priorityQueue.push((neighbour, newActionList, newCost), newCost)


    
    util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
