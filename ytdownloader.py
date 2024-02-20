import streamlit as st
import pytube
from pytube import YouTube

st.image("yt_dwn.png")
st.title("Easiest YouTube Downloader Ever!")
st.write("""  Press Enter to add link to your list :smile:  """)

def display_input_row(index):
    st.text_input('',placeholder = "Paste a Youtube link here... ", key=f'{index}')
    
if 'links' not in st.session_state:
    st.session_state['links'] = 0

def increase_rows():
    st.session_state['links'] += 1

for i in range(st.session_state['links']):
    display_input_row(i)
    
    
st.button('Add link', on_click = increase_rows)  
    
st.subheader("Your links to download:")

for i in range(st.session_state['links']):
    st.write(st.session_state[f'{i}'])    

def download_all():
    for i in range(st.session_state['links']):
        yt = YouTube(st.session_state[f'{i}'])
        video = yt.streams.get_highest_resolution()
        video.download()

st.button("Download all!", on_click = download_all)
