import streamlit as st

#Titre
st.title("Application Web - Open IA")

#Champ de saisi
user_input = st.text_input("Veuillez entrer une description de l'image que vous souhaitez générer : ")
st.write(user_input)

#image
#st.image(" ")

#Sidebare
st.sidebar.text_input("Veuillez entrer la clé Open IA")
st.write(user_input)

