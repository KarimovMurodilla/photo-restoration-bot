from typing import Sequence
from dataclasses import dataclass
from datetime import datetime

from sqlalchemy import select
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.ext.asyncio import AsyncSession

from utils.db_api.base import Base
from utils.db_api.models import Users

from data.config import DATABASE_URL


class Database:
    async def load(self) -> AsyncSession:
        engine = create_async_engine(
            DATABASE_URL,
            future=True
        )

        async with engine.begin() as conn:
            await conn.run_sync(Base.metadata.create_all)

        async_sessionmaker = sessionmaker(
            engine, expire_on_commit=False, class_=AsyncSession
        )

        self.async_session = async_sessionmaker

    # ---Для пользователей---

    async def reg_user(self, user_id: str, username: str, first_name: str):
        """Регистрация пользователя"""
        async with self.async_session() as session:
            session: AsyncSession
            await session.merge(
                Users(
                    user_id=user_id,
                    username=username,
                    first_name=first_name
                )
            )
            await session.commit()

    async def get_user(self, user_id) -> Users:
        """Получения пользователя"""
        async with self.async_session() as session:
            session: AsyncSession

            response = await session.get(Users, user_id)
            return response
    
    async def get_all_users(self) -> Sequence[Users]:
        """Получения всех пользователей"""
        async with self.async_session() as session:
            session: AsyncSession

            response = await session.execute(select(Users))
            return response.scalars().all()
