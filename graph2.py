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


ide_streamlit_style2= '''
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}
.viewerBadge_container__1QSob{visibility:hidden;}
.viewerBadge_link__1S137{visibility:hidden;}
.css-1rs6os {visibility: hidden;}
.css-17ziqus {visibility: hidden;}
.css-1aumxhk {
background-color: #011839;
background-image: none;
color: #ffffff
}
</style>
'''
st.markdown(hide_streamlit_style2, unsafe_allow_html=True) 

page_bg_img = '''
<style>
.stApp {
background-image: url("https://static.vecteezy.com/system/resources/previews/007/492/570/non_2x/sport-background-illustration-suitable-for-banners-and-more-free-vector.jpg");
background-size: cover;
}
</style>
'''
st.markdown(page_bg_img, unsafe_allow_html=True)
title_html=f'<h1 style="font-family:Calibri; color:#DEF294; font-size: 30px;">Graph Network Analysis of WC 2022 finalists, all Goals and Chances created : Argentina vs France</h1>'
st.markdown(title_html, unsafe_allow_html=True)

df=pd.read_csv(r"https://raw.githubusercontent.com/ayanatherate/WC2022finals.github.io/main/Argentina_WC2022.csv")
dff=pd.read_csv(r"https://raw.githubusercontent.com/ayanatherate/WC2022finals.github.io/main/France_WC2022.csv")

G = nx.from_pandas_edgelist(df, 'Player', 'Assists', 'xG')
G1 = nx.from_pandas_edgelist(dff, 'Player', 'Player.1', 'xG')

got_net = Network(height="750px", width="100%", bgcolor="#222222", font_color="white")
got_net1 = Network(height="750px", width="100%", bgcolor="#222222", font_color="white")


# set the physics layout of the network
got_net.from_nx(G)
got_net1.from_nx(G1)

    # Generate network with specific layout settings
got_net.repulsion(node_distance=420,
                   central_gravity=0.33,
                   spring_length=110,
                   spring_strength=0.10,
                   damping=0.95)

got_net1.repulsion(node_distance=420,
                   central_gravity=0.33,
                   spring_length=110,
                   spring_strength=0.10,
                   damping=0.95)






try:
    path = '/tmp'
    got_net.save_graph(f'{path}/pyvis_graph.html')
    got_net1.save_graph(f'{path}/pyvis_graph1.html')
    
    HtmlFile = open(f'{path}/pyvis_graph.html', 'r', encoding='utf-8')
    HtmlFile1 = open(f'{path}/pyvis_graph1.html', 'r', encoding='utf-8')

    # Save and read graph as HTML file (locally)
except:
    path = '/html_files'
    got_net.save_graph(f'{path}/pyvis_graph.html')
    HtmlFile = open(f'{path}/pyvis_graph.html', 'r', encoding='utf-8')
components.html(HtmlFile.read(), height=735,width=735)
components.html(HtmlFile1.read(), height=735,width=735)


     
