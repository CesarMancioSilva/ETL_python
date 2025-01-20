
import pandas as pd 
import psycopg2
from psycopg2 import connect, sql

def connect_to_db():
        connection = psycopg2.connect(
            host='localhost',
            database='youtube',
            user="postgres",
            password='cesarms2025',
            port=5432,
        )
        return connection
    
    
def create_table():
    table_query="""
    CREATE TABLE IF NOT EXISTS video_data (
        id SERIAL PRIMARY KEY,
        video_id TEXT,
        published_at TIMESTAMP,
        channel_id TEXT,
        title TEXT,
        description TEXT,
        channel_title TEXT,
        category_id INTEGER,
        default_audio_language TEXT,
        view_count BIGINT,
        like_count BIGINT,
        comment_count BIGINT,
        privacy_status TEXT,
        license TEXT,
        embeddable BOOLEAN,
        public_stats_viewable BOOLEAN,
        made_for_kids BOOLEAN,
        has_paid_product_placement BOOLEAN,
        category_title TEXT,
        duration INTERVAL,
        parsed_duration INTEGER
    );
    """
    try:
        conn = connect_to_db()
        cursor = conn.cursor()
        cursor.execute(table_query)
        conn.commit()
        print("Table was created")
    except Exception as e:
        print('Connection to the db failed:',e)
    finally:
         conn.close()
         cursor.close()

def load_data():
    data = pd.read_csv("dirty_cafe_sales.csv")
    print(data)
    print('data was loaded succesfuly')

