import streamlit as st

#Titre
st.title("Mon formulaire")

#Texte
st.write("Ceci est un formulaire de contact")

#Champ de saisi
user_input = st.text_input("Tapez votre texte : ")
st.write(user_input)

#image
st.image(" https://www.phosphore.com/wp-content/uploads/2023/01/LOGO-EEMI-770x374px_Plan-de-travail-1.png")
