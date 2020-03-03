-- Cities of California
-- Lists all the cities of California that can be found in the database hbtn_0d_usa.
SELECT b.id, b.name
FROM states AS a, cities AS b
WHERE a.id = b.state_id
	AND a.name = "California";
