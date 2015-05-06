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
    if d.isReachable() and d.isReachable(d.goal[0]):
    	return d.goTo()
    return d.goToHo()
def attackMove(d):  # Offensive directe vers les cages ennemies
    a = d.goToGo()
    a = d.maximizeMove(a)
    return a
def intercMove(d):  # Trajectoire optimale d'interception
    a = d.goTo(d.interBall())
    a = d.maximizeMove(a)
    return a
def supplyMove(d):  # Placement demarque
    pass            # TODO Demarquer
def trackeMove(d, u):	# Suivre a la trace (TME Solo - Question 1)
	goTo(u.position)
def escapeMove(d, z):
	d.goTo(d.escapeZone(z))
def optimaMove(d):
	# Necessite un pathfinding complet avec
	# poids du chemin fonction du ralentissement de la boue
	# (la glace etant aleatoire, elle devrait etre consideree comme obstacle infranchissable
	# sauf si la balle s'y trouve)
	pass
	
	
	

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
        
# TME Solo - Question 2
class TMESoloStrategy(SoccerStrategy):
    moves = [runnerMove]
    shots = [staticShot]
    def __init__(self, name = None, moves = None, shots = None):
        if not name:
            self.name = "TMESoloStrategy"
        else:
            self.name = name
        self.moves+= moves
        self.shots+= shots
    def addMove(self, move):
        self.moves.append(move)
    def addShot(self, shot):
        self.shots.append(shot)
    def move(self, d):    # Choisir le deplacement optimal
        for z in d.zones:
	        if d.isInZone(z):			# Si le joueur est dans une zone et pas la balle
	        	if d.isInZone(z, d.state.ball.position):
	        		self.moves[0](d)
	        	else:
					self.moves[1](d, z)		# Sortir de la zone
	        else:						# Sinon
				self.moves[0](d)		# Defendre aux cages
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

#runner = GlobalStrategy("Runner", [runnerMove], [directShot])
runner = TMESoloStrategy("TMESolo", [escapeStrategy], [directShot])
interc = GlobalStrategy("Incerceptor", [intercMove], [directShot])
