from drago import dragoiq, bot
from drago import BOTLOG_CHATID
from ..sql_helper.globals import addgvar, delgvar, gvarstatus
import asyncio
from ..Config import Config
import requests
from telethon import Button, events
from telethon.tl.functions.messages import ExportChatInviteRequest
from ..core.managers import edit_delete, edit_or_reply
#
#          
REH = "**           **"
DRAGO_PIC = "https://telegra.ph/file/99b7fa93494f6a583b83d.mp4"
Bot_Username = Config.TG_BOT_USERNAME
if Config.TG_BOT_USERNAME is not None and tgbot is not None:
    
    @tgbot.on(events.InlineQuery)
    async def inline_handler(event):
        builder = event.builder
        result = None
        DRAGO = Bot_Username.replace("@", "")
        query = event.text
        await bot.get_me()
        if query.startswith("") and event.query.user_id == bot.uid:
            buttons = Button.url("•    •", f"https://t.me/{DRAGO}")
            if DRAGO_PIC and DRAGO_PIC.endswith((".jpg", ".png", "gif", "mp4")):
                result = builder.photo(
                    DRAGO_PIC, text=REH, buttons=buttons, link_preview=False
                )
            elif DRAGO_PIC:
                result = builder.document(
                    DRAGO_PIC,
                    title="DRAGO",
                    text=REH,
                    buttons=buttons,
                    link_preview=False,
                )
            else:
                result = builder.article(
                    title="DRAGO",
                    text=REH,
                    buttons=buttons,
                    link_preview=False,
                )
        await event.answer([result] if result else None)

@bot.on(admin_cmd(outgoing=True, pattern=""))
async def repo(event):
    if event.fwd_from:
        return
    SX9OO = Config.TG_BOT_USERNAME
    if event.reply_to_msg_id:
        await event.get_reply_message()
    await bot.send_message(SX9OO, "/hack")
    response = await bot.inline_query(SX9OO, "")
    await response[0].click(event.chat_id)
    await event.delete()

@dragoiq.ar_cmd(pattern="")
async def reda(event):
    ty = event.text
    ty = ty.replace(".", "")
    ty = ty.replace(" ", "")
    if len (ty) < 2:
        return await edit_delete(event, "**         **")
    if ty == "":
        if not event.is_group:
            return await edit_delete("**         **")
        if event.is_group:
            if gvarstatus ("subgroup") == event.chat_id:
                return await edit_delete(event, "**     **")
            if gvarstatus("subgroup"):
                return await edit_or_reply(event, "**           **")
            addgvar("subgroup", f"{event.chat_id}")
            return await edit_or_reply(event, "**       **")
    if ty == "":
        if gvarstatus ("subprivate"):
            return await edit_delete(event, "**      **")
        if not gvarstatus ("subprivate"):
            addgvar ("subprivate", True)
            await edit_or_reply(event, "**      **")
    if ty not in ["", ""]:
        return await edit_delete(event, "**         **")
@dragoiq.ar_cmd(pattern="")
async def reda (event):
    cc = event.text.replace(".", "")
    cc = cc.replace(" ", "")
    if len (cc) < 2:
        return await edit_delete(event, "**      **")
    if cc == "":
        if not gvarstatus ("subgroup"):
            return await edit_delete(event, "**      **")
        if gvarstatus ("subgroup"):
            delgvar ("subgroup")
            return await edit_delete(event, "**       **")
    if cc == "":
        if not gvarstatus ("subprivate"):
            return await edit_delete(event, "**      **")
        if gvarstatus ("subprivate"):
            delgvar ("subprivate")
            return await edit_delete(event, "**      **")
    if cc not in ["", ""]:
        return await edit_delete(event, "**       **")

@dragoiq.ar_cmd(incoming=True)
async def reda(event):
    if gvarstatus ("subprivate"):
        if event.is_private:
            try:
       
                idd = event.peer_id.user_id
                tok = Config.TG_BOT_TOKEN
                ch = gvarstatus ("pchan")
                if not ch:
                    return await dragoiq.tgbot.send_message(BOTLOG_CHATID, "**        **")
                try:
                    ch = int(ch)
                except BaseException as r:
                    return await dragoiq.tgbot.send_message(BOTLOG_CHATID, f"**  \n{r}**")
                url = f"https://api.telegram.org/bot{tok}/getchatmember?chat_id={ch}&user_id={idd}"
                req = requests.get(url)
                reqt = req.text
                if "chat not found" in reqt:
                    mb = await dragoiq.tgbot.get_me()
                    mb = mb.username
                    await dragoiq.tgbot.send_message(BOTLOG_CHATID, f"**   @{mb}     **")
                    return
                if "bot was kicked" in reqt:
                    mb = await dragoiq.tgbot.get_me()
                    mb = mb.username
                    await dragoiq.tgbot.send_message(BOTLOG_CHATID, "**    @{mb}       **")
                    return
                if "not found" in reqt:
                    try:
                        c = await dragoiq.get_entity(ch)
                        chn = c.username
                        if c.username == None:
                            ra = await dragoiq.tgbot(ExportChatInviteRequest(ch))
                            chn = ra.link
                        if chn.startswith("https://"):
                            await event.reply(f"**      \n  : {chn}**", buttons=[(Button.url(" ", chn),)],
                            )
                            return await event.delete()
                        else:
                            await event.reply(f"**       \n   : @{chn} **", buttons=[(Button.url(" ", f"https://t.me/{chn}"),)],
                            )
                            return await event.delete()
                    except BaseException as er:
                        await dragoiq.tgbot.send_message(BOTLOG_CHATID, f"  \n{er}")
                if "left" in reqt:
                    try:
                        c = await dragoiq.get_entity(ch)
                        chn = c.username
                        if c.username == None:
                            ra = await dragoiq.tgbot(ExportChatInviteRequest(ch))
                            chn = ra.link
                        if chn.startswith("https://"):
                            await event.reply(f"**      \n  : {chn}**", buttons=[(Button.url(" ", chn),)],
                            )
                            return await event.message.delete()
                        else:
                            await event.reply(f"**       \n   : @{chn} **", buttons=[(Button.url(" ", f"https://t.me/{chn}"),)],
                            )
                            return await event.message.delete()
                    except BaseException as er:
                        await dragoiq.tgbot.send_message(BOTLOG_CHATID, f"  \n{er}")
                if "error_code" in reqt:
                    await dragoiq.tgbot.send_message(BOTLOG_CHATID, f"**        @SX9OO  \n{reqt}**")
                
                return
            except BaseException as er:
                await dragoiq.tgbot.send_message(BOTLOG_CHATID, f"**  \n{er}**")