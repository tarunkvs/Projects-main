#Registration form using streamlit
import streamlit as st
import pandas as pd
from streamlit_option_menu import option_menu

with st.sidebar:
        selected=option_menu(
            menu_title="Menu",
            options=["Home","About","Contact"],
            default_index=0,
        )
        if selected=="Home":
            st.title(f"{selected}")
        if selected=="About":
            st.title(f"{selected}")
        if selected=="Contact":
            st.title(f"{selected}")
st.title("Registration Form")
name=st.text_input("Enter Name")
fname=st.text_input("Enter Father Name")
roll=st.text_input("Enter Roll_No")
gender=st.radio("Pick Your Gender",["Male","Female","Others"])

dept=st.selectbox("Enter Your Department",["Computer Science","Management","Biotechnology","Finance","Law","Engineering","Mathematics","Vocational"])
def funct1(): 
    if dept=="Computer Science":
         Branches=st.radio("Enter your Branch",["Computuer Science Core","Data-Science","Machine-Learning","Artificial Intelligence","Cyber-Security"])
         cgpa=st.text_input("Enter your CGPA")
funct1()

State=st.selectbox("Enter The State You Belongs To",["Andhra Pradesh","Arunachal Pradesh",	"Assam","Bihar","Chhattisgarh","Goa",	"Chandigarh","Gujarat","Haryana	","Himachal Pradesh	","Jharkhand",	"Karnataka","Kerala	","Madhya Pradesh	","Maharashtra","Uttar Pradesh","Uttarakhand	","West Bengal"])
def funct2():
     if State=="Andhra Pradesh":
          uni=st.selectbox("Choose Your University/College",["Central University of Andhra Pradesh","Central Tribal University of Andhra Pradesh","National Sanskrit University","All India Institute of Medical Sciences","Indian Institute of Management	Visakhapatnam","Indian Institute of Science Education and Research"])
     if State=="Arunachal Pradesh":
          uni=st.selectbox("Choose Your University/College",["Central Institute of Himalayan Cultural Studies","Himalayan University","Indira Gandhi Technological and Medical Sciences University","Venkateshwara Open University","Rajiv Gandhi University"])
     if State=="Assam":
          uni=State.selectbox("Choose Your University/College",["Assam University","Tezpur University","Indian Statistical Institute Tezpur","National Institute of Technology, Silchar"])
     if State=="Uttar Pradesh":
          uni=st.selectbox("Choose Your University/College",["Banaras Hindu University","Rajiv Gandhi National Aviation University","Rani Lakshmi Bai Central Agricultural University","Gautam Buddha University","Maa Shakumbhari University","Mahatma Gandhi Kashi Vidyapeeth","Prof. Rajendra Singh (Rajju Bhaiya) University"])

funct2()
st.checkbox("ALL Above Fields Are Filled Correctly........")
but=st.button("Submit")

st.balloons()



     
   


 


