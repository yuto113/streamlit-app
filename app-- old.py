import streamlit as st
import random as ran
import time
import unicodedata

# 作るもの：＠計算＆漢字クイズアプリ＠

# カスタムCSSを追加してボタンのスタイルを変更
st.markdown("""
    <style>
    .stButton>button {
        background-image: linear-gradient(to right, #ff7e5f, #feb47b); /* グラデーション */
        color: white;
        border: none;
        padding: 15px 32px;
        text-align: center;
        text-decoration: none;
        display: inline-block;
        font-size: 16px;
        margin: 4px 2px;
        cursor: pointer;
        border-radius: 12px;
        transition: transform 0.2s; /* アニメーション */
    }
    .stButton>button:hover {
        background-image: linear-gradient(to right, #feb47b, #ff7e5f); /* ホバー時のグラデーション */
        transform: scale(1.1); /* ホバー時の拡大 */
    }
    </style>
    """, unsafe_allow_html=True)

# タイトルをつける。
st.title('計算問題アプリ')
st.write("ver.3.9β")

# セレクトボックスで問題の種類を選択
problem_type = st.selectbox(
    '問題の種類を選んでください',
    [
        '繰(く)り上(あ)がりなしの足(た)し算(ざん)',
        '繰(く)り上(あ)がりのある足(た)し算(ざん)',
        '繰(く)り下(さ)がりなしの引(ひ)き算(ざん)',
        '繰(く)り下(さ)がりのある引(ひ)き算(ざん)',
        '1けた×1けたの掛(か)け算(ざん)',
        '1けた×2けたの掛(か)け算(ざん)',
        '2けた×2けたの掛(か)け算(ざん)',
        'すべての掛(か)け算(ざん)',
        '九九でできる割(わ)り算(ざん) (小数・あまりなし)',
        '九九でできる割(わ)り算(ざん) (小数・あまりあり)',
        '2けた÷1けたの割(わ)り算(ざん) (小数・あまりなし)',
        '2けた÷1けたの割(わ)り算(ざん) (小数・あまりあり)',
        '余りを出す割(わ)り算(ざん)',
        '普通の割(わ)り算(ざん)',
        '掛け算の穴埋め問題',
        '割り算の穴埋め問題'
    ]
)

# タイムアタックモードのボタン
if st.button('タイムアタックモード'):
    st.session_state.time_attack = True
    st.session_state.start_time = time.time()
    st.session_state.problem_generated = False
    st.session_state.correct_answers = 0
    st.session_state.answer = ''  # 回答欄をリセット

# 問題を出すボタン
if st.button('計算(けいさん)の問題出題(もんだいしゅつだい)') or st.session_state.get('time_attack', False):
    st.session_state.problem_generated = False  # ここでリセット
    if not st.session_state.get('problem_generated', False):
        if problem_type == '繰(く)り上(あ)がりなしの足(た)し算(ざん)':
            while True:
                st.session_state.aa = ran.randint(10, 99)
                st.session_state.bb = ran.randint(10, 99)
                if (st.session_state.aa % 10) + (st.session_state.bb % 10) < 10 and (st.session_state.aa // 10) + (st.session_state.bb // 10) < 10:
                    break
            st.session_state.problem = f"{st.session_state.aa} + {st.session_state.bb}"
        elif problem_type == '繰(く)り上(あ)がりのある足(た)し算(ざん)':
            st.session_state.cc = ran.randint(10, 99)
            st.session_state.dd = ran.randint(10, 99)
            st.session_state.problem = f"{st.session_state.cc} + {st.session_state.dd}"
        elif problem_type == '繰(く)り下(さ)がりなしの引(ひ)き算(ざん)':
            while True:
                st.session_state.ee = ran.randint(10, 99)
                st.session_state.ff = ran.randint(10, 99)
                if (st.session_state.ee % 10) >= (st.session_state.ff % 10) and (st.session_state.ee // 10) >= (st.session_state.ff // 10):
                    break
            st.session_state.problem = f"{st.session_state.ee} - {st.session_state.ff}"
        elif problem_type == '繰(く)り下(さ)がりのある引(ひ)き算(ざん)':
            st.session_state.gg = ran.randint(10, 99)
            st.session_state.hh = ran.randint(10, 99)
            st.session_state.problem = f"{max(st.session_state.gg, st.session_state.hh)} - {min(st.session_state.gg, st.session_state.hh)}"
        elif problem_type == '1けた×1けたの掛(か)け算(ざん)':
            st.session_state.ii = ran.randint(1, 9)
            st.session_state.jj = ran.randint(1, 9)
            st.session_state.problem = f"{st.session_state.ii} ✖ {st.session_state.jj}"
        elif problem_type == '1けた×2けたの掛(か)け算(ざん)':
            st.session_state.kk = ran.randint(1, 9)
            st.session_state.ll = ran.randint(10, 99)
            st.session_state.problem = f"{st.session_state.kk} ✖ {st.session_state.ll}"
        elif problem_type == '2けた×2けたの掛(か)け算(ざん)':
            st.session_state.mm = ran.randint(10, 99)
            st.session_state.nn = ran.randint(10, 99)
            st.session_state.problem = f"{st.session_state.mm} ✖ {st.session_state.nn}"
        elif problem_type == 'すべての掛(か)け算(ざん)':
            st.session_state.qq = ran.randint(1, 99)
            st.session_state.rr = ran.randint(1, 99)
            st.session_state.problem = f"{st.session_state.qq} ✖ {st.session_state.rr}"
        elif problem_type == '九九でできる割(わ)り算(ざん) (小数・あまりなし)':
            st.session_state.ss = ran.randint(1, 9)
            st.session_state.tt = ran.randint(1, 9)
            st.session_state.problem = f"{st.session_state.ss * st.session_state.tt} ÷ {st.session_state.tt}"
        elif problem_type == '九九でできる割(わ)り算(ざん) (小数・あまりあり)':
            st.session_state.ss = ran.randint(1, 9)
            st.session_state.tt = ran.randint(1, 9)
            st.session_state.problem = f"{st.session_state.ss * st.session_state.tt + ran.randint(1, 8)} ÷ {st.session_state.tt}"
        elif problem_type == '2けた÷1けたの割(わ)り算(ざん) (小数・あまりなし)':
            st.session_state.ss = ran.randint(10, 99)
            st.session_state.tt = ran.randint(1, 9)
            st.session_state.problem = f"{st.session_state.ss * st.session_state.tt} ÷ {st.session_state.tt}"
        elif problem_type == '2けた÷1けたの割(わ)り算(ざん) (小数・あまりあり)':
            st.session_state.ss = ran.randint(10, 99)
            st.session_state.tt = ran.randint(1, 9)
            st.session_state.problem = f"{st.session_state.ss * st.session_state.tt + ran.randint(1, 8)} ÷ {st.session_state.tt}"
        elif problem_type == '余りを出す割(わ)り算(ざん)':
            st.session_state.ss = ran.randint(10, 99)
            st.session_state.tt = ran.randint(1, 9)
            st.session_state.problem = f"{st.session_state.ss} ÷ {st.session_state.tt}"
        elif problem_type == '普通の割(わ)り算(ざん)':
            st.session_state.ss = ran.randint(1, 100)
            st.session_state.tt = ran.randint(1, 100)
            st.session_state.problem = f"{st.session_state.ss} ÷ {st.session_state.tt}"
        elif problem_type == '掛け算の穴埋め問題':
            st.session_state.aa = ran.randint(1, 9)
            st.session_state.bb = ran.randint(1, 9)
            st.session_state.cc = st.session_state.aa * st.session_state.bb
            st.session_state.problem = f"{st.session_state.aa} ✖ ___ = {st.session_state.cc}"
        elif problem_type == '割り算の穴埋め問題':
            st.session_state.aa = ran.randint(1, 9)
            st.session_state.bb = ran.randint(1, 9)
            st.session_state.cc = st.session_state.aa * st.session_state.bb
            st.session_state.problem = f"{st.session_state.cc} ÷ ___ = {st.session_state.aa}"

        st.session_state.problem_generated = True
        st.session_state.start_time = time.time()
        st.session_state.answer = ''  # 回答欄をリセット

    st.markdown(f"<h2 style='text-align: center;'>{st.session_state.problem}</h2>", unsafe_allow_html=True)

# 答えを表示する関数
def show_answer():
    if 'problem' in st.session_state:
        if problem_type == '繰(く)り上(あ)がりなしの足(た)し算(ざん)':
            st.session_state.ancera = st.session_state.aa + st.session_state.bb
            correct_answer = st.session_state.ancera
        elif problem_type == '繰(く)り上(あ)がりのある足(た)し算(ざん)':
            st.session_state.ancerb = st.session_state.cc + st.session_state.dd
            correct_answer = st.session_state.ancerb
        elif problem_type == '繰(く)り下(さ)がりなしの引(ひ)き算(ざん)':
            st.session_state.ancerc = st.session_state.ee - st.session_state.ff
            correct_answer = st.session_state.ancerc
        elif problem_type == '繰(く)り下(さ)がりのある引(ひ)き算(ざん)':
            st.session_state.ancerd = abs(st.session_state.gg - st.session_state.hh)
            correct_answer = st.session_state.ancerd
        elif problem_type == '1けた×1けたの掛(か)け算(ざん)':
            st.session_state.ancerf = st.session_state.ii * st.session_state.jj
            correct_answer = st.session_state.ancerf
        elif problem_type == '1けた×2けたの掛(か)け算(ざん)':
            st.session_state.ancerg = st.session_state.kk * st.session_state.ll
            correct_answer = st.session_state.ancerg
        elif problem_type == '2けた×2けたの掛(か)け算(ざん)':
            st.session_state.ancerh = st.session_state.mm * st.session_state.nn
            correct_answer = st.session_state.ancerh
        elif problem_type == 'すべての掛(か)け算(ざん)':
            st.session_state.ancerj = st.session_state.qq * st.session_state.rr
            correct_answer = st.session_state.ancerj
        elif problem_type == '九九でできる割(わ)り算(ざん) (小数・あまりなし)':
            correct_answer = st.session_state.ss
        elif problem_type == '九九でできる割(わ)り算(ざん) (小数・あまりあり)':
            correct_answer = round(st.session_state.ss + ran.randint(1, 8) / st.session_state.tt, 2)
        elif problem_type == '2けた÷1けたの割(わ)り算(ざん) (小数・あまりなし)':
            correct_answer = st.session_state.ss
        elif problem_type == '2けた÷1けたの割(わ)り算(ざん) (小数・あまりあり)':
            correct_answer = round(st.session_state.ss + ran.randint(1, 8) / st.session_state.tt, 2)
        elif problem_type == '余りを出す割(わ)り算(ざん)':
            correct_answer = f"{st.session_state.ss // st.session_state.tt} 余り {st.session_state.ss % st.session_state.tt}"
        elif problem_type == '普通の割(わ)り算(ざん)':
            result = st.session_state.ss / st.session_state.tt
            if result.is_integer():
                st.session_state.ancerk = int(result)
            else:
                st.session_state.ancerk = f"{round(result, 5)}..."
            correct_answer = st.session_state.ancerk
        elif problem_type == '掛け算の穴埋め問題':
            correct_answer = st.session_state.bb
        elif problem_type == '割り算の穴埋め問題':
            correct_answer = st.session_state.bb

        st.session_state.correct_answer = correct_answer

        # 答え合わせとタイムの表示
        st.markdown(f"<h2 style='text-align: center;'>{st.session_state.problem} = {st.session_state.correct_answer}</h2>", unsafe_allow_html=True)

        if st.session_state.get('time_attack', False):
            end_time = time.time()
            elapsed_time = end_time - st.session_state.start_time
            st.write(f"タイムアタックモード: {elapsed_time:.2f}秒")

            # 正解数をカウント
            if 'answer' in st.session_state:
                if str(st.session_state.answer) == str(st.session_state.correct_answer):
                    st.session_state.correct_answers += 1
                    # 正解したときにランダムなキャラクターの画像を表示
                    characters = ["pikachu_happy.png", "charmander_happy.png", "bulbasaur_happy.png"]
                    character_image = ran.choice(characters)
                    st.image(character_image, caption="正解です！", width=200)

            st.session_state.problem_generated = False

        # ユーザーの答えと正解を比較
        if 'answer' in st.session_state:
            normalized_answer = unicodedata.normalize('NFKC', st.session_state.answer)
            if str(normalized_answer) == str(st.session_state.correct_answer):
                st.success("正解です！")
                # 正解したときにランダムなキャラクターの画像を表示
                characters = ["pikachu_happy.png", "charmander_happy.png", "bulbasaur_happy.png"]
                character_image = ran.choice(characters)
                st.image(character_image, caption="正解です！", width=200)
            else:
                st.error("不正解です！")

# 回答欄を表示
answer = st.text_input('答えを入力してください', key='answer')

# 答えを表示するボタン
if st.button('こたえ'):
    show_answer()

# 外部サイトへのリンクボタン
st.write('このプログラムを作る際に関係した方々の詳しい情報(個人情報は、おおよそありません。)')
st.write('https://app-d0t-1ab0.streamlit.app')


# import streamlit as st

# st.title('計算問題アプリ')
# st.write('アップデートをしています。')
# st.write('現在使用不可')
# st.write('以下のサイトをご利用ください。')
# st.write('https://app-2024-5blue-yuuto.streamlit.app')

# st.write('このプログラムを作る際に関係した方々の詳しい情報(個人情報は、おおよそありません。)')
# st.write('https://app-d0t-1ab0.streamlit.app')
