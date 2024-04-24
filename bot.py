#coding=utf-8
#!/bin/python3

############################################
#    PYTHON COOKIES EXTRACTOR BOT          #
#          BOT VERSION: 1.0.0              #
#        AUTHOR : SAMUEL MUNYOKI           #
#           LICENSE :  MIT                 #
############################################

import asyncio
from telegram import Update, Bot
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters

# async def LogoutBot():
#     botlogout = Bot(token="6532185799:AAGGRGm1mtRu8uY3_5o2LucTAj6Xaqkdha8")
#     await botlogout.log_out()

# asyncio.run(LogoutBot())


async def downloader(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # .bot.get_file(update.message.document)
    file = await context.bot.get_file(update.message.document)
    await file.download_to_drive()
    await update.message.reply_text("File Downloaded")


async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')


app = ApplicationBuilder().token("6532185799:AAGGRGm1mtRu8uY3_5o2LucTAj6Xaqkdha8").base_url("http://localhost:8081/").local_mode(True).build()
# app = ApplicationBuilder().token("6532185799:AAGGRGm1mtRu8uY3_5o2LucTAj6Xaqkdha8").build()

app.add_handler(CommandHandler("hello", hello))
app.add_handler(MessageHandler(filters.Document.FileExtension(".zip", case_sensitive=False) | filters.Document.FileExtension(".7z", case_sensitive=False) | filters.Document.FileExtension(".rar", case_sensitive=False), downloader))


app.run_polling()