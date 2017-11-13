# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import networkx as nx
import pandas as pd

def buildGraph(edge_table_filename, node_table_filename):
    # import file
    edge_table = pd.read_csv(edge_table_filename)
    node_table = pd.read_csv(node_table_filename)
    
    G = nx.DiGraph()
    
    # insert node
    for index, row in node_table.iterrows():
        G.add_node((row['node']))
        
    # insert edge
    for index, row in edge_table.iterrows():
        G.add_edge(row['source'], row['target'], weight=row['weight'])

    return G

G = buildGraph("dummy_edge.csv", "dummy_node.csv")