# -*- coding: utf8 -*-

from soccersimulator import pyglet
from soccersimulator import PygletObserver, LogObserver, PygletReplay
from soccersimulator import SoccerBattle, SoccerPlayer, SoccerTeam
from soccersimulator import InteractStrategy
from strategies import *

import glob
import pickle

CFG_1=dict({"ballBrakeConstant":0.08, "ballBrakeSquare":0.01})
CFG_2=dict({"ballBrakeConstant":0.05, "ballBrakeSquare":0.0025})
CFG_3=dict({"ballBrakeConstant":0.04, "ballBrakeSquare":0.004})

team2=SoccerTeam("Coureur")
team2.add_player(SoccerPlayer("t2j1", RunnerStrategy("Runner")))
team2.add_player(SoccerPlayer("t2j2", RunnerStrategy("Runner")))
team2.add_player(SoccerPlayer("t2j3", DefendStrategy("Runner")))
team2.add_player(SoccerPlayer("t2j4", DefendStrategy("Runner")))

team4=SoccerTeam("Interceptuer")
team4.add_player(SoccerPlayer("t4j1", RunnerStrategy("Defend")))
team4.add_player(SoccerPlayer("t4j2", RunnerStrategy("Defend")))
team4.add_player(SoccerPlayer("t4j3", DefendStrategy("Defend")))
team4.add_player(SoccerPlayer("t4j4", DefendStrategy("Defend")))

#battle = SoccerBattle(teams[2], teams[1])
#obs = PygletObserver()
#obs.set_soccer_battle(battle)
#pyglet.app.run()

#list_key_player1=['a','z']
#list_key_player2=['q','s','d']
#list_strat_player1=[defend, runner]
#list_strat_player2=[runner, interc, defend]

# arguemnts :  liste des touches, liste des strategies, nom du fichier, tout sauvegarder ou non, concatener dans un meme fichier a la suite ou non
#inter_strat_player1=InteractStrategy(list_key_player1,list_strat_player1,"test_interact.pkl")
#inter_strat_player2=InteractStrategy(list_key_player2,list_strat_player2,"test_interact.pkl",True)
#team3 = SoccerTeam("Interactive")
#team3.add_player(SoccerPlayer("t3j1",inter_strat_player1))
#team3.add_player(SoccerPlayer("t3j2",inter_strat_player2))
#team3.add_player(SoccerPlayer("t3j3",inter_strat_player2))
#team3.add_player(SoccerPlayer("t3j4",inter_strat_player2))

battle = SoccerBattle(team2, team4)
obs = PygletObserver()
obs.set_soccer_battle(battle)
pyglet.app.run()
