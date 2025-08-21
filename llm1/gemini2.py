import google.generativeai as genai
from myllm.MyApi import geminiModel
from PIL import Image


def test():
    img = Image.open("img/aa.png")
    model = geminiModel()
    response = model.generate_content(
        ["제시한 이미지를 3문장 이내에 한국어로 설몀",
         img]
    )
    print(response.text)

if __name__ == '__main__':
    test()
