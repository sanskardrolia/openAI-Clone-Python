import openai
import time

def system_initialized():
    print("Initializing... system")
    print("\r3",end='')
    time.sleep(1)
    print("\r2",end='')
    time.sleep(1)
    print("\r1",end='')
    time.sleep(1)
    print("\rSystem Intialized\n")

system_initialized()
openai.api_key="Put you API key from openai website"
model_engine = "text-davinci-002"
while(True):
    choice = int(input("1. Start\n2. Exit\nOption : "))
    if(choice==1):
        prompt = str(input("Enter prompt here : "))
        completion = openai.Completion.create(
            engine=model_engine,
            prompt=prompt,
            max_tokens = 1024,
            n=1,
            stop=None,
            temperature=0.9,
        )
        response = completion.choices[0].text
        print(response)
    else:
        print("We are under testing thankyou for choosing us!")
        break
