from datetime import datetime

import networkx as nx

from database.DAO import DAO


class Model:

    def __init__(self):
        self._graph = nx.Graph()
        self._allCountries = []
        self._idMapCountries = {}


    def buildGraph(self, year):
        self._graph.clear()
        self.getAllCountries(year)
        if len(self._allCountries) == 0:
            print("No countries found")
            return
        self._graph.add_nodes_from(self._allCountries)
        allEdges = self.getEdgesByYear(year)
        for e in allEdges:
            self._graph.add_edge(e[0], e[1])


    def tempiCalcoloRaggiungibili(self, source):
        tic = datetime.now()
        raggiungibili = self.calcolaRaggiungibiliDFS(source)
        print(f"DFS: {datetime.now() - tic} - {len(raggiungibili)}")

        tic = datetime.now()
        raggiungibili = self.calcolaRaggiungibiliBFS(source)
        print(f"BFS: {datetime.now() - tic} - {len(raggiungibili)}")

        tic = datetime.now()
        raggiungibili = self.calcolaRaggiungibiliRicorsivo(source)
        print(f"Ricorsivo: {datetime.now() - tic} - {len(raggiungibili)}")


    def calcolaRaggiungibiliDFS(self, source):
        tree = nx.dfs_tree(self._graph, source)
        raggiungibili = list(tree.nodes)
        raggiungibili.remove(source)
        return raggiungibili


    def calcolaRaggiungibiliBFS(self, source):
        tree = nx.bfs_tree(self._graph, source)
        raggiungibili = list(tree.nodes)
        raggiungibili.remove(source)
        return raggiungibili


    def calcolaRaggiungibiliRicorsivo(self, source):
        visited = []
        self._ricorsione(source, visited)
        visited.remove(source)
        return visited


    def _ricorsione(self, n, visited):
        visited.append(n)
        for c in self._graph.neighbors(n):
            if c not in visited:
                self._ricorsione(c, visited)


    def getGraphDetails(self):
        return self._graph.number_of_nodes(), self._graph.number_of_edges()


    def getNumComponentiConnesse(self):
        return nx.number_connected_components(self._graph)


    def calcolaNumConfinanti(self, country):
        return self._graph.degree(country)


    def getEdgesByYear(self, year):
        return DAO.getEdgesByYear(year, self._idMapCountries)


    def getAllCountries(self, year):
        self._allCountries = DAO.getAllCountries(year)
        for c in self._allCountries:
            self._idMapCountries[c.CCode] = c
        return self._allCountries
