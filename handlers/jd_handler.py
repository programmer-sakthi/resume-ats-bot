from telegram import Update
from telegram.ext import ContextTypes


async def handle_jd(update: Update, context: ContextTypes.DEFAULT_TYPE):

    state = context.user_data.get("state")

    # IGNORE IF NOT EXPECTING JD
    if state != "waiting_for_jd":
        return

    jd_text = update.message.text

    # STORE JD
    context.user_data["jd"] = jd_text

    print("\n===== JD RECEIVED =====\n")
    print(jd_text)

    # COMPLETE FLOW
    context.user_data["state"] = "completed"

    await update.message.reply_text(
        "JD received successfully.", read_timeout=60, write_timeout=60
    )

    # DEBUG OUTPUT
    print("\n===== USER DATA =====\n")
    print(context.user_data)
