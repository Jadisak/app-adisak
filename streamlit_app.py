import streamlit as st

st.title('🎈 ST-App')

st.title("This is a Custom-CSS")

col1, col2, col3 =st.columns(3)
col1.metric("Temperature", "70 °F", "1.2 °F")
col1.metric("Temperature", "78 °F", "1.4 °F")
col2.metric("Wind", "9 mph", "-8%")
col2.metric("Wind", "8.32 mph", "-79%")
col3.metric("Humidity", "86%", "1.2 °F")
col3.metric("Humidity", "83%", "1.2 °F")
