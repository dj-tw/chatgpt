# chatgpt

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

