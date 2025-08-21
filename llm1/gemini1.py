from myllm.MyApi import geminiModel

def test():
    model = geminiModel()
    print("\n챗봇 시작")

    chat = model.start_chat(history=[])

    while True:
        user_message = input("나: ")
        if user_message.lower() == "종료":
            break
        response = chat.send_message(user_message)
        print("Gemini:", response.text)

    print("--- 챗봇 종료 ---")
    print(chat.history)





if __name__ == '__main__':
    test()