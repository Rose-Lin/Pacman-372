from game import Agent
from game import Directions
import random

class DumbAgent (Agent):
    "An agent that goes West until it can't."

    def getAction(self, state):
        "The agent recieves a GameState (defined in pacman.py)."
        print "Location: ", state.getPacmanPosition()
        print "Actions available: ", state.getLegalPacmanActions()
        if Directions.WEST in state.getLegalPacmanActions():
            print "Going West."
            return Directions.WEST
        else:
            print "Going West."
            return Directions.STOP

class RandomAgent (Agent):
    "An agent that moves randomly."

    def getAction(self, state):
        "The agent recieves a GameState."
        print "Location: ", state.getPacmanPosition()
        
        actions_available = state.getLegalPacmanActions()
        print "Actions available: ", actions_available

        actions_available.remove('Stop')

        
        new_action = random.choice(actions_available)
        
        print "Going ", new_action
        return new_action



class ReflexAgent (Agent):

    def getAction(self, state):
        pacman_pos = state.getPacmanPosition()
        actions_available = state.getLegalPacmanActions()
        actions_available.remove('Stop')
        for action in actions_available:
            if action == 'West':
                has_food = state.hasFood(pacman_pos[0]-1, pacman_pos[1])        
            elif action == 'East':
                has_food = state.hasFood(pacman_pos[0]+1, pacman_pos[1])
            elif action == 'North':
                has_food = state.hasFood(pacman_pos[0], pacman_pos[1]+1)
            elif action =='South':
                has_food = state.hasFood(pacman_pos[0], pacman_pos[1]-1)
            if has_food:
                return action

        return random.choice(actions_available)
            
                    
            
