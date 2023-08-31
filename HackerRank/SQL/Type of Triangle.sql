-- Sample Output

-- Isosceles
-- Equilateral
-- Scalene
-- Not A Triangle
-- Explanation

-- Values in the tuple (20,20,23) form an Isosceles triangle, because A = B.
-- Values in the tuple (20,20,20) form an Equilateral triangle, because A = B. 
-- Values in the tuple (20,21,22) form a Scalene triangle, because A <> B <> C.
-- Values in the tuple (13,14,30) cannot form a triangle because the combined value of sides A and B is not larger than that of side C.

SELECT 
CASE
    WHEN (A=B) AND (B=C) THEN 'Equilateral'
    WHEN (A=B AND B!=C AND (A+B)>C) OR (A=C AND C!=B AND (A+C)>B) OR (B=C AND C!=A AND (B+C)>A) THEN 'Isosceles'
    WHEN ((A+B)>C) AND ((A+C)>B) AND ((B+C)>A) THEN 'Scalene'
    WHEN ((A+B)<=C) OR ((A+C)<=B) OR ((B+C)<=A) THEN 'Not A Triangle'
END AS traingleType
FROM triangles;