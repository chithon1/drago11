import random
import re
import time
import asyncio
import os
from datetime import datetime
from platform import python_version

from telethon import version
from telethon.errors.rpcerrorlist import (
    MediaEmptyError,
    WebpageCurlFailedError,
    WebpageMediaEmptyError,
)
from telethon.events import CallbackQuery

from drago import StartTime, dragoiq, DRAGOVERSION
from ..Config import Config
from ..core.managers import edit_or_reply
from ..helpers.functions import catalive, check_data_base_heal_th, get_readable_time
from ..helpers.utils import reply_id
from ..sql_helper.globals import gvarstatus
from . import mention
 
plugin_category = "utils"


#كتـابة وتعـديل:  @FFlXlX
#ذمة بركبتك ليوم قيامة اذا اخذت امر واحد من ملف الفحص
#ربي لايعطيك العافية والصحة اذا خمطت امر او ملف الفحص
#كس اخته الي ياخذ امر او ملف الفحص
#حسبية الله ونعمل الوكيل الي ياخذ امر او ملف الفحص
file_path = "installation_date.txt"
if os.path.exists(file_path) and os.path.getsize(file_path) > 0:
    with open(file_path, "r") as file:
        installation_time = file.read().strip()
else:
    installation_time = datetime.now().strftime("%Y-%m-%d")
    with open(file_path, "w") as file:
        file.write(installation_time)

@dragoiq.ar_cmd(pattern="فحص(?:\s|$)([\s\S]*)")

async def amireallyalive(event):
    reply_to_id = await reply_id(event)
    uptime = await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    await edit_or_reply(event, "** ⌁︙ يتـم التـأكـد انتـظر قليلا رجاءا**")
    end = datetime.now()
    ms = (end - start).microseconds / 1000
    _, check_sgnirts = check_data_base_heal_th()
    EMOJI = gvarstatus("ALIVE_EMOJI") or "⿻┊‌‎"
    ALIVE_TEXT = gvarstatus("ALIVE_TEXT") or "**父[ 𝙳𝚁𝙰𝙶𝙾 𝙸𝚂 𝚆𝙾𝚁𝙺𝙸𝙽𝙶 ](t.me/Drago_dr)父**"
    DRAGO_IMG = gvarstatus("ALIVE_PIC") or Config.A_PIC or "https://telegra.ph/file/99b7fa93494f6a583b83d.mp4"
    dragoiq_caption = gvarstatus("ALIVE_TEMPLATE") or temp
    caption = dragoiq_caption.format(
        ALIVE_TEXT=ALIVE_TEXT,
        EMOJI=EMOJI,
        mention=mention,
        uptime=uptime,
        telever=version.__version__,
        dragover=DRAGOVERSION,
        pyver=python_version(),
        dbhealth=check_sgnirts,
        ping=ms,
        Tare5=installation_time,
    )
    if DRAGO_IMG:
        drago = [x for x in DRAGO_IMG.split()]
        PIC = random.choice(drago)
        try:
            await event.client.send_file(
                event.chat_id, PIC, caption=caption, reply_to=reply_to_id
            )
            await event.delete()
        except (WebpageMediaEmptyError, MediaEmptyError, WebpageCurlFailedError):
            return await edit_or_reply(
                event,
                f"**الميـديا خـطأ **\nغـير الرابـط بأستـخدام الأمـر  \n `.اضف_فار ALIVE_PIC رابط صورتك`\n\n**لا يمـكن الحـصول عـلى صـورة من الـرابـط :-** `{PIC}`",
            )
    else:
        await edit_or_reply(
            event,
            caption,
        )


temp = """{ALIVE_TEXT}
**‎{EMOJI}‌‎𝙽𝙰𝙼𝙴 𖠄 {mention}** ٫
**‌‎{EMOJI}‌‎𝙿𝚈𝚃𝙷𝙾𝙽 𖠄 `{pyver}`** ٫
**‌‎{EMOJI}‌‎𝙳𝚁𝙰𝙶𝙾 𖠄 `{telever}`** ٫
**‌‎{EMOJI}‌‎𝚄𝙿𝚃𝙸𝙼𝙴 𖠄 `{uptime}`** ٫
‌‎**{EMOJI}‌‎‌‎𝙿𝙸𝙽𝙶 𖠄 `{ping}`** ٫
‌‎**{EMOJI}‌‎‌‎𝚂𝙴𝚃𝚄𝙿 𝙳𝙰𝚃𝙴 𖠄 `{Tare5}`** ٫
**𖠄 𝗱𝗿𝗮𝗴𝗼 𝘂𝘀𝗲𝗿𝗯𝗼𝘁 𖠄**"""