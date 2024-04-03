import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="Boston Housing Assistant",
    page_icon="🌆",
    layout="centered",
    initial_sidebar_state="auto",
    menu_items=None
)

st.title("🌆 Boston Housing Assistant")

df = pd.read_csv('https://github.com/KrantLeeee/TECHIN-510-Lab2/raw/main/Boston%20housing%20dataset.zip')

# Fill missing values in all columns with the mean
df = df.fillna(df.mean())

# Sidebar filters
with st.sidebar:
    st.write("### Filters")
    room_number_slider = st.slider(
        'Select the range of average number of rooms (RM)',
        float(df["RM"].min()),
        float(df["RM"].max()),
    )

    max_ptratio_slider = st.slider(
        'Select the maximum pupil-teacher ratio (PTRATIO)',
        float(df["PTRATIO"].min()),
        float(df["PTRATIO"].max()),
    )

    min_age, max_age = st.slider(
        'Select the range of the age of house (AGE) (0-100 years)',
        int(df['AGE'].min()), int(df['AGE'].max()), (0, 100)
    )

    max_crime_rate = st.selectbox(
        'Select the maximum crime rate (CRIM) (0-100%)',
        options=[0.1, 1, 5, 10, 20, 50, 100],
        index=None
    )

# Filter the data
if max_crime_rate:
    df = df[df["CRIM"] <= max_crime_rate]
df = df[df["RM"] <= room_number_slider]
df = df[df["PTRATIO"] <= max_ptratio_slider]
df = df[(df["AGE"] >= min_age) & (df["AGE"] <= max_age)]

st.write("## Results", df)

# Plotting in a 2x2 grid
fig, axs = plt.subplots(2, 2, figsize=(15, 10))

# Adjust subplots to provide space for titles
plt.subplots_adjust(hspace=0.3)

sns.regplot(x="CRIM", y="MEDV", data=df, scatter_kws={'alpha':0.5}, line_kws={'color': 'red'}, ax=axs[0, 0])
axs[0, 0].set_title("Trend of Median Value as CRIM varies", pad=20)
axs[0, 0].set_xlabel('Crime Rate per Capita')
axs[0, 0].set_ylabel('Median Value of Homes ($1000s)')

sns.regplot(x="AGE", y="MEDV", data=df, scatter_kws={'alpha':0.5}, line_kws={'color': 'green'}, ax=axs[0, 1])
axs[0, 1].set_title("Trend of Median Value as AGE varies", pad=20)
axs[0, 1].set_xlabel('Proportion of Owner-Occupied Units Built Prior to 1940')
axs[0, 1].set_ylabel('Median Value of Homes ($1000s)')

sns.regplot(x="DIS", y="MEDV", data=df, scatter_kws={'alpha':0.5}, line_kws={'color': 'blue'}, ax=axs[1, 0])
axs[1, 0].set_title("Trend of Median Value as DIS varies", pad=20)
axs[1, 0].set_xlabel('Weighted Distances to Five Boston Employment Centres')
axs[1, 0].set_ylabel('Median Value of Homes ($1000s)')

sns.regplot(x="RM", y="MEDV", data=df, scatter_kws={'alpha':0.5}, line_kws={'color': 'purple'}, ax=axs[1, 1])
axs[1, 1].set_title("Trend of Median Value as RM varies", pad=20)
axs[1, 1].set_xlabel('Average Number of Rooms')
axs[1, 1].set_ylabel('Median Value of Homes ($1000s)')

st.pyplot(fig)
