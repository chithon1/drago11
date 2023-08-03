import asyncio
import random
from asyncio.exceptions import TimeoutError

from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError

from drago import dragoiq
from ..helpers.utils import reply_id

# الي يخمط ويكول من كتابتي الا امه انيجه وقد اعذر من انذر
# ذمة بركبتك ليوم قيامة اذا اخذت امر او الملف
@dragoiq.on(admin_cmd(pattern="حالتي ?(.*)"))
async def _(event):
    await event.edit("**- يتم التاكد من حالتك اذا كنت محظور او لا**")
    async with bot.conversation("@SpamBot") as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=178220800)
            )
            await conv.send_message("/start")
            response = await response
            await bot.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            await event.edit("** اولا الغي حظر @SpamBot وحاول مجددا**")
            return
        await event.edit(f"- {response.message.message}\n @Drago_dr")


@dragoiq.on(admin_cmd(pattern="الاغنية ?(.*)"))
async def _(event):
    "To reverse search music by bot."
    if not event.reply_to_msg_id:
        return await event.edit("**▾∮ يجب الرد على الاغنيه اولا**")
    reply_message = await event.get_reply_message()
    chat = "@auddbot"
    try:
        async with event.client.conversation(chat) as conv:
            try:
                await event.edit("**▾∮ يتم التعرف على الاغنية انتظر**")
                start_msg = await conv.send_message("/start")
                response = await conv.get_response()
                send_audio = await conv.send_message(reply_message)
                check = await conv.get_response()
                if not check.text.startswith("Audio received"):
                    return await event.edit(
                        "**▾∮ يجب ان يكون حجم الاغنيه من 5 الى 10 ثواني **."
                    )
                await event.edit("- انتظر قليلا")
                result = await conv.get_response()
                await event.client.send_read_acknowledge(conv.chat_id)
            except YouBlockedUserError:
                await event.edit("```Mohon buka blokir ( @auddbot ) dan coba lagi```")
                return
            namem = f"**الأغنية : **{result.text.splitlines()[0]}\
        \n\n**التفاصيـل : **{result.text.splitlines()[2]}"
            await event.edit(namem)
            await event.client.delete_messages(
                conv.chat_id,
                [start_msg.id, send_audio.id, check.id, result.id, response.id],
            )
    except TimeoutError:
        return await event.edit("***حدث خطا ما حاول مجددا**")


@dragoiq.on(admin_cmd(pattern="ايميل وهمي(?: |$)(.*)"))
async def _(event):
    chat = "@TempMailBot"
    geez = await event.edit("**جاري انشاء بريد ...**")
    async with bot.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=220112646)
            )
            await conv.send_message("/start")
            await asyncio.sleep(1)
            await conv.send_message("/create")
            response = await response
            dragoiqmail = (response).reply_markup.rows[2].buttons[0].url
            await event.client.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            await geez.edit("**الغي حظر @TempMailBot  و حاول مجددا**")
            return
        await event.edit(
            f"الايميل الخاص هو `{response.message.message}`\n[ اضغط هنا لرؤية من رسائل الايميل الواردة]({dragoiqmail})"
        )
@dragoiq.on(admin_cmd(outgoing=True, pattern="غنيلي$"))
async def dragovois(vois):
  rl = random.randint(2,2301)
  url = f"https://t.me/AudiosWaTaN/{rl}"
  await vois.client.send_file(vois.chat_id,url,caption="⌁︙ BY : @Drago_dr",parse_mode="html")
  await vois.delete()

@dragoiq.on(admin_cmd(outgoing=True, pattern="شعر$"))
async def dragovois(vois):
  rl = random.randint(2,622)
  url = f"https://t.me/L1BBBL/{rl}"
  await vois.client.send_file(vois.chat_id,url,caption="⌁︙ BY : @Drago_dr",parse_mode="html")
  await vois.delete()
@dragoiq.on(admin_cmd(outgoing=True, pattern="قران$"))
async def dragovois(vois):
  rl = random.randint(2,101)
  url = f"https://t.me/KTKKVK{rl}"
  await vois.client.send_file(vois.chat_id,url,caption="⌁︙ BY : @Drago_dr",parse_mode="html")
  await vois.delete()
@dragoiq.on(admin_cmd(outgoing=True, pattern="انمي$"))
async def dragoThe(photo):
  rl = random.randint(2,999)
  url = f"https://t.me/AnimeWaTaN/{rl}"
  await photo.client.send_file(photo.chat_id,url,caption="⌁︙ Anime BY : @Drago_dr",parse_mode="html")
  await photo.delete()

@dragoiq.on(admin_cmd(outgoing=True, pattern="ماادري يعني$"))
async def event(vois):
    if vois.fwd_from:
        return
    Ti = await reply_id(vois)
    if jpvois28:
        await vois.client.send_file(vois.chat_id, jpvois28, reply_to=Ti)
        await vois.delete()
@dragoiq.on(admin_cmd(outgoing=True, pattern="منو انت$"))
async def event(vois):
    if vois.fwd_from:
        return
    Ti = await reply_id(vois)
    if jpvois29:
        await vois.client.send_file(vois.chat_id, jpvois29, reply_to=Ti)
        await vois.delete()
@dragoiq.on(admin_cmd(outgoing=True, pattern="مو صوجكم$"))
async def event(vois):
    if vois.fwd_from:
        return
    Ti = await reply_id(vois)
    if jpvois30:
        await vois.client.send_file(vois.chat_id, jpvois30, reply_to=Ti)
        await vois.delete()
@dragoiq.on(admin_cmd(outgoing=True, pattern="خوش تسولف$"))
async def event(vois):
    if vois.fwd_from:
        return
    Ti = await reply_id(vois)
    if jpvois31:
        await vois.client.send_file(vois.chat_id, jpvois31, reply_to=Ti)
        await vois.delete()
@dragoiq.on(admin_cmd(outgoing=True, pattern="يع$"))
async def event(vois):
    if vois.fwd_from:
        return
    Ti = await reply_id(vois)
    if jpvois32:
        await vois.client.send_file(vois.chat_id, jpvois32, reply_to=Ti)
        await vois.delete()
@dragoiq.on(admin_cmd(outgoing=True, pattern="يعني مااعرف$"))
async def event(vois):
    if vois.fwd_from:
        return
    Ti = await reply_id(vois)
    if jpvois35:
        await vois.client.send_file(vois.chat_id, jpvois35, reply_to=Ti)
        await vois.delete()
@dragoiq.on(admin_cmd(outgoing=True, pattern="يامرحبا$"))
async def event(vois):
    if vois.fwd_from:
        return
    Ti = await reply_id(vois)
    if jpvois36:
        await vois.client.send_file(vois.chat_id, jpvois36, reply_to=Ti)
        await vois.delete()
@dragoiq.on(admin_cmd(outgoing=True, pattern="منو انتة$"))
async def event(vois):
    if vois.fwd_from:
        return
    Ti = await reply_id(vois)
    if jpvois37:
        await vois.client.send_file(vois.chat_id, jpvois37, reply_to=Ti)
        await vois.delete()
@dragoiq.on(admin_cmd(outgoing=True, pattern="ماتستحي$"))
async def event(vois):
    if vois.fwd_from:
        return
    Ti = await reply_id(vois)
    if jpvois38:
        await vois.client.send_file(vois.chat_id, jpvois38, reply_to=Ti)
        await vois.delete()
@dragoiq.on(admin_cmd(outgoing=True, pattern="كعدت الديوث$"))
async def event(vois):
    if vois.fwd_from:
        return
    Ti = await reply_id(vois)
    if jpvois39:
        await vois.client.send_file(vois.chat_id, jpvois39, reply_to=Ti)
        await vois.delete()
@dragoiq.on(admin_cmd(outgoing=True, pattern="عيب$"))
async def event(vois):
    if vois.fwd_from:
        return
    Ti = await reply_id(vois)
    if jpvois40:
        await vois.client.send_file(vois.chat_id, jpvois40, reply_to=Ti)
        await vois.delete()
@dragoiq.on(admin_cmd(outgoing=True, pattern="عنعانم$"))
async def event(vois):
    if vois.fwd_from:
        return
    Ti = await reply_id(vois)
    if jpvois41:
        await vois.client.send_file(vois.chat_id, jpvois41, reply_to=Ti)
        await vois.delete()
@dragoiq.on(admin_cmd(outgoing=True, pattern="طبك مرض$"))
async def event(vois):
    if vois.fwd_from:
        return
    Ti = await reply_id(vois)
    if jpvois42:
        await vois.client.send_file(vois.chat_id, jpvois42, reply_to=Ti)
        await vois.delete()
@dragoiq.on(admin_cmd(outgoing=True, pattern="سييي$"))
async def event(vois):
    if vois.fwd_from:
        return
    Ti = await reply_id(vois)
    if jpvois43:
        await vois.client.send_file(vois.chat_id, jpvois43, reply_to=Ti)
        await vois.delete()
@dragoiq.on(admin_cmd(outgoing=True, pattern="سبيدر مان$"))
async def event(vois):
    if vois.fwd_from:
        return
    Ti = await reply_id(vois)
    if jpvois44:
        await vois.client.send_file(vois.chat_id, jpvois44, reply_to=Ti)
        await vois.delete()
@dragoiq.on(admin_cmd(outgoing=True, pattern="خاف حرام$"))
async def event(vois):
    if vois.fwd_from:
        return
    Ti = await reply_id(vois)
    if jpvois45:
        await vois.client.send_file(vois.chat_id, jpvois45, reply_to=Ti)
        await vois.delete()
@dragoiq.on(admin_cmd(outgoing=True, pattern="تحيه لاختك$"))
async def event(vois):
    if vois.fwd_from:
        return
    Ti = await reply_id(vois)
    if jpvois46:
        await vois.client.send_file(vois.chat_id, jpvois46, reply_to=Ti)
        await vois.delete()
@dragoiq.on(admin_cmd(outgoing=True, pattern="امشي كحبة$"))
async def event(vois):
    if vois.fwd_from:
        return
    Ti = await reply_id(vois)
    if jpvois47:
        await vois.client.send_file(vois.chat_id, jpvois47, reply_to=Ti)
        await vois.delete()
@dragoiq.on(admin_cmd(outgoing=True, pattern="امداك$"))
async def event(vois):
    if vois.fwd_from:
        return
    Ti = await reply_id(vois)
    if jpvois48:
        await vois.client.send_file(vois.chat_id, jpvois48, reply_to=Ti)
        await vois.delete()
@dragoiq.on(admin_cmd(outgoing=True, pattern="الحس$"))
async def event(vois):
    if vois.fwd_from:
        return
    Ti = await reply_id(vois)
    if jpvois49:
        await vois.client.send_file(vois.chat_id, jpvois49, reply_to=Ti)
        await vois.delete()
@dragoiq.on(admin_cmd(outgoing=True, pattern="افتهمنا$"))
async def event(vois):
    if vois.fwd_from:
        return
    Ti = await reply_id(vois)
    if jpvois50:
        await vois.client.send_file(vois.chat_id, jpvois32, reply_to=Ti)
        await vois.delete()
@dragoiq.on(admin_cmd(outgoing=True, pattern="اطلع برا$"))
async def event(vois):
    if vois.fwd_from:
        return
    Ti = await reply_id(vois)
    if jpvois51:
        await vois.client.send_file(vois.chat_id, jpvois51, reply_to=Ti)
        await vois.delete()
@dragoiq.on(admin_cmd(outgoing=True, pattern="اخت التنيج$"))
async def event(vois):
    if vois.fwd_from:
        return
    Ti = await reply_id(vois)
    if jpvois52:
        await vois.client.send_file(vois.chat_id, jpvois52, reply_to=Ti)
        await vois.delete()
@dragoiq.on(admin_cmd(outgoing=True, pattern="اوني تشان$"))
async def event(vois):
    if vois.fwd_from:
        return
    Ti = await reply_id(vois)
    if jpvois53:
        await vois.client.send_file(vois.chat_id, jpvois53, reply_to=Ti)
        await vois.delete()
@dragoiq.on(admin_cmd(outgoing=True, pattern="اوني تشان2$"))
async def event(vois):
    if vois.fwd_from:
        return
    Ti = await reply_id(vois)
    if jpvois54:
        await vois.client.send_file(vois.chat_id, jpvois54, reply_to=Ti)
        await vois.delete()        
