import time
import sqlalchemy
from sqlalchemy import create_engine
import importlib

print('sqlalchemy', sqlalchemy.__version__)
print('imported create_engine')

for m in [
    'app.core.config',
    'app.db.database',
    'app.db.session',
    'app.api.v1',
    'app.api.v1.users',
    'app.services.user_service',
    'app.models.user',
    'app.models.resume',
    'app.schemas.user',
    'app.main',
]:
    print('importing', m)
    start = time.time()
    try:
        importlib.import_module(m)
        print('imported', m, round(time.time() - start, 3), 's')
    except Exception as e:
        print('failed', m, type(e).__name__, e)
        break

print('creating sqlite engine')
engine = create_engine('sqlite:///:memory:')
print('sqlite engine created', engine)
print('creating postgres engine')
engine = create_engine('postgresql+psycopg://career_user:career_password@localhost:5432/career_agent', echo=True, pool_pre_ping=True)
print('postgres engine created', engine)
