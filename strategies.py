from soccersimulator import Vector2D, SoccerStrategy, SoccerState, SoccerBall, SoccerPlayer, SoccerAction, PLAYER_RADIUS, BALL_RADIUS, maxPlayerShoot
from soccertools import Tools

class GlobalStrategy(SoccerStrategy):
    def __init__(self, name, moves, shots):
        self.name = name
        if not moves:
            self.moves = []
        else:
            self.moves = moves
        if not shots:
            self.shots = []
        else:
            self.shots = shots
    def addStrategy(self,strat):
        self.strategies.append(strat)
    def start_battle(self,state):   # Selection strategie selon composition
        pass
    def finish_battle(self,won):
        pass
    def move(d):    # Choisir le déplacement optimal
        pass
    def shot(d):    # Choisir l'action idéale
        pass
    def compute_strategy(self,state,player,teamid):
        d = Tools(player, players, state, teamid)
        return SoccerAction(move(d), shot(d))

# Déplacements basiques
def staticMove(d):  # Debug
    return Vector2D(0, 0)
def randomMove(d):  # Debug
    return Vector2D.create_random()
def runnerMove(d):  # Course directe vers la balle
    a = state.ball.position - player.position
    a = d.maximizeMove(a)
    return a
def defendMove(d):  # Placement défensif
    pass            # TODO Défense
def intercMove(d):  # Trajectoire optimale d'interception
    a = d.interceptionBall()
    a = d.maximizeMove(a)
def supplyMove(d):  # Placement démarqué
    pass            # TODO Démarquer

# Actions basiques
def staticShot(d):  # Debug
    return Vector2D(0, 0)
def randomShot(d):  # Debug
    return Vector2D.create_random()
def directShot(d):  # Tir direct vers le but ennemi
    t = d.goToGo()
    d.maximizeShot(t)
    return
def passerShot(d):  # Passe à un allié
    pass            # TODO Passe
