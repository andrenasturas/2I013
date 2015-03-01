from soccersimulator import SoccerBattle, SoccerPlayer, SoccerTeam
from soccersimulator import PygletObserver,ConsoleListener,LogListener
from soccersimulator import pyglet
from strategies import RunnerStrategy, InterceptorStrategy

team1 = SoccerTeam("team1")
team1.add_player(SoccerPlayer("t1j1", InterceptorStrategy()))

team2 = SoccerTeam("team2")
team2.add_player(SoccerPlayer("t2j1", InterceptorStrategy()))
team2.add_player(SoccerPlayer("t2j2", InterceptorStrategy()))

team4 = SoccerTeam("team4")
team4.add_player(SoccerPlayer("t4j1", InterceptorStrategy()))
team4.add_player(SoccerPlayer("t4j2", InterceptorStrategy()))
team4.add_player(SoccerPlayer("t4j3", InterceptorStrategy()))
team4.add_player(SoccerPlayer("t4j4", InterceptorStrategy()))

teams = [team1, team2, team4]
