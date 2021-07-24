
# House Price Forecast per zipcode using NeuralProphet
### A Time-Series Modeling Library based on Neural-Networks

![nprophet](https://user-images.githubusercontent.com/67468718/121110043-80e46780-c7c1-11eb-8aa4-9b9330156d09.JPG)

## 1. Introduction: NeuralProphet vs. Prophet

**NeuralProphet** is a python library for modeling time-series data based on neural networks. It’s built on top of **PyTorch** and is heavily inspired by **Facebook Prophet** and **AR-Net** libraries.

From the library name, you may ask what is the main difference between Facebook’s Prophet library and NeuralProphet. According to NeuralProphet’s [documentation](http://neuralprophet.com/changes-from-prophet/), the added features are:
 * Using PyTorch’s Gradient Descent optimization engine making the modeling process much faster than Prophet
 * Using AR-Net for modeling time-series autocorrelation (aka serial correlation)
 * Custom losses and metrics
 * Having configurable non-linear layers of feed-forward neural networks,
 * etc.


## 2. Install

For free error **NeuralProphet** installation, please create a fresh conda enviroment before proceeding with **NeuralProphet** installation and review all packages versions to make sure they're matching **NeuralProphet** Requirements to avoid any conflicts.

There is no pip or conda package for this library at this time. You can install it by cloning the repository and installing it running pip install .However, if you are going to use the package in a Jupyter Notebook environment, you should install their live version pip install .[live]. This will provide more features such as a live plot of train and validation loss using plot_live_loss().

```
git clone https://github.com/ourownstory/neural_prophet 
cd neural_prophet 
pip install .[live]
```

## 3. Load and view the data

**Data Source:**

**[Redfin](https://www.redfin.com/)** is a real estate brokerage, meaning they have direct access to data from local multiple listing services, as well as insight from their real estate agents across the country. That’s why they’re able to offer the most reliable data on the state of the housing market. They publish existing industry data faster, and offer additional data on tours and offers that no one else has. Using the tools **[here](https://www.redfin.com/news/data-center/)**, everyone can visualize and download housing market data for metropolitan areas, cities, neighborhoods and zip codes across the nation.

**Focus Area**

We're only interested in specific area in North California representing 31 Zipcodes as shown below: 

|||||||
|:--:|:--:|:--:|:--:|:--:|:--:|
|94506|	94541|	94568|	94521|	94551|	94588|
|94507	|94544|	94577|	94523|	94553|	94595|
|94509	|94545	|94578|	94526|	94565|	94597|
|94518	|94546	|94582|	94531|	94566|	94598|
|94519	|94550|	94583|	94801|	94804|	95050|
|95051					








