


import pickle
import streamlit as st
from streamlit_option_menu import option_menu
import numpy as np
import xgboost as xgb
import pandas as pd


# Load the model

model = pickle.load(open('Model1.sav', 'rb'))

model1 = pickle.load(open('credit_card.sav', 'rb'))

# model2 = pickle.load(open("Credit_Score_Classification.sav", 'rb')) 
    
with st.sidebar:
    
    selected = option_menu('Barclays',
                          
                          ["Home","Stock Anomaly Detection","Banking Anomaly Detection",
                           'Credit-card Anomaly Detection',"Feedback"],
                          icons=["","","",""],
                          default_index=0)


if selected=="Home":
    st.title('Welcome to Barclays')
    st.image('https://www.pymnts.com/wp-content/uploads/2022/07/barclays-copper-stake.jpg')
    st.write('Select the model from the sidebar to make predictions')
    st.write("1st model is for stock Anomaly  detection")
    st.write("2nd model is for Banking Anomaly  Detection")
    st.write("3rd model is for Credit Card Anomaly  Detection")
    st.write("4th model is for Credit Score Classification")

if selected == 'Stock Anomaly Detection':
    st.title('Stock Anomaly Detection')
    st.markdown(
        "Read More about the dataset [Kaggle](https://finance.yahoo.com/quote/GS/history?period1=1230854400&period2=1576454400&interval=1d&filter=history&frequency=1d&includeAdjustedClose=true&guccounter=1&guce_referrer=aHR0cHM6Ly9jb2xhYi5yZXNlYXJjaC5nb29nbGUuY29tLw&guce_referrer_sig=AQAAALxTgaH-gTiOO7Buk3c9L23kARngePm3YPKDu_PUPqFtitW3B55uBa303QUhUAkJ3tb7eaQ_rEe5H4cQrOm0i7_emZ35cAom4RADhntujr_s8ND37dPdjc0Zy1-blGnx52Mlnp9ptaOU_FhxVD9mSGJKUbcfSCetoac9K0tGxHZE)"
    )
    st.markdown(
        "Read More about the Model Used [Google Collab Link](https://colab.research.google.com/drive/1ZsaAYRDbOIuXcvloagGyxSK9HqVb3mk3?usp=sharing)"
    )
    st.markdown("Not able to provide the input fields for the model as it is a time series data and the model is trained on the same data.")
    
    
if selected == 'Banking Anomaly Detection':
    st.title('Online Payments Anomaly Detection')
    
    st.markdown(
        "Read More about the dataset [Kaggle](https://www.kaggle.com/datasets/ealaxi/paysim1/data)"   
    )
    st.markdown(
        "Read More about the Model Used [Google Collab Link](https://colab.research.google.com/drive/1QL_wDSGfVg38KcPzRanDnA6KV-_7OoKa?usp=sharing) "
    )
    
    st.markdown(
        "Example : Transfer=4, 1000000, 1000000, 0 This is a fraud transaction as the old balance is 1000000 and the new balance is 0. So, the transaction is a fraud."
    )
    st.markdown(
        "Example : CASH OUT=1, 1000, 1000000, 999000 This is a fraud transaction as the old balance is 1000000 and the new balance is 999000. So, the transaction is a fraud."
    )
    
        # Input fields for the four values
    value1 = st.number_input('Type : CASH OUT=1 ,  PAYMENT=2 ,  CASH IN=3 ,  TRANSFER=4 ,  DEBIT=5', value=0, step=1)
    value2 = st.number_input('Amount', value=0, step=1)
    value3 = st.number_input('Old Balance In Account', value=0, step=1)
    value4 = st.number_input('New Balance IN Account', value=0, step=1)
    
    # Button to trigger the prediction
    if st.button('Predict'):
        # Make the prediction
        
        

        prediction = model.predict([[value1, value2, value3, value4]])
        # Display the prediction 
        ans = int(prediction[0])
        print(ans)
        if ans == 1:
            st.success('Prediction: Fraud')
        else:
            st.success('Prediction: Not Fraud')
            
            
            
if(selected == 'Credit-card Anomaly Detection'):
    st.title('Credit-card Anomaly Detection')
    st.markdown(
        "Read More about the dataset [Kaggle](https://www.kaggle.com/mlg-ulb/creditcardfraud)"
    )
    st.markdown(
        "Read More about the Model Used [Google Collab Link](https://colab.research.google.com/drive/1DFg9jRAKD24wURDvdIJbx2rQLYwhyXD7?usp=sharing) "
    )
    st.markdown(
        "Example for Credit-card Anomaly :[Example link](https://docs.google.com/document/d/1w21ljFBYiArDm6A49juFtN92-sflYmXN/edit?usp=sharing&ouid=100872727392622446887&rtpof=true&sd=true)"
    )
    # Input fields for the four values
    col1, col2, col3 = st.columns(3)
    
    with col1:
        value1 = st.number_input('Time', value=0, step=1)
        value2 = st.number_input('V1', value=0, step=1)
        value3 = st.number_input('V2', value=0, step=1)
        value4 = st.number_input('V3', value=0, step=1)
        value5 = st.number_input('V4', value=0, step=1)
    
    with col2:
        value6 = st.number_input('V5', value=0, step=1)
        value7 = st.number_input('V6', value=0, step=1)
        value8 = st.number_input('V7', value=0, step=1)
        value9 = st.number_input('V8', value=0, step=1)
        value10 = st.number_input('V9', value=0, step=1)
    
    with col3:
        value11 = st.number_input('V10', value=0, step=1)
        value12 = st.number_input('V11', value=0, step=1)
        value13 = st.number_input('V12', value=0, step=1)
        value14 = st.number_input('V13', value=0, step=1)
        value15 = st.number_input('V14', value=0, step=1)
    
    col4, col5, col6 = st.columns(3)
    
    with col4:
        value16 = st.number_input('V15', value=0, step=1)
        value17 = st.number_input('V16', value=0, step=1)
        value18 = st.number_input('V17', value=0, step=1)
        value19 = st.number_input('V18', value=0, step=1)
        value20 = st.number_input('V19', value=0, step=1)
    
    with col5:
        value21 = st.number_input('V20', value=0, step=1)
        value22 = st.number_input('V21', value=0, step=1)
        value23 = st.number_input('V22', value=0, step=1)
        value24 = st.number_input('V23', value=0, step=1)
        value25 = st.number_input('V24', value=0, step=1)
    
    with col6:
        value26 = st.number_input('V25', value=0, step=1)
        value27 = st.number_input('V26', value=0, step=1)
        value28 = st.number_input('V27', value=0, step=1)
        value29 = st.number_input('V28', value=0, step=1)
        Amount = st.number_input('Amount', value=0, step=1)
    
    
    if(st.button('Predict')):
        features = [[value1,value2,value3,value4,value5,value6,value7,value8,value9,value10,value11,value12,value13,value14,value15,value16,value17,value18,value19,value20,value21,value22,value23,value24,value25,value26,value27,value28,value29,Amount]]
        features_df = pd.DataFrame(features, columns = ['Time', 'V1', 'V2', 'V3', 'V4', 'V5', 'V6', 'V7', 'V8', 'V9', 'V10', 'V11', 'V12', 'V13', 'V14', 'V15', 'V16', 'V17', 'V18', 'V19', 'V20', 'V21', 'V22', 'V23', 'V24', 'V25', 'V26', 'V27', 'V28', 'Amount'])
        features_DMatrix = xgb.DMatrix(features_df)
        threshold = 0.5
        is_fraud = model1.predict(features_DMatrix) > threshold
        if is_fraud[0]:
            st.success('Prediction: Fraud')
        else:
            st.success('Prediction: Not Fraud')
            
            
# print("Credit Score Prediction : ")
# a = float(input("Annual Income: "))
# b = float(input("Monthly Inhand Salary: "))
# c = float(input("Number of Bank Accounts: "))
# d = float(input("Number of Credit cards: "))
# e = float(input("Interest rate: "))
# f = float(input("Number of Loans: "))
# g = float(input("Average number of days delayed by the person: "))
# h = float(input("Number of delayed payments: "))
# i = input("Credit Mix (Bad: 0, Standard: 1, Good: 3) : ")
# j = float(input("Outstanding Debt: "))
# k = float(input("Credit History Age: "))
# l = float(input("Monthly Balance: "))
# features = np.array([[a,b,c,d,e,f,g,h,i,j,k,l]])
# print("Predicted Credit Score = ", model.predict(features))       
# if(selected == 'Credit Score Classification'):


#     st.title('Credit Score Prediction')
    
#     st.markdown(
#         "Read More about the dataset [Kaggle](https://drive.google.com/file/d/1t0qEX194UucNUIj4DIIuD6ykCnAUXrr1/view?usp=sharing)"
#     )
#     st.markdown(
#         "Read More about the Model Used [Google Collab Link](https://colab.research.google.com/drive/1CAM8oGv-tQqIhXjcxgG-Aq0mw9e1m5T_?usp=sharing) "
#     )
#     st.markdown(
#         "Example of data :\n"
#         "Annual Income: 12 ,\n"
#         "Monthly Inhand Salary: 45 ,\n"
#         "Number of Bank Accounts: 1 ,\n"
#         "Number of Credit cards: 2 ,\n"
#         "Interest rate: 3 ,\n"
#         "Number of Loans: 3 ,\n"
#         "Average number of days delayed by the person: 4 ,\n"
#         "Number of delayed payments: 3 ,\n"
#         "Credit Mix (Bad: 0, Standard: 1, Good: 3): 5 ,\n"
#         "Outstanding Debt: 4 ,\n"
#         "Credit History Age: 3 ,\n"
#         "Monthly Balance: 56 ,\n"
#         "Predicted Credit Score = ['Standard']"
#     )
    
    
#     col1, col2, col3 = st.columns(3)

#     with col1:
#         a = st.number_input('Annual Income', value=0, step=1)
#         b = st.number_input('Monthly Inhand Salary', value=0, step=1)
#         c = st.number_input('Number of Bank Accounts', value=0, step=1)
#         k = st.number_input('Credit History Age', value=0, step=1)

#     with col2:
#         d = st.number_input('Number of Credit cards', value=0, step=1)
#         e = st.number_input('Interest rate', value=0, step=1)
#         f = st.number_input('Number of Loans', value=0, step=1)
#         l = st.number_input('Monthly Balance', value=0, step=1)

#     with col3:
#         g = st.number_input('Average number of days delayed by the person', value=0, step=1)
#         h = st.number_input('Number of delayed payments', value=0, step=1)
#         i = st.number_input('Credit Mix (Bad: 0, Standard: 1, Good: 3)', value=0, step=1)
#         j = st.number_input('Outstanding Debt', value=0, step=1)
        
       
    
    # if(st.button('Predict')):
    #     features = [[a,b,c,d,e,f,g,h,i,j,k,l]]
    #     # prediction = model2.predict(features)
    #     st.success('Predicted Credit Score = {}'.format(prediction[0]))
        
if selected=="Feedback":
    
    st.title('Thank You')
    st.write('Hope you had a great experience')
    st.write('Please provide your valuable feedback as it would help us greatly in improving in the next hackathons or projects which we will build in future.Thank you very much for taking the time to review our project')
    st.markdown(
        "Feedback Form [Link](https://colab.research.google.com/drive/1yCloe-VHQJq1SrBdkzBbbTg_QgcjBRXt?usp=sharing)"
    )

    st.write('This is the only small part of  project which we are thinking to build in future. Please provide us chance to work with you.')  
    st.image('https://t4.ftcdn.net/jpg/05/05/39/07/360_F_505390776_8ilykzGiVSpIjUqdEXFhDY1ACRJZPDRD.jpg')  
    

    
    













