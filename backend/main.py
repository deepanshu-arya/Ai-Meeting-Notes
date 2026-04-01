from fastapi import FastAPI, UploadFile, File, Depends
import shutil
import os
from fastapi.middleware.cors import CORSMiddleware

from database import SessionLocal, engine
import models
from ai_utils import generate_summary, extract_action_points
from pdf_generator import create_pdf

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # allow all
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/upload/")
async def upload_file(file: UploadFile = File(...), db=Depends(get_db)):
    content = await file.read()
    text = content.decode("utf-8")

    summary = generate_summary(text)
    action_points = extract_action_points(text)

    meeting = models.Meeting(
        filename=file.filename,
        transcript=text,
        summary=summary,
        action_points=action_points
    )

    db.add(meeting)
    db.commit()
    db.refresh(meeting)

    pdf_path = create_pdf(file.filename, summary, action_points)

    return {
        "id": meeting.id,
        "summary": summary,
        "action_points": action_points,
        "pdf": pdf_path
    }

@app.get("/meetings/")
def get_meetings(db=Depends(get_db)):
    return db.query(models.Meeting).all()


