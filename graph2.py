# -*- coding: utf-8 -*-
"""
Created on Fri Dec 16 18:40:46 2022

@author: User
"""


import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import networkx as nx
from pyvis.network import Network

df=pd.read_csv(r"https://github.com/ayanatherate/WC2022finals.github.io/blob/main/Argentina_WC2022.csv",on_bad_lines='skip')

got_net = Network(height="750px", width="100%", bgcolor="#222222", font_color="white")


# set the physics layout of the network
got_net.barnes_hut()

got_data = df

sources = got_data['Player']
targets = got_data['Assists']
weights = got_data['xG']
edge_data = zip(sources, targets, weights)

for e in edge_data:
    src = e[0]
    dst = e[1]
    w = e[2]
    
    
    got_net.add_node(src, src, title=src)
    got_net.add_node(dst, dst, title=dst)
    got_net.add_edge(src, dst, value=w)
    

neighbor_map = got_net.get_adj_list()
for node in got_net.nodes:
                node["title"] += " Neighbors:<br>" + "<br>".join(neighbor_map[node["id"]])
                node["value"] = len(neighbor_map[node["id"]])



path = '/tmp'
got_net.save_graph(f'{path}/pyvis_graph.html')
HtmlFile = open(f'{path}/pyvis_graph.html', 'r', encoding='utf-8')
components.html(HtmlFile.read(), height=435)

     
