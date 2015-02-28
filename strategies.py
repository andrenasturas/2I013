from soccersimulator import Vector2D, SoccerStrategy, SoccerState, SoccerBall, SoccerPlayer, SoccerAction, PLAYER_RADIUS, BALL_RADIUS, maxPlayerShoot
from soccertools import Tools

class GlobalStrategy(SoccerStrategy):
    def __init__(self, name, strategies):
        self.name = name
        if not strategies:
            self.strategies = []
        else:
            self.strategies = strategies
    def select(d):
        if(len(strategies) == 1):
            return 0
        else:
            if(d.isOnBall()):
                 pass

    def addStrategy(self,strat):
        self.strategies.append(strat)
    def start_battle(self,state):   # Selection strategie selon composition
        for s in self.strategies:
            s.start_battle(state)
    def finish_battle(self,won):
        for s in self.strategies:
            s.finish_battle(won)
    def compute_strategy(self,state,player,teamid):
        d = Tools(player, players, state, teamid)
        return strategies[select(d)](d)

def staticStrategy(d):  # Debug
    return SoccerAction(Vector2D(0,0), Vector2D(0,0))

def randomStrategy(d):  # Debug
    return SoccerAction(Vector2D.create_random(), Vector2D.create_random())

def yoloStrategy(d):    # Debug
    if d.isOnBall():
        t = Vector2D.create_random()
        a = t
    else:
        t = Vector2D(0,0)
        a = state.ball.position - player.position
    return SoccerAction(a, t)

def runnerStrategy(d):
    t = state.get_goal_center((not(teamid-1))+1) - player.position
    t.product(100)
    a = state.ball.position - player.position
    a.product(100)
    return SoccerAction(a, t)

def keeperStrategy(d):
    pass

def interceptorStrategy(d):
    pass

def distantStrategy(d):
    pass

# TODO : remove legacy classes

class StaticStrategy(SoccerStrategy):
    # Immobile et inactif
    def __init__(self):
        self.name="Static"
    def start_battle(self,state):
        pass
    def finish_battle(self,won):
        pass
    def compute_strategy(self,state,player,teamid):
        return SoccerAction(Vector2D(0,0), Vector2D(0,0))
    def copy(self):
        return StaticStrategy()
    def create_strategy(self):
        return StaticStrategy()

class RandomStrategy(SoccerStrategy):
    # Aleatoire
    def __init__(self):
        self.name="Random"
    def start_battle(self,state):
        pass
    def finish_battle(self,won):
        pass
    def compute_strategy(self,state,player,teamid):
        return SoccerAction(Vector2D.create_random(), Vector2D.create_random())
    def copy(self):
        return RandomStrategy()
    def create_strategy(self):
        return RandomStrategy()

class RunnerStrategy(SoccerStrategy):
    # 
    def __init__(self):
        self.name="Runner"
    def start_battle(self,state):
        pass
    def finish_battle(self,won):
        pass
    def reverse(n):
        if n == 1:
            return 2
        else:
            return 1
    def compute_strategy(self,state,player,teamid):
#       Inutile car le tir innefficace n'est pas decompte
#        if player.position.distance(state.ball.position)<(PLAYER_RADIUS+BALL_RADIUS):
#            if teamid == 2:
#                t = state.get_goal_center(1) - player.position
#            else:
#                t = state.get_goal_center(2) - player.position
#            a = t
#        else:
#            t = Vector2D(0,0)
#            a = state.ball.position - player.position

        t = state.get_goal_center((not(teamid-1))+1) - player.position
#       t.product(maxPlayerShoot)
        a = state.ball.position - player.position
        return SoccerAction(a, t)
    def copy(self):
        return RunnerStrategy()
    def create_strategy(self):
        return RunnerStrategy()
        
class YoloStrategy(SoccerStrategy):
    def __init__(self):
        self.name="Runner"
    def start_battle(self,state):
        pass
    def finish_battle(self,won):
        pass
    def compute_strategy(self,state,player,teamid):
        if player.position.distance(state.ball.position)<(PLAYER_RADIUS+BALL_RADIUS):
            t = Vector2D.create_random()
#            t.product(maxPlayerShoot)
            a = t
        else:
            t = Vector2D(0,0)
            a = state.ball.position - player.position
        return SoccerAction(a, t)
    def copy(self):
        return YoloStrategy()
    def create_strategy(self):
        return YoloStrategy()

class InterceptorStrategy(SoccerStrategy):
    def __init__(self):
        self.name="Interceptor"
    def start_battle(self,state):
        pass
    def finish_battle(self,won):
        pass
    def compute_strategy(self,state,player,teamid):
        d = Tools(player, state, teamid)
        t = state.get_goal_center((not(teamid-1))+1) - player.position
        t.product(100)
        a = d.goTo(d.interceptionBall(player, ball))
        a.product(100)
        return SoccerAction(a, t)
    def copy(self):
        return InterceptorStrategy()
    def create_strategy(self):
        return InterceptorStrategy()
