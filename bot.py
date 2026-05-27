import logging
import os

from dotenv import load_dotenv

from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters

from handlers.start_handler import start
from handlers.resume_handler import handle_resume
from handlers.jd_handler import handle_jd

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")

# LOGGING
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)


def main():

    application = ApplicationBuilder().token(BOT_TOKEN).build()

    # START COMMAND
    application.add_handler(CommandHandler("start", start))

    # RESUME HANDLER
    application.add_handler(MessageHandler(filters.Document.ALL, handle_resume))

    # JD HANDLER
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_jd))

    print("BOT IS RUNNING !!!!")

    application.run_polling()


if __name__ == "__main__":
    main()
