import streamlit as st
import random as ran
# 作るもの：＠計算＆漢字クイズアプリ＠

# タイトルをつける。
st.title('計算問題アプリ')

# 計算の問題出題(繰り上がりなしの足し算～＋～)
if 'aa' not in st.session_state:
    st.session_state.aa = ran.randint(1, 9)
    st.session_state.bb = ran.randint(1, 9)

if st.button('計算の問題出題(繰り上がりなしの足し算～＋～)'):
    st.session_state.aa = ran.randint(1, 9)
    st.session_state.bb = ran.randint(1, 9)

st.write(st.session_state.aa, '+', st.session_state.bb)

if st.button('こたえ (繰り上がりなしの足し算)'):
    st.session_state.ancera = st.session_state.aa + st.session_state.bb
    st.write(st.session_state.ancera)

# 計算の問題出題(繰り上がりのある足し算～＋～)
if 'cc' not in st.session_state:
    st.session_state.cc = ran.randint(10, 99)
    st.session_state.dd = ran.randint(10, 99)

if st.button('計算の問題出題(繰り上がりのある足し算～＋～)'):
    st.session_state.cc = ran.randint(10, 99)
    st.session_state.dd = ran.randint(10, 99)

st.write(st.session_state.cc, '+', st.session_state.dd)

if st.button('こたえ (繰り上がりのある足し算)'):
    st.session_state.ancerb = st.session_state.cc + st.session_state.dd
    st.write(st.session_state.ancerb)

# 計算の問題出題(繰り下がりなしの引き算～ー～)
if 'ee' not in st.session_state:
    st.session_state.ee = ran.randint(1, 100)
    st.session_state.ff = ran.randint(1, 100)

if st.button('計算の問題出題(繰り下がりなしの引き算～ー～)'):
    st.session_state.ee = ran.randint(1, 100)
    st.session_state.ff = ran.randint(1, 100)

st.write(max(st.session_state.ee, st.session_state.ff), '-', min(st.session_state.ee, st.session_state.ff))

if st.button('こたえ (繰り下がりなしの引き算)'):
    st.session_state.ancerc = abs(st.session_state.ee - st.session_state.ff)
    st.write(st.session_state.ancerc)

# 計算の問題出題(繰り下がりのある引き算～ー～)
if 'gg' not in st.session_state:
    st.session_state.gg = ran.randint(10, 99)
    st.session_state.hh = ran.randint(10, 99)

if st.button('計算の問題出題(繰り下がりのある引き算～ー～)'):
    st.session_state.gg = ran.randint(10, 99)
    st.session_state.hh = ran.randint(10, 99)

st.write(max(st.session_state.gg, st.session_state.hh), '-', min(st.session_state.gg, st.session_state.hh))

if st.button('こたえ (繰り下がりのある引き算)'):
    st.session_state.ancerd = abs(st.session_state.gg - st.session_state.hh)
    st.write(st.session_state.ancerd)

# 計算の問題出題(1桁×1桁の掛け算～✖～)
if 'ii' not in st.session_state:
    st.session_state.ii = ran.randint(1, 9)
    st.session_state.jj = ran.randint(1, 9)

if st.button('計算の問題出題(1桁×1桁の掛け算～✖～)'):
    st.session_state.ii = ran.randint(1, 9)
    st.session_state.jj = ran.randint(1, 9)

st.write(st.session_state.ii, '✖', st.session_state.jj)

if st.button('こたえ (1桁×1桁の掛け算)'):
    st.session_state.ancerf = st.session_state.ii * st.session_state.jj
    st.write(st.session_state.ancerf)

# 計算の問題出題(割り算～÷～)
if 'kk' not in st.session_state:
    st.session_state.kk = ran.randint(1, 100)
    st.session_state.ll = ran.randint(1, 100)

if st.button('計算の問題出題(割り算～÷～)'):
    st.session_state.kk = ran.randint(1, 100)
    st.session_state.ll = ran.randint(1, 100)

st.write(st.session_state.kk, '÷', st.session_state.ll)

if st.button('こたえ (割り算)'):
    result = st.session_state.kk / st.session_state.ll
    if result.is_integer():
        st.session_state.ancerg = int(result)
    else:
        st.session_state.ancerg = f"{round(result, 5)}..."
    st.write(st.session_state.ancerg)