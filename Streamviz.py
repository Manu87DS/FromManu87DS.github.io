# -*- coding: utf-8 -*-
"""
Created on Sun Aug 29 16:59:44 2021

@author: utilisateur
"""

import re
import string
import os
import time
import nltk
from nltk import word_tokenize
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from collections import Counter
from wordcloud import WordCloud
import streamlit as st
# import altair as alt

st.title('RAKUTEN DATAVIZ 2020')
st.markdown("""
* ** Application test for MASTER FINAL PRESENTATION
""")

df = pd.read_csv('X_train_update.csv',index_col=0)

designation = df['designation']
description = df['description']

#st.sidebar.header('User Data Selection')
st.sidebar.header('Variables Désignation & Description')

#### TESTS EN COURS !
# selector=st.sidebar.multiselect[description, designation]

#options = st.multiselect(
#    [description, designation]
#st.write('You selected:', options)




#sorted_text_data = st.sidebar.multiselect(designation, description)
# df_selected_sector = df[df.isin(sorted_text_data)]

st.write(description)

st.header('Longueur des mots des variables TEXTE RAKUTEN ')
st.write()



# ETUDE DE LA COLONNE DESIGNATION


df['designation'] = df['designation'].apply(lambda _: str(_))
words_per_review = df.designation.apply(lambda x: len(x.split(" ")))

if st.button('Show Plot Designation'):
    st.header('Longeur des mots de la variable description')    
    st.area_chart(df.designation.apply(lambda x: len(x.split(" "))))
    
# #figx= sns.histplot (words_per_review, kde=True) #(bins = 100, color='gray')    
#st.pyplot (figx)     
#if st.button('Show Plots'):
    #st.header('Longeur des mots de la variable description')
    #st.pyplot (figx)
    
df['description'] = df['description'].apply(lambda _: str(_))
words_per_review2 = df.description.apply(lambda x: len(x.split(" ")))

if st.button('Show Plot Description'):
    st.header('Longeur des mots de la variable description')    
    st.area_chart(df.description.apply(lambda x: len(x.split(" "))))
    
