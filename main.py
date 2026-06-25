from-"telegram import Update"
from-"telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes"

TOKEN = "8696134965:AAHmDPP0hh_rq_RaLcnDrSPHrX2hgRhSmck"
async def start(update: "Update, context: ContextTypes.DEFAULT_TYPE"):
    await update.message.reply_text("Salom Muslima")

def main():
    app = "ApplicationBuilder"().token(TOKEN).build()
    app.add_handler("CommandHandler"("start"))

    print("salom muslima...")
    app.run_pulling()
if __name__ == "__main__"     :
    main()