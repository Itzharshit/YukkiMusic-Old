import yt_dlp
from pyrogram import filters
from pyrogram import Client
from Yukki import app, SUDOERS, BOT_ID, BOT_USERNAME, OWNER
from Yukki import dbb, app, BOT_USERNAME, BOT_ID, ASSID, ASSNAME, ASSUSERNAME
from ..YukkiUtilities.helpers.inline import start_keyboard, personal_markup
from ..YukkiUtilities.helpers.thumbnails import down_thumb
from ..YukkiUtilities.helpers.ytdl import ytdl_opts 
from ..YukkiUtilities.helpers.filters import command
from pyrogram.types import (
    CallbackQuery,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    InputMediaPhoto,
    Message,
)
from Yukki.YukkiUtilities.database.chats import (get_served_chats, is_served_chat, add_served_chat, get_served_chats)
from Yukki.YukkiUtilities.database.queue import (is_active_chat, add_active_chat, remove_active_chat, music_on, is_music_playing, music_off)
from Yukki.YukkiUtilities.database.sudo import (get_sudoers, get_sudoers, remove_sudo)

def start_pannel():  
    buttons  = [
            [
                InlineKeyboardButton(text="❰𝗖𝗼𝗺𝗺𝗮𝗻𝗱𝘀❱", url="https://telegra.ph/EHSAAS-MUSIC-COMMAND-12-25")
            ],
            [ 
                InlineKeyboardButton(text="❰𝗢𝘄𝗻𝗲𝗿❱", url="https://t.me/army0071"),
                InlineKeyboardButton(text="❰𝗚𝗿𝗼𝘂𝗽❱", url="https://t.me/World_friends_chatting_group")
            ],
    ]
    return "✨  **𝙄 𝘼𝙈 𝘼𝙉 𝘼𝘿𝙑𝘼𝙉𝘾𝙀𝘿 𝘽𝙊𝙏 𝘾𝙍𝙀𝘼𝙏𝙀𝘿 𝙁𝙊𝙍 𝙋𝙇𝘼𝙔𝙄𝙉𝙂 𝙈𝙐𝙎𝙄𝘾 𝙄𝙉 𝙏𝙃𝙀 𝙑𝙊𝙄𝘾𝙀 𝘾𝙃𝘼𝙏𝙎 𝙊𝙁 𝙏𝙀𝙇𝙀𝙂𝙍𝘼𝙈 𝙂𝙍𝙊𝙐𝙋 & 𝘾𝙃𝘼𝙉𝙉𝙀𝙇.\n✅  𝘿𝙚𝙫𝙚𝙡𝙤𝙥𝙚𝙧 :- @ARMY0071**", buttons

pstart_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "❰➕ 𝘼𝘿𝘿 𝙈𝙀 𝙏𝙊 𝙔𝙊𝙐𝙍 𝙂𝙍𝙊𝙐𝙋 ➕❱", url="https://t.me/ehsaasmusic_bot?startgroup=true")
                ],[
                    InlineKeyboardButton(
                        "❰𝗖𝗼𝗺𝗺𝗮𝗻𝗱𝘀❱", url="https://telegra.ph/EHSAAS-MUSIC-COMMAND-12-25"),
                    InlineKeyboardButton(
                        "❰𝗗𝗼𝗻𝗮𝘁𝗲❱", url="https://t.me/army0071")
                ],[
                    InlineKeyboardButton(
                        "❰𝗚𝗿𝗼𝘂𝗽❱", url="https://t.me/World_friends_chatting_group"), 
                    InlineKeyboardButton(
                        "❰𝗢𝘄𝗻𝗲𝗿❱", url="https://t.me/ARMY0071")
                ],[
                    InlineKeyboardButton(
                        "❰𝙎𝙚𝙩𝙪𝙥 𝙂𝙪𝙞𝙙𝙚❱", url="https://telegra.ph/Setup-guide-12-25")
                ]
            ]
        )

welcome_captcha_group = 2
@app.on_message(filters.new_chat_members, group=welcome_captcha_group)
async def welcome(_, message: Message):
    chat_id = message.chat.id
    if not await is_served_chat(chat_id):
        await message.reply_text(f"❌ **𝙣𝙤𝙩 𝙞𝙣 𝙖𝙡𝙡𝙤𝙬𝙚𝙙 𝙘𝙝𝙖𝙩**\n\n𝙀𝙝𝙨𝙖𝙖𝙨 𝙞𝙨 𝙤𝙣𝙡𝙮 𝙛𝙤𝙧 𝙖𝙡𝙡𝙤𝙬𝙚𝙙 𝙘𝙝𝙖𝙩𝙨, 𝙖𝙨𝙠 𝙖𝙣𝙮 𝙨𝙪𝙙𝙤 𝙪𝙨𝙚𝙧 𝙩𝙤 𝙖𝙡𝙡𝙤𝙬 𝙮𝙤𝙪𝙧 𝙘𝙝𝙖𝙩.\n\n𝙘𝙝𝙚𝙘𝙠 𝙨𝙪𝙙𝙤 𝙪𝙨𝙚𝙧 𝙡𝙞𝙨𝙩 [From Here](https://t.me/{BOT_USERNAME}?start=sudolist)")
        return await app.leave_chat(chat_id)
    for member in message.new_chat_members:
        try:
            if member.id in OWNER:
                return await message.reply_text(f"💡 Announcement, My Owner [{member.mention}] has joined this group.")
            if member.id in SUDOERS:
                return await message.reply_text(f"💡 Announcement, The Sudo member [{member.mention}] has joined this group.")
            if member.id == ASSID:
                await remove_active_chat(chat_id)
            if member.id == BOT_ID:
                out = start_pannel()
                await message.reply_text(f"❤️ **𝙏𝙝𝙖𝙣𝙠𝙨 𝙛𝙤𝙧 𝙖𝙙𝙙𝙞𝙣𝙜 𝙢𝙚 𝙩𝙤 𝙩𝙝𝙚 𝙜𝙧𝙤𝙪𝙥 !**\n\n**𝙋𝙧𝙤𝙢𝙤𝙩𝙚 𝙢𝙚 𝙖𝙨 𝙖𝙙𝙢𝙞𝙣𝙞𝙨𝙩𝙧𝙖𝙩𝙤𝙧 𝙤𝙛 𝙩𝙝𝙚 𝙜𝙧𝙤𝙪𝙥, 𝙤𝙩𝙝𝙚𝙧𝙬𝙞𝙨𝙚 𝙄 𝙬𝙞𝙡𝙡 𝙣𝙤𝙩 𝙗𝙚 𝙖𝙗𝙡𝙚 𝙩𝙤 𝙬𝙤𝙧𝙠 𝙥𝙧𝙤𝙥𝙚𝙧𝙡𝙮.", reply_markup=InlineKeyboardMarkup(out[1]))
                return
        except:
            return

@Client.on_message(filters.group & filters.command(["start", "help"]))
async def start(_, message: Message):
    chat_id = message.chat.id
    if not await is_served_chat(chat_id):
        await message.reply_text(f"❌ **𝙣𝙤𝙩 𝙞𝙣 𝙖𝙡𝙡𝙤𝙬𝙚𝙙 𝙘𝙝𝙖𝙩**\n\n𝙀𝙝𝙨𝙖𝙖𝙨 𝙞𝙨 𝙤𝙣𝙡𝙮 𝙛𝙤𝙧 𝙖𝙡𝙡𝙤𝙬𝙚𝙙 𝙘𝙝𝙖𝙩𝙨, 𝙖𝙨𝙠 𝙖𝙣𝙮 𝙨𝙪𝙙𝙤 𝙪𝙨𝙚𝙧 𝙩𝙤 𝙖𝙡𝙡𝙤𝙬 𝙮𝙤𝙪𝙧 𝙘𝙝𝙖𝙩.\n\n𝙘𝙝𝙚𝙘𝙠 𝙨𝙪𝙙𝙤 𝙪𝙨𝙚𝙧 𝙡𝙞𝙨𝙩 [From Here](https://t.me/{BOT_USERNAME}?start=sudolist)")
        return await app.leave_chat(chat_id)
    out = start_pannel()
    await message.reply_text(f"✨ 𝙃𝙀𝙇𝙇𝙊 {message.from_user.mention}, 𝙄'𝙈 𝙀𝙃𝙎𝘼𝘼𝙎 𝙈𝙐𝙎𝙄𝘾 𝘽𝙊𝙏.\n\n💭 𝙈𝘼𝙆𝙀 𝙈𝙀 𝘼𝘿𝙈𝙄𝙉 𝙄𝙉 𝙔𝙊𝙐𝙍 𝙂𝙍𝙊𝙐𝙋 𝙎𝙊 𝙏𝙃𝘼𝙏 𝙄 𝘾𝘼𝙉 𝙋𝙇𝘼𝙔 𝙈𝙐𝙎𝙄𝘾, 𝙊𝙏𝙃𝙀𝙍𝙒𝙄𝙎𝙀 𝙔𝙊𝙐 𝘾𝘼𝙉'𝙏 𝙐𝙎𝙀 𝙈𝙔 𝙎𝙀𝙍𝙑𝙄𝘾𝙀.", reply_markup=InlineKeyboardMarkup(out[1]))
    return
        
@Client.on_message(filters.private & filters.incoming & filters.command("start"))
async def play(_, message: Message):
    if len(message.command) == 1:
        user_id = message.from_user.id
        user_name = message.from_user.first_name
        rpk = "["+user_name+"](tg://user?id="+str(user_id)+")" 
        await app.send_message(message.chat.id,
            text=f"✨ 𝙒𝙚𝙡𝙘𝙤𝙢𝙚 {rpk} !\n\n𝙄 𝘼𝙈 𝘼𝙉 𝘼𝘿𝙑𝘼𝙉𝘾𝙀𝘿 𝘽𝙊𝙏 𝘾𝙍𝙀𝘼𝙏𝙀𝘿 𝙁𝙊𝙍 𝙋𝙇𝘼𝙔𝙄𝙉𝙂 𝙈𝙐𝙎𝙄𝘾 𝙄𝙉 𝙏𝙃𝙀 𝙑𝙊𝙄𝘾𝙀 𝘾𝙃𝘼𝙏𝙎 𝙊𝙁 𝙏𝙀𝙇𝙀𝙂𝙍𝘼𝙈 𝙂𝙍𝙊𝙐𝙋 & 𝘾𝙃𝘼𝙉𝙉𝙀𝙇.\n✅  𝘿𝙚𝙫𝙚𝙡𝙤𝙥𝙚𝙧 :- @ARMY0071",
            parse_mode="markdown",
            reply_markup=pstart_markup,
            reply_to_message_id=message.message_id,
            disable_web_page_preview=True
        )
    elif len(message.command) == 2:                                                           
        query = message.text.split(None, 1)[1]
        f1 = (query[0])
        f2 = (query[1])
        f3 = (query[2])
        finxx = (f"{f1}{f2}{f3}")
        if str(finxx) == "inf":
            query = ((str(query)).replace("info_","", 1))
            query = (f"https://www.youtube.com/watch?v={query}")
            with yt_dlp.YoutubeDL(ytdl_opts) as ytdl:
                x = ytdl.extract_info(query, download=False)
            thumbnail = (x["thumbnail"])
            searched_text = f"""
💡 **Track Informations**

🏷 **Name:** {x["title"]}
⏱ **Duration:** {round(x["duration"] / 60)} min(s)
👀 **Views:** `{x["view_count"]}`
👍🏻 **Likes:** `{x["like_count"]}`
⭐️ **Ratings:** {x["average_rating"]}
📣 **Channel:** {x["uploader"]}
🔗 **Link:** {x["webpage_url"]}

⚡️ __Powered by Ehsaas Music AI__"""
            link = (x["webpage_url"])
            buttons = personal_markup(link)
            userid = message.from_user.id
            thumb = await down_thumb(thumbnail, userid)
            await app.send_photo(message.chat.id,
                photo=thumb,                 
                caption=searched_text,
                parse_mode="markdown",
                reply_markup=InlineKeyboardMarkup(buttons),
            )
        if str(finxx) == "sud":
            sudoers = await get_sudoers()
            text = "**💡 sudo users list:**\n\n"
            for count, user_id in enumerate(sudoers, 1):
                try:                     
                    user = await app.get_users(user_id)
                    user = user.first_name if not user.mention else user.mention
                except Exception:
                    continue                     
                text += f"➤ {user}\n"
            if not text:
                await message.reply_text("❌ no sudo users found")  
            else:
                await message.reply_text(text)
