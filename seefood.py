import streamlit as st
from PIL import Image
import requests
import websockets
import json
import os


def save_uploadedfile(uploadedfile):
     check_dir = ''.join([os.getcwd(), '/tempDir/'])
     if (not os.path.isdir(check_dir)):
         os.mkdir(check_dir)
    
     with open(os.path.join("tempDir",uploadedfile.name),"wb") as f:
         f.write(uploadedfile.getbuffer())
     return st.success("Saved File:{} to tempDir".format(uploadedfile.name))
 

def load_image(image_file):
    img = Image.open(image_file)
    return img
 
    
st.subheader("See Food")
image_file = st.file_uploader("Upload Images", type=["png","jpg","jpeg"])

"""
if image_file is not None:
    
    st.image(load_image(image_file),width=250)
    file_details = {"filename":image_file.name, "filetype":image_file.type,
                    "filesize":image_file.size}
    #st.write(file_details)
    save_uploadedfile(image_file)
    
    ## Extract data
    image_dir = ''.join([os.getcwd(), '/tempDir/'])
    image_file_descriptor = open(''.join([image_dir, image_file.name]), 'rb')


    api_url = 'https://api.api-ninjas.com/v1/imagetotext'
    files = {'image': image_file_descriptor}
    r = requests.post(api_url, files=files, headers={'X-Api-Key': 'hBeHlA2f2g8gkNunbnBDXg==bgAu26luCQTY4LLO'})

    full_string =[]
    arr = r.json()

    for i in range(0, len(arr)):
        full_string.append(arr[i]['text'])
        
    st.write(f' '.join(full_string[0:min(10,len(full_string))]))
    
    #Call dall e!
    
"""