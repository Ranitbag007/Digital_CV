import streamlit as st
import requests
from streamlit_lottie import st_lottie
from PIL import Image


st.set_page_config(page_title='Digital Portfolio', page_icon=':saluting_face:', layout= 'wide')

def load_url(url):
    r=requests.get(url)
    if r.status_code!=200:
        return None
    return r.json()
lottie_coding1=load_url('https://assets10.lottiefiles.com/packages/lf20_7X0d6AzODk.json')
lottie_coding2=load_url('https://assets2.lottiefiles.com/packages/lf20_vq5wzcvx.json')
img_cat=Image.open('Images/dog_cat.png')
img_Handwriten=Image.open('Images/Handwritten digit recognition.jfif')

with st.container():
    st.subheader("Hi! I am  Ranit  :wave:")
    st.title('Beginner Machine Learning coder from India')
    st.write(' Machine Learning and Technology enthusiast')
    st.subheader('CV')
    st.write('[To downlad cv in pdf format...](https://drive.google.com/file/d/16zz37KZ1J-SsxRmFpWREv9d6VJNQ22z9/view?usp=share_link)')
    st.subheader('LinkedIn')
    st.write('[LinkdIn](https://www.linkedin.com/in/ranit-bag-a5a70b219)')

with st.container():
    st.write('---')
    left_column,right_column=st.columns(2)
    with left_column:
    
        st.header('Education:')
        st.subheader("B. Tech. in Electronics and Communnication Engineering")
        st.write('Guru Nanak Institute of Technology')
        st.write('''
                Year: 2018- 2022 

                DGPA: 8.50
                ''')

        st.subheader("Higher Secondary Examination(10+2)")
        st.write("Dumdum K. K. Hindu Academy")
        st.write('''
                Year: 2018
                
                Percentage: 70.6
                ''')
                
        st.subheader("Secondary Examination (10)")
        st.write("Dumdum K. K. Hindu Academy")
        st.write('''
                Year: 2016
                
                Percentage: 78.14
                ''')
    with right_column:
        st_lottie(lottie_coding2,height=300)


with st.container():
    st.write('---')
    left_column,right_column=st.columns(2)
    with left_column:
        st.header('Skills')
        st.write('[AI & ML](https://drive.google.com/file/d/1wEsDJIuxaQZJm5dvYhhmggvf6e5kimVt/view?usp=share_link)')
        st.write('[Python](https://drive.google.com/file/d/1xeEv23ffO8YMuEzr9QZBjT3Oxdt3wlvw/view?usp=share_link)')
        st.write('[C++](https://drive.google.com/file/d/1xjgu40l6CBcZcpKkP9zXVesN1B4hYpnO/view?usp=share_link)')
        st.write('[C](https://drive.google.com/file/d/1xhIrBqYhXYM0U29i4d8yj82YSLWJk-d0/view?usp=share_link)')
    
    with right_column:
        st_lottie(lottie_coding1,height=300)
    


with st.container():
    st.write('---')
    st.header("My Projects")
    st.write('##')
    image_column, text_column=st.columns((1,2))
    with image_column:
        st.image(img_cat)

    with text_column:
        st.subheader("Image based species recognition using AI & ML")
        st.write('[Click here ...](https://drive.google.com/drive/folders/1UztykX7T5cviHxo05ApJd6FImLakokP6?usp=share_link)')
with st.container():
    image_column, text_column=st.columns((1,2))
    with image_column:
        st.image(img_Handwriten)

    with text_column:
        st.subheader("Handwritten digit recognition using AI & ML")
        st.write('[Click here ...](https://drive.google.com/drive/folders/1_Or_Kb-O1W39F90_2tM1cYSiXokQX_9Z?usp=share_link)')