-- script that uses the hbtn_0d_tvshows

SELECT name FROM tv_genres
WHERE tv_genres.id NOT IN (
		JOIN tv_show_genres ON id=tv_show_genres.genre_id
		JOIN tv_shows ON tv_shows.id=tv_show_genres.show_id
		WHERE tv_shows.title = 'Dexter')
ORDER BY tv_genres.name;
