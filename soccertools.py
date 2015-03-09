from soccersimulator import Vector2D, SoccerStrategy, SoccerState, SoccerBall, SoccerPlayer, SoccerAction, PLAYER_RADIUS, BALL_RADIUS, maxPlayerShoot, maxBallAcceleration, ballBrakeSquare, ballBrakeConstant, nbWithoutShoot

class Tools(object):
    def __init__(self, player, state, teamid):
        self.player = player
        self.state = state
        self.ball = state.ball
        if(teamid == 1):
            self.goal[1] = state.get_goal_center(2)
            self.goal[0] = state.get_goal_center(1)
            self.team[0] = team1
            self.team[1] = team2
            self.side = 0
        else:
            self.goal[1] = state.get_goal_center(1)
            self.goal[0] = state.get_goal_center(2)
            self.team[1] = team1
            self.team[0] = team2
            self.side = 1

    def maximize(vector, norm = 0):     # Maximiser la norme d'un vecteur
        while(v.norm() < norm):
            v.product(10)
        return v

    def maximizeShot(vector):           # Maximiser le tir
        return maximize(vector, maxPlayerShoot)

    def maximizeMove(vector):           # Maximiser le mouvement
        return maximize(vector, maxBallAcceleration)

    def goTo(self, pos):                # Aller a une position
        return Vector2D(pos-player.position)

    def goToGo(self):                   # Aller vers le but ennemi
        return goTo(goal[1])

    def distanceFromBall(player, ball): # Distance du joueur a la balle
        if not player:
            player = self.player
        if not ball:
            ball = this.ball
        return player.position.distance(ball.position)

    def isOnBall(self, player = None):  # Balle a portee de tir
        if not player:
            player = self.player
        if distanceFromBall(player) < (PLAYER_RADIUS + BALL_RADIUS):
            return 1
        return 0

    def closerFromBall(self):           # Classement des joueurs selon ordre croissant de leur distance a la balle
        n = 0
        for p in players:
            l[n] = (self.distanceFromBall(p, ball), p)
            n+= 1
        return l.sort()

    def positionBall(self, ball = None):# Calcul de la position de la balle au prochain top de temps
        if not ball:
            ball = self.ball
        s = ball.speed.copy()
        p = ball.position.copy()
        ns = s.product(1 - ballBrakeSquare*(s.norm**2) - ballBrakeConstant)
        p+= ns
        return SoccerBall(p, ns)

    def interBall(self, player = None): # Calcul de la trajectoire rectiligne optimale d'interception
        if not player:
            player = self.player
        n = 0
        x = 0
        b = self.ball
        y = self.distanceFromBall(b)
        while x < y:
            n+= 1
            b = self.positionBall(b)
            x = maxPlayerSpeed * n
            y = self.distanceFromBall(b)
        r = b.position
        return r

    def hasShot(player = None):
        if not player:
            player = self.player
        if player._num_before_shoot > (2 * nbWithoutShoot / 3):
            return true
        return false
