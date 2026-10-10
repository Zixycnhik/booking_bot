import aiosqlite

DB_NAME = "DataBase.db"

async def init_db():
    async with aiosqlite.connect(DB_NAME) as db:
        await db.execute("""
            CREATE TABLE IF NOT EXISTS appointments (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER,
                user_name TEXT,
                service TEXT,
                date TEXT,
                time TEXT,
                status TEXT DEFAULT 'active',
                created_at TEXT DEFAULT CURRENT_TIMESTAMP
            )
        """)
        await db.commit()

async def add_appointment(user_id: int, user_name: str, service: str, date: str, time: str):
    async with aiosqlite.connect(DB_NAME) as db:
        await db.execute("""
            INSERT INTO appointments (user_id, user_name, service, date, time)
            VALUES (?, ?, ?, ?, ?)
        """,
            (user_id, user_name, service, date, time),
        )
        await db.commit()

async def get_taken_times(date: str) -> list[str]:
    async with aiosqlite.connect(DB_NAME) as db:
        async with db.execute("""
            SELECT time FROM appointments WHERE date = ? AND status = 'active'
        """,
            (date,),
        ) as cursor:
            rows = await cursor.fetchall()
    return [row[0] for row in rows]

async def get_user_appointments(user_id: int) -> list[tuple]:
    async with aiosqlite.connect(DB_NAME) as db:
        async with db.execute("""
            SELECT id, service, date, time
            FROM appointments WHERE user_id = ? AND status = 'active'
            ORDER BY date, time
        """,
            (user_id,),
        ) as cursor:
            rows = await cursor.fetchall()
    return rows

