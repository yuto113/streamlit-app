import streamlit as st
import sqlite3
from datetime import datetime
import hashlib # パスワードハッシュ化のため追加

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

# --- パスワード関連 ---
def hash_password(password):
    """パスワードをSHA-256でハッシュ化する"""
    return hashlib.sha256(password.encode()).hexdigest()

# ユーザー名とハッシュ化されたパスワードの辞書
# 注意: このサンプルではパスワードをコード内に直接記述していますが、
# 本番環境では環境変数や外部設定ファイル、セキュアなデータベースなどを使用し、
# ユーザー登録時にハッシュ化して保存するのが一般的です。
# ここでは、事前に各ユーザーのパスワードをハッシュ化した値を設定します。
# 例: "ゆうと" のパスワードが "yutopass" の場合、hash_password("yutopass") の結果を格納
USER_PASSWORDS = {
    "初期設定": hash_password("123"),
    "ゆうと": hash_password("yutopass"),
    "ゆずの": hash_password("yuzunopass"),
    "そら": hash_password("sorapass"),
    "くるみ": hash_password("kurumipass"),
    "りさ": hash_password("risapass"),
    "りな": hash_password("rinapass"),
    "ひかり": hash_password("hikaripass"),
    "みお": hash_password("miopass"),
    'みつき': hash_password("mitsukipass"),
    'その': hash_password("sonopass"),
    'ひいろ': hash_password("hiropass"),
    'じゅんや': hash_password("junyapass"),
    'なおき': hash_password("naokipass"),
    'みと': hash_password("mitopass"),
    'さ・あや': hash_password("ayapass"), 
    'すずか': hash_password("suzukapass"),
    'ゆうすけ': hash_password("yusukepass"),
    'りせ': hash_password("risepass")
}

def verify_password(username, provided_password):
    """提供されたパスワードが保存されているハッシュと一致するか検証する"""
    if username not in USER_PASSWORDS:
        # ユーザーリストには存在するが、パスワード辞書にない場合のエラーハンドリング
        st.error(f"ユーザー '{username}' のパスワード設定が見つかりません。管理者に連絡してください。")
        return False
    stored_password_hash = USER_PASSWORDS[username]
    return stored_password_hash == hash_password(provided_password)

# --- アプリのユーザーリスト ---
APP_USERS = ["初期設定","ゆうと", "ゆずの", "そら", "くるみ", "りさ", "りな","ひかり", "みお",'みつき','その','ひいろ','じゅんや','なおき','みと','さ・あや','すずか','ゆうすけ','りせ']

# --- Streamlit アプリ ---
init_db() # データベースの初期化

st.title("アプリ内メッセージングシステム")

# セッションステートの初期化
if 'authenticated_user' not in st.session_state:
    st.session_state.authenticated_user = None
if 'selected_user_for_login' not in st.session_state:
    # 初期選択ユーザーをAPP_USERSの先頭に設定
    st.session_state.selected_user_for_login = APP_USERS[0] if APP_USERS else None

# --- ユーザー認証 ---
st.sidebar.header("ユーザー認証")

# ユーザー選択プルダウン
# `index` の計算でエラーが起きないように、`selected_user_for_login` が `APP_USERS` に存在するか確認
try:
    # st.session_state.selected_user_for_login が None の場合も考慮
    default_index = APP_USERS.index(st.session_state.selected_user_for_login) if st.session_state.selected_user_for_login in APP_USERS else 0
except ValueError:
    default_index = 0 # 万が一見つからなければ最初のユーザー

selected_user = st.sidebar.selectbox(
    "ユーザーを選択してください:",
    APP_USERS,
    index=default_index,
    key="user_selector_dropdown" # 他のウィジェットとキーが衝突しないように変更
)

# 選択されたユーザーをセッションに保存
st.session_state.selected_user_for_login = selected_user

# ユーザーが切り替わった場合、またはまだ認証されていない場合
if st.session_state.authenticated_user != selected_user:
    # 以前の認証情報をクリア
    st.session_state.authenticated_user = None

    st.sidebar.subheader(f"ログイン: {selected_user}")
    # Streamlitのキーとして使用するために、ユーザー名から特殊文字を除去または置換
    safe_username_key = "".join(c if c.isalnum() else "_" for c in selected_user)
    password_key = f"password_input_{safe_username_key}"
    password = st.sidebar.text_input("パスワード:", type="password", key=password_key)
    
    login_button_key = f"login_button_{safe_username_key}"
    if st.sidebar.button("ログイン", key=login_button_key):
        if verify_password(selected_user, password):
            st.session_state.authenticated_user = selected_user
            st.sidebar.success(f"{selected_user}としてログインしました！")
            st.rerun() # UIを更新してメインコンテンツを表示
        else:
            st.sidebar.error("パスワードが間違っています。")
    # メインコンテンツは表示せず、ログインを促すメッセージを表示
    st.info("サイドバーからログインしてください。")

elif st.session_state.authenticated_user is not None:
    # 認証済みの場合
    current_user = st.session_state.authenticated_user
    st.sidebar.write(f"ログイン中: **{current_user}**")

    def logout():
        st.session_state.authenticated_user = None
        # selected_user_for_login は現在の選択を保持
        st.rerun()

    st.sidebar.button("ログアウト", on_click=logout)

    # --- メインコンテンツ (メッセージ機能) ---
    tab1, tab2 = st.tabs(["メッセージ作成", "受信箱"])

    with tab1:
        st.header(f"メッセージ作成 (from: {current_user})")
        
        receiver_options = [user for user in APP_USERS if user != current_user]
        if not receiver_options:
            st.warning("送信できる他のユーザーがいません。")
        else:
            # ウィジェットキーの重複を避けるため、認証済みユーザーに依存するキーにする
            safe_current_user_key = "".join(c if c.isalnum() else "_" for c in current_user)
            receiver_key = f"receiver_select_{safe_current_user_key}"
            subject_key = f"subject_input_{safe_current_user_key}"
            body_key = f"body_input_{safe_current_user_key}"
            send_button_key = f"send_button_{safe_current_user_key}"

            receiver = st.selectbox("宛先:", receiver_options, key=receiver_key)
            subject = st.text_input("件名:", key=subject_key)
            body = st.text_area("本文:", key=body_key)

            if st.button("送信する", key=send_button_key):
                if receiver and subject and body:
                    add_message(current_user, receiver, subject, body)
                    st.success(f"{receiver} さんにメッセージを送信しました。")
                    # 必要であれば、送信後にフォームをクリア
                    # st.session_state[subject_key] = ""
                    # st.session_state[body_key] = ""
                    # st.rerun()
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
                try:
                    timestamp_dt = datetime.strptime(timestamp_str, '%Y-%m-%d %H:%M:%S')
                    formatted_timestamp = timestamp_dt.strftime('%Y年%m月%d日 %H:%M')
                except ValueError:
                    formatted_timestamp = timestamp_str 

                with st.expander(f"From: {sender} - Subject: {subject} ({formatted_timestamp})"):
                    st.write(body)
                if i < len(received_messages) - 1:
                    st.markdown("---")
else:
    # 初期状態 (どのユーザーも選択/認証されていない場合など)
    st.info("サイドバーからユーザーを選択し、ログインしてください。")
