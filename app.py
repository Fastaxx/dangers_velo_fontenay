import streamlit as st
import pandas as pd
import numpy as np

st.sidebar.title("Navigation")
choix = st.sidebar.selectbox("Elements",["Informations","Carte", "Statistiques"])

if choix == "Informations":
	st.title("Informations")

if choix == "Carte":
	#file_upload = st.sidebar.file_uploader("Données")
	st.title("Carte")
	path ="/Users/Louis/GitHub/dangers_velo_fontenay/accidents-corporels-de-la-circulation-millesime.csv"
	path2 = "/Users/Louis/GitHub/dangers_velo_fontenay/baro.csv"
	file_csv = pd.read_csv(path,sep=";")
	file2_csv = pd.read_csv(path2,sep=";")
	file_coordinates_probleme = pd.DataFrame(file2_csv)
	# Traitement Problèmes 
	file_coordinates_probleme["latitude"] = pd.to_numeric(file_coordinates_probleme["latitude"])
	file_coordinates_probleme["longitude"] = pd.to_numeric(file_coordinates_probleme["longitude"])
	st.write(file2_csv)

	st.map(file_coordinates_probleme)

	# Traitement Accident
	file_coordinates_accident = pd.DataFrame(file_csv["Coordonnées"])
	lat,lon = [], []
	for row in file_coordinates_accident["Coordonnées"]:
		try:
			lat.append(row.split(',')[0])
			lon.append(row.split(',')[1])
		except:
			lat.append(np.NaN)
			lon.append(np.NaN)
	file_coordinates_accident['latitude'],file_coordinates_accident['longitude'] = lat,lon
	del file_coordinates_accident["Coordonnées"]
	file_coordinates_accident = file_coordinates_accident.astype(float)
	
	st.map(file_coordinates_accident)
if choix=="Statistiques":
	st.title("Statistiques")