import streamlit as st
import pandas as pd
import seaborn as sns

st.set_page_config(
    page_title="Boston Housing Assistant",
    page_icon="🌆",
    layout="centered", # centered, wide 
    initial_sidebar_state="auto", 
    menu_items=None
)

st.title("🌆 Boston Housing Assistant")

st.write("## Raw Data")

df = pd.read_csv('/Users/krantlee/Documents/Study/University of Washington/TECHIN 510/Lab2/TECHIN-510-Lab2/Boston housing dataset.zip')

st.write(df)

# 对所有列使用均值填充缺失值
df_filled = df.fillna(df.mean())

# 验证缺失值处理后的结果
print(df_filled.isnull().sum())