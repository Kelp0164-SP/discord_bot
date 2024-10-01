import random
import sqlite3

def random_int(n):
    intN = random.randint(1,n)
    return intN

def random_db_data_get(dbName):
    # データベースに接続
    conn = sqlite3.connect('C:\discord_bot_pg\SQL\discordBot.db')
    cursor = conn.cursor()
    # テーブル「OMIKUJI」から全てのデータを取得
    cursor.execute("SELECT * FROM " + str(dbName))
    rows = cursor.fetchall()
    # ランダムに1つのデータを選択
    result = random.choice(rows)
    conn.close()
    return result

def random_quiz_data_get(category_code):
    # データベースに接続
    conn = sqlite3.connect('C:\discord_bot_pg\SQL\discordBot.db')
    cursor = conn.cursor()
    cursor.execute("""
    SELECT *
    FROM QUIZ
    WHERE category = ?
    """, (category_code,)) 
    rows = cursor.fetchall()
    # ランダムに1つのデータを選択
    result = random.choice(rows)
    conn.close()
    return result
