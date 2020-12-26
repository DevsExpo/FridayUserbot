from fridaybot.modules.sql_helper import warns_sql as sql
from fridaybot.utils import friday_on_cmd


@friday.on(friday_on_cmd(pattern="warn(?: |$)(.*)"))
async def _s(event):
    user, reason = await get_user_from_event(event)
    sed = await friday.get_permissions(event.chat_id, user.id)
    if sed.is_admin:
        await event.edit("`Demn, Admins Can't Be Warned`")
        return
    dragon = await friday.get_permissions(event.chat_id, bot.uid)
    if not dragon.is_admin:
        await event.edit("`Demn, Me nOT Admin`")
        return
    limit, soft_warn = sql.get_warn_setting(event.chat_id)
    num_warns, reasons = sql.warn_user(user.id, event.chat_id, reason)
    if num_warns >= limit:
        sql.reset_warns(user.id, event.chat_id)
        if soft_warn:
            await friday.kick_participant(event.chat_id, user.id)
            reply = "{} warnings, {} has been kicked!".format(limit, user.id)
            await event.edit(reply)
        else:
            await friday.edit_permissions(event.chat_id, user.id, view_messages=False)
            reply = "{} warnings, {} has been banned!".format(
                limit, user.id, user.first_name
            )
            await event.edit(reply)
        for warn_reason in reasons:
            reply += "\n - {}".format(warn_reason)
    else:
        reply = "{} has {}/{} warnings... watch out!".format(user.id, num_warns, limit)
        if reason:
            reply += "\nReason for last warn:\n{}".format(reason)
        await event.edit(reply)


@friday.on(friday_on_cmd(pattern="rwarn(?: |$)(.*)"))
async def _(event):
    user, reason = await get_user_from_event(event)
    sed = await friday.get_permissions(event.chat_id, user.id)
    if sed.is_admin:
        await event.edit("Demn, Admins Can't Be Warned")
        return
    dragon = await friday.get_permissions(event.chat_id, bot.uid)
    if not dragon.is_admin:
        await event.edit("Demn, Me nOT Admin")
        return
    sql.reset_warns(user.id, event.chat_id)
    await event.edit("Warnings have been reset!")


@friday.on(friday_on_cmd(pattern="allwarns(?: |$)(.*)"))
async def __(event):
    user, reason = await get_user_from_event(event)
    result = sql.get_warns(user.id, event.chat_id)
    if result and result[0] != 0:
        num_warns, reasons = result
        limit, soft_warn = sql.get_warn_setting(event.chat_id)
        if reasons:
            text = (
                "This user has {}/{} warnings, for the following reasons: \n\n".format(
                    num_warns, limit
                )
            )
            for reason in reasons:
                text += "- {} \n".format(reason)
            await event.edit(text)
        else:
            await event.edit(
                "User has {}/{} warnings, but no reasons for any of them.".format(
                    num_warns, limit
                )
            )
    else:
        await event.edit("This user hasn't got any warnings!")


@friday.on(friday_on_cmd(pattern="slimit ?(.*)"))
async def m_(event):
    args = event.pattern_match.group(1)
    if args:
        if args.isdigit():
            if int(args) < 3:
                await event.edit("The minimum warn limit is 3!")
            else:
                sql.set_warn_limit(event.chat_id, int(args))
                await event.edit("Updated the warn limit to {}".format(args))
        else:
            await event.edit("Give me a number as an arg!")
    else:
        limit, soft_warn = sql.get_warn_setting(event.chat_id)
        await event.edit("The current warn limit is {}".format(limit))


@friday.on(friday_on_cmd(pattern="wap ?(.*)"))
async def m_(event):
    args = event.pattern_match.group(1)
    if args:
        if args.lower() in ("on", "yes"):
            sql.set_warn_strength(event.chat_id, False)
            await event.edit("Too many warns will now result in a ban!")
        elif args.lower() in ("off", "no"):
            sql.set_warn_strength(event.chat_id, True)
            await event.edit(
                "Too many warns will now result in a kick! Users will be able to join again after."
            )
        else:
            await event.edit("I only understand on/yes/no/off!")
    else:
        limit, soft_warn = sql.get_warn_setting(chat.id)
        if soft_warn:
            await event.edit(
                "Warns are currently set to **kick** users when they exceed the limits."
            )
        else:
            await event.edit(
                "Warns are currently set to **ban** users when they exceed the limits."
            )


async def get_user_from_event(event):
    """ Get the user from argument or replied message. """
    args = event.pattern_match.group(1).split(" ", 1)
    extra = None
    if event.reply_to_msg_id:
        previous_message = await event.get_reply_message()
        user_obj = await event.client.get_entity(previous_message.from_id)
        extra = event.pattern_match.group(1)
    elif args:
        user = args[0]
        if len(args) == 2:
            extra = args[1]

        if user.isnumeric():
            user = int(user)

        if not user:
            await event.edit("`Pass the user's username, id or reply!`")
            return

        if event.message.entities is not None:
            probable_user_mention_entity = event.message.entities[0]

            if isinstance(probable_user_mention_entity, MessageEntityMentionName):
                user_id = probable_user_mention_entity.user_id
                user_obj = await event.client.get_entity(user_id)
                return user_obj
        try:
            user_obj = await event.client.get_entity(user)
        except (TypeError, ValueError) as err:
            await event.edit(str(err))
            return None

    return user_obj, extra


async def get_user_from_id(user, event):
    if isinstance(user, str):
        user = int(user)

    try:
        user_obj = await event.client.get_entity(user)
    except (TypeError, ValueError) as err:
        await event.edit(str(err))
        return None

    return user_obj
