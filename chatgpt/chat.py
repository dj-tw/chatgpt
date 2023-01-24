from chatgpt.api_key import api_key
import openai
import uuid


# openai.organization = "something"
openai.api_key = api_key

class Chat:
    def __init__(self, engine="text-davinci-003"):
        self.model_engine = engine
        self.conversation_id = uuid.uuid1().hex
        self.history = "Reply in this fashion, BOT: <ANSWER>"

    def chat(self, prompt):
        completion = openai.Completion.create(
            engine=self.model_engine,
            prompt=prompt,
            max_tokens=1024,
            n=1,
            stop='goodbye',
            temperature=0.0
        )

        response = completion.choices[0].text
        return response

    def __call__(self, prompt):

        print('----- History  ----')
        print(self.history)
        print('------------')

        full_prompt = f"conversation_history=({self.history}), USER: {prompt}"
        print('----- Full prompt-----')
        print(full_prompt)
        print('------------------')

        response = self.chat(full_prompt)
        self.history += f'\nUSER: {prompt}, \n{response}'
        print(response)

def run():
    c = Chat()
    while True:
        message = input()
        c(message)

if __name__ == "__main__":
    run()
