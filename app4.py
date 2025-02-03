import streamlit as st
from PIL import Image

def main() :
    img = Image.open('./data/image_03.jpg')
    st.image(img)

if __name__ == '__main__' :
    main()
