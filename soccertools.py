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

    def firstOnBall(self):
        pass

    def positionBall(ball):
        if not ball:
            ball = self.ball
        s = ball.speed.copy()
        p = ball.position.copy()

        frotte_ball_square = s.copy()
        coeff_frottement_square = ballBrakeSquare*(s.norm**2)
        frotte_ball_square.product(-coeff_frottement_square)
        frotte_ball_constant = s.copy()
        coeff_frottement_constant = ballBrakeConstant
        frotte_ball_constant.product(-coeff_frottement_constant)

        new_ball_speed = s
        new_ball_speed+= frotte_ball_square
        new_ball_speed+= frotte_ball_constant

        s = new_ball_speed
        p+= s

        return SoccerBall(p, s)

    def interceptionBall(self, player):
        a = distanceBall(player)
        t = positionBall(ball)
        b = distanceBall(player, t)
        while b < a:
            t = positionBall(t)
            a = b
            b = distanceBall(player, t)
        return a

    def isZoneClean():
        pass
