from db.connection import connect_to_db
from db.verify_table import create_table
from db.load import load_data
from api.request import get_data_from_api
from db.delete import truncate_table

conn = connect_to_db()
create_table(conn)
truncate_table(conn)
data = get_data_from_api()
load_data(data,conn)
conn.cursor().close()
conn.close()

