-- script that lists all shows from hbtn_0d_tvshows_rate

SELECT name, SUM(rate) AS rating
  FROM tv_genres AS gen
       INNER JOIN tv_show_genres AS sh
       ON sh.genre_id = geb.id
       INNER JOIN tv_show_ratings AS rt
       ON rt.show_id = sh.show_id
 GROUP BY name
 ORDER BY rating DESC;
