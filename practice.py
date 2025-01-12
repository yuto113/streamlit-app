import streamlit as st
import random
num=st.number_input('random generator',min_value=0)
if st.button('btn1'):
    for i in range(num):
        random_number=random.randint(1,10)
        st.write(random_number)