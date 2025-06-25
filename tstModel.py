import networkx as nx

from model.country import Country
from model.model import Model

mymodel = Model()
mymodel.buildGraph(1980)
n, e = mymodel.getGraphDetails()
#print(f"N: {n}, E: {e}")
mymodel.tempiCalcoloRaggiungibili(Country("USA", 2, "United States of America"))
