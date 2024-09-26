import streamlit as st

#Titre
st.title("Mon formulaire")

#Texte
st.write("Ceci est un formulaire de contact")

#Champ de saisi
user_input = st.text_input("Tapez votre texte : ")
st.write(user_input)

#image
st.image("https://www.bing.com/images/search?view=detailV2&ccid=uxOFRUZ4&id=70F67E73DE7EF7DB3619AE7E9472EA3A28974F74&thid=OIP.uxOFRUZ4IpMGhzms24iROgAAAA&mediaurl=https%3a%2f%2fcdn.dribbble.com%2fusers%2f2018170%2fscreenshots%2f14766274%2fmedia%2f3a7fd9dd9f5463b1be7d1a7a29cdb674.png%3fcompress%3d1%26resize%3d400x300%26vertical%3dtop&cdnurl=https%3a%2f%2fth.bing.com%2fth%2fid%2fR.bb13854546782293068739acdb88913a%3frik%3ddE%252bXKDrqcpR%252brg%26pid%3dImgRaw%26r%3d0&exph=300&expw=400&q=eemi&simid=608038413573454833&FORM=IRPRST&ck=77FBCA5BB1DDD54DDB9E93A6EBBB63C1&selectedIndex=5&itb=0&ajaxhist=0&ajaxserp=0 ")
