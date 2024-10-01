import discord
import discordbot_common
import sqlite3
import random
import sys
import os
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, parent_dir)
import config
from discord.ext import commands
import asyncio
import discord.interactions

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

    elif message.content == '/!bow':
        # 5%の確率で元気な犬がでる
        flagN = discordbot_common.random_int(20)
        if (flagN == 20):
            await message.channel.send('わん！🐶')
        else:
            await message.channel.send('わん')#TODO 関数化

    # ペルソナにまつわるクイズを出題
    elif message.content == '/!pquiz':
        quiz = discordbot_common.random_quiz_data_get(0)
        question = quiz[1]
        options = quiz[2]
        await message.channel.send(f"{question}\n{options}\n答えを入力してね！")

        def check(m):
            return m.author == message.author and m.channel == message.channel

        try:
            # 答えを待つ
            msg = await client.wait_for('message', check=check, timeout=30.0)
        except asyncio.TimeoutError:
            await message.channel.send('時間切れです！次のクイズに進みましょう。')
        else:
            if msg.content.upper() == quiz[3]:
                await message.channel.send('正解！ 🎉')
            else:
                await message.channel.send(f'残念！答えは {quiz[3]} でした！')



# Botの起動とDiscordサーバーへの接続
client.run(TOKEN)
