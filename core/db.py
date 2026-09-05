import aiosqlite

from core.config import Settings
class DBConnect:
    def __init__(self, db_path: str):
        self.db_path = db_path
        self.connection = aiosqlite.Connection = None
        self.cursor = aiosqlite.Cursor = None
    
    async def connect(self):
        self.connection = await aiosqlite.connect(self.db_path)
        self.cursor = await self.connection.cursor()
        
    async def close(self):
        await self.cursor.close()
        await self.connection.close()
    
    async def excute(self, query: str, params: tuple = ()):
        await self.cursor.execute(query, params)
        await self.connection.commit()
    
    async def fetchone(self, query: str, params: tuple = ()) -> tuple:
        await self.cursor.execute(query, params)
        return await self.cursor.fetchone()

    async def fetchall(self, query: str, params: tuple = ()) -> list[tuple]:
        await self.cursor.execute(query, params)
        return await self.cursor.fetchall()

    async def get_requests(self):
        results = await db.fetchall("SELECT number FROM users")
        
        number = [str(row[0]) for row in results if row[0] is not None]
        
        text = "\n".join(number) if number else "Нет заявок"
        
        return text
    
    async def get_request(self, number: int):
        result = await db.fetchone("SELECT * FROM users WHERE number = ?", (number,))
        name = result[0]
        email = result[1]
        problem = result[2]
        text = f"Заявка: <code>{number}</code>\n\nИмя: {name}\nПочта: {email}\nПроблема: {problem}"
        return text
    
    async def delete_request(self, number: int):
        await db.excute("DELETE FROM users WHERE number = ?", (number,))
    
settings = Settings()
db = DBConnect(settings.get_db_url())