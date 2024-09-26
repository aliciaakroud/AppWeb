import streamlit as st

#Titre
st.title("Dall-e 3")

#Champ de saisi
user_input = st.text_input("Veuillez entrer une description de l'image que vous souhaitez générer : ")
st.write(user_input)

#image
#st.image(" ")

#Sidebare
open_ia_key = st.sidebar.text_input("Veuillez entrer la clé Open IA")
st.write(open_ia_key)


