

import streamlit as st
import altair as alt
import re
import pandas as pd
import numpy as np
from io import StringIO




def write_file(filename, content):
    with open(filename, "w") as f:
        f.write(content)



def write_to_file(file_name, data_dict): # takes the dictionary and save it file with newlines
    with open(file_name, "w") as f:
        f.write(str(data_dict))

def read_from_file(file_name): # read the file and gives dictionary
    with open(file_name, "r") as f:
        data_text = f.read()
        data_dict = eval(data_text)
        return data_dict
    
    
    
def download_file():
    with open("data_dict.txt", "rb") as f:
        data = f.read()
    return st.download_button(
        label="Download File",
        data=data,
        file_name="my_file.txt",
        mime="text/plain",
    )


pass_code = 'yo'
if st.text_input('enter the code') == pass_code:
    
    
    file_name = 'data_dict.txt'
    data_dict = read_from_file(file_name)
    
    
    
    title = st.text_input("What do you want to write about ?")
    
    body = st.text_area("Start .... ", height=200, max_chars=None)
    
    
    
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("save entry "):
            try:
                data_x = body + '\n' + data_dict[title]
                data_dict.pop(title,None)
                data_dict[title] = data_x
                
            except:
                data_dict[title] = body
            write_to_file(file_name, data_dict)
            
    with col2:
        if st.button("show_keys"):
            st.write(list(reversed(list(data_dict.keys())))) # show the dictionary in reverse order
            
    
    if st.button("read previous entries "):
        st.write(dict(reversed(list(data_dict.items())))) # show the dictionary in reverse order
    
    
    
    
    # vertical space
    st.text("\n\n\n\n")


    if st.button("backup"):
        col1, col2 = st.columns(2)
        with col1:
            download_file()
        with col2:
            uploaded_file = st.file_uploader("Upload File")
            if uploaded_file is not None:
            # To convert to a string based IO:
                stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
            
                # To read file as string:
                string_data = stringio.read()
                st.write(string_data)
                write_to_file(file_name, string_data)
                
            
    

        
    
    
    



    








