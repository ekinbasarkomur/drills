-- 1294. Weather Type in Each Country · Easy · https://leetcode.com/problems/weather-type-in-each-country/
-- Plan: Paralel hat · SQL
--
-- Problem:
-- Approach:
-- Time O(?), space O(?)

-- ---------------------------------------------------------------- solution
# Write your MySQL query statement below
-- TODO: solve, then delete this line
-- ---------------------------------------------------------------- tests
-- schema: Create table If Not Exists Countries (country_id int, country_name varchar(20))
-- schema: Create table If Not Exists Weather (country_id int, weather_state int, day date)
-- case: {"headers": {"Countries": ["country_id", "country_name"], "Weather": ["country_id", "weather_state", "day"]}, "rows": {"Countries": [[2, "USA"], [3, "Australia"], [7, "Peru"], [5, "China"], [8, "Morocco"], [9, "Spain"]], "Weather": [[2, 15, "2019-11-01"], [2, 12, "2019-10-28"], [2, 12, "2019-10-27"], [3, -2, "2019-11-10"], [3, 0, "2019-11-11"], [3, 3, "2019-11-12"], [5, 16, "2019-11-07"], [5, 18, "2019-11-09"], [5, 21, "2019-11-23"], [7, 25, "2019-11-28"], [7, 22, "2019-12-01"], [7, 20, "2019-12-02"], [8, 25, "2019-11-05"], [8, 27, "2019-11-15"], [8, 31, "2019-11-25"], [9, 7, "2019-10-23"], [9, 3, "2019-12-23"]]}}
-- expect: {"run_only": true}
