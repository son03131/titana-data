import streamlit as st
import pandas as pd
import matplotlib as plt
import matplotlib.pyplot as plt
import numpy as np
st.header("2. 이변량 분석")
train = pd.read_csv("train.csv")

if st.button("좌석 등급별 생존율"):

    st.subheader("좌석 등급별 생존율 (좌석 등급은 생존율에 큰 영향)")

    pclass_survival = train.groupby('Pclass')['Survived'].mean() * 100

    fig2, ax2 = plt.subplots()
    bars2 = ax2.bar(pclass_survival.index.astype(str), pclass_survival.values, color='orange')
    ax2.set_xlabel("좌석 등급 (Pclass)")
    ax2.set_ylabel("생존율 (%)")
    ax2.set_title("좌석 등급에 따른 생존율")

    for bar in bars2:
        yval = bar.get_height()
        ax2.text(bar.get_x() + bar.get_width()/2, yval + 1, f"{yval:.1f}%", ha='center', va='bottom')

    st.pyplot(fig2)

    st.markdown("<h3 style='color:white;'>→ 1등석 승객의 생존율이 가장 높고, 등급이 낮을수록 생존율이 감소합니다.</h3>", unsafe_allow_html=True)


if st.button("연령대별 생존율"):
    st.subheader("연령대별 생존율 (어린 승객의 생존율이 높음)")

    bins = [0, 10, 20, 30, 40, 50, 60, 70, 80]
    train['AgeGroup'] = pd.cut(train['Age'], bins)

    age_survival = train.groupby('AgeGroup')['Survived'].mean() * 100

    fig3, ax3 = plt.subplots()
    bars3 = ax3.bar([str(i) for i in age_survival.index], age_survival.values, color='green')
    ax3.set_xlabel("연령대")
    ax3.set_ylabel("생존율 (%)")
    ax3.set_title("연령대별 생존율")
    plt.xticks(rotation=45)

    for bar in bars3:
        yval = bar.get_height()
        ax3.text(bar.get_x() + bar.get_width()/2, yval + 1, f"{yval:.1f}%", ha='center', va='bottom')

    st.pyplot(fig3)

    st.markdown("<h3 style='color:white;'>→ 어린 승객(특히 10세 이하)의 생존율이 가장 높습니다.</h3>", unsafe_allow_html=True)


if st.button("요금대별 생존율"):
    st.subheader("요금대별 생존율 (비싼 요금을 낸 승객의 생존율이 높음)")

    fare_bins = [0, 10, 30, 50, 100, 200, 600]
    train['FareGroup'] = pd.cut(train['Fare'], bins=fare_bins)

    fare_survival = train.groupby('FareGroup')['Survived'].mean() * 100

    fig4, ax4 = plt.subplots()
    bars4 = ax4.bar([str(i) for i in fare_survival.index], fare_survival.values, color='purple')
    ax4.set_xlabel("요금 구간")
    ax4.set_ylabel("생존율 (%)")
    ax4.set_title("요금대별 생존율")
    plt.xticks(rotation=45)

    for bar in bars4:
        yval = bar.get_height()
        ax4.text(bar.get_x() + bar.get_width()/2, yval + 1, f"{yval:.1f}%", ha='center', va='bottom')

    st.pyplot(fig4)

    st.markdown("<h3 style='color:white;'>→ 높은 요금을 지불한 승객일수록 생존율이 높습니다.</h3>", unsafe_allow_html=True)


if st.button("탑승 항구별 생존율"):
    st.subheader("탑승 항구별 생존율 (탑승 항구는 비교적 영향이 적음)")

    embarked_survival = train.groupby('Embarked')['Survived'].mean() * 100

    fig5, ax5 = plt.subplots()
    bars5 = ax5.bar(embarked_survival.index.astype(str), embarked_survival.values, color='brown')
    ax5.set_xlabel("탑승 항구 (Embarked)")
    ax5.set_ylabel("생존율 (%)")
    ax5.set_title("탑승 항구별 생존율")

    for bar in bars5:
        yval = bar.get_height()
        ax5.text(bar.get_x() + bar.get_width()/2, yval + 1, f"{yval:.1f}%", ha='center', va='bottom')

    st.pyplot(fig5)

    st.markdown("<h3 style='color:white;'>→ 탑승 항구에 따른 생존율 차이는 크지 않습니다.</h3>", unsafe_allow_html=True)
