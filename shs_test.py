import streamlit as st

import streamlit as st

with st.sidebar:
    with st.echo():
        st.write("This code will be printed to the sidebar.")

    with st.spinner("Loading..."):
        time.sleep(5)
    st.success("Done!")

# 타이틀 적용 : 파일을 업로드해주세요.
st.title(' 업로드해주세요.')

# Image 업로드
image_upload = st.file_uploader('이미지 첨부', type=['png', 'jpg', 'jpeg'])

