# インストールした discord.py を読み込む
import discord
import discordbot_common
import sqlite3
import random
import config

# 自分のBotのアクセストークンに置き換えてください
TOKEN = config.TOKEN
# 接続に必要なオブジェクトを生成
client = discord.Client(intents=discord.Intents.all())

# 起動時に動作する処理
@client.event
async def on_ready():
    # 起動したらターミナルにログイン通知が表示される
    print('ログインしました')

# メッセージ受信時に動作する処理
@client.event
async def on_message(message):
    # メッセージ送信者がBotだった場合は無視する
    if message.author.bot:
        return

    # 「/!neko」と発言したら「にゃーん」が返る処理
    if message.content == '/!neko':
        # 5%の確率で元気な猫がでる
        flagN = discordbot_common.random_int(20)
        if (flagN == 20):
            await message.channel.send('にゃーん！🐱')
        else:
            await message.channel.send('にゃーん')

    # 「/!kuji」でおみくじ
    elif message.content == '/!kuji':
        kuji_result = discordbot_common.random_db_data_get('OMIKUJI')
        # 選択したデータを表示
        await message.channel.send(kuji_result[1])

# Botの起動とDiscordサーバーへの接続
client.run(TOKEN)
