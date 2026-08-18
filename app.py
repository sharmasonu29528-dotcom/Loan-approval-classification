import pandas as pd
import numpy as np
import streamlit as st
import pickle

model = pickle.load(open('lr_loan_status.pkl','rb'))


st.title('Loan Approval Status Prediction App')

st.write('Fill the details to check your Loan Approval Status')

col1, col2 = st.columns(2)

with col1 :
    gender = st.selectbox('Gender',['Male','Female'])
    married = st.selectbox('Married',['Yes','No'])
    dependents = st.slider('Dependents',0,3,2)
    education = st.selectbox('Education',['Graduate','Not Graduate'])
    self_employed = st.selectbox('Self Employed',['Yes','No'])

with col2 :
    app_income = st.number_input('Applicant Income',1025,32540,2500)
    co_app_income = st.number_input('CoApplicant Income',0,8896,1200)
    loan_amount = st.number_input('Loan Amount',min_value=30.65,max_value=496.0)
    loan_amount_term = st.selectbox('Loan Amount Term',[84,120,180,240,300,360,480])
    credit_history = st.selectbox('Credit History',[0,1])
    property_area = st.selectbox('Property Area',['Rural','Urban','Semiurban'])


gender = 1 if gender=='Male' else 0
married = 1 if married=='Yes' else 0
education = 1 if education=='Graduate' else 0
self_employed = 1 if self_employed=='Yes' else 0


if property_area=='Semiurban':
    pa_su = 1
    pa_u = 0
    pa_r = 0
elif property_area=='Urban':
    pa_su = 0
    pa_u = 1
    pa_r = 0
elif property_area=='Rural':
    pa_su = 0
    pa_u = 0
    pa_r = 1


test_data = np.array([gender,married,dependents,education,self_employed,app_income,co_app_income,
                      loan_amount,loan_amount_term,credit_history,pa_su,pa_u])

test_data = test_data.reshape(1,12)
test_df = pd.DataFrame(test_data,columns = ['Gender', 'Married', 'Dependents', 'Education', 'Self_Employed',
       'ApplicantIncome', 'CoapplicantIncome', 'LoanAmount',
       'Loan_Amount_Term', 'Credit_History', 'Property_Area_Semiurban',
       'Property_Area_Urban'])

st.write(test_df)

if st.button('Predict Loan Status'):
    pred = model.predict(test_df)[0]
    if pred == "N":
        st.warning(f'prediction => {pred} - Loan Rejected')
    else:
        st.sucess(f'prediction => {pred} - Loan Approved')


