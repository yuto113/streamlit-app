import streamlit as st
import datetime

# クイズデータ
quiz_data = {
    "科学": [
        {"question": "水の化学式は何ですか？", "answer": "H2O", "meaning": "水は2つの水素原子と1つの酸素原子で構成されています。"},
        {"question": "地球の重力加速度は約何m/s²ですか？", "answer": "9.8", "meaning": "地球の重力加速度は約9.8m/s²です。"},
        {"question": "光の速さは約何km/sですか？", "answer": "300,000", "meaning": "光の速さは約300,000km/sです。"},
        {"question": "酸素の化学記号は何ですか？", "answer": "O", "meaning": "酸素の化学記号はOです。"},
        {"question": "太陽系で最も大きな惑星は何ですか？", "answer": "木星", "meaning": "木星は太陽系で最も大きな惑星です。"},
        {"question": "水は何度で沸騰しますか？", "answer": "100度", "meaning": "水は標準気圧下で100度で沸騰します。"},
        {"question": "地球の表面積の約何％が水で覆われていますか？", "answer": "71%", "meaning": "地球の表面積の約71%が水で覆われています。"},
        {"question": "最も軽い元素は何ですか？", "answer": "水素", "meaning": "水素は最も軽い元素です。"},
        {"question": "DNAの正式名称は何ですか？", "answer": "デオキシリボ核酸", "meaning": "DNAはデオキシリボ核酸の略です。"},
        {"question": "太陽のエネルギー源は何ですか？", "answer": "核融合", "meaning": "太陽のエネルギー源は水素の核融合反応です。"},
        {"question": "地球の大気の主成分は何ですか？", "answer": "窒素", "meaning": "地球の大気の約78%は窒素です。"},
        {"question": "最も硬い天然物質は何ですか？", "answer": "ダイヤモンド", "meaning": "ダイヤモンドは最も硬い天然物質です。"},
        {"question": "ニュートンが発見した法則は何ですか？", "answer": "運動の法則", "meaning": "ニュートンは運動の法則を発見しました。"},
        {"question": "電流の単位は何ですか？", "answer": "アンペア", "meaning": "電流の単位はアンペアです。"},
        {"question": "最も多い元素は何ですか？", "answer": "水素", "meaning": "宇宙で最も多い元素は水素です。"},
        {"question": "地球の年齢は約何年ですか？", "answer": "46億年", "meaning": "地球の年齢は約46億年です。"},
        {"question": "最も高い山は何ですか？", "answer": "エベレスト", "meaning": "エベレストは地球で最も高い山です。"},
        {"question": "最も深い海溝は何ですか？", "answer": "マリアナ海溝", "meaning": "マリアナ海溝は地球で最も深い海溝です。"},
        {"question": "光が1秒間に進む距離は何kmですか？", "answer": "約30万km", "meaning": "光は1秒間に約30万km進みます。"},
        {"question": "地球の自転周期は約何時間ですか？", "answer": "24時間", "meaning": "地球の自転周期は約24時間です。"},
        {"question": "最も小さい惑星は何ですか？", "answer": "水星", "meaning": "水星は太陽系で最も小さい惑星です。"},
        {"question": "最も重い元素は何ですか？", "answer": "ウラン", "meaning": "ウランは自然界で最も重い元素です。"},
        {"question": "地球の核の主成分は何ですか？", "answer": "鉄", "meaning": "地球の核の主成分は鉄です。"},
        {"question": "最も近い恒星は何ですか？", "answer": "太陽", "meaning": "太陽は地球に最も近い恒星です。"},
        {"question": "地球の衛星は何ですか？", "answer": "月", "meaning": "月は地球の唯一の衛星です。"},
        {"question": "最も高い気温が記録された場所はどこですか？", "answer": "デスバレー", "meaning": "デスバレーは最も高い気温が記録された場所です。"},
        {"question": "最も低い気温が記録された場所はどこですか？", "answer": "南極", "meaning": "南極は最も低い気温が記録された場所です。"},
        {"question": "地球の表面積は約何平方キロメートルですか？", "answer": "5億1千万平方キロメートル", "meaning": "地球の表面積は約5億1千万平方キロメートルです。"},
        {"question": "最も古い化石は何ですか？", "answer": "ストロマトライト", "meaning": "ストロマトライトは最も古い化石です。"},
        {"question": "最も長い川は何ですか？", "answer": "ナイル川", "meaning": "ナイル川は地球で最も長い川です。"},
        {"question": "最も大きな砂漠は何ですか？", "answer": "サハラ砂漠", "meaning": "サハラ砂漠は地球で最も大きな砂漠です。"},
        {"question": "最も高い滝は何ですか？", "answer": "エンジェルフォール", "meaning": "エンジェルフォールは地球で最も高い滝です。"},
        {"question": "最も大きな湖は何ですか？", "answer": "カスピ海", "meaning": "カスピ海は地球で最も大きな湖です。"}
    ],
    "歴史": [
        {"question": "日本の初代首相は誰ですか？", "answer": "伊藤博文", "meaning": "伊藤博文は日本の初代内閣総理大臣です。"},
        {"question": "第二次世界大戦は何年に終わりましたか？", "answer": "1945", "meaning": "第二次世界大戦は1945年に終結しました。"},
        {"question": "フランス革命が始まった年は何年ですか？", "answer": "1789", "meaning": "フランス革命は1789年に始まりました。"},
        {"question": "アメリカ独立宣言が採択された年は何年ですか？", "answer": "1776", "meaning": "アメリカ独立宣言は1776年に採択されました。"},
        {"question": "明治維新が始まった年は何年ですか？", "answer": "1868", "meaning": "明治維新は1868年に始まりました。"},
        {"question": "ローマ帝国が滅亡した年は何年ですか？", "answer": "476年", "meaning": "西ローマ帝国は476年に滅亡しました。"},
        {"question": "ナポレオンが皇帝に即位した年は何年ですか？", "answer": "1804年", "meaning": "ナポレオンは1804年に皇帝に即位しました。"},
        {"question": "第一次世界大戦が始まった年は何年ですか？", "answer": "1914年", "meaning": "第一次世界大戦は1914年に始まりました。"},
        {"question": "ベルリンの壁が崩壊した年は何年ですか？", "answer": "1989年", "meaning": "ベルリンの壁は1989年に崩壊しました。"},
        {"question": "日本が鎖国を始めた年は何年ですか？", "answer": "1639年", "meaning": "日本は1639年に鎖国を始めました。"},
        {"question": "アメリカの初代大統領は誰ですか？", "answer": "ジョージ・ワシントン", "meaning": "ジョージ・ワシントンはアメリカの初代大統領です。"},
        {"question": "中国の秦の始皇帝が即位した年は何年ですか？", "answer": "紀元前221年", "meaning": "秦の始皇帝は紀元前221年に即位しました。"},
        {"question": "ペリーが日本に来航した年は何年ですか？", "answer": "1853年", "meaning": "ペリーは1853年に日本に来航しました。"},
        {"question": "イギリスの産業革命が始まったのは何世紀ですか？", "answer": "18世紀", "meaning": "イギリスの産業革命は18世紀に始まりました。"},
        {"question": "大化の改新が行われた年は何年ですか？", "answer": "645年", "meaning": "大化の改新は645年に行われました。"},
        {"question": "最初のオリンピックが開催された年は何年ですか？", "answer": "紀元前776年", "meaning": "最初のオリンピックは紀元前776年に開催されました。"},
        {"question": "最初の世界地図を作成したのは誰ですか？", "answer": "エラトステネス", "meaning": "エラトステネスは最初の世界地図を作成しました。"},
        {"question": "最初の印刷機を発明したのは誰ですか？", "answer": "グーテンベルク", "meaning": "グーテンベルクは最初の印刷機を発明しました。"},
        {"question": "最初の月面着陸は何年ですか？", "answer": "1969年", "meaning": "アポロ11号が1969年に月面着陸しました。"},
        {"question": "最初の電話を発明したのは誰ですか？", "answer": "アレクサンダー・グラハム・ベル", "meaning": "ベルは最初の電話を発明しました。"},
        {"question": "最初の飛行機を発明したのは誰ですか？", "answer": "ライト兄弟", "meaning": "ライト兄弟は最初の飛行機を発明しました。"},
        {"question": "最初のコンピュータを発明したのは誰ですか？", "answer": "チャールズ・バベッジ", "meaning": "バベッジは最初のコンピュータを発明しました。"},
        {"question": "最初の人工衛星は何ですか？", "answer": "スプートニク1号", "meaning": "スプートニク1号は最初の人工衛星です。"},
        {"question": "最初の核爆弾が使用されたのは何年ですか？", "answer": "1945年", "meaning": "最初の核爆弾は1945年に使用されました。"},
        {"question": "最初のインターネットが開発されたのは何年ですか？", "answer": "1969年", "meaning": "インターネットは1969年に開発されました。"}
    ],
    "スポーツ": [
        {"question": "オリンピックは何年ごとに開催されますか？", "answer": "4年", "meaning": "オリンピックは4年ごとに開催される国際的なスポーツイベントです。"},
        {"question": "サッカーで1チームの選手数は何人ですか？", "answer": "11人", "meaning": "サッカーでは1チーム11人で試合を行います。"},
        {"question": "テニスの試合で最初にサーブを打つのはどちらのプレイヤーですか？", "answer": "任意", "meaning": "テニスではサーブを打つプレイヤーはコイントスで決まります。"},
        {"question": "バスケットボールの試合時間は通常何分ですか？", "answer": "48分", "meaning": "NBAの試合時間は通常48分です。"},
        {"question": "野球で1試合のイニング数は通常何回ですか？", "answer": "9回", "meaning": "野球では通常9回で試合が行われます。"},
        {"question": "マラソンの距離は何kmですか？", "answer": "42.195km", "meaning": "マラソンの距離は42.195kmです。"},
        {"question": "野球で1イニングは何アウトで終了しますか？", "answer": "3アウト", "meaning": "野球では1イニングは3アウトで終了します。"},
        {"question": "サッカーの試合時間は通常何分ですか？", "answer": "90分", "meaning": "サッカーの試合時間は通常90分です。"},
        {"question": "オリンピックのシンボルマークは何本の輪で構成されていますか？", "answer": "5本", "meaning": "オリンピックのシンボルマークは5本の輪で構成されています。"},
        {"question": "バレーボールの1チームの選手数は何人ですか？", "answer": "6人", "meaning": "バレーボールでは1チーム6人で試合を行います。"},
        {"question": "テニスのグランドスラム大会は年間何回開催されますか？", "answer": "4回", "meaning": "テニスのグランドスラム大会は年間4回開催されます。"},
        {"question": "ラグビーの試合時間は通常何分ですか？", "answer": "80分", "meaning": "ラグビーの試合時間は通常80分です。"},
        {"question": "卓球の試合で1ゲームは何点先取で勝利ですか？", "answer": "11点", "meaning": "卓球では1ゲーム11点先取で勝利です。"},
        {"question": "ゴルフで1ラウンドは通常何ホールですか？", "answer": "18ホール", "meaning": "ゴルフでは1ラウンドは通常18ホールです。"},
        {"question": "スキーのジャンプ競技で使用する板の長さは通常何cm以上ですか？", "answer": "240cm", "meaning": "スキーのジャンプ競技で使用する板の長さは通常240cm以上です。"},
        {"question": "最も多くのゴールを決めたサッカー選手は誰ですか？", "answer": "ペレ", "meaning": "ペレは最も多くのゴールを決めたサッカー選手です。"},
        {"question": "最も多くの金メダルを獲得したオリンピック選手は誰ですか？", "answer": "マイケル・フェルプス", "meaning": "フェルプスは最も多くの金メダルを獲得しました。"},
        {"question": "最も速い100m走の記録を持つ選手は誰ですか？", "answer": "ウサイン・ボルト", "meaning": "ボルトは最も速い100m走の記録を持っています。"},
        {"question": "最も多くのホームランを打った野球選手は誰ですか？", "answer": "バリー・ボンズ", "meaning": "ボンズは最も多くのホームランを打ちました。"},
        {"question": "最も多くのグランドスラムタイトルを獲得したテニス選手は誰ですか？", "answer": "ノバク・ジョコビッチ", "meaning": "ジョコビッチは最も多くのグランドスラムタイトルを獲得しました。"}
    ]
}

# 2025年の祝日リスト（日本の祝日）
holidays = [
    datetime.date(2025, 1, 1),   # 元日
    datetime.date(2025, 1, 13),  # 成人の日
    datetime.date(2025, 2, 11),  # 建国記念の日
    datetime.date(2025, 3, 20),  # 春分の日
    datetime.date(2025, 4, 29),  # 昭和の日
    datetime.date(2025, 5, 3),   # 憲法記念日
    datetime.date(2025, 5, 4),   # みどりの日
    datetime.date(2025, 5, 5),   # 子供の日
    datetime.date(2025, 7, 21),  # 海の日
    datetime.date(2025, 8, 11),  # 山の日
    datetime.date(2025, 9, 15),  # 敬老の日
    datetime.date(2025, 9, 23),  # 秋分の日
    datetime.date(2025, 10, 13), # スポーツの日
    datetime.date(2025, 11, 3),  # 文化の日
    datetime.date(2025, 11, 23), # 勤労感謝の日
    datetime.date(2025, 12, 23)  # 天皇誕生日
]

# 土日・祝日を除いた営業日を計算
def get_next_business_day(start_date, offset):
    current_date = start_date
    business_days = 0

    while business_days < offset:
        current_date += datetime.timedelta(days=1)
        # 平日かつ祝日でない場合のみカウント
        if current_date.weekday() < 5 and current_date not in holidays:
            business_days += 1

    return current_date

# 日付を計算してすべてのクイズを表示
def display_all_quizzes(genre):
    if genre == "科学":
        start_date = datetime.date(2025, 4, 1)  # 科学のクイズ1を2025年4月1日から開始
    elif genre == "歴史":
        start_date = get_next_business_day(datetime.date(2025, 4, 1), 33)  # 歴史は34番目から続ける
    elif genre == "スポーツ":
        start_date = get_next_business_day(datetime.date(2025, 4, 1), 33 + len(quiz_data["歴史"]))  # スポーツは歴史の続きから

    quizzes = quiz_data[genre]

    st.subheader(f"{genre}のクイズ一覧")
    for i, quiz in enumerate(quizzes):
        quiz_date = get_next_business_day(start_date, i)
        st.write(f"クイズ {i + 1} ({quiz_date.month}月{quiz_date.day}日): {quiz['question']}")
        st.write(f"答え: {quiz['answer']}")
        st.write(f"意味: {quiz['meaning']}")
        st.write("---")  # 区切り線

# Streamlitアプリ
st.title("ジャンルごとのクイズ一覧")

# ジャンル選択
genre = st.selectbox("ジャンルを選んでください", list(quiz_data.keys()))

# すべてのクイズを表示
display_all_quizzes(genre)
