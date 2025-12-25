import streamlit as st
import plotly.express as px

st.set_page_config(page_title="Auto Visualizations", layout="wide")

st.title("📈 Auto-Visualization Engine")

if 'df' in st.session_state:
    df = st.session_state['df']
    
    st.sidebar.header("Chart Controls")
    
    # User selects axes [cite: 78]
    all_columns = df.columns.tolist()
    numeric_columns = df.select_dtypes(include=['number']).columns.tolist()
    
    x_axis = st.sidebar.selectbox("Select X-Axis", all_columns)
    y_axis = st.sidebar.selectbox("Select Y-Axis", numeric_columns)
    
    # Selection logic based on column types [cite: 60]
    chart_choice = st.sidebar.selectbox("Select Chart Type", 
        ["Bar Chart", "Line Chart", "Scatter Plot", "Histogram", "Boxplot"])

    st.subheader(f"{chart_choice}: {x_axis} vs {y_axis}")

    # Render engine [cite: 59, 79]
    try:
        if chart_choice == "Bar Chart":
            fig = px.bar(df, x=x_axis, y=y_axis, template="plotly_white", color=x_axis)
        elif chart_choice == "Line Chart":
            fig = px.line(df, x=x_axis, y=y_axis, markers=True)
        elif chart_choice == "Scatter Plot":
            fig = px.scatter(df, x=x_axis, y=y_axis, trendline="ols")
        elif chart_choice == "Histogram":
            fig = px.histogram(df, x=x_axis, marginal="rug")
        elif chart_choice == "Boxplot":
            fig = px.box(df, x=x_axis, y=y_axis)
        
        # Output downloadable and interactive chart [cite: 113]
        st.plotly_chart(fig, use_container_width=True)
        
    except Exception as e:
        st.error(f"Could not render chart: {e}")
else:
    st.warning("No data found. Please upload a dataset in the 'Upload' section first.")
    
    