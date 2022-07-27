import streamlit as st


st.subheader("See Food")

image_file = st.file_uploader("Upload Images", type=["png","jpg","jpeg"])

im_file_path = '/Users/vikassewani/Desktop/thisimage.png'

if image_file is not None:
    st.image(load_image(image_file),width=250)
    file_details = {"filename":image_file.name, "filetype":image_file.type,
                    "filesize":image_file.size}
    st.write(file_details)

api_url = 'https://api.api-ninjas.com/v1/imagetotext'

image_file_descriptor = open('/Users/vikassewani/Desktop/thisimage.png', 'rb')
files = {'image': image_file_descriptor}
r = requests.post(api_url, files=files, headers={'X-Api-Key': 'hBeHlA2f2g8gkNunbnBDXg==bgAu26luCQTY4LLO'})

full_string =[]
arr = r.json()

for i in range(0, len(arr)):
    full_string.append(arr[i]['text'])

st.write(f' '.join(full_string[0:min(10,len(full_string))]))