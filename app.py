import streamlit as st
import random as ran
# 作るもの：＠計算＆漢字クイズアプリ＠

# タイトルをつける。
st.title('計算＆漢字クイズアプリ')
#プログラム↓
if st.button('計算の問題出題(足し算～＋～)'):
    
    st.session_state.aa=ran.randint(1,100)
    st.session_state.bb=ran.randint(1,100)
st.write(st.session_state.aa,'+',st.session_state.bb)
if st.button('こたえ'):
    st.session_state.ancer=st.session_state.aa+st.session_state.bb
st.write(st.session_state.ancer)