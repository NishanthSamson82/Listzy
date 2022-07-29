import streamlit as st

flag = False

def addTask(str):
    global ls
    ls = str.split(",")
    global lc
    lc = []
    ln = ls.copy()
    global length
    for j in range(len(ls)):
        task = ls[j]
        done = st.checkbox(task, help ='Check to mark as completed')
        if(done):
            lc.append(task)
            ln.remove(task)
            length = len(ln)
            if(length == 0):
                st.balloons()

    st.header("Completed Tasks")
    for task in lc:
        st.write(task)
    st.header("Incomplete Tasks")
    for task in ln:
        st.write(task)


with st.container():
    name = st.text_input('Enter your name', placeholder = 'Name')
    if(name != ''):
        flag = True
        st.write("Hello, ", name)
    elif(name == ''):
        st.write('Please enter a valid name')


if(flag):
    st.title(name + "'s To-Do list")

    tasks = st.text_input('Enter your tasks', placeholder = 'Enter comma separated tasks')
    if(tasks):
        button = st.button('Done', on_click = addTask(tasks))
        prog = len(lc)/len(ls)
        st.progress(prog)
        if(button):
            if(length==0):
                st.success("Hooray! All tasks Completed")
            else:
                st.error("Tasks remain!")



