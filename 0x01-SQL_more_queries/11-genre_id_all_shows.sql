-- list all shows in the database
FROM tv_shows
LEFT JOIN tv_show_genres
ON a.id = b.show_id
ORDER BY a.title ASC, b.genre_id ASC;