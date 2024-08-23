import streamlit as st


def add_task(task):
    file = open("tasks.txt", "a")
    file.write(task + "\n")
    file.close()


def get_tasks():
    try:
        with open("tasks.txt", "r") as file:
            tasks = file.readlines()
    except FileNotFoundError:
        with open("tasks.txt", "w") as file:
            tasks = []
    return tasks


def remove_task(task_to_remove):
    tasks = get_tasks()
    file = open("tasks.txt", "w")
    for task in tasks:
        if task.strip() != task_to_remove:
            file.write(task)
    file.close()


st.title("Simple To-Do List")

task = st.text_input("Enter a task")
if st.button("Add Task"):
    add_task(task)
    st.success(f"Task '{task}' added.")

st.subheader("Your Tasks")
tasks = get_tasks()
for task in tasks:
    task = task.strip()
    if st.checkbox(task):
        remove_task(task)
        st.success(f"Task '{task}' removed.")
