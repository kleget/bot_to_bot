import sqlite3 as sq

async def db_update(text):
    with sq.connect(f'db.db') as con:
        sql = con.cursor()
        sql.execute(f"UPDATE users SET txt = (?) ", (str(text),))
        con.commit()

async def db_select():
    with sq.connect(f'db.db') as con:
        sql = con.cursor()
        sql.execute(f"SELECT txt FROM users")
        return sql.fetchone()