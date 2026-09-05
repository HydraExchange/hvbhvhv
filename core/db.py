import os
import aiosqlite


class DBConnect:
    def __init__(self, db_path: str):
        self.db_path = db_path
        self.connect_db = None
        self.cursor = None

    async def connect(self):
        db_dir = os.path.dirname(self.db_path)

        if db_dir:
            os.makedirs(db_dir, exist_ok=True)

        self.connect_db = await aiosqlite.connect(self.db_path)
        self.cursor = await self.connect_db.cursor()

        # Создаём таблицу заявок, если её ещё нет
        await self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                email TEXT NOT NULL,
                TEXT TEXT NOT NULL,
                number INTEGER NOT NULL
            )
        """)

        await self.connect_db.commit()

    async def excute(self, query, params=()):
        await self.cursor.execute(query, params)
        await self.connect_db.commit()

    async def fetchall(self, query, params=()):
        await self.cursor.execute(query, params)
        return await self.cursor.fetchall()

    async def fetchone(self, query, params=()):
        await self.cursor.execute(query, params)
        return await self.cursor.fetchone()

    async def close(self):
        if self.cursor:
            await self.cursor.close()

        if self.connect_db:
            await self.connect_db.close()


db = DBConnect("/app/data/base.db")
