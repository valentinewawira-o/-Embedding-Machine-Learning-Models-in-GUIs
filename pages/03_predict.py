import streamlit as st
import joblib
import pickle
import pandas as pd

st.set_page_config(
    page_title="PREDICT",
    page_icon="",
    layout="wide"
)

# Load models
@st.cache(allow_output_mutation=True)
def load_dt_model():
    pipeline = pickle.load(open('models/dt_model(1).pkl', 'rb'))
    return pipeline

@st.cache(allow_output_mutation=True)
def load_pipeline_preprocessor():
    pipeline = pickle.load(open('models/pipeline_preprocessor.pkl', 'rb'))
    return pipeline

def predict_batch():
    uploaded_file = st.file_uploader("Upload Dataset (CSV)", type=["csv"])

def select_model():
    selected_model = st.selectbox('Select a model', options=['pipeline_preprocessor', 'dt'])
    return selected_model

st.title('Prediction')

def predict_page():
    with st.form('my_form'):
        pipeline = None
        selected_model = select_model()
        if selected_model == "pipeline_preprocessor":
            pipeline = load_pipeline_preprocessor()
        elif selected_model == "dt":
            pipeline = load_dt_model()

        col1, col2, col3 = st.columns(3)

        with col1:
            st.write("### Personal Information")
            st.number_input("Enter Age", min_value=18, max_value=60, step=5, key='age')
            Customer_ID = st.text_input('Customer ID')
            gender = st.selectbox('Gender', options=['Male', 'Female'])
            senior_citizen = st.selectbox("SeniorCitizen", options=['True', 'False'])
            Dependents = st.selectbox("Dependents", options=['True', 'False'])
            partner = st.selectbox("Partner", options=['True', 'False'], key='marital_status')
            tenure = st.number_input('Tenure', step=1, key='years_worked_in_the_company')

        with col2:
            st.write("### Device Information")
            phone_service = st.selectbox("PhoneService", options=['True', 'False'])
            multiple_lines = st.selectbox("MultipleLines", options=['True', 'False'])
            internet_service = st.selectbox("InternetService", options=["DSL", "Fiber optic", "No"])
            online_security = st.selectbox("OnlineSecurity", options=['True', 'False'])
            online_backup = st.selectbox("OnlineBackup", options=['True', 'False'])
            device_protection = st.selectbox("DeviceProtection", options=['True', 'False'])
            tech_support = st.selectbox("TechSupport", options=['True', 'False'])
            streaming_tv = st.selectbox("StreamingTV", options=['True', 'False'])
            streaming_movies = st.selectbox("StreamingMovies", options=['True', 'False'])

        with col3:
            st.write("### Payment Information")
            contract = st.selectbox("Contract", options=['Month-to-month', 'One year', 'Two years'])
            payment_method = st.selectbox("Payment", options=['Bank transfer (automatic)', 'Credit card (automatic)', 'Electronic check', 'Mailed check'])
            paperless_billing = st.selectbox("PaperlessBilling", options=['True', 'False'])
            monthly_charges = st.number_input("MonthlyCharges")
            total_charges = st.number_input("TotalCharges")
            churn = st.selectbox("Churn", options=['True', 'False'])

        if st.form_submit_button('Submit'):
            pass  # Placeholder for further processing

if __name__ == '__main__':
    predict_page()
    st.write(st.session_state)
