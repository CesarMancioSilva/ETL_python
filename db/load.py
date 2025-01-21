from datetime import datetime
import re

def remove_emojis(text):
    emoji_pattern = re.compile("[\U00010000-\U0010ffff]", flags=re.UNICODE)
    return emoji_pattern.sub(r'', text)


def load_data(data, conn):
    
    try:
        print("Armazenando dados...")
        for video in data:
            published_at = datetime.strptime(video['publishedAt'], "%Y-%m-%dT%H:%M:%SZ").strftime('%Y-%m-%d %H:%M:%S')

            title=remove_emojis(video['title']).strip()

            data_tuple= (
                video.get('id', ''), 
                published_at, 
                video.get('channelId', ''), 
                title, 
                video.get('description', '').strip(),
                video.get('channelTitle', ''), 
                video.get('categoryId', ''),
                video.get('viewCount', 0),  
                video.get('likeCount', 0),  
                video.get('commentCount', 0),  
                video.get('privacyStatus', ''), 
                video.get('license', ''), 
                video.get('embeddable', False),  
                video.get('publicStatsViewable', False),  
                video.get('madeForKids', False),  
                video.get('hasPaidProductPlacement', False),  
                video.get('categoryTitle', ''),
                video.get('caption', False), 
                video.get('duration', ''), 
                video.get('parsedDuration', 0)  
            ) 

            with conn.cursor() as cursor:
                cursor.execute("""
                    INSERT INTO video_data (
                        video_id, published_at, channel_id,title, description,channel_title,
                        category_id, view_count ,like_count,comment_count,privacy_status,license,embeddable,public_stats_viewable,made_for_kids,has_paid_product_placement,category_title ,caption,duration,parsed_duration
                    ) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);
                """, data_tuple)
                conn.commit()
        print("Dados armazenados com sucesso")
            
    except Exception as e:
        print("Erro para armazenar dados: ", e)
