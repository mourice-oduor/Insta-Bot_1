from instabot import Bot

bot = Bot()

#bot.login(ask_for_code=True)
bot.login(username="IG_Uname",password="PASS_HERE")
#here, the name I've passed was the account name which contain users to be follwed
#n=20, the number of followers to be followed on that account
bot.follow_followers('mourice_otieno_moryso', nfollow=20)

