SELECT movies.title FROM movies
JOIN stars ON stars.movie_id = movies.id
JOIN people ON people.id = stars.person_id
WHERE (people.name = "Johnny Depp" OR people.name = "Helena Bonham Carter")
GROUP BY movies.id
HAVING COUNT(people.id) = 2;