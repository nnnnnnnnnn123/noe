import streamlit as st
import pandas as pd
import plotly.express as px

# Load the healthcare data
df_healthcare = pd.read_csv("healthcare-dataset-stroke-data 2.csv")

# Plot Contour Plot
st.header("Contour Plot of Age vs. Average Glucose Level")
fig_contour = px.density_contour(df_healthcare, x='age', y='avg_glucose_level', color='stroke',
                                 title='Contour Plot of Age vs. Average Glucose Level',
                                 color_discrete_map={0: 'blue', 1: 'red'})
fig_contour.update_layout(xaxis_title='Age', yaxis_title='Average Glucose Level')
st.plotly_chart(fig_contour)

# Plot Scatterplot Matrix
st.header("Scatterplot Matrix for Hypertension")
numerical_columns = ['age', 'avg_glucose_level', 'bmi']
fig_scatter_matrix = px.scatter_matrix(df_healthcare, dimensions=numerical_columns, color='hypertension',
                                       title='Scatterplot Matrix Hypertension for Hypertension',
                                       labels={col: col for col in numerical_columns})
st.plotly_chart(fig_scatter_matrix)

# Plot Sunburst Chart
st.header("Sunburst Chart: Relationship between Smoking Status, Gender, and Stroke")
data_smoking_gender = {
    'smoking_status': ['formerly smoked', 'never smoked', 'never smoked', 'smokes', 'never smoked', 'formerly smoked', 'never smoked', 'Unknown', 'Unknown', 'formerly smoked'],
    'gender': ['Male', 'Female', 'Male', 'Female', 'Female', 'Male', 'Male', 'Female', 'Female', 'Female'],
    'stroke': [1, 1, 0, 1, 0, 1, 0, 1, 0, 1]
}
df_smoking_gender = pd.DataFrame(data_smoking_gender)
fig_sunburst = px.sunburst(df_smoking_gender, path=['smoking_status', 'gender'], values='stroke',
                           title='Sunburst Chart: Relationship between Smoking Status, Gender, and Stroke',
                           color_continuous_scale='Viridis')
st.plotly_chart(fig_sunburst)

# Plot Animated Bar Chart
st.header("Animated Bar Chart: Strokes Over Age")
data_age_stroke = {
    'age': [30, 35, 40, 45, 50, 55, 60, 65, 70, 75],
    'stroke': [0, 0, 1, 0, 1, 0, 1, 0, 1, 0]
}
df_age_stroke = pd.DataFrame(data_age_stroke)
fig_bar = px.bar(df_age_stroke, x='age', y='stroke', title='Animated Bar Chart: Strokes Over Age',
                 labels={'age': 'Age', 'stroke': 'Stroke'},
                 animation_frame='age',
                 range_x=[30, 75],
                 range_y=[0, 1],
                 color='stroke',
                 color_discrete_map={0: 'blue', 1: 'red'},
                 text='stroke')
fig_bar.update_layout(yaxis_title='Stroke Occurrence (0 or 1)')
st.plotly_chart(fig_bar)
