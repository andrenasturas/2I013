from soccersimulator import pyglet
from soccersimulator import SoccerBattle, SoccerPlayer, SoccerTeam
from soccersimulator import PygletObserver, ConsoleListener, LogListener
from strategies import *

team1 = SoccerTeam("team1")
team1.add_player(SoccerPlayer("t1j1",RunnerStrategy()))

team2 = SoccerTeam("team2")
team2.add_player(SoccerPlayer("t2j1",RunnerStrategy()))
team2.add_player(SoccerPlayer("t2j2",RunnerStrategy()))

team4 = SoccerTeam("team4")
team4.add_player(SoccerPlayer("t4j1",RunnerStrategy()))
team4.add_player(SoccerPlayer("t4j2",RunnerStrategy()))
team4.add_player(SoccerPlayer("t4j3",RunnerStrategy()))
team4.add_player(SoccerPlayer("t4j4",RunnerStrategy()))

team4 = SoccerTeam("team8")
team4.add_player(SoccerPlayer("t8j1",InterceptorStrategy()))
team4.add_player(SoccerPlayer("t8j2",InterceptorStrategy()))
team4.add_player(SoccerPlayer("t8j3",InterceptorStrategy()))
team4.add_player(SoccerPlayer("t8j4",InterceptorStrategy()))

teams = [team1, team2, team4, team8]

battle =SoccerBattle(teams[2],teams[3])
obs=PygletObserver()
obs.set_soccer_battle(battle)
pyglet.app.run()
