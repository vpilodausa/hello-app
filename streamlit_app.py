

import streamlit as st
import altair as alt
import re
import pandas as pd
import numpy as np




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
    with open("my_file.txt", "rb") as f:
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
    
    if st.button("save entry "):
        try:
            data_x = body + '\n' + data_dict[title]
            data_dict.pop(title,None)
            data_dict[title] = data_x
            
        except:
            data_dict[title] = body
        write_to_file(file_name, data_dict)
        
    
    if st.button("read previous entries "):
        st.write(dict(reversed(list(data_dict.items())))) # show the dictionary in reverse order
    
    
    
    filename = "my_file.txt"
    content = str({
  "Rules": "Never be low on energy. Avoid long walks in the sun. Your face will loose luster, you will not have energy to appreciate if you encounter something beautiful. ",
  "Automation": "-- Laser solder ball generator\n-- TIW laser cutter workshop",
  "organize": "Salvage components \n- take a backup of this hello-app every night before sleep. \n- make a server to backup files from your apps on your previous laptop and replace it with resberry pi.\n- Learn to access google drive API in python.",
  "simulation": "- if you want to learn or explore or play with something new, break it apart and play with it in template, record your learning and then include it in you original file.\n-simulation : always keep a basic template, keep adding the new commands to the template, keep a readme text file with template (later on you can change it to markdown and access it by streamlit), add the commands and things you learned to the readme,\n- simulation : write a code to attach all or one screenshot in the download to notability pdf file, make a template and attach figures by python, save it to dropbox."
})
    
    
    write_file(filename, content)
    
    
    
    
    
    
    

    st.title("Streamlit Download Button")
    download_file()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    








