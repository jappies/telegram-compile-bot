Introduction
============

Telegram-bot-compiler is, as the name suggests, a telegram bot that compiles and executes code. It takes pastebin urls from messages, compiles and executes the code in a Docker container and pipes the output to a telegram message.

Usage
-----

Clone the repository by executing the following command:

```
git clone --recursive https://github.com/flammified/telegram-compile-bot.git
```


Then run the compilebox, supplied as a git submodule:

```
nodejs compilebox/app.js
```

You can edit settings inside app.js as well. If you want to read more about that project, click on [this](https://github.com/remoteinterview/compilebox/)  link. It is not my project :)


After that put your telegram http token in a file called token.txt in the root folder and do:

```
python main.py
```
