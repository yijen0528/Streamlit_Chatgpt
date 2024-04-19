# 導入必要的 library
import openai
import streamlit as st
from functions import talk

# 定義主函數


def main():

    # 在 Streamlit 應用中添加子標題
    st.subheader("AI 文案練成神器")

    # 創建文案輸入區域，請求用戶輸入文案
    msg_ar = st.text_area("請輸入您的文案",
                          value="Y2K風格的手機")

    # 創建下拉列表，請求用戶指定要在哪個社群平台上發布
    platform = st.selectbox(
        '請問您要發在哪個社群平台？',
        ('Facebook',
         'Instagram',
         'Twitter',
         'Linkedln'
         ))

    # 創建下拉列表，請求用戶選擇如何優化文案
    better_box = st.selectbox(
        '請問您要想要如何優化本篇文案？',
        ('加長',
         '精簡',
         '換句話說'
         ))

    # 創建多選框，請求用戶選擇要呈現的風格
    style = st.multiselect(
        '您希望這篇文案呈現的風格是什麼？(可多選)',
        ['輕鬆活潑',
         '正式嚴肅',
         '有說服力'])

    if st.button("文案產生"):

        api_key = ""  # 請輸入您的 API KEY

        # 使用 talk() 函數產生文案
        response = talk(api_key, msg_ar, platform, better_box, style)

        # 在 Streamlit 中顯示文案結果 (st.text_area)
        results = st.text_area('文案結果', response, height=300)


if __name__ == '__main__':
    main()
