import openai


# 定義 talk 方法，用於文案撰寫與優化
def talk(api_key, artitle, platform, better_box, style):
    """
        調用 OpenAI 的 API，生成文本並返回結果。

        Args:
            api_key(str): 個人的 API Key
            article (str): 需要優化的文章。
            platform (str): 發布平台。
            better_box (str): 修飾方式。ex:精簡文章、加長文章
            style (str): 顯示風格。ex:專業

        Returns:
            str: 優化後的文本。

---
            openai.ChatCompletion.create()：這是OpenAI API中的一個函數，

            它允許使用者使用已經訓練好的GPT模型生成自然語言文本。

            model=：這是一個參數，用於指定要使用的GPT模型。
            使用者需要提供已經在OpenAI平台上訓練好的模型的ID或是名稱。

            messages=：這是一個參數，用於指定GPT模型的輸入訊息。
            使用者需要以列表的形式提供一個或多個字典，每個字典都包含兩個鍵值對："role"和"content"。
            "role"是指定這個訊息是由使用者還是機器人所產生的，而"content"是指定這個訊息的內容。

        """

    # 設置 API Key
    openai.api_key = api_key #使用自己的

    # 使用 OpenAI API 進行對話生成，並將生成的結果返回
    response = openai.ChatCompletion.create(

        #輸入要使用的gpt模型
        model="gpt-3.5-turbo",

        #用於指定gpt模型的輸入訊息
        #role可以選擇"使用者"或是"機器人"
        #content 請gpt產生的文本
        messages=[
            {"role": "user", "content": f"請幫我優化本篇文章: {artitle}，根據以下資訊修改\
                                        1. 請使用{style}的風格呈現這篇文案，\
                                        2. 根據{platform}的風格撰寫\
                                        3. 將文案{better_box}，\
                                        綜合以上資訊產出最終的一個中文繁體的版本。"}],
        temperature=0.4,  # 生成文本的溫度，"控制模型生成多樣性"，0.0 為完全固定，1.0 為完全隨機
        max_tokens=1024,  # 產生的文本長度上限，"控制模型生成的長度"
        top_p=1,  # top-p 生成文本，控制模型生成文本的機率分布
        frequency_penalty=0.6,  # 重複文本的懲罰程度，控制模型避免重複生成相似的文本
        presence_penalty=0.6,  # 未出現過的文本的懲罰程度，控制模型傾向於生成已經出現過的文本
    )

    return (response["choices"][0]["message"]["content"])
