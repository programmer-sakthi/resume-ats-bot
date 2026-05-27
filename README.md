# Resume ATS Bot

A Telegram bot designed to assist with Applicant Tracking System (ATS) workflows. The bot receives resumes from users, parses them using Optical Character Recognition (OCR), and accepts Job Descriptions (JDs) to help match candidates to jobs.

## Features

- **Telegram Interface**: Easy-to-use bot built with `python-telegram-bot`.
- **Resume Upload**: Supports multiple formats including PDF, JPG, JPEG, and PNG.
- **OCR Processing**: Utilizes `PaddleOCR` to scan resumes, extract text, and generate visualization images of the scanned documents.
- **Job Description Input**: Allows users to input Job Descriptions for comparison and analysis.

## Project Structure

- `bot.py`: The main entry point for running the Telegram bot.
- `handlers/`: Contains individual handlers for bot commands and messages.
  - `start_handler.py`: Handles the `/start` command.
  - `resume_handler.py`: Processes document uploads and triggers OCR scanning.
  - `jd_handler.py`: Receives and stores Job Description text.
- `services/`: Contains core business logic.
  - `ocr_service.py`: Integrates with PaddleOCR to scan and process resumes.
- `requirements.txt`: Python dependencies required for the project.

## Prerequisites

- Python 3.8+
- A Telegram Bot Token (obtained from [BotFather](https://core.telegram.org/bots#botfather))

## Installation

1. **Clone the repository:**

   ```bash
   git clone <repository_url>
   cd resume-ats-bot
   ```

2. **Create a virtual environment (optional but recommended):**

   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows use: .venv\Scripts\activate
   ```

3. **Install the dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables:**
   Create a `.env` file in the root directory and add your Telegram Bot Token:
   ```env
   BOT_TOKEN=your_telegram_bot_token_here
   ```

## Usage

Start the bot by running the main script:

```bash
python bot.py
```

Once the bot is running, open your Telegram app, search for your bot, and send the `/start` command to begin the interaction flow.

## Future Plans (In Progress)

- **Generative AI Integration**: Pass the extracted resume text and JD to a GenAI model to extract key points and generate a matching score or analysis in JSON format.
