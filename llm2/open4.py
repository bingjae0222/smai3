from myllm.MyApi import openAiModelArg, makeMsg, openAiModel



def test(prompt):
    openModel = openAiModel()
    response = openModel.images.generate(

        model="dall-e-3",

        prompt="a white siamese cat and borwn dog",

        size="1024x1024",

        quality="standard",

        n=1,

    )
    image_url = response.data[0].url

    print(image_url)


if __name__ == '__main__':
    prompt = "갈색 강아지 흰 고양이 사진 만들어:"
    test(prompt)
