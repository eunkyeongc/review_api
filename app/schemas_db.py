'''
app/schemas_db.py
------------------
DB 관련 스키마
'''
from datetime import datetime

from pydantic import BaseModel, ConfigDict

from app.schemas import ReviewResponse

class ReviewRecord(ReviewResponse):
    '''리뷰를 기록하는 클래스'''
    # from_attributes=True : SQLAlchemy 객체를 바로 응답으로 변환
    model_config = ConfigDict(from_attributes=True)

    id: int
    review_text: str
    llm_model: str
    created_at: datetime

class StatsResponse(BaseModel):
    ''' 상태를 응답받도록 하는 클래스'''
    total: int
    by_sentiment: dict[str, int]
    by_category: dict[str, int]
