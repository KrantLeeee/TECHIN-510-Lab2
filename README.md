# TECHIN-510-Lab2

## Overview

This is a Boston Housing Assistant App by Krant Lee

## How to run

Open the terminal and run the following commands:
```
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```
```
steamlit run ap.py
```

## What's Included

- `app.py`: The main application

## Lessons learned
- Better collect the latitude and longitude data, so that map can be applied.
- Markdown language and its application in document writing.
- The relationship between Python and Markdown, and how Python handles Markdown documents.
- How to read and handle missing values, including methods for filling them with the mean.

- How to use controls (such as sliders, drop-down menus, and selectors) to filter data in Streamlit applications.
- Move filter controls to the sidebar to optimize app layout.

- Use the Matplotlib and Seaborn libraries for data visualization, including creating scatter plots and regression lines to analyze data trends.
- Beautify and customize scatter plots, such as setting transparency, line color, and chart title.

## Questions
- The current visualization is static. How should I add interactive functionality like showing more information when the user hovers over a certain point on the scatter plot?