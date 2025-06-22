import streamlit as st
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import os
font_path = r"font/malgun-gothic.ttf"  
fm.fontManager.addfont(font_path)  

font_prop = fm.FontProperties(fname=font_path)
plt.rcParams['font.family'] = font_prop.get_name() 
plt.rcParams['axes.unicode_minus'] = False

train = pd.read_csv("train.csv")

st.title("데이터 개요")

st.markdown("""
**데이터 설명**

이 데이터는 1912년 4월 15일 대서양에서 침몰한 타이타닉호 승객 정보를 기반으로 합니다.  
목표는 승객들의 특징을 바탕으로 생존 여부를 분석하고 예측하는 것입니다.

**주요 변수 설명:**

- `PassengerId` : 승객 고유 ID
- `Survived` : 생존 여부 (0 = 사망, 1 = 생존)
- `Pclass` : 좌석 등급 (1 = 1등석, 2 = 2등석, 3 = 3등석)
- `Name` : 승객 이름
- `Sex` : 성별
- `Age` : 나이
- `SibSp` : 동반 형제/배우자 수
- `Parch` : 동반 부모/자녀 수
- `Ticket` : 티켓 번호
- `Fare` : 요금
- `Cabin` : 선실 번호
- `Embarked` : 탑승 항구 (C = Cherbourg, Q = Queenstown, S = Southampton)

**전체 데이터 특징:**

- 총 승객 수: 약 891명
- 약 38% 생존, 62% 사망
- 여러 변수들이 생존율에 영향을 미침:
    - 성별
    - 좌석 등급
    - 나이
    - 요금
    - 탑승 항구

이 데이터를 통해 생존율에 영향을 주는 다양한 요인을 분석할 수 있습니다.
""")

st.title("고객 검색")
search_term = st.text_input("검색 이름 입력하세요:")
if search_term:
    filtered_data = train[train['Name'].str.contains(search_term, case=False, na=False)]
    st.write(f"Số kết quả tìm thấy: {filtered_data.shape[0]}")
    st.dataframe(filtered_data)
else:
    st.write("검색 원하는 이름을 입력해주세요.")

st.title("1. TITANIC의 종합데이터")

train = pd.read_csv("train.csv")
sex_options = ['모두'] + train['Sex'].unique().tolist()
selected_sex = st.selectbox("성별을 선택 :", sex_options)
pclass_options = ['모두'] + train['Pclass'].unique().astype(str).tolist()
selected_pclass = st.selectbox("크래스 (Pclass):", pclass_options)
filtered_data = train.copy()
if selected_sex != '모두':
    filtered_data = filtered_data[filtered_data['Sex'] == selected_sex]

if selected_pclass != '모두':
    filtered_data = filtered_data[filtered_data['Pclass'] == int(selected_pclass)]


st.write(f"Số dòng dữ liệu sau khi lọc: {filtered_data.shape[0]}")
st.dataframe(filtered_data)
df = pd.read_csv("train.csv")
df['Sex'] = df['Sex'].map({'male': 'Nam', 'female': 'Nữ'})
train = pd.read_csv("train.csv")
if st.button("성별 및 생존율 분석 차트 표시"):
  
    sex_counts = train['Sex'].value_counts()
    st.subheader("남녀 비율")
    fig1, ax1 = plt.subplots()
    ax1.pie(sex_counts, labels=sex_counts.index.map({'male': '남성', 'female': '여성'}), autopct='%1.1f%%', startangle=90)
    ax1.axis('equal')
    st.pyplot(fig1)

    survival_by_sex = train.groupby('Sex')['Survived'].mean() * 100
    st.subheader("성별 생존율")
    fig2, ax2 = plt.subplots()
    bars = ax2.bar(survival_by_sex.index.map({'male': '남성', 'female': '여성'}), survival_by_sex.values, color=['skyblue', 'lightcoral'])
    ax2.set_ylabel('생존율 (%)')
    ax2.set_title('성별에 따른 생존율')

    for bar in bars:
        yval = bar.get_height()
        ax2.text(bar.get_x() + bar.get_width()/2, yval + 1, f"{yval:.1f}%", ha='center', va='bottom')

    st.pyplot(fig2)
    st.markdown(
        "<h1 style='font-family:Arial; color:white; font-size:30px;'> -> 남성 승객 비율이 더 높지만, 생존율은 여성 승객이 더 높습니다.</h1>",
        unsafe_allow_html=True
    )

if st.button("좌석 등급별 차트 표시"):

    pclass_counts = train['Pclass'].value_counts().sort_index()

    st.subheader("좌석 등급 분포 비율")
    fig2, ax2 = plt.subplots()
    ax2.bar(pclass_counts.index.astype(str), pclass_counts.values)
    ax2.set_xlabel("좌석 등급 (Pclass)")
    ax2.set_ylabel("승객 수")
    st.pyplot(fig2)

