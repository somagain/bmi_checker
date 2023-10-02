
### new
from PIL import Image    
import streamlit as st
import math
st.title("This is my BMI calculator")
img = Image.open("bmi2.jpg")
st.image(img)

st.subheader("Introduction")
st.text("""
        BMI in an individual is calculated by the use of a mathematical formula.
        It can also be estimated using tables in which one can match height in inches, 
        centimeters or meters to weight in pounds or kilograms to estimate BMI. 
        This BMI calculators help you calculate your BMI  and gives you a BMI grade. 
        The formula used - BMI = (Weight in kilograms) divided by (Height in metres squared)
        A normal BMI score is one that falls between 18.5 and 24.9. This indicates that a person
        is within the normal weight range for his or her height. A BMI chart is used to categorize
        a person as underweight, normal, overweight, or obese.
        
""", )

weight=st.number_input("Enter your weight in kg", step=0.1, min_value =1.0, max_value=1000.0)
height =st.number_input("Enter your height in meters", step=0.1, min_value =1.0, max_value=5.0)

  
bmi = weight/(height)**2
st.button("Reset", type="primary")
if st.button('Calculate BMI'):
    st.success(f"Your BMI is {bmi}")


def grader(bmi):
    if bmi < 18.5:
        grade = "Underweight"
    elif 18.5 < bmi < 24.9:
        grade = "Normal weight"
    elif 25 < bmi < 29:
        grade = "Overweight"
    elif  bmi > 30:
        grade = "Obese"
    else:
        grade = "Infinity"
    
    return st.success(f"Your are {grade}") 


img = Image.open("bmigif.gif")
st.sidebar.image(img)


st.sidebar.button("Reset", type="secondary")
if st.sidebar.button('Grade of BMI'):
    grader(bmi)
