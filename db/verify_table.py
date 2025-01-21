def create_table(conn):
    
    table_query = """
    CREATE TABLE video_data (
        id SERIAL PRIMARY KEY,
        video_id TEXT,
        published_at TIMESTAMP,
        channel_id TEXT,
        title TEXT,
        description TEXT,
        channel_title TEXT,
        category_id TEXT,
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
        caption BOOLEAN,
        duration INTERVAL,
        parsed_duration INTEGER
    );
    """
    cursor = conn.cursor()
    try:
        cursor.execute("""
            SELECT EXISTS (
                SELECT FROM information_schema.tables 
                WHERE table_name = 'video_data'
            );
        """)
        exists = cursor.fetchone()[0]

        if exists:
            print("A tabela 'video_data' já existe.")
        else:
            cursor.execute(table_query)
            conn.commit()
            print("Tabela 'video_data' foi criada.")

    except Exception as e:
        print('Erro na execução de query', e)
