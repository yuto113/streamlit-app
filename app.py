import streamlit as st
import random as ran
# 作るもの：＠計算＆漢字クイズアプリ＠

# タイトルをつける。
st.title('計算問題アプリ')

# セレクトボックスで問題の種類を選択
problem_type = st.selectbox(
    '問題の種類を選んでください',
    [
        '繰り上がりなしの足し算',
        '繰り上がりのある足し算',
        '繰り下がりなしの引き算',
        '繰り下がりのある引き算',
        '1桁×1桁の掛け算',
        '1桁×2桁の掛け算',
        '2桁×2桁の掛け算',
        'すべての掛け算',
        '割り算'
    ]
)

# 問題を出すボタン
if st.button('計算の問題出題'):
    if problem_type == '繰り上がりなしの足し算':
        st.session_state.aa = ran.randint(1, 9)
        st.session_state.bb = ran.randint(1, 9)
        st.session_state.problem = f"{st.session_state.aa} + {st.session_state.bb}"
    elif problem_type == '繰り上がりのある足し算':
        st.session_state.cc = ran.randint(10, 99)
        st.session_state.dd = ran.randint(10, 99)
        st.session_state.problem = f"{st.session_state.cc} + {st.session_state.dd}"
    elif problem_type == '繰り下がりなしの引き算':
        st.session_state.ee = ran.randint(1, 100)
        st.session_state.ff = ran.randint(1, 100)
        st.session_state.problem = f"{max(st.session_state.ee, st.session_state.ff)} - {min(st.session_state.ee, st.session_state.ff)}"
    elif problem_type == '繰り下がりのある引き算':
        st.session_state.gg = ran.randint(10, 99)
        st.session_state.hh = ran.randint(10, 99)
        st.session_state.problem = f"{max(st.session_state.gg, st.session_state.hh)} - {min(st.session_state.gg, st.session_state.hh)}"
    elif problem_type == '1桁×1桁の掛け算':
        st.session_state.ii = ran.randint(1, 9)
        st.session_state.jj = ran.randint(1, 9)
        st.session_state.problem = f"{st.session_state.ii} ✖ {st.session_state.jj}"
    elif problem_type == '1桁×2桁の掛け算':
        st.session_state.kk = ran.randint(1, 9)
        st.session_state.ll = ran.randint(10, 99)
        st.session_state.problem = f"{st.session_state.kk} ✖ {st.session_state.ll}"
    elif problem_type == '2桁×2桁の掛け算':
        st.session_state.mm = ran.randint(10, 99)
        st.session_state.nn = ran.randint(10, 99)
        st.session_state.problem = f"{st.session_state.mm} ✖ {st.session_state.nn}"
    elif problem_type == 'すべての掛け算':
        st.session_state.qq = ran.randint(1, 99)
        st.session_state.rr = ran.randint(1, 99)
        st.session_state.problem = f"{st.session_state.qq} ✖ {st.session_state.rr}"
    elif problem_type == '割り算':
        st.session_state.ss = ran.randint(1, 100)
        st.session_state.tt = ran.randint(1, 100)
        st.session_state.problem = f"{st.session_state.ss} ÷ {st.session_state.tt}"

    st.write(st.session_state.problem)

# 答えを表示するボタン
if st.button('こたえ'):
    if problem_type == '繰り上がりなしの足し算':
        st.session_state.ancera = st.session_state.aa + st.session_state.bb
        st.write(f"{st.session_state.problem} = {st.session_state.ancera}")
    elif problem_type == '繰り上がりのある足し算':
        st.session_state.ancerb = st.session_state.cc + st.session_state.dd
        st.write(f"{st.session_state.problem} = {st.session_state.ancerb}")
    elif problem_type == '繰り下がりなしの引き算':
        st.session_state.ancerc = abs(st.session_state.ee - st.session_state.ff)
        st.write(f"{st.session_state.problem} = {st.session_state.ancerc}")
    elif problem_type == '繰り下がりのある引き算':
        st.session_state.ancerd = abs(st.session_state.gg - st.session_state.hh)
        st.write(f"{st.session_state.problem} = {st.session_state.ancerd}")
    elif problem_type == '1桁×1桁の掛け算':
        st.session_state.ancerf = st.session_state.ii * st.session_state.jj
        st.write(f"{st.session_state.problem} = {st.session_state.ancerf}")
    elif problem_type == '1桁×2桁の掛け算':
        st.session_state.ancerg = st.session_state.kk * st.session_state.ll
        st.write(f"{st.session_state.problem} = {st.session_state.ancerg}")
    elif problem_type == '2桁×2桁の掛け算':
        st.session_state.ancerh = st.session_state.mm * st.session_state.nn
        st.write(f"{st.session_state.problem} = {st.session_state.ancerh}")
    elif problem_type == 'すべての掛け算':
        st.session_state.ancerj = st.session_state.qq * st.session_state.rr
        st.write(f"{st.session_state.problem} = {st.session_state.ancerj}")
    elif problem_type == '割り算':
        result = st.session_state.ss / st.session_state.tt
        if result.is_integer():
            st.session_state.ancerk = int(result)
        else:
            st.session_state.ancerk = f"{round(result, 5)}..."
        st.write(f"{st.session_state.problem} = {st.session_state.ancerk}")