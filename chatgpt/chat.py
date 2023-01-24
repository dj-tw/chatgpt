from api_key import api_key
import openai

openai.api_key = api_key

class Chat:
    def __init__(self, engine="text-davinci-003"):
        """
        Instantiate, store the engine and a conversation log
        :param engine:
        """
        self.model_engine = engine
        self.history = "Reply in this fashion, BOT: <ANSWER>"

    def _chat(self, prompt):
        """
        Raw chat, if you want to remember history use __call__
        :param prompt:
        :return:
        """
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

    def clear_conversation(self):
        """
        Forget what has been discussed and start over fresh
        :return: None
        """
        self.history = ""

    def __call__(self, prompt, show_history=False):
        full_prompt = f"conversation_history=({self.history}), USER: {prompt}"

        if show_history:
            print('----- Full prompt-----')
            print(full_prompt)
            print('------------------')

        response = self._chat(full_prompt)
        self.history += f'\nUSER: {prompt}, \n{response}'
        print(response)
