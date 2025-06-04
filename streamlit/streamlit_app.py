import streamlit as st  

st.badge("hello world", icon="❤️", color="violet")
st.write("hello world")

selected_colour = st.color_picker("pick your colour")
print(selected_colour)
st.title("You selected " + selected_colour)

selected_fruit = st.selectbox("Select your favourite fruit", options=["apple", "orange", "banana"])
st.badge(selected_fruit, icon="🍎" if selected_fruit == "apple" else "🍉", color="orange")