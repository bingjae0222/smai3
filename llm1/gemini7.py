import requests
from myllm.MyApi import geminiModel
from io import BytesIO
from PIL import Image

def test(prompt,img):
    model = geminiModel()
    response = model.generate_content([prompt,img])
    print(response.text)


if __name__ == '__main__':
    image_url = "https://images.unsplash.com/photo-1624552184280-9e9631bbeee9?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=M3wxMTc3M3wwfDF8c2VhcmNofDJ8fGNva2UlMjB8ZW58MHx8fHwxNjk1MjE3NjAwfDA&ixlib=rb-4.0.3&q=80&w=1200"
    respose_image = requests.get(image_url)
    img = Image.open(BytesIO(respose_image.content))
    prompt = "이 이미지의 영양 성분,당 함류,칼로리알려줘"
    test(prompt,img)