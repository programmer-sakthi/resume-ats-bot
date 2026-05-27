from telegram import Update
from telegram.ext import ContextTypes

async def start(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    # RESET FLOW
    context.user_data.clear()

    context.user_data["state"] = (
        "waiting_for_resume"
    )

    await update.message.reply_text(
        "Upload your resume as a document."
    )