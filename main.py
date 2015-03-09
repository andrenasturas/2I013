from soccersimulator import pyglet
from soccersimulator import SoccerBattle, SoccerPlayer, SoccerTeam
from soccersimulator import PygletObserver, ConsoleListener, LogListener
from strategies import *

team1=SoccerTeam("Aventurier Errant")
team1.add_player(SoccerPlayer("t1j1",GlobalStrategy()))

team2=SoccerTeam("Aventuriers Errants")
team2.add_player(SoccerPlayer("t2j1",GlobalStrategy()))
team2.add_player(SoccerPlayer("t2j2",GlobalStrategy()))

team4=SoccerTeam("Aventuriers Errants")
team4.add_player(SoccerPlayer("t4j1",GlobalStrategy()))
team4.add_player(SoccerPlayer("t4j2",GlobalStrategy()))

teams = [team1, team2, team4]

battle=SoccerBattle(teams[2],teams[1])
obs=PygletObserver()
obs.set_soccer_battle(battle)
pyglet.app.run()
