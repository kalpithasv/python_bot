import hikari
import lightbulb

bot =lightbulb.BotApp(token='MTAwn')
@bot.listen(hikari.startedEvent)
async def on_start(event):
    print("hello i'm a student")
bot.run()
