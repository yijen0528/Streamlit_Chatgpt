import openai
import streamlit as st
from functions import talk


def main():

    # 在畫面上顯示一個子標題
    st.subheader("競品分析")

    # 使用者可以在畫面左側的側邊欄輸入競品1、競品2和競品3 (st.sidebar.text_input)
    msg_ar001 = st.sidebar.text_input(
        "請輸入競品1",
        "Apple")

    msg_ar002 = st.sidebar.text_input(
        "請輸入競品2",
        "Samsung")

    msg_ar003 = st.sidebar.text_input(
        "請輸入競品3",
        "HTC")

    # 使用者按下「開始分析」按鈕後執行競品分析
    if st.sidebar.button("開始分析"):

        # 輸入OpenAI API的API KEY
        api_key = ""

        # 執行競品分析，並獲得結果
        response = talk(api_key, msg_ar001, msg_ar002, msg_ar003)

        # 將分析結果顯示在畫面上
        msg_ar = st.text_area('分析結果', response, height=300)


if __name__ == '__main__':
    main()
