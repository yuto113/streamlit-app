import streamlit as st
import random as ran
# 作るもの：＠計算＆漢字クイズアプリ＠

# タイトルをつける。
st.title('計算＆漢字クイズアプリ')

# 計算の問題出題(足し算～＋～)
if 'aa' not in st.session_state:
    st.session_state.aa = ran.randint(1, 100)
    st.session_state.bb = ran.randint(1, 100)

if st.button('計算の問題出題(足し算～＋～)'):
    st.session_state.aa = ran.randint(1, 100)
    st.session_state.bb = ran.randint(1, 100)

st.write(st.session_state.aa, '+', st.session_state.bb)

if st.button('こたえ (足し算)'):
    st.session_state.ancera = st.session_state.aa + st.session_state.bb
    st.write(st.session_state.ancera)

# 計算の問題出題(引き算～ー～)
if 'cc' not in st.session_state:
    st.session_state.cc = ran.randint(1, 100)
    st.session_state.dd = ran.randint(1, 100)

if st.button('計算の問題出題(引き算～ー～)'):
    st.session_state.cc = ran.randint(1, 100)
    st.session_state.dd = ran.randint(1, 100)

st.write(max(st.session_state.cc, st.session_state.dd), '-', min(st.session_state.cc, st.session_state.dd))

if st.button('こたえ (引き算)'):
    st.session_state.ancerb = abs(st.session_state.cc - st.session_state.dd)
    st.write(st.session_state.ancerb)

# 計算の問題出題(掛け算～✖～)
if 'ee' not in st.session_state:
    st.session_state.ee = ran.randint(1, 100)
    st.session_state.ff = ran.randint(1, 100)

if st.button('計算の問題出題(掛け算～✖～)'):
    st.session_state.ee = ran.randint(1, 100)
    st.session_state.ff = ran.randint(1, 100)

st.write(st.session_state.ee, '✖', st.session_state.ff)

if st.button('こたえ (掛け算)'):
    st.session_state.ancerc = st.session_state.ee * st.session_state.ff
    st.write(st.session_state.ancerc)

# 計算の問題出題(割り算～÷～)
if 'gg' not in st.session_state:
    st.session_state.gg = ran.randint(1, 100)
    st.session_state.hh = ran.randint(1, 100)

if st.button('計算の問題出題(割り算～÷～)'):
    st.session_state.gg = ran.randint(1, 100)
    st.session_state.hh = ran.randint(1, 100)

st.write(st.session_state.gg, '÷', st.session_state.hh)

if st.button('こたえ (割り算)'):
    st.session_state.ancerd = round(st.session_state.gg / st.session_state.hh, 1)
    st.write(st.session_state.ancerd)