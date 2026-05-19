from sqlalchemy.ext.asyncio.engine import AsyncEngine
from sqlalchemy.ext.asyncio.session import AsyncSession
import os 
from dotenv import load_dotenv 
from sqlalchemy.ext.asyncio import create_async_engine , async_sessionmaker 

load_dotenv()
database_url = os.environ["DATABASE_URL"]

engine: AsyncEngine = create_async_engine(
    database_url
)

create_session: async_sessionmaker[AsyncSession] = async_sessionmaker(
    bind = engine,
    expire_on_commit=False
)

async def get_session():
    async with create_session() as session:
        yield session 
