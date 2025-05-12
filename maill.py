import streamlit as st
import sqlite3
from datetime import datetime

# --- データベース関連の初期設定 ---
DB_NAME = "app_messages.db"

def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    # messages テーブル: 送信者、受信者、件名、本文、タイムスタンプ
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS messages (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            sender TEXT NOT NULL,
            receiver TEXT NOT NULL,
            subject TEXT NOT NULL,
            body TEXT NOT NULL,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    # users テーブル (今回は簡易的に固定リストを使用するため、DBには作成しない)
    # 本格的なアプリではユーザー管理もDBで行う
    conn.commit()
    conn.close()

def add_message(sender, receiver, subject, body):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO messages (sender, receiver, subject, body)
        VALUES (?, ?, ?, ?)
    ''', (sender, receiver, subject, body))
    conn.commit()
    conn.close()

def get_received_messages(receiver_username):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        SELECT sender, subject, body, timestamp FROM messages
        WHERE receiver = ? ORDER BY timestamp DESC
    ''', (receiver_username,))
    messages = cursor.fetchall()
    conn.close()
    return messages

# --- アプリのユーザー (簡易的に固定) ---
APP_USERS = ["初期設定","ゆうと", "ゆずの", "そら", "くるみ", "りさ", "りな","ひかり", "みお"]

# --- Streamlit アプリ ---
init_db() # データベースの初期化

st.title("アプリ内メッセージングシステム")

# ユーザー選択 (簡易的なログインの代わり)
st.sidebar.header("ユーザー選択")
current_user = st.sidebar.selectbox("ログインユーザーを選択してください:", APP_USERS)
st.sidebar.write(f"現在のユーザー: **{current_user}**")

# タブで機能を分ける
tab1, tab2 = st.tabs(["メッセージ作成", "受信箱"])

with tab1:
    st.header(f"メッセージ作成 (from: {current_user})")
    
    # 送信先のユーザーリスト (自分自身は除く)
    receiver_options = [user for user in APP_USERS if user != current_user]
    if not receiver_options:
        st.warning("送信できる他のユーザーがいません。")
    else:
        receiver = st.selectbox("宛先:", receiver_options)
        subject = st.text_input("件名:")
        body = st.text_area("本文:")

        if st.button("送信する"):
            if receiver and subject and body:
                add_message(current_user, receiver, subject, body)
                st.success(f"{receiver} さんにメッセージを送信しました。")
            else:
                st.error("宛先、件名、本文をすべて入力してください。")

with tab2:
    st.header(f"受信箱 ({current_user})")
    
    received_messages = get_received_messages(current_user)
    
    if not received_messages:
        st.info("新しいメッセージはありません。")
    else:
        for i, msg in enumerate(received_messages):
            sender, subject, body, timestamp_str = msg
            # タイムスタンプのフォーマットを調整
            try:
                timestamp_dt = datetime.strptime(timestamp_str, '%Y-%m-%d %H:%M:%S')
                formatted_timestamp = timestamp_dt.strftime('%Y年%m月%d日 %H:%M')
            except ValueError:
                formatted_timestamp = timestamp_str # パース失敗時はそのまま表示

            with st.expander(f"From: {sender} - Subject: {subject} ({formatted_timestamp})"):
                st.write(body)
            if i < len(received_messages) - 1: # 最後のメッセージ以外は区切り線
                st.markdown("---")

