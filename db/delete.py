
def truncate_table(conn):
    conn.cursor().execute("TRUNCATE TABLE video_data;")
    conn.commit()
    print('Tabela restaurada para atualização')
