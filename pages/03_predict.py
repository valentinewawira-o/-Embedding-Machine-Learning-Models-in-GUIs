import streamlit as st
import joblib
import pickle
import pandas as pd


st.set_page_config(
    page_title="PREDICT",
    page_icon="",
    layout="wide"
)


st.cache_resource(show_spinner='Model Loading')
def load_dt_model():
  pipeline=pickle.load('models/dt_model(1).pkl')
  return pipeline


st.cache_resource(show_spinner='Model Loading')
def load_pipeline_preprocessor():
  pipeline=pickle.load('models/pipeline_preprocessor.pkl')

  return pipeline

def predict_batch():
    uploaded_file = st.file_uploader("vodafone_customer_churn.csv", type=["csv"])

    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)

def make_prediction(pipeline):
  Patner=st.session_state['mariatal_status']


          
def select_model():
  col1, col2 =st.columns(2)
  with col1:
    selected_model= st.selectbox('select a model', options=['pipeline_preprocessor','dt'])
  with col2:
    pass
if 'selected_model' not in st.session_state:
  st.session_state['selected_model'] = select_model
else:
  selected_model = st.session_state['selected_model']

  if st.session_state['selected_model']=="pipeline_preprocessor":
    load_pipeline_preprocessor()
  elif selected_model=="dt":
    load_dt_model()

st.title('prediction')

def predict_batch():
    uploaded_file = st.file_uploader("Upload Dataset (CSV)", type=["csv"])

  
def predict_page():

 with st.form('my_form'):
    
    pipeline=select_model()
    col1,col2,col3=st.columns(3)

    with col1:
       st.write("### personal information")
       st.number_input("enter age", min_value=18, max_value=60, step=5,key='age')
       Customer_ID=st.text_input('Customer ID')
       gender=st.selectbox('gender',options=['Male','Female'])
       senior_citizen= st.selectbox("SeniorCitizen", options=['True','False'])
       Dependents=st.selectbox("Dependents", options=['True','False'])
       partner= st.selectbox("Partner", options=['True','False'], key='mariatal status')
       tenure=st.number_input('tenure',step=1, key='years worked in the company')
         
       

    with col2:
      st.write("### Device information")
      phone_service=st.selectbox("PhoneService", options=['True','False'])
      multiple_lines=st.selectbox("MultipleLines", options=['True','False'])
      internet_service=st.selectbox("internetService",options=["DSL","Fiber optic", "no"])
      online_security=st.selectbox("OnlineSecurity", options=['True','False'])
      online_backup=st.selectbox("OnlineBackup", options=['True','False'])
      device_protection= st.selectbox("DeviceProtection", options=['True','False'])
      tech_support=st.selectbox("TechSupport", options=['True','False'])
      streaming_tv=st.selectbox("StreamingTV", options=['True','False'])
      streaming_movies=st.selectbox("StreamingMovies", options=['True','False'])
      

      
    with col3:
      st.write("### Payment  Information")
      contract=st.selectbox("Contract",options=['month-to-month','one year','two years'])
      payment_method=st.selectbox("Payment",options=['Bank transfer(automatic)','credit card(automatic)','electronic check','mailed check'])
      paperless_billing=st.selectbox("PaperlessBilling", options=['True','False'])
      monthly_charges=st.number_input(" MonthlyCharges")
      total_charges=st.number_input("TotalCharges")
      churn=st.selectbox("Churn", options=['True','False'])


data={[gender, senior_citizen,partner,dependents,tenure,phone_service,multiple_lines,internet_service,online_security,online_backup,device_protection,tech_support,streaming_tv,streaming_movies, contract, paperless_billing, payment_method,monthly_charges,
total_charges]}
columns=['gender','SeniorCitizen','Partner','Dependents','tenure','PhoneService','MultipleLines','InternetService','OnlineSecurity','OnlineBackup',
      'DeviceProtection','TechSupport','StreamingTV','StreamingMovies','Contract','PaperlessBilling','PaymentMethod','MonthlyCharges','TotalCharges']

if st.button('Predict'):
  df=pd.DataFrame(data,columns)
  
  st.form_submit_button('submit',on_click=make_prediction,kwargs=dict (pipeline=pipeline))

if __name__ == '__main__':

  
  select_model()
  predict_page()
  
  st.write(st.session_state)