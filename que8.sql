SELECT temperature FROM records;

SELECT distinct city FROM records;

SELECT * FROM records WHERE country="India";

SELECT city, country, season FROM records WHERE AVG(rainfall) BETWEEN 200 and 400;

SELECT city, country FROM records WHERE rainfall > 20 ORDER BY temperature;

SELECT SUM(rainfall) FROM records WHERE country="Cairo";

SELECT SUM(rainfall) FROM records GROUP BY season;
