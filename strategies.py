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
    a = d.goToMi()
    a = d.maximizeMove(a)
    return a
def keeperMove(d):  # Rester dans les cages
    a = d.goToHo()
    a = d.maximizeMove(a)
    return a
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

# Actions basiques
def staticShot(d):  # Debug
    return Vector2D(0, 0)
def randomShot(d):  # Debug
    return Vector2D.create_random()
def directShot(d):  # Tir direct vers le but ennemi
    t = d.goToGo()
    d.maximizeShot(t)
    return t

class GlobalStrategy(SoccerStrategy):
    def __init__(self, name = None, moves = None, shots = None):
        if not name:
            self.name = "GlobalStrategy"
        else:
            self.name = name
        self.moves = moves
        self.shots = shots
    def move(self, d):    # Choisir le deplacement optimal
        return self.moves[0](d)
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

################# Joueur Special #################
## Implementation d'un pouvoir de teleportation ##

class OverpoweredStrategy(GlobalStrategy):  # Strategie speciale
    @property
    def pos(self):
    	return self._pos
    def __init__(self, name = None, moves = None, shots = None):
        if not name:
            self.name = "OverpoweredStrategy"
        else:
            self.name = name
        self.moves+= moves
        self.shots+= shots
        self._pos = Vector2D()
    def compute_strategy(self, state, player, teamid):
    	self._pos = state.ball.position+state.ball.speed
        d = Tools(player, state, teamid)
        return SoccerAction(self.move(d), self.shot(d))

class OverpoweredPlayer(SoccerPlayer):
	def __init__(self,name="Overpowered"):
		self._name=name
		self.position=Vector2D(75, 45)
		if 1 == 1:
			self._angle=0.
		self._speed=4.5
		self._num_before_shoot=0
		self.id =-1
		self._speed_v=Vector2D()
		self._strategy=OverpoweredStrategy("Overpowered", [runnerMove, runnerMove], [directShot])
		self.state=None

	@property
	def angle(self):
		self._num_before_shoot=0          # Override de la limite de tir (inactif ?)
		self.position=self._strategy.pos  # Teleportation
		return self._angle
	@angle.setter
	def angle(self,a):
		pass                              # Override du setter (angle fixe)

	@property
	def speed(self):
		return self._speed
	@speed.setter
	def speed(self,s):
		pass                              # Override du setter (vitesse fixe)

	@property
	def speed_v(self):
		self._speed_v=Vector2D()
		return self._speed_v.copy()
	@speed_v.setter
	def speed_v(self,v):
		pass                              # Override du setter (vitesse fixe)

	def copy(self,safe=False):            # Redefintion de la copie
		player=OverpoweredPlayer(self._name,self._strategy)
		player.position=self.position
		player.angle=self.angle
		player.speed=self.speed
		player._num_before_shoot=0
		player.id=self.id
		if safe:
			player._strategy=strategies.SoccerStrategy(self.strategy.name)
		return player

	def dec_num_before_shoot(self):
		self._num_before_shoot=0

	def set_position(self,x,y,angle):
		self.angle=float(angle)

	def init_num_before_shoot(self, v):
		self._num_before_shoot=0          # Override de la limite de tir (inactif ?)

	def get_num_before_shoot(self):
		self._num_before_shoot=0          # Override de la limite de tir (inactif ?)
		return 0

##################################################


class DefendStrategy(GlobalStrategy):
    def __init__(self, name = None):
        super(DefendStrategy, self).__init__("DefendStrategy", [defendMove, defendMove], [staticShot, directShot])

class RunnerStrategy(GlobalStrategy):
    def __init__(self, name = None):
        super(RunnerStrategy, self).__init__("RunnerStrategy", [runnerMove, runnerMove], [staticShot, directShot])
