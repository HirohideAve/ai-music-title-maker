import streamlit as st
import openai
import os
# OpenAI APIキー設定（環境変数で管理推奨）
openai.api_key = os.getenv("OPENAI_API_KEY")

st.title("曲名プロンプト生成アプリ")
st.markdown("""
ChatGPTなどAIに食わせるプロンプト文章を生成するだけの簡単なフォームです。  
DTMerの皆様にもご提供いたします。よければご利用ください。  
**Hirohide AveがGitHubに公開・作成しています。**
""")

# 入力フォーム
key = st.text_input("調性（例：長調、短調）")
instruments = st.text_input("使用楽器（例：ピアノ、ストリングス）")
tempo = st.text_input("テンポ感（例：ゆったり、速い）")
mood = st.text_input("雰囲気（例：哀愁、幻想的）")
background = st.text_input("作曲背景（例：亡き人への追悼）")
purpose = st.text_input("使用目的（例：映像作品のエンディング）")

if st.button("プロンプトを生成"):
    prompt = f"#曲名生成 #{key} #{instruments} #{tempo} #{mood} #{background} #{purpose} この特徴に合う印象的な曲名を提案してください。"
    st.success("生成されたプロンプト：")
    st.code(prompt, language="markdown")

    # AIに曲名を生成させる
    with st.spinner("AIが曲名を考えています..."):
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "あなたは音楽のタイトルを考える専門家です。"},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7
        )
        ai_title = response.choices[0].message["content"]
        st.subheader("AIが提案した曲名")
        st.write(ai_title)
