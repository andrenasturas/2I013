import numpy as np
import pickle
from soccersimulator import TreeIA, TreeStrategy
from strats import *
import os

def gen_feature_simple(state, teamid, playerid):
    d = Tools(state.get_player(teamid, playerid), state, teamid)
    return np.array([d.goToBa(), d.goToGo(), d.goToHo()])

if __name__=="__main__":
    treeia=TreeIA(gen_feature_simple)
    treeia.learn(fn="test_interact.pkl")
    treeia.save("myfirsttree.pkl")
