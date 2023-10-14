-- ranks country origins of bands
-- ordered by the number of (non-unique) fans

SELECT country, COUNT(*) AS fan_count
FROM metal_bands
GROUP BY country
ORDER BY fan_count DESC;
