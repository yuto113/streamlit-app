import streamlit as st
import random as ran
# 作るもの：＠計算＆漢字クイズアプリ＠

# タイトルをつける。
st.title('計算＆漢字クイズアプリ')
#プログラム↓
if st.button('計算の問題出題(足し算～＋～)'):
    aa=ran.randint(1,100)
    bb=ran.randint(1,100)
    st.write(aa,'+',bb)
    if st.button('こたえ'):
        ancer=aa+bb
        st.write(ancer)