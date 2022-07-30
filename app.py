import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
import csv
selected = option_menu("Menu", ["Home",'Tasks','Upload','Settings'],
        icons=['house','list-check','upload', 'gear',], menu_icon="caret-down-fill", default_index=1,orientation="horizontal")
if(selected == "Tasks"):


    flag = False

    def addTask(str):
        global ls
        ls = str.split(",")
        global lc
        lc = []
        global ln
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
        elif(name == '1'):
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
            columns = ls
            dict = {'Tasks':columns}
            df = pd.DataFrame(dict)
            csv = df.to_csv(index=False)
            st.download_button(label="Download data as CSV", data=csv, file_name='mytasks.csv')

if(selected=="Upload"):

    def addTask(mytsks):
        global ls
        ls = mytsks.copy()
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

    mytsks = []
    uploaded_file = st.file_uploader("Upload .csv format of comma separated tasks", type = ['csv'])
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        mytsks = df.columns.to_list()

        button = st.button('Done', on_click = addTask(mytsks))
        prog = len(lc)/len(ls)
        st.progress(prog)
        if(button):
            if(length==0):
                st.success("Hooray! All tasks Completed")
            else:
                st.error("Tasks remain!")
        csv = df.to_csv()
        st.download_button(label="Download data as CSV", data=csv, file_name='mytasks.csv')
