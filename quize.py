import streamlit as st
import openai

# OpenAI APIキーの設定
openai.api_key = "your_openai_api_key"  # ここにAPIキーを入力してください

# クイズデータ
quiz_data = {
    "科学": [
        {"question": "水の化学式は何ですか？", "answer": "H2O", "meaning": "水は2つの水素原子と1つの酸素原子で構成されています。"},
        {"question": "地球の重力加速度は約何m/s²ですか？", "answer": "9.8", "meaning": "地球の重力加速度は約9.8m/s²です。"}
    ],
    "歴史": [
        {"question": "日本の初代首相は誰ですか？", "answer": "伊藤博文", "meaning": "伊藤博文は日本の初代内閣総理大臣です。"},
        {"question": "第二次世界大戦は何年に終わりましたか？", "answer": "1945", "meaning": "第二次世界大戦は1945年に終結しました。"}
    ],
    "スポーツ": [
        {"question": "オリンピックは何年ごとに開催されますか？", "answer": "4年", "meaning": "オリンピックは4年ごとに開催される国際的なスポーツイベントです。"},
        {"question": "サッカーで1チームの選手数は何人ですか？", "answer": "11人", "meaning": "サッカーでは1チーム11人で試合を行います。"}
    ]
}

# Streamlitアプリ
st.title("ジャンルごとのクイズ")

# ジャンル選択
genre = st.selectbox("ジャンルを選んでください", list(quiz_data.keys()) + ["AIで生成"])

if genre == "AIで生成":
    # ユーザー入力
    user_input = st.text_input("クイズのジャンルやキーワードを入力してください")
    if st.button("クイズを生成"):
        if user_input:
            # OpenAI APIを使用してクイズを生成
            response = openai.Completion.create(
                engine="text-davinci-003",
                prompt=f"以下のキーワードに基づいてクイズを作成してください: {user_input}\n"
                       f"フォーマット: question, answer, meaning",
                max_tokens=150
            )
            generated_quiz = response.choices[0].text.strip().split("\n")
            for i, line in enumerate(generated_quiz):
                st.subheader(f"クイズ {i + 1}: {line.split(',')[0]}")
                if st.button(f"答えを見る ({i + 1})"):
                    st.write(f"答え: {line.split(',')[1]}")
                    st.write(f"意味: {line.split(',')[2]}")
        else:
            st.warning("キーワードを入力してください！")
else:
    # 選択されたジャンルのクイズを取得
    quizzes = quiz_data[genre]

    # クイズを表示
    for i, quiz in enumerate(quizzes):
        st.subheader(f"クイズ {i + 1}: {quiz['question']}")
        if st.button(f"答えを見る ({i + 1})"):
            st.write(f"答え: {quiz['answer']}")
            st.write(f"意味: {quiz['meaning']}")
