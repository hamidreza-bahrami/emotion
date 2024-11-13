import streamlit as st
import pickle
import re
import numpy as np
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from sklearn.feature_extraction.text import TfidfVectorizer
port_stem = PorterStemmer()
import time
from pygoogletranslation import Translator
import nltk
# nltk.download('stopwords')


st.set_page_config(page_title='تشخیص احساسات متن- RoboAi', layout='centered', page_icon='💬')

vector = pickle.load(open('vector.pkl', 'rb'))
load_model = pickle.load(open('model.pkl', 'rb'))

translator = Translator()

def stemming(content):
  con = re.sub('[^a-zA-Z]', ' ', content)
  con = con.lower()
  con = con.split()
  con = [port_stem.stem(word) for word in con if not word in stopwords.words('english')]
  con = ' '.join(con)
  return con

def thoughty(text):
  text = stemming(text)
  input_text = [text]
  vector1 = vector.transform(input_text)
  prediction = load_model.predict(vector1)
  return prediction

def show_page():
    st.write("<h3 style='text-align: center; color: gold;'>سامانه تشخیص احساسات متن 💬</h3>", unsafe_allow_html=True)
    st.write("<h5 style='text-align: center; color: white;'>Robo-Ai.ir طراحی شده توسط</h5>", unsafe_allow_html=True)
    st.link_button("Robo-Ai بازگشت به", "https://robo-ai.ir")
    with st.sidebar:
        col1, col2, col3 = st.columns(3)
        with col1:
            st.write(' ')
        with col2:
            st.image('img.png')
        with col3:
            st.write(' ')
        st.divider()
        st.write("<h4 style='text-align: center; color: white;'>تشخیص احساس</h4>", unsafe_allow_html=True)
        st.write("<h4 style='text-align: center; color: white;'>با تحلیل متن کاربر</h4>", unsafe_allow_html=True)
        st.divider()
        st.write("<h5 style='text-align: center; color: white;'>طراحی و توسعه</h5>", unsafe_allow_html=True)
        st.write("<h5 style='text-align: center; color: white;'>حمیدرضا بهرامی</h5>", unsafe_allow_html=True)


    container = st.container(border=True)
    container.write("<h6 style='text-align: right; color: white;'>تشخیص مثبت یا منفی بودن متن 💬</h6>", unsafe_allow_html=True)
    
    text_3 = st.text_area('متن خود را وارد کنید',height=None,max_chars=None,key=None)

    button_3 = st.button('تشخیص احساس')
    if button_3:
        if text_3 == "":
            with st.chat_message("assistant"):
                with st.spinner('''درحال تحلیل'''):
                    time.sleep(1)
                    st.success(u'\u2713''تحلیل انجام شد')
                    text1 = 'لطفا متن را وارد کنید'
                    def stream_data1():
                        for word in text1.split(" "):
                            yield word + " "
                            time.sleep(0.09)
                    st.write_stream(stream_data1)
    
        
        else:
            out = translator.translate(text_3)
            prediction_class = thoughty(out.text)
            if prediction_class == [1]:
                with st.chat_message("assistant"):
                    with st.spinner('''درحال تحلیل'''):
                        time.sleep(1)
                        st.success(u'\u2713''تحلیل انجام شد')
                        text1 = 'بر اساس تحلیل من ، متن وارد شده دارای احساس منفی است'
                        text2 = 'Based on my analysis , the entered text is Negative'
                        def stream_data1():
                            for word in text1.split(" "):
                                yield word + " "
                                time.sleep(0.09)
                        st.write_stream(stream_data1)
                        def stream_data2():
                            for word in text2.split(" "):
                                yield word + " "
                                time.sleep(0.09)
                        st.write_stream(stream_data2)

            else:
                with st.chat_message("assistant"):
                    with st.spinner('''درحال تحلیل'''):
                        time.sleep(1)
                        st.success(u'\u2713''تحلیل انجام شد')
                        text3 = 'بر اساس تحلیل من ، متن وارد شده دارای احساس مثبت است'
                        text4 = 'Based on my analysis , the entered text is Positive'
                        def stream_data3():
                            for word in text3.split(" "):
                                yield word + " "
                                time.sleep(0.09)
                        st.write_stream(stream_data3)
                        def stream_data4():
                            for word in text4.split(" "):
                                yield word + " "
                                time.sleep(0.09)
                        st.write_stream(stream_data4)

    else:
        pass

show_page()
