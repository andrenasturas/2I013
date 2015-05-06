from soccersimulator import SoccerBattle, SoccerPlayer, SoccerTeam
from soccersimulator import PygletObserver,ConsoleListener,LogListener
from soccersimulator import pyglet
from strategies import runner

team1 = SoccerTeam("Aventurier Errant")
team1.add_player(SoccerPlayer("t1j1", runner))

team2 = SoccerTeam("Aventuriers Errants")
team2.add_player(SoccerPlayer("t2j1", runner))
team2.add_player(SoccerPlayer("t2j2", runner))

team4 = SoccerTeam("Aventuriers Errants")
team4.add_player(SoccerPlayer("t4j1", runner))
team4.add_player(SoccerPlayer("t4j2", runner))
team4.add_player(SoccerPlayer("t4j3", runner))
team4.add_player(SoccerPlayer("t4j4", runner))

teamTMESolo = SoccrerTeam("Team TME Solo")
teamTMESolo.add_player(SoccerPlayer("Player", TMESoloStrategy(team2.players[0])))
teamTMESolo.add_player(SoccerAction("Player2", runner))

teams = [team2, teamTMESolo]
