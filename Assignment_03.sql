'''Question - 1 
Select All'''
SELECT * FROM CITY;


'''Question - 2
Select By ID'''
SELECT * FROM CITY WHERE ID = 1661;


'''Question - 3 
Employee Names'''
SELECT NAME FROM EMPLOYEE ORDER BY NAME;


'''Question - 4 
Japanese Cities Attributes'''
SELECT * FROM CITY WHERE COUNTRYCODE = 'JPN';


'''Question - 5 
Weather Observation Station 1'''
SELECT CITY, STATE FROM STATION;


'''Question - 6 
Weather Observation Station 3'''
SELECT DISTINCT CITY FROM STATION WHERE MOD(ID, 2) = 0;


'''Question - 7 
Weather Observation Station 4'''
SELECT COUNT(CITY) - COUNT(DISTINCT CITY) AS Difference FROM STATION;


'''Question - 8 
Weather Observation Station 5'''
(SELECT CITY, LENGTH(CITY) AS name_length
 FROM STATION
 ORDER BY LENGTH(CITY) ASC, CITY ASC
 LIMIT 1)

UNION ALL

(SELECT CITY, LENGTH(CITY) AS name_length
 FROM STATION
 ORDER BY LENGTH(CITY) DESC, CITY ASC
 LIMIT 1);


'''Question - 9 
Average Population'''
SELECT AVG(POPULATION) FROM CITY;


'''Question - 10 
Average Population of Each Continent'''
SELECT 
    co.Continent,
    FLOOR(AVG(ci.Population)) AS avg_city_population
FROM 
    CITY ci
JOIN 
    COUNTRY co ON ci.CountryCode = co.Code
GROUP BY 
    co.Continent
ORDER BY 
    co.Continent;