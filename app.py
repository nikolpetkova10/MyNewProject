import streamlit as st
st.title("Моето първо Streamlit приложение")
name = st.text_input("Как се казваш?")
if name:
  st.write(f"Здравей, {name}!")
age = st.text_input("На колко години си?")
if age:
   st.write(f"Забавно е да си на {age}!")
  
