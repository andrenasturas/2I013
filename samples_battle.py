from soccersimulator import Vector2D, SoccerBattle, SoccerPlayer, SoccerTeam, SoccerAction, SoccerStrategy
from soccersimulator import PygletObserver,ConsoleListener,LogListener
from soccersimulator import PLAYER_RADIUS, BALL_RADIUS
from soccersimulator import pyglet
from strategies import StaticStrategy, RandomStrategy, RunnerStrategy, YoloStrategy
        

team1=SoccerTeam("team1")
team2=SoccerTeam("team2")
team1.add_player(SoccerPlayer("t1j1",RunnerStrategy()))
team2.add_player(SoccerPlayer("t2j1",RunnerStrategy()))
team1.add_player(SoccerPlayer("t1j2",RunnerStrategy()))
team2.add_player(SoccerPlayer("t2j2",RunnerStrategy()))
battle=SoccerBattle(team1,team2)
obs=PygletObserver()
obs.set_soccer_battle(battle)
pyglet.app.run()
