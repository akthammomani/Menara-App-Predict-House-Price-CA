# Calculating The Distance between Houses and Schools Using Haversine Formula


![globe](https://user-images.githubusercontent.com/67468718/116970776-6a506b00-ac6d-11eb-80a6-2922f6f28929.JPG)

## 1.  Introduction<a id='1_Introduction'></a>

**The Haversine formula** is perhaps the first equation to consider when understanding how to calculate distances on a sphere. The word "Haversine" comes from the function:

$haversine(θ) = sin²(θ/2)$

The following equation where φ is latitude, λ is longitude, R is earth’s radius (mean radius = 6,371km) is how we translate the above formula to include latitude and longitude coordinates. Note that angles need to be in radians to pass to trig functions:

$a = sin²(φB — φA/2) + cos φA * cos φB * sin²(λB — λA/2)$

$c = 2 * atan2( √a, √(1−a) )$

$d = R ⋅ c$

## 2. Objective

**The Haversine formula** will help us to find all schools within 3 miles of every house and then we can calculate the average GreatSchool Ratings for all schools within 3 miles of every house in our database.

