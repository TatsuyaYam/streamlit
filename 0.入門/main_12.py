import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time

st.title('Streamlit 超入門')

st.write('プログレスバーの表示')
'Start!!!'

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration{i+1}')
    bar.progress(i+1)
    time.sleep(0.1)
'Done!!!'

left_column,right_column = st.beta_columns(2)
button = left_column.button('右カラムに文字を表示')
if button:
    right_column.write('ここは右カラム')

expander1 = st.beta_expander('問合せ1')
expander1.write('問合せ回答1')
expander2 = st.beta_expander('問合せ2')
expander2.write('問合せ回答2')
expander3 = st.beta_expander('問合せ3')
expander3.write('問合せ回答3')

# condition = st.slider('あなたの今の調子は？',0,100,50)
# text = st.text_input('あなたの趣味を教えてください')
# 'コンディション：',condition
# 'あなたの趣味：',text

# option = st.selectbox(
#     'あなたが好きな数字を教えてください',
#     list(range(1,11))
# )
#'あなたの好きな数字は、',option,'です。'

#if st.checkbox('Show Image'):
#    img = Image.open('0.入門/thumbnail_yaruki_aru_suit.jpg')
#    st.image(img,caption='irasutoya',use_column_width=True)
