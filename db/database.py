from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from common import constants as con
from pathlib import Path
from dotenv import load_dotenv
import os

load_dotenv()

DATABASE_URL=os.getenv(con.DB_URL_KEY)
if DATABASE_URL is None: DATABASE_URL=f'sqlite:///{Path(__file__).parent.parent / con.DB_FALLBACK_FOLDER / con.DB_FALLBACK_FILE}'
Engine=create_engine(DATABASE_URL)
SessionLocal=sessionmaker(bind=Engine)
Base=declarative_base()