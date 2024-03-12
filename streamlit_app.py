import streamlit as st


st.sidebar.title('Input')
url_input = st.sidebar.text_input('YOUR TEXT', '')

if url_input:
    st.subheader('Output')
    st.success(f'The wind of happy are gone : {url_input}')
else:
    st.subheader('Enter your URL please')
    st.error('Awaiting your INPUT...!')

st.title('🎈 ST-App')

st.header("This is a Custom-CSS")

col1, col2, col3 =st.columns(3)

col1.metric("Temperature", "70 °F", "1.2 °F")
col2.metric("Wind", "9 mph", "-8%")
col3.metric("Humidity", "86%", "1.2 °F")

col1.metric("Temperature", "78 °F", "1.4 °F")
col2.metric("Wind", "8.32 mph", "-7.9%")
col3.metric("Humidity", "83%", "1.2 °F")
