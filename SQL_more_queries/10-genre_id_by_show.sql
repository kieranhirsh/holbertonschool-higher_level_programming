-- Task 9: Write a script that lists all cities contained in the database hbtn_0d_usa.
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_show_genres
LEFT JOIN tv_shows ON tv_shows.id=tv_show_genres.show_id
ORDER BY title ASC, genre_id ASC;