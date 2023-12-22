import os, oracledb,dotenv
from sqlalchemy import create_engine
from sqlalchemy import text
dotenv.load_dotenv()
un = os.getenv('ORACLE_USER')
cs = 'localhost/xe'
pw = os.getenv('ORACLE_PASSWORD')
thick_mode = False
engine = create_engine(
    f"oracle+oracledb://{un}:{pw}@localhost:1521/xe",
    thick_mode=thick_mode,
)
with engine.connect() as connection:
    print(connection.scalar(text("""SELECT UNIQUE CLIENT_DRIVER
                                    FROM V$SESSION_CONNECT_INFO
                                    WHERE SID = SYS_CONTEXT('USERENV', 'SID')""")))