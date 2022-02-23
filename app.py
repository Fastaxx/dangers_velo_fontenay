import streamlit as st
import pandas as pd
import numpy as np

st.sidebar.title("Navigation")
file_upload = st.sidebar.file_uploader("Données")
choix = st.sidebar.selectbox("Elements",["Informations","Carte", "Statistiques"])

if choix == "Informations":
	st.title("Informations")

if choix == "Carte":
	st.title("Carte")
	path ="/Users/Louis/GitHub/dangers_velo_fontenay/accidents-corporels-de-la-circulation-millesime.csv"
	file_csv = pd.read_csv(path,sep=";")
	file_coordinates = pd.DataFrame(file_csv["Coordonnées"])
	lat,lon = [], []
	for row in file_coordinates["Coordonnées"]:
		try:
			lat.append(row.split(',')[0])
			lon.append(row.split(',')[1])
		except:
			lat.append(np.NaN)
			lon.append(np.NaN)
	file_coordinates['latitude'],file_coordinates['longitude'] = lat,lon
	del file_coordinates["Coordonnées"]
	st.write(file_coordinates)
	st.map(file_coordinates)
if choix=="Statistiques":
	st.title("Statistiques")