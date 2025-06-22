import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib import font_manager as fm

font_path = r"font/malgun-gothic.ttf"  
fm.fontManager.addfont(font_path)  

font_prop = fm.FontProperties(fname=font_path)
plt.rcParams['font.family'] = font_prop.get_name() 
plt.rcParams['axes.unicode_minus'] = False

train = pd.read_csv("train.csv")
st.title("상관관계 분석 (Correlation Analysis)")
numeric_cols = ['Survived', 'Pclass', 'Age', 'SibSp', 'Parch', 'Fare']
train_corr = train[numeric_cols].copy()
train_corr['Age'] = train_corr['Age'].fillna(train_corr['Age'].median())
corr_matrix = train_corr.corr()
st.subheader("상관계수 테이블:")
st.dataframe(corr_matrix.style.format("{:.2f}"))
st.subheader("상관계수 히트맵:")
fig, ax = plt.subplots(figsize=(8, 6))
sns.heatmap(corr_matrix, annot=True, fmt=".2f", cmap='coolwarm', ax=ax)
st.pyplot(fig)
st.markdown(
    "<h3 style='color:white;'>→ Pclass와 Fare는 생존율(Survived)과 꽤 강한 상관관계를 보입니다. Age, SibSp, Parch는 상대적으로 낮은 상관관계를 가집니다.</h3>",
    unsafe_allow_html=True
)


