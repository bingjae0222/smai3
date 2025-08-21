from myllm.MyApi import openAiModelArg, makeMsg, openAiModel


def test(prompt):
    promptMp3 = "prompt.mp3"
    model = openAiModel()
    response = model.audio.speech.create(
        model="tts-1",
        input="아~ 오늘 파이썬 배우기 정말 좋은 날이네~",
        voice="alloy",
        response_format="mp3",
        speed=1.1,
    )

    response.stream_to_file(promptMp3)


    modelName = "gpt-4o"
    msg = makeMsg("너는 똑똑한 한국어 선생님",prompt)
    result = openAiModelArg(modelName,msg)
    print(result)

    #결과를 음성으로 변화하시오
    resultMp3 = "result.mp3"
    response = model.audio.speech.create(
        model="tts-1",
        input="아~ 오늘 파이썬 배우기 정말 좋은 날이네~",
        voice="alloy",
        response_format="mp3",
        speed=1.1,
    )

    response.stream_to_file(resultMp3)


if __name__ == '__main__':
    prompt = "우간다의 수도는?:"
    test(prompt)
