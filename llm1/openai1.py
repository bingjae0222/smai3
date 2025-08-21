from myllm.MyApi import openAiModel, geminiModel, openAiModelArg, makeMsg


def test():

    response = openAiModelArg("gpt-4o",
                                  makeMsg("한국 선생님","이더리움 가격이 올라갈까?"))
    print(response)



if __name__ == "__main__":
    test()