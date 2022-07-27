import streamlit as st


st.subheader("See Food")

image_file = st.file_uploader("Upload Images", type=["png","jpg","jpeg"])

im_file_path = '/Users/vikassewani/Desktop/thisimage.png'

if image_file is not None:
    st.image(load_image(image_file),width=250)
    file_details = {"filename":image_file.name, "filetype":image_file.type,
                    "filesize":image_file.size}
    st.write(file_details)
    