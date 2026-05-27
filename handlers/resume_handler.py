import os

from telegram import Update
from telegram.ext import ContextTypes

from services.ocr_service import scan_resume

DOWNLOAD_FOLDER = "resumes"

os.makedirs(
    DOWNLOAD_FOLDER,
    exist_ok=True
)

async def handle_resume(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    state = context.user_data.get(
        "state"
    )

    # IGNORE IF NOT EXPECTING RESUME
    if state != "waiting_for_resume":
        return

    # CHECK DOCUMENT
    if not update.message.document:

        await update.message.reply_text(
            "Please upload the resume as a document."
        )
        return

    document = update.message.document

    allowed_extensions = (
        ".pdf",
        ".jpg",
        ".jpeg",
        ".png"
    )

    if not document.file_name.lower().endswith(
        allowed_extensions
    ):

        await update.message.reply_text(
            "Unsupported file type."
        )
        return

    # DOWNLOAD FILE
    file = await context.bot.get_file(
        document.file_id
    )

    file_name = (
        f"{update.effective_user.id}_"
        f"{document.file_name}"
    )

    file_path = os.path.join(
        DOWNLOAD_FOLDER,
        file_name
    )

    await file.download_to_drive(
        file_path
    )

    # STORE FILE PATH
    context.user_data["resume_path"] = (
        file_path
    )

    await update.message.reply_text(
        "Scanning resume..."
    )

    # OCR
    output_images = scan_resume(
        file_path=file_path,
        output_dir=DOWNLOAD_FOLDER
    )

    # SEND OCR IMAGES
    for image_path in output_images:

        with open(image_path, "rb") as image:

            await update.message.reply_photo(
            photo=image,
            caption="Your scanned resume",
            read_timeout=60,
            write_timeout=60
            )

    # MOVE TO NEXT STEP
    context.user_data["state"] = (
        "waiting_for_jd"
    )

    await update.message.reply_text(
        "Now send the Job Description (JD) as text."
    )