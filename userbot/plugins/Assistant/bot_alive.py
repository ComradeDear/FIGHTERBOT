from telethon import events

from userbot import ALIVE_NAME, bot

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "Unknown"
PM_IMG = "https://telegra.ph/file/3bc2b89fd6fe407ebcaeb.jpg"
pm_caption = "➥ **ASSISTANT IS:** `ONLINE`\n\n"
pm_caption += "➥ **SYSTEMS STATS**\n"
pm_caption += "➥ **Telethon Version:** `1.15.0` \n"
pm_caption += "➥ **Python:** `3.10` \n"
pm_caption += "➥ **Database Status:**  `Functional`\n"
pm_caption += f"➥ **Version** : `1.0`\n"
pm_caption += f"➥ **My Boss** : {DEFAULTUSER} \n"
pm_caption += "➥ **Heroku Database** : `AWS - Working Properly`\n\n"
pm_caption += "➥ **License** : [GNU General Public License v3.0](github.com/ComradeDear/FIGHTERBOT/blob/master/LICENSE)\n"
pm_caption += "➥ **Copyright** : By [FIGHTERBOT](https://t.me/fighterbot_support)\n"
pm_caption += "[Assistant By FIGHTERBOT](https://t.me/fighterbot_support)"

# only Owner Can Use it
@tgbot.on(events.NewMessage(pattern="^/alive", func=lambda e: e.sender_id == bot.uid))
async def _(event):
    await tgbot.send_file(event.chat_id, PM_IMG, caption=pm_caption)
