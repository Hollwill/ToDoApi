from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.ext.declarative import declarative_base

SQLALCHEMY_DATABASE_URL = "sqlite+aiosqlite:///./test_app.db"
# SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"

engine = create_async_engine(
    SQLALCHEMY_DATABASE_URL
)
SessionLocal = async_sessionmaker(bind=engine)

Base = declarative_base()


# async def init_db():
#     async with engine.begin() as conn:
#         await conn.run_sync(Base.metadata.create_all)


class AbstractDAO:
    def __init__(self):
        self.session = SessionLocal()

    def __aenter__(self):
        self.session.__aenter__()
        return self

    def __aexit__(self, exc_type, exc_val, exc_tb):
        self.session.__aexit__(exc_type, exc_val, exc_tb)
