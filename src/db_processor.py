import sqlite3

def create_movie_db():
    print('Creating Database...')

    connection = sqlite3.connect('movie.sqlite')

    sql = """CREATE TABLE IF NOT EXISTS movies (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        movie_group_name TEXT NOT NULL,
        chinese_name TEXT,
        english_name TEXT,
        start_time TEXT,
        movie_age TEXT,
        movie_play TEXT,
        movie_language TEXT
        )"""

    cursor = connection.cursor()
    cursor.execute(sql)

    connection.commit()
    connection.close()

    print('Database Created!!')

def get_movie_data():
    connection = sqlite3.connect('movie.sqlite')
    sql = 'SELECT * FROM movies'
    cursor = connection.cursor()
    cursor.execute(sql)
    
    return [row for row in cursor.fetchall()]

    connection.close()

def insert_movie_data(group_name, chinese_name, english_name, start_time, movie_age, movie_play, language):
    connection = sqlite3.connect('movie.sqlite')
    cursor = connection.cursor()
    sql = f"""
        INSERT INTO movies (movie_group_name, chinese_name, english_name, start_time, movie_age, movie_play, movie_language)
        VALUES ('{group_name}', '{chinese_name}', '{english_name}', '{start_time}', '{movie_age}', '{movie_play}', '{language}')
        """
    print(sql)
    cursor.execute(sql)
    connection.commit()

    connection.close()

def has_duplicated_movie_data(group_name, movie_play, movie_language):
    connection = sqlite3.connect('movie.sqlite')
    cursor = connection.cursor()
    sql = f"SELECT id FROM movies WHERE movie_group_name = '{group_name}' AND movie_play = '{movie_play}' AND movie_language = '{movie_language}'"

    cursor.execute(sql)
    result = [row for row in cursor.fetchall()]

    if len(result) != 0:
        return True
    else:
        return False

if __name__ == '__main__':
    create_movie_db()
    print('__name__: ', __name__)
    print('Movie Data: ', get_movie_data())
    print('There is the movie "血衛2D英文版"?', has_duplicated_movie_data('血衛','2D數位','英文版')) # 此應為存在資料
    # print('There is the movie "血衛2D中文版"?', has_duplicated_movie_data('血衛','2D數位','中文版')) # 此應為不存在資料