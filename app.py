import streamlit as st
st.title("Моето първо Streamlit приложение")
name = st.text_input("Как се казваш?")
if name:
  st.write(f"Здравей, {name}!")
name = st.text_input("На колко години си?")
 if name:
   st.write(f"Интересно!")
  
