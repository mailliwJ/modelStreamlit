import streamlit as st
import requests

st.title('Rainfall Prediction App')
st.markdown('Enter climatic paramters to predict rainfall in mm')

pressure = st.number_input('Pressure', min_value=0, max_value=150000)
sunshine = st.number_input('Sunshine', min_value=0, max_value=20)
mean_temp = st.number_input('Mean Temperature', min_value=-50, max_value=50)

if st.button('Predict Rainfall'):
    api_url = 'https://mailliwj.pythonanywhere.com/predict'
    payload = {
        'pressure': pressure,
        'sunshine': sunshine,
        'mean_temp': mean_temp
    }

    try:
        response = requests.post(api_url, json=payload)
        response.raise_for_status()
        result = response.json()
        prediction = result.get('prediction', None)

        if prediction is not None:
            st.success(f' The predicted rainfall is {prediction:.1f}mm')
        else:
            st.error('Could not retrieve a valid prediction from the API')

    except requests.exceptions.RequestException as e:
        st.error(f'Error contacting the API: (e)')
