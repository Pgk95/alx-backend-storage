-- lists all bands with "Glam rock" as their main genre
-- categorized by their longevity

SELECT
    band_name,
    (IFNULL(split, 2022) - formed) AS lifespan
FROM
    metal_bands
Where
    style LIKE '%Glam rock%'
ORDER BY
    lifespan DESC;