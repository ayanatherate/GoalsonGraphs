import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import networkx as nx
from pyvis.network import Network

HtmlFile = open(f'index.html','r')

components.html(HtmlFile.read(),width=600,height=1000)
