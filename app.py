import streamlit as st
from src.inference import get_prediction

# Initialise session state variable
if 'input_features' not in st.session_state:
    st.session_state['input_features'] = {}

def app_sidebar():
    st.sidebar.header('Details')
# BMI,Pregnancies,Glucose,BloodPressure,Insulin,DiabetesPedigreeFunction
    Pregnancies = st.sidebar.slider('Pregnancies', 0, 20, 0, 1)
    Glucose = st.sidebar.text_input("Glucose")
    BMI = st.sidebar.text_input("BMI")
    BloodPressure = st.sidebar.text_input("Blood Pressure")
    Insulin = st.sidebar.text_input("Insulin")
    DiabetesPedigreeFunction = st.sidebar.text_input("Diabetes Pedigree Function")
    def get_input_features():
        input_features = {'Pregnancies': int(Pregnancies),
                          'Glucose': int(Glucose),
                          'BMI': int(BMI),
                          'BloodPressure': int(BloodPressure),
                          'Insulin': int(Insulin),
                          'DiabetesPedigreeFunction': float(DiabetesPedigreeFunction)
                         }
        return input_features
    sdb_col1, sdb_col2 = st.sidebar.columns(2)
    with sdb_col1:
        predict_button = st.sidebar.button("Assess", key="predict")
    with sdb_col2:
        reset_button = st.sidebar.button("Reset", key="clear")
    if predict_button:
        st.session_state['input_features'] = get_input_features()
    if reset_button:
        st.session_state['input_features'] = {}
    return None

def app_body():
    title = '<p style="font-family:arial, sans-serif; color:Black; font-size: 40px;"><b> Welcome to DSSI Diabetes Assessment</b></p>'
    st.markdown(title, unsafe_allow_html=True)
    default_msg = '**System assessment says:** {}'
    if st.session_state['input_features']:
        assessment = get_prediction(Pregnancies=st.session_state['input_features']['Pregnancies'],
                                    Glucose=st.session_state['input_features']['Glucose'],
                                    BMI=st.session_state['input_features']['BMI'],
                                    BloodPressure=st.session_state['input_features']['BloodPressure'],
                                    DiabetesPedigreeFunction=st.session_state['input_features']['DiabetesPedigreeFunction'],
                                    Insulin=st.session_state['input_features']['Insulin'])
        print("Assessment result:", assessment)  
        if assessment == 0:
            st.success(default_msg.format('Low risk of Diabetes'))
        else:
            st.warning(default_msg.format('High risk of Diabetes'))
    return None

def main():
    app_sidebar()
    app_body()
    return None

if __name__ == "__main__":
    main()