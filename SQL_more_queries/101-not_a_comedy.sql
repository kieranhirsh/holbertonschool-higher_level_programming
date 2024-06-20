-- Task 18: Write a script that lists all shows without the genre Comedy in the database hbtn_0d_tvshows.
SELECT tv_shows.title
FROM tv_shows
LEFT JOIN (
    SELECT tv_shows.title
    FROM tv_genres
    LEFT JOIN tv_show_genres
    ON tv_genres.id=tv_show_genres.genre_id
    LEFT JOIN tv_shows
    ON tv_shows.id=tv_show_genres.show_id
    WHERE tv_genres.name="Comedy"
) AS comedies
ON tv_shows.title=comedies.title
WHERE comedies.title IS NULL
ORDER BY tv_shows.title ASC;