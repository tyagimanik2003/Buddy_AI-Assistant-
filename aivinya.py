import requests
import json
import pyttsx3

speech = pyttsx3.init()

url = "https://api.aivinya.education/api/public/aivachat"
while True:
    print("Open AI feedback: ")
    x="alai_darwaza"
    aitext=f"Tell me about {x} in 30 words"
    payload = json.dumps({
    "text": aitext
    })
    headers = {
    'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    answer=json.loads(response.text)
    answer = answer["res"]
    # # tr=a[a.find("n")+3:]
    # # a1=(tr[:tr.find('"')-1])
    print(answer)
    speech.say(answer)
    speech.runAndWait()


# print("OpenAI response is: ")
# a="alai_darwaza"
# payload = json.dumps({
# "text": f"tell me about {a} ?"
# })
# headers = {
# 'Content-Type': 'application/json'
# }
# response = requests.request("POST", url, headers=headers, data=payload)            
# try:
#     result=json.loads(response.text)
# except json.JSONDecodeError as e:
#     print(f"Error decoding response: {e}")
#     result = {}
# answer=result["res"]