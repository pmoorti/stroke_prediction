import streamlit as st
import seaborn as sns
import plotly.express as px
import pandas as pd
import matplotlib.pyplot as plt
import plotly.figure_factory as ff
def create_dashboard(data):
    st.title("Stroke Prediction Analysis Dashboard")
    
    # Box Plot
    st.header("Distribution of Numerical Features by Stroke Status")
    numeric_var = st.selectbox("Select Variable", ["age", "bmi", "avg_glucose_level"])
    fig_box = px.box(data, x="stroke", y=numeric_var)
    st.plotly_chart(fig_box)
    
    # Scatter Plot
    st.header("Age vs BMI Relationship Scatter Plot")
    fig_scatter = px.scatter(data, x="age", y="bmi", color="stroke")
    st.plotly_chart(fig_scatter)
    
    # Correlation Heatmap
    st.header("Feature Correlation Heatmap")
    # Define numeric columns
    numeric_cols = ['age', 'bmi', 'avg_glucose_level','hypertension','heart_disease', 'stroke']
    # Calculate correlation
    correlation_matrix = data[numeric_cols].corr()
    
    # Create heatmap
    fig_heat = ff.create_annotated_heatmap(
        z=correlation_matrix.values,
        x=correlation_matrix.columns.tolist(),
        y=correlation_matrix.columns.tolist(),
        annotation_text=correlation_matrix.round(2).values,
        showscale=True
    )
    st.plotly_chart(fig_heat)
    

data = pd.read_csv('downsampled_stroke_final.csv') 
create_dashboard(data)

