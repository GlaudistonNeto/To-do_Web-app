import streamlit as st
import functions

def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    functions.write_todos(todos)


todos = functions.get_todos()

st.title("My Todo App")
st.subheader("This is my too App.")
st.write("This app is to increase your prouctivity.")


for todo in todos:
    st.checkbox(todo)

st.text_input(label="", placeholder="Add new todo... ", on_change=add_todo, key='new_todo')

st.session_state