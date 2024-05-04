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

def depthFirstSearch(problem: SearchProblem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    
    # Initializing variables
    MyStack = util.Stack() #
    visited = set()
    start_state = problem.getStartState()
    MyStack.push((start_state, []))

    while not MyStack.isEmpty(): # while there is still data is in the stack
        currentState,actions = MyStack.pop() # where are we RN
        if problem.isGoalState(currentState): # if we are at goal, return
            return actions
        if currentState not in visited: # if we are at a new location
            visited.add(currentState) # report that weve been here.
            successors = problem.getSuccessors(currentState) # get next states
            for next, action, cost in successors: #search along tree
                if next not in visited:
                    MyStack.push((next,actions + [action]))
    
    util.raiseNotDefined()

def breadthFirstSearch(problem: SearchProblem):
    """Search the shallowest nodes in the search tree first."""
    MyQueue = util.Queue() #
    visited = set()
    start_state = problem.getStartState()
    MyQueue.push((start_state, []))


    #litereally same thing as depth but with Queue instead of stack
    while not MyQueue.isEmpty():  # while there is still data is in the stack
        currentState,actions = MyQueue.pop() # where are we RN
        if problem.isGoalState(currentState): # if we are at goal, return
            return actions
        if currentState not in visited: # if we are at a new location
            visited.add(currentState) # report that weve been here.
            successors = problem.getSuccessors(currentState) # get next states
            for next, action, cost in successors: #search along tree
                if next not in visited:
                    MyQueue.push((next,actions + [action]))

    util.raiseNotDefined()

def uniformCostSearch(problem: SearchProblem):
    """Search the node of least total cost first."""
    
    MyPQueue = util.PriorityQueue() #
    visited = set()
    start_state = problem.getStartState()
    MyPQueue.push((start_state, [], 0),0)
    
    while not MyPQueue.isEmpty():
        currentState, actions, totalCost = MyPQueue.pop()  # where we are
        if problem.isGoalState(currentState): # if we are at ending return
            return actions
        if currentState not in visited: #if we havent been here before, 
            visited.add(currentState) #add it to the set
            successors = problem.getSuccessors(currentState) # get next states
            for  next, action, cost in successors:
                if next not in visited: # if we are at a new location
                    MyAction = actions + [action]
                    MyCost = totalCost + cost
                    MyPQueue.push((next,MyAction,MyCost),MyCost)

    util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem: SearchProblem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    MyPQueue = util.PriorityQueue() #
    visited = set()
    start_state = problem.getStartState()
    MyPQueue.push((start_state, [], 0),heuristic(start_state,problem))

    while not MyPQueue.isEmpty():
        currentState,actions,totalCost = MyPQueue.pop()
        if problem.isGoalState(currentState):
            return actions
        if currentState not in visited:
            visited.add(currentState)
            successors = problem.getSuccessors(currentState)
            for next,action,cost in successors:
                if next not in visited:
                    MyAction = actions + [action]
                    MyCost = totalCost + cost
                    priority = MyCost + heuristic(next,problem)
                    MyPQueue.push((next,MyAction,MyCost),priority)


    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
