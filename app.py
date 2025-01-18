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
    st.session_state.ancera=st.session_state.aa+st.session_state.bb
st.write(st.session_state.ancera)

if st.button('計算の問題出題(足し算～ー～)'):
    
    st.session_state.cc=ran.randint(1,100)
    st.session_state.dd=ran.randint(1,100)
st.write(st.session_state.cc,'-',st.session_state.dd)
if st.button('こたえ'):
    st.session_state.ancerb=st.session_state.cc-st.session_state.dd
st.write(st.session_state.ancerb)