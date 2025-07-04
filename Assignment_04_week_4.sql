'''Question - 1
Weather Observation Station 8 : Query the two cities in STATION with the shortest and longest CITY names, as well as their respective lengths .'''
SELECT DISTINCT CITY FROM STATION WHERE CITY REGEXP '^[aeiouAEIOU].*[aeiouAEIOU]$';


'''Question - 2
Population Density Difernece : Query the difference between the maximum and minimum populations in CITY.'''
SELECT MAX(POPULATION) - MIN(POPULATION) AS Population_Difference FROM CITY;


'''Question - 3
Weather Observation Station 19 : Query the Euclidean Distance between points and and format your answer to display decimal digits.'''
SELECT 
    ROUND(
        SQRT(
            POWER(MAX(LAT_N) - MIN(LAT_N), 2) + 
            POWER(MAX(LONG_W) - MIN(LONG_W), 2)
        ), 4) AS Euclidean_Distance
FROM STATION;


'''Question - 4
Weather Observation Station 20 :Query the median of the Northern Latitudes (LAT_N) from STATION and round your answer to decimal places.'''
SELECT ROUND(LAT_N, 4) AS median_latitude
FROM (
    SELECT LAT_N, 
           ROW_NUMBER() OVER (ORDER BY LAT_N) AS row_num,
           COUNT(*) OVER () AS total_count
    FROM STATION
) AS ranked
WHERE row_num IN (FLOOR((total_count + 1) / 2), FLOOR((total_count + 2) / 2));


'''Question - 5
African Cities : Query the names of all cities where the CONTINENT is 'Africa'.'''
SELECT CITY.Name FROM CITY
JOIN COUNTRY ON CITY.CountryCode = COUNTRY.Code
WHERE COUNTRY.Continent = 'Africa';


'''Question - 6
African Cities : Query the names of all cities where the CONTINENT is 'Africa'.'''
SELECT CITY.Name FROM CITY
JOIN COUNTRY ON CITY.CountryCode = COUNTRY.Code
WHERE COUNTRY.Continent = 'Africa';


'''Question - 7
Report : Write a SQL Query to create a report.'''
SELECT 
    CASE WHEN g.Grade >= 8 THEN s.Name ELSE NULL END AS Name,
    g.Grade,
    s.Marks
FROM 
    Students s
JOIN 
    Grades g ON s.Marks BETWEEN g.Min_Mark AND g.Max_Mark
ORDER BY 
    g.Grade DESC,
    CASE WHEN g.Grade >= 8 THEN s.Name END ASC,
    CASE WHEN g.Grade < 8 THEN s.Marks END ASC;


'''Question - 8
Top Compettitors : Write SQL Query to find out top competitors.'''
SELECT h.hacker_id, h.name FROM Hackers h
JOIN 
    Submissions s ON h.hacker_id = s.hacker_id
JOIN 
    Challenges c ON s.challenge_id = c.challenge_id
JOIN 
    Difficulty d ON c.difficulty_level = d.difficulty_level
WHERE 
    s.score = d.score
GROUP BY h.hacker_id, h.name HAVING COUNT(s.challenge_id) > 1
ORDER BY COUNT(s.challenge_id) DESC, h.hacker_id ASC;


'''Question - 9
Ollivanders Inventory : Question based on Joins.'''
SELECT w.id, p.age, w.coins_needed, w.power FROM Wands w 
JOIN 
    Wands_Property p ON w.code = p.code
WHERE 
    p.is_evil = 0
    AND w.coins_needed = (
        SELECT MIN(coins_needed)
        FROM Wands w2
        JOIN Wands_Property p2 ON w2.code = p2.code
        WHERE p2.is_evil = 0
        AND w2.power = w.power
        AND p2.age = p.age
    )
ORDER BY 
    w.power DESC,
    p.age DESC;


'''Question - 10
Contest Leaderboard : Question based on joins'''
SELECT h.hacker_id, h.name, SUM(max_scores.max_score) AS total_score
FROM Hackers h
JOIN (
    SELECT 
        hacker_id,
        challenge_id,
        MAX(score) AS max_score
    FROM 
        Submissions
    GROUP BY 
        hacker_id, challenge_id
) max_scores ON h.hacker_id = max_scores.hacker_id
GROUP BY h.hacker_id, h.name
HAVING SUM(max_scores.max_score) > 0
ORDER BY total_score DESC, h.hacker_id ASC;
