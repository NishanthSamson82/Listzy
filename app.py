import streamlit as st
from streamlit_option_menu import option_menu
from streamlit_lottie import st_lottie
import pandas as pd
import requests

def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

st.set_page_config(page_title='LISTZY', page_icon = 'Favicon.png', initial_sidebar_state = 'auto',layout="wide")


selected = option_menu("LISTZY", ["Home",'Tasks','Upload','Settings'],
        icons=['house','list-check','upload', 'gear',], menu_icon="chevron-double-down", default_index=1,orientation="horizontal")

if(selected=="Home"):
    original_title = '<span style="font-family:Montserrat; color:#FFFFFF; font-size: 80px;"><b>LIST</b></span><span style="font-family:Montserrat; color:#8B55D8; font-size: 80px;"><b>ZY</b></span>'
    st.markdown(original_title, unsafe_allow_html=True)
    left_col, right_col = st.columns(2)
    with left_col:
        "###"
        st.title("Welcome to Listzy")
        "Listzy is an amazing way to keep your *tasks* organized and achieve your goals"
        "With Listzy you can store, manage and take your tasks along with you wherever you go"
        punch = '<p style="font-family:Montserrat; color:#8B55D8; font-size: 15px;"><b>Never miss a deadline again!</b></p>'
        st.markdown(punch, unsafe_allow_html=True)
        "#"
        "#"
        st.title("Never gonna give you up, literally!")
        "You heard us, that's what we say to our tasks"
        "Listzy offers simple and easy tools for you to achieve greater productivity levels and push yourself to your limits"
        "##"
        st.title("Say no to distractions")
        "With our simple and Ad-free UI, say goodbye to distractions and interruptions"
        "It's just you and your tasks"
        "##"
        st.title("Got a flight to catch? No problem!")
        "Take your tasks with you wherever you go"
        "Export and store your tasks"
        "##"

    with right_col:
        lottie_json = load_lottieurl("https://assets9.lottiefiles.com/packages/lf20_5nchtofv.json")
        st_lottie(lottie_json, quality = "high", speed = 0.75, height=300)

        "#####"

        lottie_json2 = load_lottieurl("https://assets8.lottiefiles.com/packages/lf20_5odpfcjb.json")
        st_lottie(lottie_json2, quality = "high", speed = 1, height=350)

        "#"
        "######"

        lottie_json3 = load_lottieurl("https://assets1.lottiefiles.com/packages/lf20_qy2hc1lc.json")
        st_lottie(lottie_json3, quality = "high", speed = 1, height=200)




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
        length = len(ln)
        for j in range(len(ls)):
            task = ls[j]
            done = st.checkbox(task, help ='Check to mark as completed')
            if(done):
                lc.append(task)
                ln.remove(task)
                length = len(ln)
                if(length == 0):
                    st.balloons()

        with st.expander("Completed Tasks", expanded=False):
            st.header("Completed Tasks")
            for task in lc:
                st.write(":heavy_check_mark: "+ task)
        with st.expander("Incomplete Tasks", expanded=False):
            st.header("Incomplete Tasks")
            for task in ln:
                st.write(":x: " + task)


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
            fields = ls.copy()
            tasklist = ""
            for task in fields:
                tasklist += task +','
            tasklist = tasklist[:-1]
            st.download_button(label="Download data as CSV", data=tasklist, file_name='mytasks.csv')

if(selected=="Upload"):

    def addTask(mytsks):
        global ls
        ls = mytsks.copy()
        global lc
        lc = []
        ln = ls.copy()
        global length
        length = len(ln)
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
if(selected=="Settings"):

    st.header("Thank you for using Listzy, any feedback on the app would be much appreciated!")
    "#"
    st.write("Developed and designed by: *Nishanth Samson*")
    st.write("[Github profile](https://github.com/NishanthSamson82)")
    st.write("[More about me](http://www.nishanthsamson.me/)")
    st.header(":mailbox: Feedback")

    contact_form = """
    <form action="https://formsubmit.co/waduhek825@gmail.com" method="POST">
         <input type="hidden" name="_captcha" value="false">
         <input type="text" name="name" placeholder="Your name" required>
         <input type="email" name="email" placeholder="Your email" required>
         <textarea name="message" placeholder="Your thoughts"></textarea>
         <button type="submit">Send</button>
    </form>
    """

    st.markdown(contact_form, unsafe_allow_html=True)

    def local_css(file_name):
        with open(file_name) as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


    local_css("style.css")


