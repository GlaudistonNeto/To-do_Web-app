import streamlit as st
import functions

todos = functions.get_todos()

st.title("My Todo App")
st.subheader("This is my too App.")
st.write("This app is to increase your prouctivity.")

st.checkbox("Buy grocery.")
st.checkbox("Throw the cat's box.")


for todo in todos:
    st.checkbox(todo)

st.text_input(label="", placeholder="Add new todo... ")