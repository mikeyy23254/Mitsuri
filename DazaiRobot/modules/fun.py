import html
import random
import time

from telegram import ChatPermissions, ParseMode, Update
from telegram.error import BadRequest
from telegram.ext import CallbackContext

import DazaiRobot.modules.fun_strings as fun_strings
from DazaiRobot import dispatcher
from DazaiRobot.modules.disable import DisableAbleCommandHandler
from DazaiRobot.modules.helper_funcs.chat_status import is_user_admin
from DazaiRobot.modules.helper_funcs.extraction import extract_user


def runs(update: Update, context: CallbackContext):
    update.effective_message.reply_text(random.choice(fun_strings.RUN_STRINGS))


def sanitize(update: Update, context: CallbackContext):
    message = update.effective_message
    name = (
        message.reply_to_message.from_user.first_name
        if message.reply_to_message
        else message.from_user.first_name
    )
    reply_animation = (
        message.reply_to_message.reply_animation
        if message.reply_to_message
        else message.reply_animation
    )
    reply_animation(random.choice(fun_strings.GIFS), caption=f"*Sanitizes {name}*")


def slap(update: Update, context: CallbackContext):
    bot, args = context.bot, context.args
    message = update.effective_message
    chat = update.effective_chat

    reply_text = (
        message.reply_to_message.reply_text
        if message.reply_to_message
        else message.reply_text
    )

    curr_user = html.escape(message.from_user.first_name)
    user_id = extract_user(message, args)

    if user_id == bot.id:
        temp = random.choice(fun_strings.SLAP_FALLEN_TEMPLATES)

        if isinstance(temp, list):
            if temp[2] == "tmute":
                if is_user_admin(chat, message.from_user.id):
                    reply_text(temp[1])
                    return

                mutetime = int(time.time() + 60)
                bot.restrict_chat_member(
                    chat.id,
                    message.from_user.id,
                    until_date=mutetime,
                    permissions=ChatPermissions(can_send_messages=False),
                )
            reply_text(temp[0])
        else:
            reply_text(temp)
        return

    if user_id:
        slapped_user = bot.get_chat(user_id)
        user1 = curr_user
        user2 = html.escape(slapped_user.first_name)

    else:
        user1 = bot.first_name
        user2 = curr_user

    temp = random.choice(fun_strings.SLAP_TEMPLATES)
    item = random.choice(fun_strings.ITEMS)
    hit = random.choice(fun_strings.HIT)
    throw = random.choice(fun_strings.THROW)

    if update.effective_user.id == 1096215023:
        temp = "@NeoTheKitty scratches {user2}"

    reply = temp.format(user1=user1, user2=user2, item=item, hits=hit, throws=throw)

    reply_text(reply, parse_mode=ParseMode.HTML)


def pat(update: Update, context: CallbackContext):
    bot = context.bot
    args = context.args
    message = update.effective_message

    reply_to = message.reply_to_message if message.reply_to_message else message

    curr_user = html.escape(message.from_user.first_name)
    user_id = extract_user(message, args)

    if user_id:
        patted_user = bot.get_chat(user_id)
        user1 = curr_user
        user2 = html.escape(patted_user.first_name)

    else:
        user1 = bot.first_name
        user2 = curr_user

    pat_type = random.choice(("Text", "Gif", "Sticker"))
    if pat_type == "Gif":
        try:
            temp = random.choice(fun_strings.PAT_GIFS)
            reply_to.reply_animation(temp)
        except BadRequest:
            pat_type = "Text"

    if pat_type == "Sticker":
        try:
            temp = random.choice(fun_strings.PAT_STICKERS)
            reply_to.reply_sticker(temp)
        except BadRequest:
            pat_type = "Text"

    if pat_type == "Text":
        temp = random.choice(fun_strings.PAT_TEMPLATES)
        reply = temp.format(user1=user1, user2=user2)
        reply_to.reply_text(reply, parse_mode=ParseMode.HTML)

def kawai(update: Update, context: CallbackContext):
    bot = context.bot
    args = context.args
    message = update.effective_message

    reply_to = message.reply_to_message if message.reply_to_message else message

    curr_user = html.escape(message.from_user.first_name)
    user_id = extract_user(message, args)

    if user_id:
        kawaii_user = bot.get_chat(user_id)
        user1 = curr_user
        user2 = html.escape(kawaii_user.first_name)

    else:
        user1 = bot.first_name
        user2 = curr_user

    kawai_type = random.choice(("Text", "Gif", "Sticker"))
    if kawai_type == "Gif":
        try:
            temp = random.choice(fun_strings.KAWAI_GIFS)
            reply_to.reply_animation(temp)
        except BadRequest:
            hug_type = "Sticker"

    if kawai_type == "Sticker":
        try:
            temp = random.choice(fun_strings.KAWAI_STICKERS)
            reply_to.reply_sticker(temp)
        except BadRequest:
            kawai_type = "Gif"

    if kawai_type == "Text":
        temp = random.choice(fun_strings.KAWAI_TEMPLATES)
        reply = temp.format(user1=user1, user2=user2)
        reply_to.reply_text(reply, parse_mode=ParseMode.HTML)

def kiss(update: Update, context: CallbackContext):
    bot = context.bot
    args = context.args
    message = update.effective_message

    reply_to = message.reply_to_message if message.reply_to_message else message

    curr_user = html.escape(message.from_user.first_name)
    user_id = extract_user(message, args)

    if user_id:
        kissed_user = bot.get_chat(user_id)
        user1 = curr_user
        user2 = html.escape(kissed_user.first_name)

    else:
        user1 = bot.first_name
        user2 = curr_user

    kiss_type = random.choice(("Text", "Gif", "Sticker"))
    if kiss_type == "Gif":
        try:
            temp = random.choice(fun_strings.KISS_GIFS)
            reply_to.reply_animation(temp)
        except BadRequest:
            kiss_type = "Sticker"

    if kiss_type == "Sticker":
        try:
            temp = random.choice(fun_strings.KISS_STICKERS)
            reply_to.reply_sticker(temp)
        except BadRequest:
            kiss_type = "Gif"

    if kiss_type == "Text":
        temp = random.choice(fun_strings.KISS_TEMPLATES)
        reply = temp.format(user1=user1, user2=user2)
        reply_to.reply_text(reply, parse_mode=ParseMode.HTML)


def hug(update: Update, context: CallbackContext):
    bot = context.bot
    args = context.args
    message = update.effective_message

    reply_to = message.reply_to_message if message.reply_to_message else message

    curr_user = html.escape(message.from_user.first_name)
    user_id = extract_user(message, args)

    if user_id:
        hugged_user = bot.get_chat(user_id)
        user1 = curr_user
        user2 = html.escape(hugged_user.first_name)

    else:
        user1 = bot.first_name
        user2 = curr_user

    hug_type = random.choice(("Text", "Gif", "Sticker"))
    if hug_type == "Gif":
        try:
            temp = random.choice(fun_strings.HUG_GIFS)
            reply_to.reply_animation(temp)
        except BadRequest:
            hug_type = "Sticker"

    if hug_type == "Sticker":
        try:
            temp = random.choice(fun_strings.HUG_STICKERS)
            reply_to.reply_sticker(temp)
        except BadRequest:
            hug_type = "Gif"

    if hug_type == "Text":
        temp = random.choice(fun_strings.HUG_TEMPLATES)
        reply = temp.format(user1=user1, user2=user2)
        reply_to.reply_text(reply, parse_mode=ParseMode.HTML)

def bam(update: Update, context: CallbackContext):
    bot = context.bot
    args = context.args
    message = update.effective_message

    reply_to = message.reply_to_message if message.reply_to_message else message

    curr_user = html.escape(message.from_user.first_name)
    user_id = extract_user(message, args)

    if user_id:
        bammed_user = bot.get_chat(user_id)
        user1 = curr_user
        user2 = html.escape(bammed_user.first_name)

    else:
        user1 = bot.first_name
        user2 = curr_user

    bam_type = random.choice(("Text", "Gif", "Sticker"))
    if bam_type == "Gif":
        try:
            temp = random.choice(fun_strings.BAM_GIFS)
            reply_to.reply_animation(temp)
        except BadRequest:
            bam_type = "Sticker"

    if bam_type == "Sticker":
        try:
            temp = random.choice(fun_strings.BAM_STICKERS)
            reply_to.reply_sticker(temp)
        except BadRequest:
            bam_type = "Gif"

    if bam_type == "Text":
        temp = random.choice(fun_strings.BAM_TEMPLATES)
        reply = temp.format(user1=user1, user2=user2)
        reply_to.reply_text(reply, parse_mode=ParseMode.HTML)

def gbam(update: Update, context: CallbackContext):
    bot = context.bot
    args = context.args
    message = update.effective_message

    reply_to = message.reply_to_message if message.reply_to_message else message

    curr_user = html.escape(message.from_user.first_name)
    user_id = extract_user(message, args)

    if user_id:
        gbammed_user = bot.get_chat(user_id)
        user1 = curr_user
        user2 = html.escape(gbammed_user.first_name)

    else:
        user1 = bot.first_name
        user2 = curr_user

    gbam_type = random.choice(("Text", "Gif", "Sticker"))
    if gbam_type == "Gif":
        try:
            temp = random.choice(fun_strings.GBAM_GIFS)
            reply_to.reply_animation(temp)
        except BadRequest:
            gbam_type = "Sticker"

    if gbam_type == "Sticker":
        try:
            temp = random.choice(fun_strings.GBAM_STICKERS)
            reply_to.reply_sticker(temp)
        except BadRequest:
            gbam_type = "Gif"

    if gbam_type == "Text":
        temp = random.choice(fun_strings.GBAM_TEMPLATES)
        reply = temp.format(user1=user1, user2=user2)
        reply_to.reply_text(reply, parse_mode=ParseMode.HTML)

def roll(update: Update, context: CallbackContext):
    update.message.reply_text(random.choice(range(1, 7)))


def shout(update: Update, context: CallbackContext):
    args = context.args
    text = " ".join(args)
    result = []
    result.append(" ".join(list(text)))
    for pos, symbol in enumerate(text[1:]):
        result.append(symbol + " " + "  " * pos + symbol)
    result = list("\n".join(result))
    result[0] = text[0]
    result = "".join(result)
    msg = "```\n" + result + "```"
    return update.effective_message.reply_text(msg, parse_mode="MARKDOWN")


def toss(update: Update, context: CallbackContext):
    update.message.reply_text(random.choice(fun_strings.TOSS))


def shrug(update: Update, context: CallbackContext):
    msg = update.effective_message
    reply_text = (
        msg.reply_to_message.reply_text if msg.reply_to_message else msg.reply_text
    )
    reply_text(r"¯\_(ツ)_/¯")


def bluetext(update: Update, context: CallbackContext):
    msg = update.effective_message
    reply_text = (
        msg.reply_to_message.reply_text if msg.reply_to_message else msg.reply_text
    )
    reply_text(
        "/BLUE /TEXT\n/MUST /CLICK\n/I /AM /A /STUPID /ANIMAL /THAT /IS /ATTRACTED /TO /COLORS"
    )


def rlg(update: Update, context: CallbackContext):
    eyes = random.choice(fun_strings.EYES)
    mouth = random.choice(fun_strings.MOUTHS)
    ears = random.choice(fun_strings.EARS)

    if len(eyes) == 2:
        repl = ears[0] + eyes[0] + mouth[0] + eyes[1] + ears[1]
    else:
        repl = ears[0] + eyes[0] + mouth[0] + eyes[0] + ears[1]
    update.message.reply_text(repl)


def decide(update: Update, context: CallbackContext):
    reply_text = (
        update.effective_message.reply_to_message.reply_text
        if update.effective_message.reply_to_message
        else update.effective_message.reply_text
    )
    reply_text(random.choice(fun_strings.DECIDE))


def eightball(update: Update, context: CallbackContext):
    reply_text = (
        update.effective_message.reply_to_message.reply_text
        if update.effective_message.reply_to_message
        else update.effective_message.reply_text
    )
    reply_text(random.choice(fun_strings.EIGHTBALL))


def table(update: Update, context: CallbackContext):
    reply_text = (
        update.effective_message.reply_to_message.reply_text
        if update.effective_message.reply_to_message
        else update.effective_message.reply_text
    )
    reply_text(random.choice(fun_strings.TABLE))


__help__ = """
 ❍ /runs*:* reply a random string from an array of replies
 ❍ /slap*:* slap a user, or get slapped if not a reply
 ❍ /shrug*:* get shrug XD
 ❍ /table*:* get flip/unflip :v
 ❍ /decide*:* Randomly answers yes/no/maybe
 ❍ /toss*:* Tosses A coin
 ❍ /bluetext*:* check urself :V
 ❍ /roll*:* Roll a dice
 ❍ /rlg*:* Join ears,nose,mouth and create an emo ;-;
 ❍ /shout <keyword>*:* write anything you want to give loud shout
 ❍ /weebify <text>*:* returns a weebified text
 ❍ /sanitize*:* always use this before /pat or any contact
 ❍ /pat*:* pats a user, or get patted
 ❍ /bam*:* troll a user, or get trolled
 ❍ /gbam*:* troll a user, or get trolled
 ❍ /kiss*:* kiss a user, or get kissed
 ❍ /kawai*:* kawaii
 ❍ /hug*:* hug a user, or get hugged
 ❍ /8ball*:* predicts using 8ball method 
"""

SANITIZE_HANDLER = DisableAbleCommandHandler("sanitize", sanitize, run_async=True)
RUNS_HANDLER = DisableAbleCommandHandler("runs", runs, run_async=True)
SLAP_HANDLER = DisableAbleCommandHandler("slap", slap, run_async=True)
PAT_HANDLER = DisableAbleCommandHandler("pat", pat, run_async=True)
KISS_HANDLER = DisableAbleCommandHandler("kiss", kiss, run_async=True)
KAWAI_HANDLER = DisableAbleCommandHandler("kawai", kawai, run_async=True)
HUG_HANDLER = DisableAbleCommandHandler("hug", hug, run_async=True)
BAM_HANDLER = DisableAbleCommandHandler("bam", bam, run_async=True)
GBAM_HANDLER = DisableAbleCommandHandler("gbam", gbam, run_async=True)
ROLL_HANDLER = DisableAbleCommandHandler("roll", roll, run_async=True)
TOSS_HANDLER = DisableAbleCommandHandler("toss", toss, run_async=True)
SHRUG_HANDLER = DisableAbleCommandHandler("shrug", shrug, run_async=True)
BLUETEXT_HANDLER = DisableAbleCommandHandler("bluetext", bluetext, run_async=True)
RLG_HANDLER = DisableAbleCommandHandler("rlg", rlg, run_async=True)
DECIDE_HANDLER = DisableAbleCommandHandler("decide", decide, run_async=True)
EIGHTBALL_HANDLER = DisableAbleCommandHandler("8ball", eightball, run_async=True)
TABLE_HANDLER = DisableAbleCommandHandler("table", table, run_async=True)
SHOUT_HANDLER = DisableAbleCommandHandler("shout", shout, run_async=True)

dispatcher.add_handler(SHOUT_HANDLER)
dispatcher.add_handler(SANITIZE_HANDLER)
dispatcher.add_handler(RUNS_HANDLER)
dispatcher.add_handler(SLAP_HANDLER)
dispatcher.add_handler(PAT_HANDLER)
dispatcher.add_handler(KISS_HANDLER)
dispatcher.add_handler(KAWAI_HANDLER)
dispatcher.add_handler(HUG_HANDLER)
dispatcher.add_handler(BAM_HANDLER)
dispatcher.add_handler(GBAM_HANDLER)
dispatcher.add_handler(ROLL_HANDLER)
dispatcher.add_handler(TOSS_HANDLER)
dispatcher.add_handler(SHRUG_HANDLER)
dispatcher.add_handler(BLUETEXT_HANDLER)
dispatcher.add_handler(RLG_HANDLER)
dispatcher.add_handler(DECIDE_HANDLER)
dispatcher.add_handler(EIGHTBALL_HANDLER)
dispatcher.add_handler(TABLE_HANDLER)

__mod_name__ = "Fᴜɴ​"
__command_list__ = [
    "runs",
    "slap",
    "roll",
    "toss",
    "shrug",
    "bluetext",
    "rlg",
    "decide",
    "table",
    "pat",
    "kawai",
    "hug",
    "kiss",
    "bam",
    "gbam",
    "sanitize",
    "shout",
    "weebify",
    "8ball",
]
__handlers__ = [
    RUNS_HANDLER,
    SLAP_HANDLER,
    PAT_HANDLER,
    KISS_HANDLER,
    KAWAI_HANDLER,
    HUG_HANDLER,
    BAM_HANDLER,
    GBAM_HANDLER,
    ROLL_HANDLER,
    TOSS_HANDLER,
    SHRUG_HANDLER,
    BLUETEXT_HANDLER,
    RLG_HANDLER,
    DECIDE_HANDLER,
    TABLE_HANDLER,
    SANITIZE_HANDLER,
    SHOUT_HANDLER,
    EIGHTBALL_HANDLER,
]
