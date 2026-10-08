'''
app/models.py
---------------
Review을 담을 테이블 생성
'''
from datetime import datetime

from sqlalchemy import DateTime, Float, String, Text, func
from sqlalchemy.orm import Mapped, mapped_column

from app.database import Base

class Review(Base):
    __tablename__ = "reviews"

    id: Mapped[int] = mapped_column(primary_key=True)
    review_text: Mapped[str] = mapped_column(Text)

    # LLM이 돌려주는 값이라 길이를 넉넉히 잡는다. (너무 짧으면 긴 값이 올 때 저장이 실패한다)
    # index=True : 감성/카테고리별로 모아 볼 때(GROUP BY, WHERE) 빠르게 찾기 위한 색인
    sentiment: Mapped[str] = mapped_column(String(50), index=True)
    category: Mapped[str] = mapped_column(String(50), index=True)
    summary: Mapped[str] = mapped_column(Text)
    confidence: Mapped[float] = mapped_column(Float)

    # 어떤 모델로 분석했는지. 모델이 바뀌면 결과 품질도 달라지므로 기록해 둔다.
    llm_model: Mapped[str] = mapped_column(String(100))

    # server_default=func.now() : 저장 시각을 파이썬이 아니라 DB가 채운다.
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())