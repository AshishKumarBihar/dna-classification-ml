import numpy as np
import pandas as pd
from sklearn.preprocessing import OrdinalEncoder
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingClassifier
from sklearn import metrics
import streamlit as st
import warnings
warnings.filterwarnings("ignore", category=UserWarning)

# dataset
df=pd.read_csv("https://raw.githubusercontent.com/gopiashokan/dataset/main/diabetes_prediction_dataset.csv")

enc=OrdinalEncoder()
df["smoking_history"]=enc.fit_transform(df[["smoking_history"]])
df["gender"]=enc.fit_transform(df[["gender"]])

x= df.drop("diabetes",axis=1)
y=df["diabetes"]
x_train , x_test , y_train, y_test = train_test_split(x,y,test_size=0.3)

model = GradientBoostingClassifier().fit(x_train,y_train)
y_pred = model.predict(x_test)
accuracy = metrics.accuracy_score(y_test,y_pred)


# project title & icon
st.set_page_config(page_title='Diabetes Prediction', page_icon=':mag:')
st.markdown(f'<h1 style="text-align: center;">Diabetes Prediction</h1>', unsafe_allow_html=True)

col1, col2 = st.columns(2, gap='large')

with col1:
    gender = st.selectbox(label='Gender', options=['Male', 'Female', 'Other'])
    gender_dict = {'Female':0.0, 'Male':1.0, 'Other':2.0}

    age = st.text_input(label='Age')

    hypertension = st.selectbox(label='Hypertension', options=['No', 'Yes'])
    hypertension_dict = {'No':0, 'Yes':1}

    heart_disease = st.selectbox(label='Heart Disease', options=['No', 'Yes'])
    heart_disease_dict = {'No':0, 'Yes':1}

with col2:
    smoking_history = st.selectbox(label='Smoking History', 
                                options=['Never', 'Current', 'Former', 'Ever', 'Not Current', 'No Info'])
    smoking_history_dict = {'Never':4.0, 'No Info':0.0, 'Current':1.0, 'Former':3.0, 'Ever':2.0, 'Not Current':5.0}

    bmi = st.text_input(label='BMI')

    hba1c_level = st.text_input(label='HbA1c Level')

    blood_glucose_level = st.text_input(label='Blood Glucose Level')

st.write('')
submit = st.button(label='Submit')
st.write('')

if submit:
    user_data = np.array( [[ gender_dict[gender], age, hypertension_dict[hypertension], heart_disease_dict[heart_disease],
                            smoking_history_dict[smoking_history], bmi, hba1c_level, blood_glucose_level ]] )

    test_result = model.predict(user_data)

    if test_result[0] == 0:
        st.success('Result: Negative')
        st.balloons()

    else:
        st.error('Result: Positive')