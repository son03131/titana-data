import streamlit as st
import pandas as pd
import numpy as np 
from millify import prettify
st.title("이제는 TITANIC 데이터를 활용하여 분석 시작하겠다")

main_page = st.Page("page_1.py", title = "생촌 비율과 성별")
page_2 = st.Page("page_2.py", title = "이변량 분석")
page_3 = st.Page("page_3.py", title = "상관 분석")
pg = st.navigation([main_page, page_2,page_3])
pg.run()