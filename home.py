import io
import streamlit as st
#import snowflake_dcr as dcr
import os
from zipfile import ZipFile

# Page settings
st.set_page_config(
    page_title="DCR Setup Assistant",
    page_icon="❄️️",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'About': "This app generates scripts for data clean rooms!"
    }
)

# Set up main page
col1, col2 = st.columns((6, 1))
col1.title("TATD : To ALL the Dreamers_//")
st.image("images/back_bar.jpeg")
#col2.image("imagess/snowflake_dcr_multi.png", width=120)
#st.sidebar.title(" TATD ")
#st.sidebar.image("images/toallthedreamers.jpeg")
#action = st.sidebar.radio("category",("whisky","cocktail","wine","food"))

st.markdown("모든 위스키 1,000 원 추가시 하이볼로 변경 가능합니다.")
st.markdown("토닉워터 / 클럽소다 / 진저에일 선택( 기본 : 클럽소다 )")
st.markdown("바틀 주문시 토닉 * 4 제공됩니다.")
st.markdown("잔 파손시 금액 발생됩니다. (1만원)")
st.markdown("결정되시면 직원을 불러주세요!")

# Create dcr object




