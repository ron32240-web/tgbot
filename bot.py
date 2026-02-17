import asyncio
import logging
from datetime import datetime
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = "8350979819:AAFpl46urjnfBodpa4deFhM2zqasryKHghU"
OWNER_ID = 8540192486

logging.basicConfig(level=logging.INFO)

async def log_user(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    username = f"@{user.username}" if user.username else "нет юзернейма"
    time = datetime.now().strftime("%d.%m.%Y %H:%M:%S")
    command = update.message.text
    await context.bot.send_message(chat_id=OWNER_ID, text=(
        f"[+] Новый запрос\n"
        f"━━━━━━━━━━━━━━━\n"
        f"Команда:  {command}\n"
        f"Имя:      {user.full_name}\n"
        f"Юзернейм: {username}\n"
        f"ID:       {user.id}\n"
        f"Время:    {time}\n"
        f"━━━━━━━━━━━━━━━"
    ))

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await log_user(update, context)
    await update.message.reply_text(
        "[+] Connecting to unknown host...\n"
        "[+] Identity: not found\n"
        "[+] Access: granted (unfortunately)\n\n"
        "Ё, че тебе здесь надо?\n\n"
        "/whoami\n"
        "/skills\n"
        "/status\n"
        "/contact\n"
        "/exit"
    )

async def whoami(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await log_user(update, context)
    await update.message.reply_text(
        "> whoami\n\n"
        "Человек который тушит пожары бензином.\n"
        "Идентификация: невозможна.\n"
        "Опасность: вероятна."
    )

async def skills(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await log_user(update, context)
    await update.message.reply_text(
        "> skills --list\n\n"
        "[01] Напиши мне хуйню — отвечу ещё хуже, но со смыслом.\n\n"
        "[02] Сразу говорю: ваше мнение может не совпадать с моим. "
        "Это значит что вы не правы и ваше мнение нужно поменять на моё. "
        "Потому что я прав, а вы нет.\n\n"
        "[03] Умею кастовать фиолетовый."
    )

async def status(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await log_user(update, context)
    await update.message.reply_text(
        "> status\n\n"
        "[~] Режим: наблюдатель\n"
        "[~] Активность: есть\n"
        "[~] Цель: неизвестна"
    )

async def contact(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await log_user(update, context)
    await update.message.reply_text(
        "> contact --find\n\n"
        "Как связаться? Никак)\n\n"
        "[ERROR] Connection refused."
    )

async def exit_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await log_user(update, context)
    await update.message.reply_text(
        "> exit\n\n"
        "[+] Закрываю соединение...\n"
        "[+] Тебя здесь не было.\n"
        "[+] Удачи.\n\n"
        "— [SYS://unknown]"
    )

def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("whoami", whoami))
    app.add_handler(CommandHandler("skills", skills))
    app.add_handler(CommandHandler("status", status))
    app.add_handler(CommandHandler("contact", contact))
    app.add_handler(CommandHandler("exit", exit_cmd))
    print("[+] Бот запущен")
    app.run_polling()

if name == "__main__":
    main()
