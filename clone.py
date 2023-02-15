import openai
import urllib.request
import time

def connect(host='https://openai.com'):
    try:
        urllib.request.urlopen(host) #Python 3.x
        return True
    except:
        return False

def initial_system():
    if connect():
        print("Connecting to system....")
        print("\r3",end='')
        time.sleep(1)
        print("\r2",end='')
        time.sleep(1)
        print("\r1",end='')
        time.sleep(1)
        print("\rConnected\n")
    else:
        print("No internet")
        exit()
        
count=0
initial_system()
openai.api_key="Enter generated API Key here"
model_engine = "text-davinci-002"
while(True):
    choice = int(input("1. Start\n2. Exit\nOption : "))
    if(choice==1):
        prompt = str(input("Enter prompt here : "))
        completion = openai.Completion.create(
            engine=model_engine,
            prompt=prompt,
            max_tokens = 2048,
            n=1,
            stop=None,
            temperature=0.7,
        )
        response = completion.choices[0].text
        print(response)
    elif(choice==2):
        print("\nWe are under testing thankyou for choosing us!")
        break
    else:
        print("\nEnter valid input\n")
