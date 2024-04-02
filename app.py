import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="Boston Housing Assistant",
    page_icon="🌆",
    layout="centered", # centered, wide 
    initial_sidebar_state="auto", 
    menu_items=None
)

st.title("🌆 Boston Housing Assistant")

df = pd.read_csv('https://github.com/KrantLeeee/TECHIN-510-Lab2/raw/main/Boston%20housing%20dataset.zip')

# Fill missing values in all columns with the mean
df_filled = df.fillna(df.mean())

# Use a slider to select the range of average number of rooms (RM)
min_rooms, max_rooms = st.slider(
    'Select the range of average number of rooms (RM)',
    float(df_filled['RM'].min()), float(df_filled['RM'].max()), (3.0, 8.0)
)

# Use a dropdown menu to select the maximum crime rate (CRIM)
max_crime_rate = st.selectbox(
    'Select the maximum crime rate (CRIM) %',
    options=[0.1, 1, 5, 10, 20, 50, 100],
    index=None
)

# Use a selector to choose the maximum pupil-teacher ratio (PTRATIO)
max_ptratio = st.selectbox(
    'Select the maximum pupil-teacher ratio (PTRATIO)',
    options=sorted(df_filled['PTRATIO'].unique()),
    index=None
)

# Filter the data
filtered_data = df_filled[
    (df_filled['RM'] >= min_rooms) & 
    (df_filled['RM'] <= max_rooms) & 
    (df_filled['CRIM'] <= max_crime_rate) &
    (df_filled['PTRATIO'] <= max_ptratio)
]

# Data visualization
st.write("Filtered Data", filtered_data)

# Plot a scatter plot
fig, ax = plt.subplots()
ax.scatter(filtered_data['RM'], filtered_data['MEDV'])
ax.set_xlabel('Average Number of Rooms')
ax.set_ylabel('Median Value of Homes')
st.pyplot(fig)
