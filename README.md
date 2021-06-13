# Menara App: 
First and Only App for House Price Estimation, Forecast and GreatSchools Search

![SF_painted_ladies](https://user-images.githubusercontent.com/67468718/103456623-c483f400-4cac-11eb-8cdb-d508d23d80ba.jpg)

Whether you want to buy, sell, refinance, or even remodel a home, **MENARA** offers many resources, estimates and forecasts to help you make the most informed decision. 
With a user-friendly interface, and offering many resources for buyers, sellers, and landlords alike. **MENARA** offers:

  * The lowest 8.5% margin off error for off- market homes in North California ***(Competitive to the most known Home Estimate Sites e.g., [Redfin](https://www.redfin.com/redfin-estimate))*** by using the most sophisticated Machine learning Alogorithms.

  * A golden opportunity to give you a sneak peek into the future; Up to 14 Months of house price forecast per zipcode 
    by using a new model called **Neural Prophet**.
    
  * A unique access to **[GreatSchools](https://www.greatschools.org/)**; the most trusted source of schools rating for many buyers and not just buyers with children because at **MENARA**  we KNOW that “location, location, location,” means “schools, schools, schools."
 
## Target: Predict house prices using multiple Machine Learning Algorithms considering different sets of house and zip code features:

1. Main Dataset: Source www.redfin.com:
    * Obtained sold houses from Dec 2019-Dec 2020.
    * The sold houses located in North California distributed between 49 cities and 94 Zip Codes.
    * Data has 8,790 Observations and 27 Variables.

         ### 🌟🌟🌟🌟 Adding more Datasets to enhance our prediction 🌟🌟🌟🌟

2. Adding Median Income per Zip code:
    * Source: http://www.usa.com/rank/california-state--median-household-income--zip-code-rank.htm and since the data from 2010-2014, and according to              
      https://www.statista.com/statistics --> the median Income in California has grown by 6.36% we’ll use this % to adjust this Dataset YoY.
      
3. Adding Hotness score (0-100) to refelect the demand and supply per zip code:
    * Source: https://www.realtor.com/research/data/
      
4. Adding Public School per zip code:
    * Source: https://hifld-geoplatform.opendata.arcgis.com/datasets/87376bdb0cb3490cbda39935626f6604_0
    
5. Adding GreatSchools Rating to reflect Schools rating in all the selected 47 cities in North California:
    * Source: GreatSchools.org API https://www.greatschools.org/api/request-api-key

6. Adding Shoping and Mall centers in CA per city:
    * Source: https://en.wikipedia.org/wiki/List_of_shopping_malls_in_California
    
7. Adding Universities and colleges list in CA per city:
    * Source: http://www.free-4u.com/Colleges/California-Colleges.html
    
8. Adding BART (Bay Area Rapid Transit) stations with parking (Y/N) per zip code in North California:
    * Source: https://www.bart.gov/stations
    
9. We have 8 Datasets to support this project, so Data cleaning & Wrangling will be needed:
    * Clean NANs, duplicate values, wrong values and removing insignificant columns.
    * Merging and concatenation will be needed.
    * The GreatSchools API is a REST-based web service: will need to use Python Packages: requests, xml.etree.ElementTree and glob:
         - requests: To request the data from GreatSchools API
         - xml.etree.ElementTree module : to implement a simple and efficient API for parsing and creating XML data.
         - glob: to concatenate all the API output in one final DataFrame.
    


