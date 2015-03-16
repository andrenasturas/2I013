from soccersimulator import Vector2D, SoccerStrategy, SoccerState, SoccerBall, SoccerPlayer, SoccerAction, PLAYER_RADIUS, BALL_RADIUS, maxPlayerShoot
from soccertools import Tools

# Deplacements basiques
def staticMove(d):  # Debug
    return Vector2D(0, 0)
def randomMove(d):  # Debug
    return Vector2D.create_random()
def runnerMove(d):  # Course directe vers la balle
    a = d.goToBa()
    a = d.maximizeMove(a)
    return a
def defendMove(d):  # Placement defensif
    pass            # TODO Defense
def attackMove(d):
    a = d.goToGo()
    a = d.maximizeMove(a)
    return a
def intercMove(d):  # Trajectoire optimale d'interception
    a = d.goTo(d.interBall())
    a = d.maximizeMove(a)
    return a
def supplyMove(d):  # Placement demarque
    pass            # TODO Demarquer

# Actions basiques
def staticShot(d):  # Debug
    return Vector2D(0, 0)
def randomShot(d):  # Debug
    return Vector2D.create_random()
def directShot(d):  # Tir direct vers le but ennemi
    t = d.goToGo()
    d.maximizeShot(t)
    return t
def passerShot(d):  # Passe a un allie
    pass            # TODO Passe
def contreShot(d):  # Contre-tir
    pass            # TODO Contre

class GlobalStrategy(SoccerStrategy):
    moves = [attackMove]
    shots = [staticShot]
    def __init__(self, name = None, moves = None, shots = None):
        if not name:
            self.name = "GlobalStrategy"
        else:
            self.name = name
        self.moves+= moves
        self.shots+= shots
    def addMove(self, move):
        self.moves.append(move)
    def addShot(self, shot):
        self.shots.append(shot)
    def move(self, d):    # Choisir le deplacement optimal
        if d.isOnBall():
            return self.moves[0](d)
        else:
            return self.moves[1](d)
    def shot(self, d):    # Choisir l'action ideale
        if d.isOnBall():
            return self.shots[1](d)
        else:
            return self.shots[0](d)
    def begin_battles(self, state, count, max_step):
        pass
    def start_battle(self, state):
        pass
    def finish_battle(self, won):
        pass
    def compute_strategy(self, state, player, teamid):
        d = Tools(player, state, teamid)
        return SoccerAction(self.move(d), self.shot(d))

runner = GlobalStrategy("Runner", [runnerMove], [directShot])
interc = GlobalStrategy("Incerceptor", [intercMove], [directShot])
