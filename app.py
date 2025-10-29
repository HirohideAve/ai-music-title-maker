import streamlit as st

st.title("曲名プロンプト生成アプリ")

# 説明文を追加
st.markdown("""
ChatGPTなどAIに食わせるプロンプト文章を生成するだけの簡単なフォームです。  
DTMerの皆様にもご提供いたします。よければご利用ください。  
**Hirohide AveがGitHubに公開・作成しています。**
""")

#ホームページのリンクを追加
st.markdown('<a href="https://sites.google.com/view/sysxtem" target="_blank-color:#4CAF50;color:white;border:none;padding:10px 20px;">私のホームページ（sysXtem)</button></a>', unsafe_allow_html=True)


# 入力フォーム
key = st.text_input("調性（例：長調、短調）")
instruments = st.text_input("使用楽器（例：ピアノ、ストリングス）")
tempo = st.text_input("テンポ感（例：ゆったり、速い）")
mood = st.text_input("雰囲気（例：哀愁、幻想的）")
background = st.text_input("作曲背景（例：亡き人への追悼）")
purpose = st.text_input("使用目的（例：映像作品のエンディング）")

# ボタンを押すとプロンプト生成
if st.button("プロンプトを生成"):
    prompt = f"#曲名生成 #{key} #{instruments} #{tempo} #{mood} #{background} #{purpose} この特徴に合う印象的な曲名を提案してください。"
    st.success("生成されたプロンプト：")
    st.code(prompt, language="markdown")
