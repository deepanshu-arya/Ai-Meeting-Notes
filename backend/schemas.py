from pydantic import BaseModel

class MeetingResponse(BaseModel):
    id: int
    filename: str
    transcript: str
    summary: str
    action_points: str

    class Config:
        from_attributes = True