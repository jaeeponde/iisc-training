import pandas as pd
import glob
import seaborn as sns 
import networkx as nx
import matplotlib.pyplot as plt
import os


#initialising an undirected graph 
G_ud=nx.Graph()

G_ud.add_nodes_from(["A","B","C","D","E"])
G_ud.add_edges_from([("A","B"), ("A", "E"), ("A", "E"), ("E", "C"),("C", "B")])

#print(G_ud.adj)
#print(G_ud.nodes)
#print(G_ud.edges)

#initialising a directed graph with node attributes

G_ud.graph["Name"]="Undirected"
G_ud.nodes["A"]["E_M"]="Epi_Marker"

print(G_ud.nodes(data=True))

df=nx.to_pandas_adjacency(G_ud)

print(df)