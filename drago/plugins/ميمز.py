import asyncio
import random
from asyncio.exceptions import TimeoutError

from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError

from drago import dragoiq
from ..helpers.utils import reply_id
from ..sql_helper.locks_sql import *

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
@dragoiq.on(admin_cmd(outgoing=True, pattern="تخوني$"))
async def event(vois):
    if vois.fwd_from:
        return
    Ti = await reply_id(vois)
    if dragovois1:
        await vois.client.send_file(vois.chat_id, dragovois1, reply_to=Ti)
        await vois.delete()

@dragoiq.on(admin_cmd(outgoing=True, pattern="مستمرة الكلاوات$"))
async def event(vois):
    if vois.fwd_from:
        return
    Ti = await reply_id(vois)
    if dragovois2:
        await vois.client.send_file(vois.chat_id, dragovois2, reply_to=Ti)
        await vois.delete()
@dragoiq.on(admin_cmd(outgoing=True, pattern="احب العراق$"))
async def event(vois):
    if vois.fwd_from:
        return
    Ti = await reply_id(vois)
    if dragovois3:
        await vois.client.send_file(vois.chat_id, dragovois3, reply_to=Ti)
        await vois.delete()
@dragoiq.on(admin_cmd(outgoing=True, pattern="احبك$"))
async def event(vois):
    if vois.fwd_from:
        return
    Ti = await reply_id(vois)
    if dragovois4:
        await vois.client.send_file(vois.chat_id, dragovois4, reply_to=Ti)
        await vois.delete()
@dragoiq.on(admin_cmd(outgoing=True, pattern="اخت التنيج$"))
async def event(vois):
    if vois.fwd_from:
        return
    Ti = await reply_id(vois)
    if dragovois5:
        await vois.client.send_file(vois.chat_id, dragovois5, reply_to=Ti)
        await vois.delete()
@dragoiq.on(admin_cmd(outgoing=True, pattern="اذا اكمشك$"))
async def event(vois):
    if vois.fwd_from:
        return
    Ti = await reply_id(vois)
    if dragovois6:
        await vois.client.send_file(vois.chat_id, dragovois6, reply_to=Ti)
        await vois.delete()
@dragoiq.on(admin_cmd(outgoing=True, pattern="اسكت$"))
async def event(vois):
    if vois.fwd_from:
        return
    Ti = await reply_id(vois)
    if dragovois7:
        await vois.client.send_file(vois.chat_id, dragovois7, reply_to=Ti)
        await vois.delete()
@dragoiq.on(admin_cmd(outgoing=True, pattern="افتهمنا$"))
async def event(vois):
    if vois.fwd_from:
        return
    Ti = await reply_id(vois)
    if dragovois8:
        await vois.client.send_file(vois.chat_id, dragovois8, reply_to=Ti)
        await vois.delete()
@dragoiq.on(admin_cmd(outgoing=True, pattern="اكل خرا$"))
async def event(vois):
    if vois.fwd_from:
        return
    Ti = await reply_id(vois)
    if dragovois9:
        await vois.client.send_file(vois.chat_id, dragovois9, reply_to=Ti)
        await vois.delete()
@dragoiq.on(admin_cmd(outgoing=True, pattern="العراق$"))
async def event(vois):
    if vois.fwd_from:
        return
    Ti = await reply_id(vois)
    if dragovois10:
        await vois.client.send_file(vois.chat_id, dragovois10, reply_to=Ti)
        await vois.delete()
@dragoiq.on(admin_cmd(outgoing=True, pattern="الكعده وياكم$"))
async def event(vois):
    if vois.fwd_from:
        return
    Ti = await reply_id(vois)
    if dragovois11:
        await vois.client.send_file(vois.chat_id, dragovois11, reply_to=Ti)
        await vois.delete()
@dragoiq.on(admin_cmd(outgoing=True, pattern="الكمر اني$"))
async def event(vois):
    if vois.fwd_from:
        return
    Ti = await reply_id(vois)
    if dragovois12:
        await vois.client.send_file(vois.chat_id, dragovois12, reply_to=Ti)
        await vois.delete()
@dragoiq.on(admin_cmd(outgoing=True, pattern="اللهم لا شماته$"))
async def event(vois):
    if vois.fwd_from:
        return
    Ti = await reply_id(vois)
    if dragovois13:
        await vois.client.send_file(vois.chat_id, dragovois13, reply_to=Ti)
        await vois.delete()
@dragoiq.on(admin_cmd(outgoing=True, pattern="اني مااكدر$"))
async def event(vois):
    if vois.fwd_from:
        return
    Ti = await reply_id(vois)
    if dragovois14:
        await vois.client.send_file(vois.chat_id, dragovois14, reply_to=Ti)
        await vois.delete()
@dragoiq.on(admin_cmd(outgoing=True, pattern="بقولك ايه$"))
async def event(vois):
    if vois.fwd_from:
        return
    Ti = await reply_id(vois)
    if dragovois15:
        await vois.client.send_file(vois.chat_id, dragovois15, reply_to=Ti)
        await vois.delete()
@dragoiq.on(admin_cmd(outgoing=True, pattern="تف على شرفك$"))
async def event(vois):
    if vois.fwd_from:
        return
    Ti = await reply_id(vois)
    if dragovois16:
        await vois.client.send_file(vois.chat_id, dragovois16, reply_to=Ti)
        await vois.delete()
@dragoiq.on(admin_cmd(outgoing=True, pattern="شجلبت$"))
async def event(vois):
    if vois.fwd_from:
        return
    Ti = await reply_id(vois)
    if dragovois17:
        await vois.client.send_file(vois.chat_id, dragovois17, reply_to=Ti)
        await vois.delete()
@dragoiq.on(admin_cmd(outgoing=True, pattern="شكد شفت ناس$"))
async def event(vois):
    if vois.fwd_from:
        return
    Ti = await reply_id(vois)
    if dragovois18:
        await vois.client.send_file(vois.chat_id, dragovois18, reply_to=Ti)
        await vois.delete()
@dragoiq.on(admin_cmd(outgoing=True, pattern="صباح القنادر$"))
async def event(vois):
    if vois.fwd_from:
        return
    Ti = await reply_id(vois)
    if dragovois19:
        await vois.client.send_file(vois.chat_id, dragovois19, reply_to=Ti)
        await vois.delete()
@dragoiq.on(admin_cmd(outgoing=True, pattern="ضحكة فيطية$"))
async def event(vois):
    if vois.fwd_from:
        return
    Ti = await reply_id(vois)
    if dragovois20:
        await vois.client.send_file(vois.chat_id, dragovois20, reply_to=Ti)
        await vois.delete()
@dragoiq.on(admin_cmd(outgoing=True, pattern="طار القلب$"))
async def event(vois):
    if vois.fwd_from:
        return
    Ti = await reply_id(vois)
    if dragovois21:
        await vois.client.send_file(vois.chat_id, dragovois21, reply_to=Ti)
        await vois.delete()
@dragoiq.on(admin_cmd(outgoing=True, pattern="غطيلي$"))
async def event(vois):
    if vois.fwd_from:
        return
    Ti = await reply_id(vois)
    if dragovois22:
        await vois.client.send_file(vois.chat_id, dragovois22, reply_to=Ti)
        await vois.delete()
@dragoiq.on(admin_cmd(outgoing=True, pattern="في منتصف الجبهة$"))
async def event(vois):
    if vois.fwd_from:
        return
    Ti = await reply_id(vois)
    if dragovois23:
        await vois.client.send_file(vois.chat_id, dragovois23, reply_to=Ti)
        await vois.delete()
@dragoiq.on(admin_cmd(outgoing=True, pattern="لاتقتل المتعه$"))
async def event(vois):
    if vois.fwd_from:
        return
    Ti = await reply_id(vois)
    if dragovois24:
        await vois.client.send_file(vois.chat_id, dragovois24, reply_to=Ti)
        await vois.delete()
@dragoiq.on(admin_cmd(outgoing=True, pattern="لا لتغلط$"))
async def event(vois):
    if vois.fwd_from:
        return
    Ti = await reply_id(vois)
    if dragovois25:
        await vois.client.send_file(vois.chat_id, dragovois25, reply_to=Ti)
        await vois.delete()
@dragoiq.on(admin_cmd(outgoing=True, pattern="لا يمه لا$"))
async def event(vois):
    if vois.fwd_from:
        return
    Ti = await reply_id(vois)
    if dragovois26:
        await vois.client.send_file(vois.chat_id, dragovois26, reply_to=Ti)
        await vois.delete()
@dragoiq.on(admin_cmd(outgoing=True, pattern="لحد يحجي وياي$"))
async def event(vois):
    if vois.fwd_from:
        return
    Ti = await reply_id(vois)
    if dragovois27:
        await vois.client.send_file(vois.chat_id, dragovois27, reply_to=Ti)
        await vois.delete()
@dragoiq.on(admin_cmd(outgoing=True, pattern="ماادري يعني$"))
async def event(vois):
    if vois.fwd_from:
        return
    Ti = await reply_id(vois)
    if dragovois28:
        await vois.client.send_file(vois.chat_id, dragovois28, reply_to=Ti)
        await vois.delete()
@dragoiq.on(admin_cmd(outgoing=True, pattern="منو انت$"))
async def event(vois):
    if vois.fwd_from:
        return
    Ti = await reply_id(vois)
    if dragovois29:
        await vois.client.send_file(vois.chat_id, dragovois29, reply_to=Ti)
        await vois.delete()
@dragoiq.on(admin_cmd(outgoing=True, pattern="مو صوجكم$"))
async def event(vois):
    if vois.fwd_from:
        return
    Ti = await reply_id(vois)
    if dragovois30:
        await vois.client.send_file(vois.chat_id, dragovois30, reply_to=Ti)
        await vois.delete()
@dragoiq.on(admin_cmd(outgoing=True, pattern="خوش تسولف$"))
async def event(vois):
    if vois.fwd_from:
        return
    Ti = await reply_id(vois)
    if dragovois31:
        await vois.client.send_file(vois.chat_id, dragovois31, reply_to=Ti)
        await vois.delete()
@dragoiq.on(admin_cmd(outgoing=True, pattern="يع$"))
async def event(vois):
    if vois.fwd_from:
        return
    Ti = await reply_id(vois)
    if dragovois32:
        await vois.client.send_file(vois.chat_id, dragovois32, reply_to=Ti)
        await vois.delete()
@dragoiq.on(admin_cmd(outgoing=True, pattern="يعني مااعرف$"))
async def event(vois):
    if vois.fwd_from:
        return
    Ti = await reply_id(vois)
    if dragovois35:
        await vois.client.send_file(vois.chat_id, dragovois35, reply_to=Ti)
        await vois.delete()
@dragoiq.on(admin_cmd(outgoing=True, pattern="يامرحبا$"))
async def event(vois):
    if vois.fwd_from:
        return
    Ti = await reply_id(vois)
    if dragovois36:
        await vois.client.send_file(vois.chat_id, dragovois36, reply_to=Ti)
        await vois.delete()
@dragoiq.on(admin_cmd(outgoing=True, pattern="منو انتة$"))
async def event(vois):
    if vois.fwd_from:
        return
    Ti = await reply_id(vois)
    if dragovois37:
        await vois.client.send_file(vois.chat_id, dragovois37, reply_to=Ti)
        await vois.delete()
@dragoiq.on(admin_cmd(outgoing=True, pattern="ماتستحي$"))
async def event(vois):
    if vois.fwd_from:
        return
    Ti = await reply_id(vois)
    if dragovois38:
        await vois.client.send_file(vois.chat_id, dragovois38, reply_to=Ti)
        await vois.delete()
@dragoiq.on(admin_cmd(outgoing=True, pattern="كعدت الديوث$"))
async def event(vois):
    if vois.fwd_from:
        return
    Ti = await reply_id(vois)
    if dragovois39:
        await vois.client.send_file(vois.chat_id, dragovois39, reply_to=Ti)
        await vois.delete()
@dragoiq.on(admin_cmd(outgoing=True, pattern="عيب$"))
async def event(vois):
    if vois.fwd_from:
        return
    Ti = await reply_id(vois)
    if dragovois40:
        await vois.client.send_file(vois.chat_id, dragovois40, reply_to=Ti)
        await vois.delete()
@dragoiq.on(admin_cmd(outgoing=True, pattern="عنعانم$"))
async def event(vois):
    if vois.fwd_from:
        return
    Ti = await reply_id(vois)
    if dragovois41:
        await vois.client.send_file(vois.chat_id, dragovois41, reply_to=Ti)
        await vois.delete()
@dragoiq.on(admin_cmd(outgoing=True, pattern="طبك مرض$"))
async def event(vois):
    if vois.fwd_from:
        return
    Ti = await reply_id(vois)
    if dragovois42:
        await vois.client.send_file(vois.chat_id, dragovois42, reply_to=Ti)
        await vois.delete()
@dragoiq.on(admin_cmd(outgoing=True, pattern="سييي$"))
async def event(vois):
    if vois.fwd_from:
        return
    Ti = await reply_id(vois)
    if dragovois43:
        await vois.client.send_file(vois.chat_id, dragovois43, reply_to=Ti)
        await vois.delete()
@dragoiq.on(admin_cmd(outgoing=True, pattern="سبيدر مان$"))
async def event(vois):
    if vois.fwd_from:
        return
    Ti = await reply_id(vois)
    if dragovois44:
        await vois.client.send_file(vois.chat_id, dragovois44, reply_to=Ti)
        await vois.delete()
@dragoiq.on(admin_cmd(outgoing=True, pattern="خاف حرام$"))
async def event(vois):
    if vois.fwd_from:
        return
    Ti = await reply_id(vois)
    if dragovois45:
        await vois.client.send_file(vois.chat_id, dragovois45, reply_to=Ti)
        await vois.delete()
@dragoiq.on(admin_cmd(outgoing=True, pattern="تحيه لاختك$"))
async def event(vois):
    if vois.fwd_from:
        return
    Ti = await reply_id(vois)
    if dragovois46:
        await vois.client.send_file(vois.chat_id, dragovois46, reply_to=Ti)
        await vois.delete()
@dragoiq.on(admin_cmd(outgoing=True, pattern="امشي كحبة$"))
async def event(vois):
    if vois.fwd_from:
        return
    Ti = await reply_id(vois)
    if dragovois47:
        await vois.client.send_file(vois.chat_id, dragovois47, reply_to=Ti)
        await vois.delete()
@dragoiq.on(admin_cmd(outgoing=True, pattern="امداك$"))
async def event(vois):
    if vois.fwd_from:
        return
    Ti = await reply_id(vois)
    if dragovois48:
        await vois.client.send_file(vois.chat_id, dragovois48, reply_to=Ti)
        await vois.delete()
@dragoiq.on(admin_cmd(outgoing=True, pattern="الحس$"))
async def event(vois):
    if vois.fwd_from:
        return
    Ti = await reply_id(vois)
    if dragovois49:
        await vois.client.send_file(vois.chat_id, dragovois49, reply_to=Ti)
        await vois.delete()
@dragoiq.on(admin_cmd(outgoing=True, pattern="افتهمنا$"))
async def event(vois):
    if vois.fwd_from:
        return
    Ti = await reply_id(vois)
    if dragovois50:
        await vois.client.send_file(vois.chat_id, dragovois32, reply_to=Ti)
        await vois.delete()
@dragoiq.on(admin_cmd(outgoing=True, pattern="اطلع برا$"))
async def event(vois):
    if vois.fwd_from:
        return
    Ti = await reply_id(vois)
    if dragovois51:
        await vois.client.send_file(vois.chat_id, dragovois51, reply_to=Ti)
        await vois.delete()
@dragoiq.on(admin_cmd(outgoing=True, pattern="اخت التنيج$"))
async def event(vois):
    if vois.fwd_from:
        return
    Ti = await reply_id(vois)
    if dragovois52:
        await vois.client.send_file(vois.chat_id, dragovois52, reply_to=Ti)
        await vois.delete()
@dragoiq.on(admin_cmd(outgoing=True, pattern="اوني تشان$"))
async def event(vois):
    if vois.fwd_from:
        return
    Ti = await reply_id(vois)
    if dragovois53:
        await vois.client.send_file(vois.chat_id, dragovois53, reply_to=Ti)
        await vois.delete()
@dragoiq.on(admin_cmd(outgoing=True, pattern="اوني تشان2$"))
async def event(vois):
    if vois.fwd_from:
        return
    Ti = await reply_id(vois)
    if dragovois54:
        await vois.client.send_file(vois.chat_id, dragovois54, reply_to=Ti)
        await vois.delete()
