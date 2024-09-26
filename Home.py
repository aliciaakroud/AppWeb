import streamlit as st

#Titre
st.title("Mon formulaire")

#Texte
st.write("Ceci est un formulaire de contact")

#Champ de saisi
user_input = st.text_input("Tapez votre texte : ")
st.write(user_input)

#image
st.video("https://youtu.be/kK3gGPkO9L8")

#Sidebare
st.sidebar.image("https://cdn.dribbble.com/users/2018170/screenshots/14771091/media/8244197cd8d6a675f0fca573bfb5498f.png?compress=1&resize=400x300")
st.sidebar.title("Alicia Akroud")

#Select bare
st.selectbox("Selectionnez votre niveau d'étude", ["Bac", "Bac +2", "Bac +5"])

#Select slider
age = st.select_slider("Quel est votre age ?", range(10,99))
if age < 18 : 
    st.write("Vous etes mineur")
else: 
    st.write("Vous etes majeur")
