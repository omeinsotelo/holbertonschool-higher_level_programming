-- Number by score
-- script that lists the number of records with the same score in the table 
SELECT score, count(*) number FROM second_table GROUP BY score ORDER BY score DESC;
