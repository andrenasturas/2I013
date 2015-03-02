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
    def addMove(self, move):
        self.moves.append(move)
    def addShot(self, shot):
        self.shots.append(shot)
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
    a = d.goToGo()
    a = d.maximizeMove(a)
    return a
def defendMove(d):  # Placement défensif
    pass            # TODO Défense
def intercMove(d):  # Trajectoire optimale d'interception
    a = d.goTo(d.interceptionBall())
    a = d.maximizeMove(a)
    return a
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
    return t
def passerShot(d):  # Passe à un allié
    pass            # TODO Passe
def contreShot(d):  # Contre-tir
    pass            # TODO Contre
