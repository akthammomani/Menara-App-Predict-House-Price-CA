# First, let's import all the necessary Libraries:
import streamlit as st
import pandas as pd
import pickle as pkl
import gzip, pickletools
import numpy as np
from PIL import Image
import plotly.express as px
import matplotlib.pyplot as plt
import haversine as hs
from haversine import Unit
import requests
import urllib.parse
import time
import io
import msoffcrypto
import plotly.graph_objects as go
from neuralprophet import NeuralProphet
from neuralprophet import set_random_seed


# At the begining let's change default streamlit app and icon to give our app a unique characterstics:
# let's change streamlit default icon to a lighthouse icone
icon = Image.open("light_house.JPG")

# Now, let's change page config by changing layout to 'Wide, give the app a new name and then change the icon:
st.set_page_config(layout='wide', page_title='MENARA', page_icon=icon)

#ok, now let's remove the menu button from Streamlit!!!
#st.markdown(""" <style>
#MainMenu {visibility: hidden;}
#footer {visibility: hidden;}
#</style> """, unsafe_allow_html=True)


# This app will be using a new layout options for Streamlit, so to have a clear visbility 
# we'll design the app to have a grid with many columns and rows as shown below: 


# Row number (Zero): This is to give the App title:
null0_1, row0_2, null0_2, row0_3, null0_3 = st.beta_columns((0.23, 5, 0.1, 5, 0.1))

with row0_2:
    st.title("MENARA")
    #st.subheader("First and Only App for House Price Estimation, Forecast and GreatSchools Search")
    st.write(
    """
    **First and Only Web App for House Price Estimation, Forecast and GreatSchools Search**
    """)   

# Row number (1): This is to give the App Introduction: we'll have 5 Columns:
null1_1, row1_2, null1_2, row1_3, null1_3 = st.beta_columns((0.23, 5, 0.3, 5, 0.17))

# Let's give a brief summary about our app Menara:

with row1_3:
    st.write(
    """
      ### **Introduction**
    """) 

with row1_3:
    st.write(
    """
    Whether you want to buy, sell, refinance, or even remodel a home, **MENARA** offers many resources, estimates and forecasts to help you make the most informed decision. 
    With a user-friendly interface, and offering many resources for buyers, sellers, and landlords alike. **MENARA** offers:

    * The lowest 8.5% margin off-error for off-market homes in North California ***(Competitive to the most known Home Estimate Sites e.g., [Redfin](https://www.redfin.com/redfin-estimate))*** by using the most sophisticated Machine learning algorithms.

    * A golden opportunity to give you a sneak peek into the future; Up to 14 Months of house price forecast per zipcode 
    by using a new model called **Neural Prophet**.

    * A unique access to **[GreatSchools](https://www.greatschools.org/)**; the most trusted source of schools rating for many buyers and not just buyers with children because at **MENARA**  we KNOW that “location, location, location,” means “schools, schools, schools.”

    """) 

# Let's upload the painted Ladies image:
image = Image.open("house_5.JPG")
# let's specify which column, fix its width and let's give this image a caption:
row1_2.image(Image.open("house_8.JPG"), use_column_width=True, caption='San Francisco - The Painted Ladies')

# Row number (2): in this row we'll have 6 columns:
null2_1, row2_1, row2_2, row2_3 , row2_4, row2_5= st.beta_columns((0.1, 2.8,0.1, 0.8, 0.8, 0.1))

# Here, we'll be dealing with "House Price Estimation" Section:
#let's give user inputs the headlines:
with row2_1:
    st.write(
    """
    ### **House Price Estimation**
    """) 

with row2_3:
    st.write(
    """

    #### **Enter House Details:**
    """)   

with row2_4:    
    st.write(
    """
   
    #### **Enter Neighborhood Details:**
    """)   


# Now, let's divide user's input into 2 groups: House Details & Neighborhood Details and each will be in seperate column: row2_3 & row2_4
sqft = row2_3.number_input('Living Space - Sqft', min_value=381, max_value=5000, value=4800, help="Min=381, Max=5000")
median_price_sqft_cluster = row2_4.number_input('Median sqft Price',min_value=207, max_value=850, value=720, help="Min=207, Max=850")
gsRating = row2_4.number_input('GreatSchools Rating', min_value=1, max_value=10, value=9, help="Min=1, Max=10, [GreatSchools.org](https://www.greatschools.org/)")
median_income = row2_4.number_input('Annual Income', min_value=45000, max_value=182000, value=170000, help="Min=$25K, Max=$182K")
lot_size = row2_3.number_input('Lot Size', min_value=0, max_value=18000, value=4800, help="Min=0, Max=18000")
property_type = row2_3.selectbox('Property Type', ('Single Family Residential', 'Condo/Co-op', 'Townhouse'), index=0)
beds = row2_3.selectbox('Num of Bedrooms', (1, 2, 3, 4, 5), index=3)
zipcode = row2_4.selectbox('Zip Code', (94506,94507,94509,94518,94519,94521,94523,94526,94531,94541,94544,94545,
                                       94546,94550,94551,94553,94565,94566,94568,94577,94578,94582,94583,94588,
                                       94595,94597,94598,94801,94804,95050,95051), index=18)

# Row number (3): in this row we'll have 5 columns:
null3_0,row3_1, row3_2, row3_3 , row3_4= st.beta_columns((0.1,2.7,0.2, 1.6, 0.1))

# This will explain what's behind House Price Estimation:
with row2_1:
    st.write(
    """
    At **MENARA**, since the beginning, we made our mind to be unique in approaching this typical supervised machine learning problem, so here are the main reasons why you should trust our app: 

    * Built our dataset from scratch, utilizing multiple reliable sources (e.g., **[redfin](https://www.redfin.com/news/data-center/)**, **[realtor](https://www.realtor.com/research/data/)**, **[GreatSchools API](https://www.greatschools.org/)**,.. etc). For more details, check **[Data Wrangling](https://github.com/akthammomani/Capstone-Project-2-Menara-App-Predicting-House-Prices-CA/tree/main/Notebooks/Data_Wrangling)**.
    * Applied state of the art techniques in feature engineering: integrated Unsupervised Machine Learning - Clustering using K-Means and used Haversine Formula with Python to create crucial features in order to improve our final ML Model.
    * Selected Stacking Regressor as our final Model because it managed to make predictions that have better performance than any single model we trained. So, in Stacking, we used a meta-learning algorithm (Ridge) to learn how to best combine the predictions from Four ML Algorithms (Random Forest, GB, XGBoost and LightGBM).
    """)    
 
# This button will control the heart of the APP which is the Machine Learning part :)
btn1 = row2_1.button('Get Estimated Market Value')            


# Now, let's load our saved Stacking Regressor Model:
# In this Regressor, I managed to trained 4 machine learning models (Random Forests, Gradient Boosting, XGboost and Light GBM) and combined the predictions using a Meta Model (Ridge Model):

filepath = "Tuned_stacking_deploy_np_v1.pkl"

@st.cache(allow_output_mutation=True)
def load_model():
    with gzip.open(filepath, 'rb') as f:
        p = pkl.Unpickler(f)
        model = p.load()
        return model

model =  load_model()       


#model = pkl.load(open("Tuned_stacking_deploy_np.pkl", 'rb'))
#forecast_model = pkl.load(open("forecast_model_v1.pkl", 'rb'))


if btn1:
    try:
        x = np.array([[sqft, median_price_sqft_cluster,gsRating,median_income,lot_size,property_type,beds,zipcode]])
        df = pd.DataFrame(x, columns=['sqft', 'median_price_sqft_cluster','gsRating','median_income','lot_size','property_type','beds','zipcode'])
        
        # let's encode 'Property Type':
        df.loc[df['property_type'] == 'Single Family Residential', 'property_type'] = 0.00
        df.loc[df['property_type'] == 'Condo/Co-op', 'property_type'] = 1.00
        df.loc[df['property_type'] == 'Townhouse', 'property_type'] = 2.00

       
        # Now let's change datatype from object to float:
        df = df.astype('float64')

        result = model.predict(df)[0]

        # Applying 95% Confidence Interval:                
        max_value = result + 119240.0888
        min_value = max_value - 100306.5285
        final = (max_value + min_value)/2
        with row2_1:
            st.write("Menara Estimate: ${:0,.2f}".format(final))
        with row2_1:
            st.write('Estimated Sales Price Range:', " ${:0,.2f}".format(min_value), " - ", " ${:0,.2f}".format(max_value))


    except Exception as e:
        row2_1.error(e)

with row2_1:
    st.write(
    """
    #### **Learn More**
    [![](https://img.shields.io/badge/GitHub%20-Machine%20Learning%20Models-informational)](https://github.com/akthammomani/Menara-App-Predict-House-Price-CA/tree/main/Notebooks/Modeling/)
    """)          

st.write('---')   
null4_0,row4_1, row4_2, row4_3 , row4_5= st.beta_columns((0.17,6,0.1, 1.6, 0.17))

URL = ("redfine_houses_sales_2012_2021.csv")

@st.cache(allow_output_mutation=True)
def fetch_data():
    df_2 = pd.read_csv(URL, infer_datetime_format=True)
    return df_2

price_forecast = fetch_data()

#price_forecast = pd.read_csv(URL, infer_datetime_format=True)
#Now, let's reshape df dataframe for better visibility using .melt(): df
price_forecast = pd.melt(price_forecast, id_vars=['zipcode'], value_vars=price_forecast.columns[1:])
#let's reorder columns:
price_forecast = price_forecast[['variable', 'value', 'zipcode']]
price_forecast['variable'] = price_forecast['variable'].astype('datetime64[ns]')
price_forecast['value'] = price_forecast['value'].astype('float64')
price_forecast['zipcode'] = price_forecast['zipcode'].astype('float64')

# Let's rename the following columns for NeuralProphet:
price_forecast.rename(columns = {list(price_forecast)[0]: 'ds', list(price_forecast)[1]: 'y', list(price_forecast)[2]: 'zipcode'}, inplace = True)

with row4_1:
    st.write(
    """
    ### **Median House Price Forecast Per Zip Code**
    """) 

with row4_1:
    st.write(
    """
    If you're interested in buying or selling a house in 2021/2022, then, **MENARA** is offering a golden opportunity to give you a sneak peek into the future; Up to 14 Months of house price forecast per zipcode 
    by using a new model called **Neural Prophet**. This model is a Neural Network based Time-Series Model, built on top of PyTorch and is heavily inspired by Facebook Prophet and AR-Net libraries **([Neural Prophet Site](http://neuralprophet.com/))**.

    For the Data used in **Neural Prophet**, we're utilizing multiple reliable sources **(e.g., [redfin](https://www.redfin.com/news/data-center/) and [realtor](https://www.realtor.com/research/data/))**, because they have direct access to data from local multiple listing services, as well as insight from their real estate agents across the country.

    """)  
null5_0,row5_1, row5_2, null= st.beta_columns((0.23,6, 4, 0.1))   
with row4_3:    
    st.write(
    """
    #### **Enter Zipcode to Forecast:** 
    """)     
zipcode_forecast = row4_3.selectbox('Select Zipcode', (94506,94507,94509,94518,94519,94521,94523,94526,94531,94541,94544,94545,
                                                       94546,94550,94551,94553,94565,94566,94568,94577,94578,94582,94583,94588,
                                                       94595,94597,94598,94801,94804,95050,95051), index=18)
btn2 = row4_3.button('Get Zip Code Median House Price Forecast')                                        
if btn2:   
    try:
        xz = np.array([[zipcode_forecast]])
        df_new = pd.DataFrame(xz, columns=['zipcode'])
             
        # now let's change datatype from object to float:
        df_new = df_new.astype('float64')
        filter_zippp = df_new['zipcode'].values[0]     
        
        price_forecast = price_forecast[price_forecast['zipcode']==float(filter_zippp)]
       
        price_forecast.drop('zipcode', axis=1, inplace=True)
        model_final = NeuralProphet(
                                    n_changepoints=40,
                                    changepoints_range=0.90,
                                    num_hidden_layers=2,
                                    #learning_rate=1.0,
                                    seasonality_mode="multiplicative",
                                    #n_lags=14,
                                    #n_forecasts=14,
                                   ) 
        # For reporducibility and to have identical forecast each time, let's set the seed from prophet:
        set_random_seed(0)
        metrics = model_final.fit(price_forecast, freq='MS')
       
        future = model_final.make_future_dataframe(price_forecast, periods=14, 
                                                   n_historic_predictions=len(price_forecast)) #forecast for 14 Months
        forecast = model_final.predict(future) 
       
        with row5_1:
            fig1 = go.Figure()
            fig1.add_trace(go.Scatter(x=forecast['ds'], y=forecast['y'], 
                                      name='Actual Price', opacity=0.7,
                                      line=dict(color='green', width=4)))
            fig1.add_trace(go.Scatter(x=forecast['ds'],y=forecast['yhat1'], 
                                      name = 'Forecast Price',
                                      line=dict(color='firebrick', width=4, dash='dash')))

            fig1.add_vrect(x0="2021-05-01", x1="2022-06-01", 
                           line_width=0, fillcolor="red", opacity=0.2, annotation_text="Forecast  ", annotation_position="inside top left",
                           annotation=dict(font_size=14, font_family="Comic Sans MS"))
            fig1.add_vrect(x0="2021-04-01", x1="2021-04-01", 
                           line_width=8, fillcolor="green", opacity=0.8, annotation_text="Current  ", annotation_position="outside top left",
                           annotation=dict(font_size=14, font_family="Comic Sans MS"))

            fig1.update_xaxes(rangeselector_activecolor="#EBD2B9",
                              rangeslider_visible=True,
                              rangeselector=dict(
                                                 buttons=list([
                                                               dict(count=2, label="2y", step="year", stepmode="backward"),
                                                               dict(count=3, label="3y", step="year", stepmode="backward"),
                                                               dict(count=4, label="4y", step="year", stepmode="backward"),
                                                               dict(count=5, label="5y", step="year", stepmode="backward"),
                                                               dict(step="all")
                                                             ])
                                                )
                              )               
            # Edit the layout
            fig1.update_layout(title='House Sale Price Actual vs Forecast [Neural Prophet]',
                               xaxis_title='Time', height=600,
                               yaxis_title='House Price')
            st.plotly_chart(fig1, use_container_width=True)
        analytics = forecast
        analytics.drop(['y', 'residual1', 'trend', 'season_yearly'], axis=1, inplace=True)
        analytics.set_index('ds', inplace=True)
        monthly = analytics.loc[:,'yhat1'].resample('3M').mean()
        monthly = pd.DataFrame(monthly).round()
        monthly['pct_chng'] = monthly.yhat1.pct_change()
        monthly.pct_chng = monthly.pct_chng.round(3)
        
      
        yearly = analytics.loc[:,'yhat1'].resample('4Q').mean()
        yearly = pd.DataFrame(yearly).round()
        yearly['pct_chng'] = yearly.yhat1.pct_change()
        yearly.pct_chng = yearly.pct_chng.round(3)
       

        with row5_2:         
            st.write(
                """ 
                #
                ### **Zip code Insights based on Neural Prophet Forecast**
                """ )
            yoy_2021_2022 =   (monthly['pct_chng'].iloc[-4] * 100) +  (monthly['pct_chng'].iloc[-3] * 100) + (monthly['pct_chng'].iloc[-2] * 100) + (monthly['pct_chng'].iloc[-1] * 100)
            
            st.write(" For the selected zipcode: {:.0f}".format(int(filter_zippp)),", Our Forecast Model is expecting to have:")
            st.write(" * {:.2f}".format(yoy_2021_2022), "% in 2021/2022 compared to 2019/2020!")
            st.write(" * {:.2f}".format(monthly['pct_chng'].iloc[-4] * 100), "% in  Q3 of 2021!")
            st.write(" * {:.2f}".format(monthly['pct_chng'].iloc[-3] * 100), "% in  Q4 of 2021!")
            st.write(" * {:.2f}".format(monthly['pct_chng'].iloc[-2] * 100), "% in  Q1 of 2022!")
            st.write(" * {:.2f}".format(monthly['pct_chng'].iloc[-1] * 100), "% in  Q2 of 2022!")
            if yoy_2021_2022 > 15:
                st.success("Wooow, That's Awesome!. According to our Forecast Model, the median house price for the selected Zipcode is expected to grow more than 15% in 2021/2022 compared to 2019/2020 🚀🚀.")
            elif (yoy_2021_2022 > 10) & (yoy_2021_2022 <= 15):
                st.success("That's Awesome!. According to our Forecast Model, the median house price for the selected Zipcode is expected to grow between 10-15% in 2021/2022 compared to 2019/2020 🥳🥳.")    
            elif (yoy_2021_2022 > 5) & (yoy_2021_2022 <= 10):    
                st.info("That's Great!. According to our Forecast Model, the median house price for the selected Zipcode is expected to grow between 5-10% in 2021/2022 compared to 2019/2020 😊.")
            elif (yoy_2021_2022 > 0) & (yoy_2021_2022 <= 5):    
                st.warning("That's OK!. According to our Forecast Model, the median house price for the selected Zipcode is expected to grow between 0-5% in 2021/2022 compared to 2019/2020. In North California there're many Zip Codes where house price is expected to grow more than 15% in 2021/2022, so it's better to keep searching!! 👼.")    
            else:
                st.error("That's a Bummer!. According to our Forecast Model, the median house price for the selected Zipcode is expected to lose some of its value in 2021/2022 compared to 2019/2020. So, it's better to keep searching for another Zip Code 😞.")

    except Exception as e:
        row5_1.error(e)

with row5_1:
    st.write(
    """
    #### **Learn More**
    [![](https://img.shields.io/badge/GitHub%20-Neural%20Prophet%20(Facebook)-informational)](https://github.com/akthammomani/Capstone-Project-2-Predicting-House-Prices-CA-Bay-Area/tree/main/Notebooks/Neural-Prophet-Forecast)
    """)         
    

st.write('---')         

null6_0,row6_1, null, row6_2, null= st.beta_columns((0.17,6,0.1, 1.6, 0.17))     
with row6_1:
    st.write(
    """
    ### **GreatSchools Search**
    """)   

with row6_2:    
    st.write(
    """
    #### **Enter Search Location:** 
    """)   


null7_0,row7_1, row7_2, null= st.beta_columns((0.21,4, 5, 0.1))   


with row6_1:
    st.write(
    """
    Most buyers understand that they may not be able to find a home that covers every single item on their wish list, but new survey data from **[realtor](http://wwww.realtor.com)** shows that school districts are an 
    area where many buyers aren’t willing to compromise. For many buyers and not just buyers with children, “location, location, location,” means “schools, schools, schools.”

    Good schools desire by **78%** of buyers makes **[GreatSchools](https://www.greatschools.org/)** the trusted source of schools rating for many parents and the partner of choice for so many leading real estate websites (e.g., redfin, zillow, realtor) 
    simply because **GreatSchools** are the nation’s leading source of school performance information and offer the most comprehensive set of school data available. Last year, **GreatSchools** had more than 55 million unique visitors, including over half of American families with school-age children.

    Special Thanks to **GreatSchools**, in particular Lindsay Zavala - Partnership Manager for providing a **free API trial key**. REST API access was essential to request GreatSchools Rating
    of all schools in specific zipcodes/Cities in North California.
    """)    


Address = row6_2.text_input('Address', '200 Civic Plaza, Dublin, CA, 94568', help="Format: Street address, City, CA, zipcode")       
                
url = 'https://nominatim.openstreetmap.org/search/' + urllib.parse.quote(Address) +'?format=json'
response = requests.get(url).json()
lat = response[0]["lat"]
lon = response[0]["lon"]          


Address = Address +','+ lat +','+ lon
data = io.StringIO(Address)
columns=['Street Name', 'city', 'State', 'zipcode', 'lat','lon']
search = pd.read_csv(data, sep=",", header=None, names=columns)

Search_radius = row6_2.selectbox('Search Distance [miles]',(1,2,3), index=2, help="Available North California Cities: Alameda,Alamo,Albany,Antioch,Bay Point,Berkeley,Brentwood,Castro Valley,Clayton,Concord,Danville,Dublin,East Palo Alto,El Cerrito,El Sobrante,Emeryville,Hayward,Kensington,Lafayette,Livermore,Los Alamos,Los Altos,Los Altos Hills,Martinez,Menlo Park,Mountain View,Oakland,Oakley,Palo Alto,Piedmont,Pittsburg,Pleasant Hill,Pleasanton,Portola Valley,Richmond,San Jose,San Leandro,San Lorenzo,San Pablo,San Ramon,Santa Clara,Stanford,Sunnyvale,Sunol,Union City,Walnut CreeK")   


DATA_URL = ("NCA_df_app_v2.xlsx")

#school = pd.read_csv(DATA_URL)

#@st.cache(allow_output_mutation=True, hash_funcs={type(st.secrets): _hash_st_secrets)
def fetch_school():
    #df = pd.read_excel(DATA_URL)
    file = msoffcrypto.OfficeFile(open(DATA_URL, "rb"))
    #st.write("password:", st.secrets["password"])
    file.load_key(st.secrets["password"]) # Use password
    decrypted = io.BytesIO()
    file.decrypt(decrypted)
    df = pd.read_excel(decrypted)
    return df

school = fetch_school()


s = np.array([[Search_radius]])
distance = pd.DataFrame(s, columns=['radius'])
distance['radius'] = distance['radius'].astype('int64')


# let's first prepare both of the dataframes for haversine function:
# Concatenating lat and long to create a consolidated location as accepted by haversine function (Tuple: (lat, long) format)
search['coor'] = search[['lat', 'lon']].apply(tuple, axis=1)
school['coor'] = school[['lat', 'lon']].apply(tuple, axis=1)


# Defining a function to calculate distance between two locations 
# loc1= location of user search
# loc2= location of schools
def distance_from(loc1,loc2): 
    dist=hs.haversine(loc1,loc2,unit=Unit.MILES) # By default the haversine function returns distance in kms, so let's change it miles.
    return round(dist,2)

# Running a loop which will parse house's location one by one to distance from function:
for _,row in school.iterrows():
    search[row.ncesId]=search['coor'].apply(lambda x: distance_from(row.coor,x))    

search_school = pd.melt(search, id_vars=['city', 'zipcode', 'lat', 'lon'], value_vars=school['ncesId'])

search_school.rename(columns = {list(search_school)[4]: 'ncesId', list(search_school)[5]: 'Distance [miles]'}, inplace = True)


school = school[['name', 'ncesId', 'gsRating', 'enrollment', 'gradeRange' ,'lat', 'lon']]

school.rename(columns = {list(school)[3]: 'Students', list(school)[5]: 'latitude', list(school)[6]: 'longitude'}, inplace = True)
search_school_rating = pd.merge(search_school, school, how='left', on='ncesId')

btn_school = row6_2.button('Search Schools')
import plotly.graph_objects as go
import plotly.graph_objs as go
from numpy import pi, sin, cos
    
if btn_school:
    try:
        filter = distance['radius'].values[0]
        zip = search['zipcode'].values[0]
        search_school_rating.rename(columns = {list(search_school_rating)[6]: 'School Name', list(search_school_rating)[7]: 'GreatSchools Rating'}, inplace = True)
        search_school_rating = search_school_rating[['city','zipcode','lat','lon','School Name', 'GreatSchools Rating', 'Students','gradeRange','Distance [miles]', 'latitude', 'longitude']]
       
        zipcode_stats= search_school_rating[search_school_rating['zipcode'] == zip]
        schools_count_all = zipcode_stats.groupby('zipcode')['School Name'].count().reset_index()
        avg_rate_all = zipcode_stats.groupby('zipcode')['GreatSchools Rating'].mean().reset_index()
        max_rate_all = zipcode_stats.groupby('zipcode')['GreatSchools Rating'].max().reset_index()
        min_rate_all = zipcode_stats.groupby('zipcode')['GreatSchools Rating'].min().reset_index()
        avg_stud_zip_all = zipcode_stats.groupby('zipcode')['Students'].mean().reset_index()
        
        search_school_rating = search_school_rating[search_school_rating['Distance [miles]'] <= filter]
        with row7_2:    # Let's create some spacing between different rows     
            st.write(
            """ 

            ##
            """)     
        with row7_2:    
            st.write(
                """ 
                #### **All Rated Schools within search location:**
                """ )                                                                                                                   # Using hack to remove index:) assign(hack='').set_index('hack')
            st.dataframe(search_school_rating[['School Name', 'gradeRange','GreatSchools Rating', 'Students','Distance [miles]']].assign(hack='').set_index('hack'), width=1500, height=250)
     
            schools_count = search_school_rating.groupby('zipcode')['School Name'].count().reset_index()
            avg_rate = search_school_rating.groupby('zipcode')['GreatSchools Rating'].mean().reset_index()
            max_rate = search_school_rating.groupby('zipcode')['GreatSchools Rating'].max().reset_index()
            min_rate = search_school_rating.groupby('zipcode')['GreatSchools Rating'].min().reset_index()
            longest_distance = search_school_rating.groupby('zipcode')['Distance [miles]'].max().reset_index()
            closest_distance = search_school_rating.groupby('zipcode')['Distance [miles]'].min().reset_index()
            avg_stud_zip = search_school_rating.groupby('zipcode')['Students'].mean().reset_index()
  
        with row7_2:         
            st.write(
                """ 
                #### **Schools Insights based on Search Location:**
                """ )
            st.write("* Within", filter, "miles of the search location", ", There are", schools_count['School Name'].values[0], "Schools, where The closest is within ", closest_distance['Distance [miles]'].values[0], "miles and The farthest is within", longest_distance['Distance [miles]'].values[0], "miles")
            st.write("* For the above ", schools_count['School Name'].values[0], "Schools, the GreatSchools Rating Range is between: ", min_rate['GreatSchools Rating'].values[0], " - ", max_rate['GreatSchools Rating'].values[0],
                     ", and the average GreatSchools Rating is ", round(avg_rate['GreatSchools Rating'].values[0], 2), ".")
            st.write("* The Average Students enrolled in these ", schools_count['School Name'].values[0], "Schools, is: ", int(avg_stud_zip['Students'].values[0]), " Students.")
        with row7_2:     
            st.write(
                """ 
                #### **Now let's compare your search location's result with the entire zipcode:**
                """ )     
            st.write("* For zipcode ", int(zipcode_stats['zipcode'].values[0]), ", the GreatSchools Rating Range is between: ", min_rate_all['GreatSchools Rating'].values[0], " - ", max_rate_all['GreatSchools Rating'].values[0],
                     ", and the average GreatSchools Rating is ", round(avg_rate_all['GreatSchools Rating'].values[0], 2), ".")
            st.write("* The Average Students enrolled in zipcode ",  int(zipcode_stats['zipcode'].values[0]), "is: ", int(avg_stud_zip_all['Students'].values[0]), " Students.")            
            if int(avg_rate['GreatSchools Rating'].values[0]) > int(avg_rate_all['GreatSchools Rating'].values[0]):
                st.success("That's Awesome!, looks like Average GreatSchools Rating in your search location is better than the entire zipcode. lucky! you nailed it first time 😊.")
            else:
                st.error("That's a Bummer!, looks like the Average GreatSchools Rating in your search location is less than the entire zipcode. So, it's better to keep searching for another location 😞.")
            

        with row7_2:  
            st.write(
            """
            ##### ***Source: [GreatSchools.Org](https://www.greatschools.org/)***
            """)  

            #mapbox_access_token = open("pk.eyJ1IjoiYWt0aGFtbW9tYW5pIiwiYSI6ImNrcDU0dGJsbTAzY2gydnJyempia3FpZ2QifQ.3oOkDE4Mh3rZ9WCosKSFcQ").read()

            fig = px.scatter_mapbox(search_school_rating, lat='latitude', hover_data =['School Name', 'GreatSchools Rating', 'Students','gradeRange','Distance [miles]'], lon='longitude', mapbox_style='open-street-map', 
                                     center=dict(lon=search_school_rating['lon'].values[0], lat=search_school_rating['lat'].values[0]),zoom=11, size_max=10, 
                                     height=850, title = 'Schools per GreatSchools Rating', size='GreatSchools Rating', color='GreatSchools Rating', color_continuous_scale= [
                                                                                                                                                                              "black",
                                                                                                                                                                              "red",
                                                                                                                                                                              "magenta",
                                                                                                                                                                              "darkgoldenrod",
                                                                                                                                                                              "darkgray", 
                                                                                                                                                                              "darkviolet",
                                                                                                                                                                              "deepskyblue", 
                                                                                                                                                                              "blue", 
                                                                                                                                                                              "MidnightBlue",
                                                                                                                                                                              "ForestGreen"])


            size_sezrch=filter * 120
            fig.add_trace(go.Scattermapbox(
                                          lat=search_school_rating['lat'],
                                          lon=search_school_rating['lon'],
                                          marker = {'size': size_sezrch, 'opacity': 0.01, 'color':'red', 'symbol':'circle'})

                                          )
                           
            fig.update_layout(
                             autosize=False,
                             hovermode='closest',
                             showlegend=False,
                                                          )

                                                                                            
            row7_1.plotly_chart(fig, use_container_width=True)                              

    except Exception as e:
            row7_2.error(e)      
with row7_1:
    st.write(
    """
    #### **Learn More**
    [![](https://img.shields.io/badge/GitHub%20-GreatSchools%20API%20and%20Haversine%20Formula%20Using%20Python-informational)](https://github.com/akthammomani/Menara-App-Predict-House-Price-CA/tree/main/Notebooks/GreatSchools_API_Haversine)
    """)  
          
st.write('---')      

null8_0,row8_1= st.beta_columns((0.09,4))   

with row8_1:
    st.write(
    """
    ### **Contacts**
    [![](https://img.shields.io/badge/GitHub-Follow-informational)](https://github.com/akthammomani/Menara-App-Predict-House-Price-CA)
    [![](https://img.shields.io/badge/Linkedin-Connect-informational)](https://www.linkedin.com/in/akthammomani/)
    [![](https://img.shields.io/badge/Open-Issue-informational)](https://github.com/akthammomani/Capstone-Project-2-Predicting-House-Prices-CA-Bay-Area/issues)
    [![MAIL Badge](https://img.shields.io/badge/-aktham.momani81@gmail.com-c14438?style=flat-square&logo=Gmail&logoColor=white&link=mailto:aktham.momani81@gmail.com)](mailto:aktham.momani81@gmail.com)

    ##### © Aktham Momani, 2021
    """
)  

