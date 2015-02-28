from soccersimulator import Vector2D, SoccerStrategy, SoccerState, SoccerBall, SoccerPlayer, SoccerAction, PLAYER_RADIUS, BALL_RADIUS, maxPlayerShoot, maxBallAcceleration, ballBrakeSquare, ballBrakeConstant

class Tools(object):
    def __init__(self, player, players, state, teamid):
        self.player = player
        self.players = players
        self.state = state
        self.teamid = teamid
        self.ball = state.ball

    def goTo(self, pos):
        return Vector2D(pos-player.position)

    def distanceFromBall(player, ball):
        if not player:
            player = self.player
        if not ball:
            ball = this.ball
        return player.position.distance(ball.position)

    def isOnBall(self, player):
        if not player:
            player = self.player
        if distanceFromBall(player) < (PLAYER_RADIUS + BALL_RADIUS):
            return 1
        return 0

    def closerFromBall(self):
        n = 0
        for p in players:
            l[n] = distanceFromBall(p, ball)
            n+= 1
        return l.index(min(l))

    def positionBall(self, ball = 0):       # Calcul de la position de la balle au prochain top de temps
        if not ball:
            ball = self.ball
        s = ball.speed.copy()
        p = ball.position.copy()
        ns = s.product(1 - ballBrakeSquare*(s.norm**2) - ballBrakeConstant)
        p+= ns
        return SoccerBall(p, ns)

    def interceptionBall(self, player = 0): # Calcul de la trajectoire optimale d'interception
        if not player:
            player = self.player
        a = distanceBall(player)
        b =
        t = positionBall(ball)
        b = distanceBall(player, t)
        while b < a:
            t = positionBall(t)
            a = b
            b = distanceBall(player, t)
        return a

    def firstOnBall(self):
        pass

    def isZoneClean():
        pass
