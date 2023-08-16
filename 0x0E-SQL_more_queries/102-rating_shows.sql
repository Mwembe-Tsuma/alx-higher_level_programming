-- script that lists all shows from hbtn_0d_tvshows_rate

SELECT `title`, SUM(`rate`) AS `rating`
  FROM `tv_shows` AS tl
       INNER JOIN `tv_show_ratings` AS rt
       ON tl.`id` = rt.`show_id`
 GROUP BY `title`
 ORDER BY `rating` DESC;
