import openai


def talk(api_key, competitive01, competitive02, competitive03):

    # 定義函式，名稱為 talk。
    # 函式的功能是透過 OpenAI 的 GPT 模型來生成競品分析，
    # 用於分析三個競品的最新資訊，包括價格、晶片、更多相關資訊，並用一句話總結他們。
    # competitive01、competitive02、competitive03 分別為三個競品的名稱。

    #設置api key
    openai.api_key = api_key

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": f"幫我分析以下競品的最新資訊:\n\n{competitive01}\n\n{competitive02}\n\n{competitive03}\n\n，\
                                                    例如價格、晶片、更多相關資訊，並用一句話總結他們"}],
        temperature=0.4,
        max_tokens=1121,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
    )

    return (response["choices"][0]["message"]["content"])
