from soccersimulator import SoccerBattle, SoccerPlayer, SoccerTeam
from soccersimulator import PygletObserver,ConsoleListener,LogListener
from soccersimulator import pyglet
from strategies import runner
from apprentissage import *

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

team_tree = SoccerTeam("Team Tree")
treeia=TreeIA(gen_feature_simple,dict({"Random":RandomStrategy(),"Fonceur":FonceurStrategy()}))

### Apprentissage
fn=os.path.join(os.path.dirname(os.path.realpath(__fil	e__)),"myfirsttree.pkl")
treeia.load(fn)
TreeST=TreeStrategy("tree1",treeia)

team_tree.add_player(SoccerPlayer("Tree 1",TreeST))
team_tree.add_player(SoccerPlayer("Tree 2",TreeST))

teams = [team1, team2, team4]
