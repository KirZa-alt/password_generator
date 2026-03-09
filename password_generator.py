import streamlit as st 
import random
import string

title= st.title("Password Generator App")
lenght=st.slider("Enter Password Lenght", 6, 20, 10)

characters=string.ascii_letters + string.digits + string.punctuation

if st.button("Generate password"):
        password = ''.join(random.choice(characters) for i in range(lenght))
        st.success(password)