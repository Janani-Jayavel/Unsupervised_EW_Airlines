import pandas as pd
import numpy as np
import warnings; warnings.filterwarnings('ignore')
import joblib as jb
import streamlit as st

model = jb.load('package.pkl')
data = pd.read_csv('dataset.txt')

def model_prediction(Balance,Qual_miles,cc1_miles,cc2_miles,cc3_miles,Bonus_miles,Bonus_trans,Flight_miles_12mo,Flight_trans_12,Days_since_enroll,Award):
    new = [Balance,Qual_miles,cc1_miles,cc2_miles,cc3_miles,Bonus_miles,Bonus_trans,Flight_miles_12mo,Flight_trans_12,Days_since_enroll,Award]
    new = pd.DataFrame([new],columns = ['Balance','Qual_miles','cc1_miles','cc2_miles','cc3_miles','Bonus_miles','Bonus_trans','Flight_miles_12mo','Flight_trans_12','Days_since_enroll','Award'])
    prediction = model.predict(new)
    return prediction
    

def front_page():
    st.title('EW_Airlines')
    
    name = '''
    <div style = 'background-color:red;'>
    <h2 style = 'color:white;text-align:centre;'>Cluster Prediction</h2>
    </div>
    '''
    
    Balance = st.number_input('Enter the balance hours')
    Qual_miles = st.number_input('Enter the Qual miles')
    cc1_miles  = st.selectbox('select cc1 miles',np.unique(data['cc1_miles']))
    cc2_miles  = st.selectbox('select cc2 miles',np.unique(data['cc2_miles']))   
    cc3_miles  = st.selectbox('select cc3 miles',np.unique(data['cc3_miles']))       
    Bonus_miles = st.number_input('Enter the Bonus miles')    
    Bonus_trans = st.number_input('Enter the Bonus trans',min_value = 1, max_value = 100)      
    Flight_miles_12mo = st.number_input('Enter the Flight Miles')   
    Flight_trans_12 = st.number_input('Enter the Flight trans')   
    Days_since_enroll =st.number_input('Enter the days since enroll')   
    Award = st.selectbox('select your award status',np.unique(data['Award']))          

    res = ''
    if st.button('Click here to find the cluster'):
        res = model_prediction(Balance,Qual_miles,cc1_miles,cc2_miles,cc3_miles,Bonus_miles,Bonus_trans,Flight_miles_12mo,Flight_trans_12,Days_since_enroll,Award)
        
    if (res==0):
        st.success('you belong to category 1')
    elif (res ==1):
        st.success('you belog to catgeory 2')
            
if __name__ == '__main__':
    front_page()
    