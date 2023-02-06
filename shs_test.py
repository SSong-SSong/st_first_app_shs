import streamlit as st
import numpy as np
from PIL import Image

#이것은 타이틀
st.title("EAN_기술연구소_스마트도시연구본부")

# 탭 적용 : PJ1, PJ2, PJ3
tab1, tab2, tab3 = st.tabs(['PJ1', 'PJ2', 'PJ3'])

with tab1:
    st.header("Green Remodeling")
    st.image("그린리모델링.jpg", width=500)
    st.text("2016년 이후로 그린리모델링 업무를 수행해왔습니다.")

with tab2:
    st.header("Regression Metro")
    st.text("이것은 철도기술연구원3차원 공간정보 기반 철도역사 용역입니다.")

with tab3:
    st.header("GreenHouse Gas Emmision")
    st.text("이것은 건물부문 온실가스 계수 산정연구 용역입니다.")

# 타이틀 적용 : 파일을 업로드해주세요.
st.title(' 업로드해주세요.')

# Image 업로드
image_upload = st.file_uploader('이미지 첨부', type=['png', 'jpg', 'jpeg'])
if image_upload is not None:
  st.image(image_upload)

