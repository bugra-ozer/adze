#Internal Modules
from db.database import Engine, Base
from db.storer import seed_providers
import app as api

#External Modules
from dotenv import load_dotenv

if __name__ == '__main__':
    load_dotenv()
    Base.metadata.create_all(Engine)
    seed_providers()
    api.app.run()