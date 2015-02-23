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

teams = [team1, team2, team4]

battle =SoccerBattle(teams[2],teams[2])
obs=PygletObserver()
obs.set_soccer_battle(battle)
pyglet.app.run()
