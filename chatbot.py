import openai
from dotenv import dotenv_values
import argparse

config=dotenv_values(".env")
openai.api_key=config['OPENAI_API_KEY']


def main():

    parser=argparse.ArgumentParser(description="Simple command line chatbot with GPT-3.5")
    parser.add_argument("--personality",type=str,help="A brief summary of chatbot's personality",default="friendly and helpful")
    args=parser.parse_args()
    print(args.personality)

    initial_prompt=f"You are a conversational chatbot your personality is: {args.personality}"
    messages=[{"role":"system","content":initial_prompt}]

    while True:
        try:
            user_input=input("You: ")
            messages.append({"role":"user","content":user_input})

            res=openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=messages
            )
            messages.append(res['choices'][0]['message'].to_dict())
            print("Assistant: ",res['choices'][0]['message']['content'])
        except KeyboardInterrupt:
            print("Exiting...")
            break

if __name__=="__main__":
    main()