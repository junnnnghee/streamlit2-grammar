# 이미지, 동영상, 음악파일을 화면에 보여주는 방법

import streamlit as st
# 이미지 처리를 위한 라이브러리
# PIL(파이썬이미지라이브러리)
from PIL import Image

def main() :
    # 1. 저장되어있는 이미지파일을 화면에 보여주기
    img = Image.open('./data/image_03.jpg')
    st.image(img)

if __name__ == '__main__' :
    main()
