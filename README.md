# ssher-telegram

You can run the ssh forwarding like this, you need to have a telegram bot and get your chatid from your chat or group. You can also set this program as a system service which will run in boot. 

```
#!/bin/bash
cd [path]
export PORT=22
export TELEGRAM_TOKEN=[YOUR_TOKEN]
export CHATID=[TELEGRAM_CHAT_ID]
export NGROK_TOKEN=[YOUR_TOKEN]

python3 ssher.py
```

Open an issue if you have any questions.
