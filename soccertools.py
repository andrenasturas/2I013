from soccersimulator import Vector2D, SoccerStrategy, SoccerState, SoccerBall, SoccerPlayer, SoccerAction, PLAYER_RADIUS, BALL_RADIUS, maxPlayerShoot, maxBallAcceleration, ballBrakeSquare, ballBrakeConstant

class Tools(object):
    def __init__(self, player, players, state, teamid):
        self.player = player
        self.players = players
        self.state = state
        self.teamid = teamid
        self.ball = state.ball
        if(teamid == 1):    # FIXME À normaliser (terrain miroir)
            targetGoal = state.get_goal_center(2)
            defendGoal = state.get_goal_center(1)
        else:
            targetGoal = state.get_goal_center(1)
            defendGoal = state.get_goal_center(2)

    def maximize(vector, norm = 0):     # Maximiser la norme d'un vecteur
        while(v.norm() < norm):
            v.product(10)
        return v

    def maximizeShot(vector):           # Maximiser le tir
        return maximize(vector, maxPlayerShoot)

    def maximizeMove(vector):           # Maximiser le mouvement
        return maximize(vector, maxBallAcceleration)

    def goTo(self, pos):                # Aller à une position
        return Vector2D(pos-player.position)

    def goToGo(self):                   # Aller vers le but ennemi
        return goTo(targetGoal)

    def distanceFromBall(player, ball): # Distance du joueur à la balle
        if not player:
            player = self.player
        if not ball:
            ball = this.ball
        return player.position.distance(ball.position)

    def isOnBall(self, player):         # Balle à portée de tir
        if not player:
            player = self.player
        if distanceFromBall(player) < (PLAYER_RADIUS + BALL_RADIUS):
            return 1
        return 0

    def closerFromBall(self):           # Classement des joueurs selon ordre croissant de leur distance à la balle
        n = 0
        for p in players:
            l[n] = distanceFromBall(p, ball)
            n+= 1
        return l.index(min(l))

    def firstOnBall(self):              # Premier joueur à intercepter la balle
        pass

    def positionBall(ball = 0):         # Position de la balle au prochain top de temps
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

    def interceptionBall(self):         # Calcul de la trajectoire optimale d'optimisation
        a = distanceBall(player)        # FIXME Corriger et vérifier le calcul
        t = positionBall(ball)
        b = distanceBall(player, t)
        while b < a:
            t = positionBall(t)
            a = b
            b = distanceBall(player, t)
        return a

    def isZoneClean():
        pass
