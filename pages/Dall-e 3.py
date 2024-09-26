import streamlit as st
from openai import OpenAI
#Titre
st.title("Dall-e 3")

#Champ de saisi
user_input = st.text_input("Veuillez entrer une description de l'image que vous souhaitez générer : ")


#Sidebare
open_ia_key = st.sidebar.text_input("Veuillez entrer la clé Open IA")

client = OpenAI(api_key=open_ia_key)

image = client.images.generate(
    model="dall-e-2",
    prompt=user_input,
    size="512x512",
    quality="standard",
    n=1,
)
image_url = image.data[0].url
st.image(image_url)
