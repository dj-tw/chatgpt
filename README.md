# chatgpt

A quick and dirty chatgpt client. Unlike the base API, this will
remember the last things that were discussed so you can have an 
actual conversation. It does this with a simple hack of storing 
the conversation and sending it back in. Perhaps there is a 
better way.

Not entirely sure if this connects to Davinci-003 or ChatGPT. It is a bit confusing.

## Get API key

Get from openai.com
Copy this into a file in root dir names api_key.py
with contents like:

api_key = "YOUR_KEY_HERE"

## To install:

source install.sh

To activate the virtualenv (if you open a new shell)
source venv/bin/activate

## To run:

ipython 

```
from chatgpt.chat import Chat
chat = Chat()
```

```
chat("Hello")
```
BOT: Hi there! How can I help you?

```
chat("What is your name?")
```
BOT: My name is Bot. Nice to meet you!

```
chat("How do you say that in Chinese?")
```

BOT: Wo shuo zhe yi ju zen me shuo?

