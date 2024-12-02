import streamlit as st
import requests


BASE_URL = 'https://mailliwj.pythonanywhere.com/'

# Endpoints
HOME_URL = f'{BASE_URL}'
PREDICT_URL = f'{BASE_URL}/predict'

def main():
    st.title('Rainfall Prediction Application')
    st.sidebar.title('')

    menu = st.sidebar.radio('Menu', ['Predict', 'Forecast', 'Update Data', 'Retrain'])
    if menu == "Predict":
        predict(PREDICT_URL)
    elif menu == "Forecast":
        st.write('Forecast feature coming soon')
    elif menu == 'Update Data':
        st.write('Update Data feature coming soon')
    elif menu == 'Retrain':
        st.write('Retrain feature coming soon')

def predict(PREDICT_URL):
    st.title('Make a rainfall predictions')
    st.markdown('Enter climatic paramters to predict rainfall in mm')

    pressure = st.number_input('Pressure (Pa)', min_value=0, max_value=200000)
    sunshine = st.number_input('Sunshine (hrs)', min_value=0, max_value=24)
    mean_temp = st.number_input('Mean Temperature (oC)', min_value=-50, max_value=50)

    if st.button('Predict Rainfall'):
        payload = {
            'pressure': pressure,
            'sunshine': sunshine,
            'mean_temp': mean_temp
        }

        try:
            response = requests.post(PREDICT_URL, json=payload)
            response.raise_for_status()
            result = response.json()
            prediction = result.get('Prediction', None)

            if prediction is not None:
                st.success(f' The predicted rainfall is {prediction:.1f}mm')
            else:
                st.error('Could not retrieve a valid prediction from the API')

        except requests.exceptions.RequestException as e:
            st.error(f'Error contacting the API: (e)')

if __name__ == '__main__':
    main()