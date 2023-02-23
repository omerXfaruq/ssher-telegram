import sys
import os
from httpx import AsyncClient
from pyngrok import ngrok
import asyncio


async def send_request(url:str, payload: dict):
    async with AsyncClient() as client:
        request = await client.post(url, json=payload)
        print(request.json())
    await asyncio.sleep(3600*24*365) ## keep tunneling open

if __name__ == "__main__":
    telegram_token = str(os.environ.get("TELEGRAM_TOKEN"))
    port = int(os.environ.get("PORT"))
    chat_id = str(os.environ.get("CHATID"))
    ngrok_token = str(os.environ.get("NGROK_TOKEN"))
    ngrok.set_auth_token(ngrok_token)
    ssh_tunnel = ngrok.connect(port, "tcp")
    ssh_url_all = ssh_tunnel.public_url
    ssh_temp = ssh_url_all.split("tcp://",1)[1]
    ssh_url , ssh_port = ssh_temp.split(":",1)
    print(ssh_url, ssh_port)
    TELEGRAM_SEND_MESSAGE_URL = f"https://api.telegram.org/bot{telegram_token}/sendMessage"

    asyncio.run(
        send_request(
            TELEGRAM_SEND_MESSAGE_URL,
            {
                'chat_id': chat_id,
                'text': f"ssh -p {ssh_port} ubuntu@{ssh_url}"
            },
        )
    )