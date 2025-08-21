from myllm.MyApi import geminiModel

def test(prompt):
    model = geminiModel()
    response = model.generate_content(prompt)
    print(response.text)
if __name__ == '__main__':
    code_prompt = "python으로 피보나치 수열을 계산하는 함수 작성해"
    test(code_prompt)