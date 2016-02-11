Introduction
============

Telegram-bot-compiler is, as the name suggests, a telegram bot that compiles and executes code. It takes pastebin urls from messages, compiles and executes the code in a Docker container and pipes the output to a telegram message.

Usage
-----

Run the compilebox, supplied as a git submodule:

```
nodejs app.js
```

Then put your telegram http token in file called token.txt and edit the host in the code. Afterwards run:

```
python main.py
```
