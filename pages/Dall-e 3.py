import streamlit as st
from openai import OpenAI

#Titre
st.title("Dall-e 3")

#Champ de saisi
user_input = st.text_input("Veuillez entrer une description de l'image que vous souhaitez générer : ")
st.write(user_input)

#Sidebare
open_ia_key = st.sidebar.text_input("Veuillez entrer la clé Open IA")
st.write(open_ia_key)

open_ia_key = OpenAI(api_key=OpenAIKEY)

st.image = open_ia_key.images.generate(
    model="dall-e-2",
    prompt=prompt,
    size="512x512",
    quality="standard",
    n=1,
) 
