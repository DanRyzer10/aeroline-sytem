
import getpass

import oracledb
import dotenv
import os

dotenv.load_dotenv()


un = os.getenv('ORACLE_USER')
cs = 'localhost/xe'
pw = os.getenv('ORACLE_PASSWORD')
with oracledb.connect(user=un, password=pw, dsn=cs) as connection:
    with connection.cursor() as cursor:
        sql = """select sysdate from dual"""
        for r in cursor.execute(sql):
            print(r)
        connection.commit()
       
