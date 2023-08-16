-- script that lists all shows from hbtn_0d_tvshows_rate

SELECT `name`, SUM(`rate`) AS `rating`
  FROM `tv_genres` AS gen
       INNER JOIN `tv_show_genres` AS show
       ON show.`genre_id` = gen.`id`

       INNER JOIN `tv_show_ratings` AS rate
       ON rate.`show_id` = show.`show_id`
 GROUP BY `name`
 ORDER BY `rating` DESC;
