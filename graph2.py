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

df=pd.read_csv(r"https://raw.githubusercontent.com/ayanatherate/WC2022finals.github.io/main/Argentina_WC2022.csv")

G = nx.from_pandas_edgelist(df, 'Player', 'Assists', 'xG')
got_net = Network(height="750px", width="100%", bgcolor="#222222", font_color="white")


# set the physics layout of the network
got_net.from_nx(G)

    # Generate network with specific layout settings
got_net.repulsion(node_distance=420,
                   central_gravity=0.33,
                   spring_length=110,
                   spring_strength=0.10,
                   damping=0.95)






try:
    path = '/tmp'
    got_net.save_graph(f'{path}/pyvis_graph.html')
    HtmlFile = open(f'{path}/pyvis_graph.html', 'r', encoding='utf-8')

    # Save and read graph as HTML file (locally)
except:
    path = '/html_files'
    got_net.save_graph(f'{path}/pyvis_graph.html')
    HtmlFile = open(f'{path}/pyvis_graph.html', 'r', encoding='utf-8')
components.html(HtmlFile.read(), height=635,width=435)


     
