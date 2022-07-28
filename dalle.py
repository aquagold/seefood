#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 27 12:24:32 2022

@author: vikassewani
"""

import requests
import base64
import streamlit as st

URL = "https://hindu-slides-full-specialty.trycloudflare.com"
headers = {'Bypass-Tunnel-Reminder': "go",
           'mode': 'no-cors'}

def check_if_valid_backend(url):
    try:
        resp = requests.get(url, timeout=5, headers=headers)
        return resp.status_code == 200
    except requests.exceptions.Timeout:
        return False
    
def call_dalle(url, text, num_images=1):
    data = {"text": text, "num_images": num_images}
    resp = requests.post(url + "/dalle", headers=headers, json=data)
    if resp.status_code == 200:
        return resp
    
def create_and_show_images(text, num_images):
    valid = check_if_valid_backend(URL)
    if not valid:
        st.write("Backend service is not running")
    else:
        resp = call_dalle(URL, text, num_images)
        if resp is not None:
            arr = resp.json()
            im_data = arr['generatedImgs']
            img_data_base64 = base64.b64decode(im_data[0])
            st.image(img_data_base64)
          #  st.image(im_data, output_format='JPEG')
          #  for data in resp.json():
          #      img_data = base64.b64decode(data)
          #      st.image(img_data)
         