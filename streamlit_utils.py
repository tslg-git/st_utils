import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
from graphviz import Digraph
import plotly.figure_factory as ff

st.set_page_config(layout="wide")

def blank_html(height = 45):
    html_code = '''<!DOCTYPE html>
        <html>
          <head>
            <meta charset="UTF-8">
            <title>Thin Gray Line</title>
            <style>
              hr {
                border: none;
                border-top: 0.px solid #F4F4F4;
                height: 0px;
                margin: 0px 0;
                margin-left: -10px;
              }
            </style>
          </head>
          <body>
            <hr>
          </body>
        </html>'''
    
    st.components.v1.html(html_code, height = height)

def separator():
    html_code = '''<!DOCTYPE html>
        <html>
          <head>
            <meta charset="UTF-8">
            <title>Thin Gray Line</title>
            <style>
              hr {
                border: none;
                border-top: 0.1px solid #CCCCCC;
                height: 0.1px;
                margin: 0.1px 0;
                margin-left: -10px;
              }
            </style>
          </head>
          <body>
            <hr>
          </body>
        </html>'''
    
    return html_code
    
def generate_text(font_type = 'regular', font_size = 36, font_weight = 100, bold_weight = 300, color = '#061844',\
                  font_ref = 'https://fonts.googleapis.com/css?family=Lato:100,300,700', \
                  string = 'nakiena'):
    

    html_code = '''<!DOCTYPE html>
    <html>
      <head>
        <meta charset="UTF-8">
        <title>String</title>
        <link href="''' + font_ref + '''" rel="stylesheet">
        <style>
          .str {
            font-family: 'Lato', sans-serif;
            font-size: ''' + str(font_size) + '''px;
            font-weight: '''+ str(font_weight) + ''';
            color: ''' + color + ''';
            letter-spacing: -0.02em;
            margin-left: -10px;
          }
          .bold {
            font-weight:''' + str(bold_weight) + ''';
          }
        </style>
      </head>
      <body>
        <div class="str"><strong class="bold">'''+string+'''</strong></div>
      </body>
    </html>'''
                  
    return html_code
    
def display_table(df):
    
    return 
    
col1, col2 = st.columns([3.5,1])
with col1:
    text = generate_text(string = 'Nakine', bold_weight = 400)

    st.components.v1.html(text, height = 52)
    
with col2:
    text = generate_text(string = 'comercial', font_weight = 10, color = '#333333')
    st.components.v1.html(text, height = 52)

sep = separator()
st.components.v1.html(sep, height = 22)

#col1, col2 = st.columns(2)

#with col1:
#    text = generate_text(font_size = 24, font_weight = 100, bold_weight = 100)
#    sep = separator()

#    st.components.v1.html(text, height = 45)
#    st.components.v1.html(sep, height = 22)    
    
#with col2:
#    text = generate_text(font_size = 24, font_weight = 100, bold_weight = 700)
#    sep = separator()

#    st.components.v1.html(text, height = 45)
#    st.components.v1.html(sep, height = 22)   
    
    
df = pd.DataFrame({'F_Cliente': np.random.choice(['F_' + str(x) for x in range(40)], 3000),
                             'F_Produto': np.random.choice(['F_' + str(x) for x in range(30,60)], 3000),
                             'Qt_Pos': 10000* np.random.normal(loc=10.0, scale=1.0, size=3000),
                             'P_Cliente': 1000000* np.random.normal(loc=10.0, scale=1.0, size=3000),
                             'PL_Produto': 1000000* np.random.normal(loc=10.0, scale=1.0, size=3000),
                             'Peer_Classe': np.random.choice(['A', 'B', 'C', 'D', 'E'], 3000),
                             'Peer_Dur':  np.random.choice(['L', 'C', 'M'],3000),
                             'Peer_Vol': np.random.choice(['A', 'B', 'M'],3000),
                             'Peer_Cli': np.random.choice(['F_' + str(x) for x in range(30,60)], 3000),
                             'Peer_Int': np.random.choice(['F_' + str(x) for x in range(60)], 3000),
                             'F_Cliente_Nak' : np.random.choice([1,0],3000, p = [0.08, 0.92]),
                             'F_Produto_Nak' : np.random.choice([1,0],3000, p = [0.08, 0.92])
                             })
        
text = generate_text(string = 'Categorização de Peers', font_size = 30)
sep = separator()
st.components.v1.html(text, height = 45)

col1, col2 = st.columns([1.8,3.6])
with col1:
    #default = st.radio('Utilizar categorização original de Peers', ['Não', 'Sim'])
    default = st.selectbox('Utilizar categorização original de Peers', ['Não', 'Sim'])
with col2:
    if default == 'Não':
        peer_dic = {'Classe': 'Peer_Classe', 'Duração': 'Peer_Dur', 'Volatilidade': 'Peer_Vol',
                   'Nicho Cliente': 'Peer_Cli'}
        selected_categories = st.multiselect('Categorias para construção de Peer', peer_dic.keys(), peer_dic.keys())
        categories = [peer_dic[x] for x in selected_categories]

streamlit_style = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Roboto:wght@100&display=swap');

html, body, [class*="css"]  {
font-family: 'Roboto', sans-serif;
}
</style>
"""
st.markdown(streamlit_style, unsafe_allow_html=True)

import plotly.graph_objs as go

import plotly.graph_objects as go

fig = go.Figure(data=[go.Sankey(
    node = dict(
      pad = 15,
      thickness = 14,
      line = dict(color = "black", width = 0),
      label = ["A1", "B1", "B2", "C1", "C2"],
      color = "#061844"
    ),
    link = dict(
      source = [0, 1, 0, 2, 3, 3], # indices correspond to labels, eg A1, A2, A1, B1, ...
      target = [2, 3, 3, 4, 4, 5],
      value = [8, 4, 2, 8, 4, 2],
        color = '#D9D9D9'
  ))])

fig.update_layout(title_text="Basic Sankey Diagram", font_size=10)

st.plotly_chart(fig)

def create_table(df):
    header_color = '#061844'
    even_row_color = '#F4F4F4'
    odd_row_color = '#E5E5E5'
    colorscale = [[0, '#061844'],[.5, '#f4f4f4'],[1, '#e5e5e5']]

    fig =  ff.create_table(df.iloc[:10,:4], colorscale=colorscale)
    st.plotly_chart(fig)
    
create_table(df)
