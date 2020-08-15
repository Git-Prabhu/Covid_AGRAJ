import streamlit as st
import numpy as np
import pandas as pd
from sklearn import datasets


st.title('COVID AGRAJ Project - COVID Predictor')

def user_input_features():
        gender = st.sidebar.selectbox("Select Gender",("Male", "Female"))
        age = st.sidebar.selectbox("Select Age group",("0-24", "25-34", "35-44", "45-54", "55-64", "65-74", "75-84", "Above 85"))
        race = st.sidebar.selectbox("Select your Race",("White", "Black", "Asian", "LatinX", "American Indian/Alaskan Native", "Others"))
        state = st.sidebar.selectbox("Select your state",("Alabama", "Alaska", "Arizona", "Arkansas", "California", "Colarado", "Connecticut","Delaware","Florida", "Georgia","Hawaii",
            "Idaho","Illinois","Indiana","Iowa","Kansas","Kentucky","Louisiana","Maine","Maryland","Massachusetts","Michigan","Minnesota","Mississippi","Missouri","Montana","Nebraska","Nevada",
            "New Hampshire","New Jersey","New Mexico","New York","North Carolina","North Dakota","Ohio","Oklahoma","Oregon","Pennsylvania","Rhode Island","South Carolina","South Dakota",
            "Tennessee","Texas","Utah","Vermont","Virginia","Washington","West Virginia","Wisconsin","Wyoming"))

        st.sidebar.text ("")
        st.sidebar.text ("")

        NPI1 = st.sidebar.checkbox ("I wash my hands as per CDC Guidelines")
        NPI2 = st.sidebar.checkbox ("I practice social distancing as per CDC Guidelines")
        NPI3 = st.sidebar.checkbox ("I use face coverings as per CDC Guidelines")
        data = {'gender': gender,
                'age': age,
                'race': race,
                'state': state,
                'NPI1': NPI1,
                'NPI2': NPI2,
                'NPI3': NPI3}
        features = pd.DataFrame (data,index=[0])
        return features

input_df = user_input_features()

st.sidebar.text ("")
st.sidebar.text ("")

st.sidebar.checkbox ("I understand the terms and conditions")

st.sidebar.text ("")

#st.sidebar.button('Submit')

#image = Image.open('sunrise.jpg')
#st.Image (image, caption ='Your risk of Covid', use_column_width = True)


#st.header("Image of Guage")
#filename = "Gauge.png"
#data = si.get_images().get(filename)
#st.image(data, caption=filename, output_format="PNG")
st.text ("")
st.text ("")
st.text ("")
st.text ("")

st.subheader ('Your selections - User inputs (Development team, pick values from input parameter dataframe):')
st.write(input_df)

st.text ("")
st.text ("")



st.write("""
## Your chance of contracting Covid is...
""")

st.write("""
### Results will be displayed here...
""")

#st.write(pd.DataFrame({
#    'Raw score': [1, 2, 3, 4, 5, 6],
#    'Weighted Score': [10, 20, 0, 40, 45, 55],
#    }))
