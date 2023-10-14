-- lists all bands with "Glam rock" as their main genre
-- categorized by their longevity

SELECT
    band_name,
    IFNULL(2022 - CAST(SUBSTRING_INDEX(SUBSTRING_INDEX(longevity, ' - ', 1), '-', -1) AS SIGNED), 0) AS longevity
FROM
    metal_bands
Where
    FIND_IN_SET('Glam rock', main_genre) > 0
ORDER BY
    lifespan DESC;