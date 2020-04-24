from requests_html import HTMLSession
import movie_db

url = 'https://www.in89.com.tw/api/connect.php?cinema=taipei.in89.com.tw&method=getAllMovies&theater_code=&TheaterId=3'
session = HTMLSession()
data = eval(session.get(url).text)
movies = data['showing_movies']

for movie in movies:
    movie_group_name = movie['movie_group_name'].strip()
    movie_chinese_name = movie['cn_name'].strip()
    movie_english_name = movie['en_name'].strip()
    start_time = movie['start_time'].strip()
    movie_age = movie['movie_age_desc'].strip()
    movie_play = movie['movie_play_desc'].strip()
    movie_language = movie['movie_lang_desc'].strip()

    if movie_db.has_duplicated_movie_data(movie_group_name, movie_play, movie_language) != True:
        movie_db.insert_movie_data(group_name = movie_group_name, chinese_name = movie_chinese_name, english_name = movie_english_name, start_time = start_time, movie_age = movie_age, movie_play = movie_play, language = movie_language)