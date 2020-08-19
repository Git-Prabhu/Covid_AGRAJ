import streamlit as st
import numpy as np
import pandas as pd
from sklearn import datasets
import plotly.graph_objects as go
from PIL import Image
import custom_gauge as cg

image = Image.open('COVID_Agraj_image.jpg')
st.image (image, caption='A COVID-19 Predictor', use_column_width=True)

gender = st.sidebar.selectbox("Select Gender",("Male", "Female"))
age = st.sidebar.selectbox("Select Age group",("0-24", "25-34", "35-44", "45-54", "55-64", "65-74", "75-84", "Above 85"))
race = st.sidebar.selectbox("Select your Race",("White", "Black", "Asian", "LatinX", "American Indian/Alaskan Native", "Others"))
state = st.sidebar.selectbox("Select your state",("Alabama", "Alaska", "Arizona", "Arkansas", "California", "Colarado", "Connecticut","Delaware","Florida", "Georgia","Hawaii",
            "Idaho","Illinois","Indiana","Iowa","Kansas","Kentucky","Louisiana","Maine","Maryland","Massachusetts","Michigan","Minnesota","Mississippi","Missouri","Montana","Nebraska","Nevada",
            "New Hampshire","New Jersey","New Mexico","New York","North Carolina","North Dakota","Ohio","Oklahoma","Oregon","Pennsylvania","Rhode Island","South Carolina","South Dakota",
            "Tennessee","Texas","Utah","Vermont","Virginia","Washington","West Virginia","Wisconsin","Wyoming"))
st.sidebar.text ("")
st.sidebar.text ("")
NPI1 = st.sidebar.checkbox ("I follow all CDC guidlines (Practice social distancing, Mandatory Mask-wearing in public spaces, Lockdown (Staying at home unless otherwise necessary))")
#NPI2 = st.sidebar.checkbox ("I practice social distancing as per CDC Guidelines")
#NPI3 = st.sidebar.checkbox ("I use face coverings as per CDC Guidelines")

st.sidebar.text ("")
st.sidebar.text ("")

st.sidebar.button('Submit')

def user_input_features():
        data = {'gender': gender,
                'age': age,
                'race': race,
                'state': state,
                'NPI1': NPI1}
                #'NPI2': NPI2,
                #'NPI3': NPI3}
        features = pd.DataFrame (data,index=[0])
        return features

input_df = user_input_features()

def output_gender():
       data = None
       if gender == 'Male':
               data = 12.19
       else:
               data = 11.73
       x = data
       return x
output_df1 = output_gender ()

def output_race():
        data = None
        if race == 'White':
            data = 4.85
        elif race == 'Black':
            data = 10.38
        elif race == 'Asian':
            data = 4.15
        elif race == 'LatinX':
            data = 5.08
        elif race == 'American Indian/Alaskan Native':
            data = 6.56
        else:
            data = 7.83
        y = data
        return y
output_df2 = output_race()

def output_age():
        data = None
        if age == '0-24':
            data = 0.60
        elif age == '25-34':
            data = 1.68
        elif age == '35-44':
            data = 5.03
        elif age == '45-54':
            data = 7.52
        elif age == '55-64':
            data = 8.92
        elif age == '65-74':
            data = 9.15
        elif age == '75-84':
            data = 9.04
        else:
            data = 7.61
        a = data
        return a
output_df4 = output_age()

def output_NPI():
        data = None
        if NPI1 == 1:
            data = 0.18
        else:
            data = 0.82
        b = data
        return b
output_df5 = output_NPI()

def output_state():
        data = None
        if state == 'Alabama':
            data = 5.52
        elif state == 'Alaska':
            data = 1.14
        elif state == 'Arizona':
            data = 8.77
        elif state == 'Arkansas':
            data = 2.68
        elif state == 'California':
            data = 6.32
        elif state == 'Colorado':
            data = 8.54
        elif state == 'Connecticut':
            data = 30.24
        elif state == 'Delaware':
            data = 12.88
        elif state == 'Florida':
            data = 5.77
        elif state == 'Georgia':
            data = 8.83
        elif state == 'Hawaii':
            data = 0.51
        elif state == 'Idaho':
            data = 2.40
        elif state == 'Illinois':
            data = 14.22
        elif state == 'Indiana':
            data = 9.47
        elif state == 'Iowa':
            data = 6.10
        elif state == 'Kansas':
            data = 2.76
        elif state == 'Kentucky':
            data = 3.30
        elif state == 'Louisiana':
            data = 16.79
        elif state == 'Maine':
            data = 1.81
        elif state == 'Maryland':
            data = 13.47
        elif state == 'Massachusetts':
            data = 27.02
        elif state == 'Michigan':
            data = 13.68
        elif state == 'Minnesota':
            data = 7.74
        elif state == 'Mississippi':
            data = 9.31
        elif state == 'Missouri':
            data = 4.13
        elif state == 'Montana':
            data = 1.03
        elif state == 'Nebraska':
            data = 4.12
        elif state == 'Nevada':
            data = 6.03
        elif state == 'New Hampshire':
            data = 6.80
        elif state == 'New Jersey':
            data = 34.52
        elif state == 'New Mexico':
            data = 6.95
        elif state == 'New York':
            data = 48.16
        elif state == 'North Carolina':
            data = 4.87
        elif state == 'North Dakota':
            data = 2.81
        elif state == 'Ohio':
            data = 6.08
        elif state == 'Oklahoma':
            data = 2.97
        elif state == 'Oregon':
            data = 1.75
        elif state == 'Pennsylvania':
            data = 11.64
        elif state == 'Rhode Island':
            data = 20.52
        elif state == 'South Carolina':
            data = 5.50
        elif state == 'South Dakota':
            data = 3.32
        elif state == 'Tennessee':
            data = 2.62
        elif state == 'Texas':
            data = 5.22
        elif state == 'Utah':
            data = 2.86
        elif state == 'Vermont':
            data = 2.21
        elif state == 'Virginia':
            data = 6.33
        elif state == 'Washington':
            data = 5.63
        elif state == 'West Virginia':
            data = 1.49
        elif state == 'Wisconsin':
            data = 3.66
        else:
            data = 1.19
        c = data
        return c
output_df6 = output_state()

def aggregate_calc():
    #data = ((output_df1*0.25)+(output_df2*0.25)+(output_df4*0.25)+(output_df6*0.25))/4*(output_df5)
    data = ((output_df1+output_df2+output_df4+output_df6)*output_df5)
    z = data
    return z
output_df3 = aggregate_calc()

st.sidebar.text ("")
st.sidebar.text ("")

#st.sidebar.checkbox ("I understand the terms and conditions")

#st.sidebar.text ("")

#st.sidebar.button('Submit')

#image = Image.open('sunrise.jpg')
#st.Image (image, caption ='Your risk of Covid', use_column_width = True)

#st.header("Image of Guage")
#filename = "Gauge.png"
#data = si.get_images().get(filename)
#st.image(data, caption=filename, output_format="PNG")

#st.text ("")
#st.text ("")
#st.text ("")
#st.text ("")

st.subheader ('User inputs:')
st.write(input_df)

st.text ("")
st.text ("")

#st.write(output_df3,'%')

#st.write(pd.DataFrame({
#    'Raw score': [1, 2, 3, 4, 5, 6],
#    'Weighted Score': [10, 20, 0, 40, 45, 55],
#    }))

st.write("""
## Mortality Rate:
""")

cg.render_gauge((int(output_df3)))

fig = go.Figure(go.Indicator(
    mode = "number+gauge+delta", value = output_df3,
    gauge = {
    'shape': "bullet"},
    #'axis': {'range': [None, 100]},
    #value = output_df3,
    #delta = {'reference': 100},
    domain = {'x': [0, 1], 'y': [0, 1]},
    title = {'text': "Score"}))
fig.update_layout(height = 300)
#fig.show()
#st.write(fig)
