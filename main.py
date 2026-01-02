from telethon import TelegramClient, events

api_id = 29199084
api_hash = "32b0c3f696a54816c7fffe4c513b042a"

client = TelegramClient("userbot", api_id, api_hash)

# Har bir foydalanuvchi uchun holat saqlaymiz
user_state = {}
# format:
# user_state[user_id] = {
#     "auto_replied": True/False,
#     "unanswered_count": int
# }

@client.on(events.NewMessage(incoming=True))
async def handler(event):
    if not event.is_private:
        return

    user_id = event.sender_id

    # Agar foydalanuvchi hali yo‘q bo‘lsa — boshlang‘ich holat
    if user_id not in user_state:
        user_state[user_id] = {
            "auto_replied": False,
            "unanswered_count": 0
        }

    state = user_state[user_id]

    # 1️⃣ Birinchi xabar → darhol javob
    if not state["auto_replied"]:
        await event.reply(
            "Assalomu alaykum 😊\n\n"
            "Xabaringiz uchun rahmat.\n"
            "Hozir bandman, bo‘shaganimda albatta javob beraman.\n\n"
            "Savolingiz bo‘lsa yozib qoldirishingiz mumkin ✍️\n"
            "Hozircha avtomatik yordamchi (userbot) javob bermoqda."
        )
        state["auto_replied"] = True
        state["unanswered_count"] = 0
        return

    # 2️⃣ Keyingi xabarlar — sanaymiz
    state["unanswered_count"] += 1

    # 3️⃣ Agar 8 ta xabar yig‘ilsa → yana javob
    if state["unanswered_count"] >= 8:
        await event.reply(
            "Xabaringizni ko‘rdim 😊\n"
            "Hozircha javob bera olmayapman.\n"
            "Iltimos, biroz sabr qiling 🙏"
        )
        state["unanswered_count"] = 0  # qayta sanash boshlanadi

client.start()
print("Userbot ishga tushdi...")
client.run_until_disconnected()