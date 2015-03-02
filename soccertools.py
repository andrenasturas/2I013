from soccersimulator import Vector2D, SoccerStrategy, SoccerState, SoccerBall, SoccerPlayer, SoccerAction, PLAYER_RADIUS, BALL_RADIUS, maxPlayerShoot, maxPlayerSpeed, maxBallAcceleration, ballBrakeSquare, ballBrakeConstant

class Tools(object):
    def __init__(self, player, state, teamid):
        self.player = player
        self.state = state
        self.teamid = teamid
        self.ball = state.ball

    def goTo(self, pos):
        return pos - self.player.position

    def distanceFromBall(self, player = None, ball = None):
        if not player:
            player = self.player
        if not ball:
            ball = self.ball
        return player.position.distance(ball.position)

    def isOnBall(self, player):
        if not player:
            player = self.player
        if self.distanceFromBall(player) < (PLAYER_RADIUS + BALL_RADIUS):
            return 1
        return 0

#    def closerFromBall(self):
#        n = 0
#        for p in players:
#            l[n] = distanceFromBall(p, ball)
#            n+= 1
#        return l.index(min(l))

    def positionBall(self, ball = None):       # Calcul de la position de la balle au prochain top de temps
        if not ball:
            ball = self.ball
        s = ball.speed.copy()
        p = ball.position.copy()
        ns = s.product(1 - ballBrakeSquare*(s.norm**2) - ballBrakeConstant)
        p+= ns
        return SoccerBall(p, ns)

    def interceptionBall(self, player = None): # Calcul de la trajectoire rectiligne optimale d'interception
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

    def firstOnBall(self):
        pass

    def isZoneClean():
        pass
