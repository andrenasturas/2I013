from soccersimulator import SoccerBattle, SoccerPlayer, SoccerTeam
from soccersimulator import PygletObserver,ConsoleListener,LogListener
from soccersimulator import pyglet
from strategies import RunnerStrategy, DefendStrategy
from apprentissage import *

team1 = SoccerTeam("Aventurier Errant")
team1.add_player(SoccerPlayer("t1j1", RunnerStrategy("Runner")))

team2 = SoccerTeam("Aventuriers Errants")
team2.add_player(SoccerPlayer("t2j1", RunnerStrategy("Runner")))
team2.add_player(SoccerPlayer("t2j2", DefendStrategy("Defend")))

team4 = SoccerTeam("Aventuriers Errants")
team4.add_player(SoccerPlayer("t4j1", RunnerStrategy("Runner")))
team4.add_player(SoccerPlayer("t4j2", RunnerStrategy("Runner")))
team4.add_player(SoccerPlayer("t4j3", DefendStrategy("Defend")))
team4.add_player(SoccerPlayer("t4j4", DefendStrategy("Defend")))

## Overpowered ##
oeam1 = SoccerTeam("Overpowered")
oeam1.add_player(OverpoweredPlayer("t1j1"))

oeam2 = SoccerTeam("Overpowered")
oeam2.add_player(OverpoweredPlayer("t2j1"))
oeam2.add_player(OverpoweredPlayer("t2j2"))

oeam4 = SoccerTeam("Overpowered")
oeam4.add_player(OverpoweredPlayer("t4j1"))
oeam4.add_player(OverpoweredPlayer("t4j2"))
oeam4.add_player(OverpoweredPlayer("t4j3"))
oeam4.add_player(OverpoweredPlayer("t4j4"))
#################

team_tree = SoccerTeam("Team Tree")
treeia=TreeIA(gen_feature_simple,dict({"Random":RandomStrategy(),"Fonceur":FonceurStrategy()}))

### Apprentissage
fn=os.path.join(os.path.dirname(os.path.realpath(__fil	e__)),"myfirsttree.pkl")
treeia.load(fn)
TreeST=TreeStrategy("tree1",treeia)

team_tree.add_player(SoccerPlayer("Tree 1",TreeST))
team_tree.add_player(SoccerPlayer("Tree 2",TreeST))

oeams = [oeam1, oeam2, oeam4]
teams = [team1, team2, team4]
