import random

from pymongo import MongoClient
from pyrogram import Client, filters
from pyrogram.enums import ChatAction
from pyrogram.types import Message

from config import MONGO_DB_URI
from PURVIMUSIC import app


@app.on_message(
    (filters.text | filters.sticker | filters.group) & ~filters.private & ~filters.bot
)
async def chatbot_text(client: Client, message: Message):
    try:
        if message.text.startswith("!") or message.text.startswith("/"):
            return
    except Exception:
        pass
    chatdb = MongoClient(MONGO_DB_URI)
    chatai = chatdb["Word"]["WordDb"]

    if not message.reply_to_message:
        Radhadb = MongoClient(MONGO_DB_URI)
        Radha = Radhadb["RadhaDb"]["Radha"]
        is_Radha = Radha.find_one({"chat_id": message.chat.id})
        if not is_Radha:
            await client.send_chat_action(message.chat.id, ChatAction.TYPING)
            K = []
            is_chat = chatai.find({"word": message.text})
            k = chatai.find_one({"word": message.text})
            if k:
                for x in is_chat:
                    K.append(x["text"])
                hey = random.choice(K)
                is_text = chatai.find_one({"text": hey})
                Yo = is_text["check"]
                if Yo == "sticker":
                    await message.reply_sticker(f"{hey}")
                if not Yo == "sticker":
                    await message.reply_text(f"{hey}")

    if message.reply_to_message:
        Radhadb = MongoClient(MONGO_DB_URI)
        Radha = Radhadb["RadhaDb"]["Radha"]
        is_Radha = Radha.find_one({"chat_id": message.chat.id})
        if message.reply_to_message.from_user.id == client.id:
            if not is_Radha:
                await client.send_chat_action(message.chat.id, ChatAction.TYPING)
                K = []
                is_chat = chatai.find({"word": message.text})
                k = chatai.find_one({"word": message.text})
                if k:
                    for x in is_chat:
                        K.append(x["text"])
                    hey = random.choice(K)
                    is_text = chatai.find_one({"text": hey})
                    Yo = is_text["check"]
                    if Yo == "sticker":
                        await message.reply_sticker(f"{hey}")
                    if not Yo == "sticker":
                        await message.reply_text(f"{hey}")
        if not message.reply_to_message.from_user.id == client.id:
            if message.sticker:
                is_chat = chatai.find_one(
                    {
                        "word": message.reply_to_message.text,
                        "id": message.sticker.file_unique_id,
                    }
                )
                if not is_chat:
                    chatai.insert_one(
                        {
                            "word": message.reply_to_message.text,
                            "text": message.sticker.file_id,
                            "check": "sticker",
                            "id": message.sticker.file_unique_id,
                        }
                    )
            if message.text:
                is_chat = chatai.find_one(
                    {"word": message.reply_to_message.text, "text": message.text}
                )
                if not is_chat:
                    chatai.insert_one(
                        {
                            "word": message.reply_to_message.text,
                            "text": message.text,
                            "check": "none",
                        }
                    )


@app.on_message(
    (filters.sticker | filters.group | filters.text) & ~filters.private & ~filters.bot
)
async def chatbot_sticker(client: Client, message: Message):
    try:
        if message.text.startswith("!") or message.text.startswith("/"):
            return
    except Exception:
        pass
    chatdb = MongoClient(MONGO_DB_URI)
    chatai = chatdb["Word"]["WordDb"]

    if not message.reply_to_message:
        Radhadb = MongoClient(MONGO_DB_URI)
        Radha = Radhadb["RadhaDb"]["Radha"]
        is_Radha = Radha.find_one({"chat_id": message.chat.id})
        if not is_Radha:
            await client.send_chat_action(message.chat.id, ChatAction.TYPING)
            K = []
            is_chat = chatai.find({"word": message.sticker.file_unique_id})
            k = chatai.find_one({"word": message.text})
            if k:
                for x in is_chat:
                    K.append(x["text"])
                hey = random.choice(K)
                is_text = chatai.find_one({"text": hey})
                Yo = is_text["check"]
                if Yo == "text":
                    await message.reply_text(f"{hey}")
                if not Yo == "text":
                    await message.reply_sticker(f"{hey}")

    if message.reply_to_message:
        Radhadb = MongoClient(MONGO_DB_URI)
        Radha = Radhadb["RadhaDb"]["Radha"]
        is_Radha = Radha.find_one({"chat_id": message.chat.id})
        if message.reply_to_message.from_user.id == Client.id:
            if not is_Radha:
                await client.send_chat_action(message.chat.id, ChatAction.TYPING)
                K = []
                is_chat = chatai.find({"word": message.text})
                k = chatai.find_one({"word": message.text})
                if k:
                    for x in is_chat:
                        K.append(x["text"])
                    hey = random.choice(K)
                    is_text = chatai.find_one({"text": hey})
                    Yo = is_text["check"]
                    if Yo == "text":
                        await message.reply_text(f"{hey}")
                    if not Yo == "text":
                        await message.reply_sticker(f"{hey}")
        if not message.reply_to_message.from_user.id == Client.id:
            if message.text:
                is_chat = chatai.find_one(
                    {
                        "word": message.reply_to_message.sticker.file_unique_id,
                        "text": message.text,
                    }
                )
                if not is_chat:
                    toggle.insert_one(
                        {
                            "word": message.reply_to_message.sticker.file_unique_id,
                            "text": message.text,
                            "check": "text",
                        }
                    )
            if message.sticker:
                is_chat = chatai.find_one(
                    {
                        "word": message.reply_to_message.sticker.file_unique_id,
                        "text": message.sticker.file_id,
                    }
                )
                if not is_chat:
                    chatai.insert_one(
                        {
                            "word": message.reply_to_message.sticker.file_unique_id,
                            "text": message.sticker.file_id,
                            "check": "none",
                        }
                    )


@app.on_message(
    (filters.text | filters.sticker | filters.group) & ~filters.private & ~filters.bot
)
async def chatbot_pvt(client: Client, message: Message):
    try:
        if message.text.startswith("!") or message.text.startswith("/"):
            return
    except Exception:
        pass
    chatdb = MongoClient(MONGO_DB_URI)
    chatai = chatdb["Word"]["WordDb"]
    if not message.reply_to_message:
        await client.send_chat_action(message.chat.id, ChatAction.TYPING)
        K = []
        is_chat = chatai.find({"word": message.text})
        for x in is_chat:
            K.append(x["text"])
        hey = random.choice(K)
        is_text = chatai.find_one({"text": hey})
        Yo = is_text["check"]
        if Yo == "sticker":
            await message.reply_sticker(f"{hey}")
        if not Yo == "sticker":
            await message.reply_text(f"{hey}")
    if message.reply_to_message:
        if message.reply_to_message.from_user.id == client.id:
            await client.send_chat_action(message.chat.id, ChatAction.TYPING)
            K = []
            is_chat = chatai.find({"word": message.text})
            for x in is_chat:
                K.append(x["text"])
            hey = random.choice(K)
            is_text = chatai.find_one({"text": hey})
            Yo = is_text["check"]
            if Yo == "sticker":
                await message.reply_sticker(f"{hey}")
            if not Yo == "sticker":
                await message.reply_text(f"{hey}")


@app.on_message(
    (filters.sticker | filters.sticker | filters.group)
    & ~filters.private
    & ~filters.bot,
)
async def chatbot_sticker_pvt(client: Client, message: Message):
    try:
        if message.text.startswith("!") or message.text.startswith("/"):
            return
    except Exception:
        pass
    chatdb = MongoClient(MONGO_DB_URI)
    chatai = chatdb["Word"]["WordDb"]
    if not message.reply_to_message:
        await client.send_chat_action(message.chat.id, ChatAction.TYPING)
        K = []
        is_chat = chatai.find({"word": message.sticker.file_unique_id})
        for x in is_chat:
            K.append(x["text"])
        hey = random.choice(K)
        is_text = chatai.find_one({"text": hey})
        Yo = is_text["check"]
        if Yo == "text":
            await message.reply_text(f"{hey}")
        if not Yo == "text":
            await message.reply_sticker(f"{hey}")
    if message.reply_to_message:
        if message.reply_to_message.from_user.id == client.id:
            await client.send_chat_action(message.chat.id, ChatAction.TYPING)
            K = []
            is_chat = chatai.find({"word": message.sticker.file_unique_id})
            for x in is_chat:
                K.append(x["text"])
            hey = random.choice(K)
            is_text = chatai.find_one({"text": hey})
            Yo = is_text["check"]
            if Yo == "text":
                await message.reply_text(f"{hey}")
            if not Yo == "text":
                await message.reply_sticker(f"{hey}")


@app.on_message(filters.text)
async def handle_messages(bot, message):
    try:
        unwanted_symbols = ["/", ":", ";", "*", "?"]

        
        if message.text[0] in unwanted_symbols:
            print(f"Ignored message: {message.text}")
            return

        await bot.send_chat_action(message.chat.id, ChatAction.TYPING)

        query = message.text
        print(f"Processing query: {query}")

        headers = {
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json"
        }
        payload = {
            "model": "meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo",
            "messages": [
                {
                    "role": "user",
                    "content": query
                }
            ]
        }

        response = requests.post(BASE_URL, json=payload, headers=headers)

        if response.status_code == 200 and response.text.strip():
            response_data = response.json()
            if "choices" in response_data and len(response_data["choices"]) > 0:
                result = response_data["choices"][0]["message"]["content"]
                await message.reply_text(
                    f"{result}",
                    parse_mode=ParseMode.MARKDOWN
                )
            else:
                await message.reply_text("❍ ᴇʀʀᴏʀ: No response from API.")
        else:
            await message.reply_text(f"❍ ᴇʀʀᴏʀ: API request failed. Status code: {response.status_code}")

    except Exception as e:
        print(f"Error: {e}")
        await message.reply_text(f"❍ ᴇʀʀᴏʀ: {e}")



if __name__ == "__main__":
    print("Bot is running...")
    app.run()
                  
