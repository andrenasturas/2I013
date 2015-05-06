from soccersimulator import pyglet
from soccersimulator import SoccerBattle, SoccerPlayer, SoccerTeam
from soccersimulator import PygletObserver, ConsoleListener, LogListener
from strategies import *

team1=SoccerTeam("Aventurier Errant")
team1.add_player(SoccerPlayer("t1j1", runner))

team2=SoccerTeam("Aventuriers Errants Coureurs")
team2.add_player(SoccerPlayer("t2j1", runner))
team2.add_player(SoccerPlayer("t2j2", runner))

team4=SoccerTeam("Aventuriers Errants Intercepteurs")
team4.add_player(SoccerPlayer("t4j1", interc))
team4.add_player(SoccerPlayer("t4j2", TMESoloStrategy()))

teams = [team1, team2, team4]

battle = SoccerBattle(teams[2], teams[1])
obs = PygletObserver()
obs.set_soccer_battle(battle)
pyglet.app.run()
