# ***\*Introduction\**** 

Suppose there is a real estate company based in the United States, specializing in the sale of houses 

in various locations. In the real estate market, house prices are influenced by a variety of factors, 

including location, size, noise level, air conditions, etc. To help real estate investors make informed 

decisions, the company regularly releases information on house sales in different areas. By 

providing comprehensive sales data, the company empowers investors to design accurate and 

effective house price prediction systems. By analyzing sales data, investors can identify latent 

patterns and develop predictive models that are useful to make data-driven decisions on house 

transactions. 

# ***\*Dataset\**** 

The dataset is described as follows: 

**1. Train_Data.csv** contains 4000 samples of estate basic information, and the target variable is 

the ***\*Total Cost\**** status: 

● Date – The date when the sample is collected. 

● Number of rooms – number of rooms in the house. 

● Security level of the community – the higher the safer. 

● Residence space – square feet area of the living rooms. 

● Building space – square feet area of the whole building. 

● Noise level – the lower the value, the greater the noise. 

● Waterfront – If the house has water front or not. 

● View – Number of viewings before the house is sold. 

● Air quality level – the higher the value, the better the air quality. 

● Aboveground space – square feet area of the above house. 

● Basement space – square feet area of the basement in the house. 

● Building year – the year in which the house was built. 

● Decoration year – the year in which the house was decorated. 

● District – the address of the house. 

● City – the city in which the house is located. 

Group ProjectPage 1The Hong Kong Polytechnic University 

● Zip code – the zip code of the house. 

● Region – the region of the house. 

● Exchange rate – when the house is sold, the exchange rate between the US dollar and the 

Hong Kong dollar. 

● Unit price of residence space – the unit price of residence space (US dollars). 

● Unit price of building space – the unit price of building space (US dollars). 

● ***\*Total cost – the total price of residence and building space (Hong Kong dollars).\**** 

**2. Test_Data.csv** contains 400 samples of estate basic information and the ***\*total cost\**** is unknown. 

# ***\*Task\**** 

This project contains three tasks: 

\1. Suppose you are an employee of the company, calculate the total cost (in ***\*Hong Kong dollars\****) 

of each house (***\*including residence and building costs\****) based on the data in **Train_Data.csv**. 

It is ***\*required to use MapReduce\**** to handle the calculation. Suppose there are ***\*5 mappers\**** and 

***\*2 reducers\****. 

# ***\*Hint:\**** 

(1) The total area of the house includes two parts: residence and building. 

(2) The **Train_Data.csv** can be distributed equally among 5 mappers. 

(3) The calculation rule of the total cost is: 

**(The unit price of residence space \* Residence space + Unit price of building space \* Building** 

**space) \* Exchange rate = Total cost.** 

(4) Here is an example to calculate the total cost of the first sample in **Train_Data.csv** : 

**(11.88640925 \* 2820 + 0.977028065 \* 67518) \* 6.784829586=675000 HKD** 

 

 

 

 

 