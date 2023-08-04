from sqlalchemy import Boolean, Column, String

from . import BASE, SESSION


class Locks(BASE):
    __tablename__ = "locks"
    chat_id = Column(String(14), primary_key=True)
    # Booleans are for "is this locked", _NOT_ "is this allowed"
    bots = Column(Boolean, default=False)
    commands = Column(Boolean, default=False)
    email = Column(Boolean, default=False)
    forward = Column(Boolean, default=False)
    url = Column(Boolean, default=False)

    def __init__(self, chat_id):
        self.chat_id = str(chat_id)  # ensure string
        self.bots = False
        self.commands = False
        self.email = False
        self.forward = False
        self.url = False


Locks.__table__.create(checkfirst=True)


def init_locks(chat_id, reset=False):
    curr_restr = SESSION.query(Locks).get(str(chat_id))
    if reset:
        SESSION.delete(curr_restr)
        SESSION.flush()
    restr = Locks(str(chat_id))
    SESSION.add(restr)
    SESSION.commit()
    return restr


def update_lock(chat_id, lock_type, locked):
    curr_perm = SESSION.query(Locks).get(str(chat_id))
    if not curr_perm:
        curr_perm = init_locks(chat_id)
    if lock_type == "bots":
        curr_perm.bots = locked
    elif lock_type == "commands":
        curr_perm.commands = locked
    elif lock_type == "email":
        curr_perm.email = locked
    elif lock_type == "forward":
        curr_perm.forward = locked
    elif lock_type == "url":
        curr_perm.url = locked
    SESSION.add(curr_perm)
    SESSION.commit()


def is_locked(chat_id, lock_type):
    curr_perm = SESSION.query(Locks).get(str(chat_id))
    SESSION.close()
    if not curr_perm:
        return False
    if lock_type == "bots":
        return curr_perm.bots
    if lock_type == "commands":
        return curr_perm.commands
    if lock_type == "email":
        return curr_perm.email
    if lock_type == "forward":
        return curr_perm.forward
    if lock_type == "url":
        return curr_perm.url

dragovois1 = "drago/helpers/styles/Voic/تخوني ؟.ogg"
dragovois2 = "drago/helpers/styles/Voic/مستمرة الكلاوات.ogg"
dragovois3 = "drago/helpers/styles/Voic/احب العراق.ogg"
dragovois4 = "drago/helpers/styles/Voic/احبك .ogg"
dragovois5 = "drago/helpers/styles/Voic/اخت التنيج.ogg"
dragovois6 = "drago/helpers/styles/Voic/اذا اكمشك ماكو.ogg"
dragovois7 = "drago/helpers/styles/Voic/اسكت.ogg"
dragovois8 = "drago/helpers/styles/Voic/افتهمنا.ogg"
dragovois9 = "drago/helpers/styles/Voic/اكل خرة لك.ogg"
dragovois10 = "drago/helpers/styles/Voic/الة اخلي العراق امريكا.ogg"
dragovois11 = "drago/helpers/styles/Voic/الكعدة وياكم حلوة.ogg"
dragovois12 = "drago/helpers/styles/Voic/الكمر اني النجم اني.ogg"
dragovois13 = "drago/helpers/styles/Voic/اللهم لا شماتة.ogg"
dragovois14 = "drago/helpers/styles/Voic/انا ما اكدر بعد.ogg"
dragovois15 = "drago/helpers/styles/Voic/بقولك اي يا قلبي كسمك.ogg"
dragovois16 = "drago/helpers/styles/Voic/تف على شرفك.ogg"
dragovois17 = "drago/helpers/styles/Voic/شجلبت.ogg"
dragovois18 = "drago/helpers/styles/Voic/شكد شفت ناس مدودة.ogg"
dragovois19 = "drago/helpers/styles/Voic/صباح القنادر.ogg"
dragovois20 = "drago/helpers/styles/Voic/ضحكة فيطية.ogg"
dragovois21 = "drago/helpers/styles/Voic/طار القلب.ogg"
dragovois22 = "drago/helpers/styles/Voic/غطيلي واغطيلك.ogg"
dragovois23 = "drago/helpers/styles/Voic/في منتصف الجبهة.ogg"
dragovois24 = "drago/helpers/styles/Voic/لا تقتل المتعة .ogg"
dragovois25 = "drago/helpers/styles/Voic/لا لتغلط.ogg"
dragovois26 = "drago/helpers/styles/Voic/لا يمه لا محاجي.ogg"
dragovois27 = "drago/helpers/styles/Voic/لحد يحجي وياي.ogg"
dragovois28 = "drago/helpers/styles/Voic/ما ادري يعني.ogg"
dragovois29 = "drago/helpers/styles/Voic/منو انت لخاطر النجف.ogg"
dragovois30 = "drago/helpers/styles/Voic/مو صوجكم يا زبايل.ogg"
dragovois31 = "drago/helpers/styles/Voic/والله انت خوش تسولف.ogg"
dragovois32 = "drago/helpers/styles/Voic/يعععع.ogg"
dragovois33 = "drago/helpers/styles/Voic/زيج.ogg"
dragovois34 = "drago/helpers/styles/Voic/زيح2.ogg"
dragovois35 = "drago/helpers/styles/Voic/يعني مااعرف.ogg"
dragovois36 = "drago/helpers/styles/Voic/يامرحبا.ogg"
dragovois37 = "drago/helpers/styles/Voic/منو انتة.ogg"
dragovois38 = "drago/helpers/styles/Voic/ماتستحي.ogg"
dragovois39 = "drago/helpers/styles/Voic/كعدت الديوث.ogg"
dragovois40 = "drago/helpers/styles/Voic/عيب.ogg"
dragovois41 = "drago/helpers/styles/Voic/عنعانم.ogg"
dragovois42 = "drago/helpers/styles/Voic/طبك مرض.ogg"
dragovois43 = "drago/helpers/styles/Voic/سييي.ogg"
dragovois44 = "drago/helpers/styles/Voic/سبيدر مان.ogg"
dragovois45 = "drago/helpers/styles/Voic/خاف حرام.ogg"
dragovois46 = "drago/helpers/styles/Voic/تحيه لاختك.ogg"
dragovois47 = "drago/helpers/styles/Voic/امشي كحبة.ogg"
dragovois48 = "drago/helpers/styles/Voic/امداك.ogg"
dragovois49 = "drago/helpers/styles/Voic/الحس.ogg"
dragovois50 = "drago/helpers/styles/Voic/افتهمنا.ogg"
dragovois51 = "drago/helpers/styles/Voic/اطلع برا.ogg"
dragovois52 = "drago/helpers/styles/Voic/اخت التنيج.ogg"
dragovois53 = "drago/helpers/styles/Voic/اوني تشان.ogg"
dragovois54 = "drago/helpers/styles/Voic/اوني تشان2.ogg"

def get_locks(chat_id):
    try:
        return SESSION.query(Locks).get(str(chat_id))
    finally:
        SESSION.close()
