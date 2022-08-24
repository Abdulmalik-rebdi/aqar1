# analyzing riyadh's rental apartments

understanding the riyadh's rental apartments and creating a classification model that tell if the apartmant will be rented or not in specific time 
in 6/8/2022 i started web scraping and after that i webScraped every day , i left join the new data with the main data (6/8/2022) and check which apartment got rented and i kept doing that for 10 days yet now from 6/8/2022 there are 2328 rented apartment out of 6762 apartment
![image](https://user-images.githubusercontent.com/74616700/185017719-af131382-16ee-45dd-a499-d50b1b305ef8.png)


you can use your own apartment to chaeck how long the apartment need to get rented in this [site](https://abdulmalik-rebdi-riyadh-rental-apartments-lrapp-n8sh72.streamlitapp.com/)


# About the Dataset

i create the dataSet until it got Ready for the EDA in 5 main steps 
| fileName | Description |
| --- | --- |
| Webscraping | in this file a gather the information from  [aqar site ](sa.aqar.fm) the information i gathered is all apartments in riyadh that are rented yearly . Everyday i ran this file to gather more inforamtion about the rental apartments  |
| cleaning.ipynb | after i scrpaed the data i needed to clean the data (i convert the date in create date in from second to date , and create columns from existing columns (user) to (review ,  profileImg ,UserName ,phone ,iam_verified ,rega_id  )that there are in user columns and then deleted columns (phone ,category , street_direction ,native ,rent_period ,city ,__typename ,phone , type, uri   )  ) |
| join | after that  combine the data into the data of today with the main data (left outter join)  |
| timeBeforeRent.ipynb | i create a new feature that how long was the apartment there when it got rented    |
| onMarket | i create a new feature that  till how many days is the post of the ad existing  |
| EDA | basic EDA |
| featureEng | preprocecing the data for implementing the models |
| classification | classification model |
| regression | regression model |

# Dataset
after cleaning the data this is the data i will work with 


| no | columnName | Description| 
|----------|---------------------------|----------------------------------------------------------------------------------|
| 1 | beds | how many bedrooms are there | 
| 2 | livings | how many leving room are there | 
| 3 | wc | no of water closet | 
| 4 | user_id | each user has his own id |
| 5 | id | each post/ad has it own id (this is unique) |
| 6 | title | title of the post |
| 7 | content | content in the page of each post | 
| 8 | imgs | list contain the images of each pos |
| 9 | create_time | the creation of the pag |
| 10 | refresh | last time it was upddated |
| 11 | district | neighborhood name |
| 12 | street_width | the width of the street |
| 13 | age | how old is the apartment |
| 14/15/16 | kitchen , ac , furnished | does the apartment contain this facilitys or not | 
| 17 | location | the lat and mag of the apartment (if needed i will separate them) | 
| 18/19 | width ,length | the width and the length | 
| 20 | area | the area of the apartment |
| 21 | advertiser_type | what type of dealer (exclusive marketer , normal marketer , owner , agent ) | 
| 22 | review | the reviews of the advertiser |
| 23 | profileImg | does the advertiser has image or not | 
| 24 | userName | the username of the advertiser | 
| 25 | iam_verified | is the advertiser verified or not |
| 26 | path | indicate the path of the path of the post from the home page | 
| 27 | price | the price of the apartment | 
| 28 | last_update | what time was the last update to the page |
| 29 | DayOFRent | at what day was it rented |
| 30 | timeBeforRent | how long did it take to get rented |
| 31 | onMarket | how long is the post posted (the time from the creation of the post till today ) |
| 32 | isRent | check if the apartment rented or not ) |


the data stucture is
```{bash}
├── LR
│   └── app.py <----- bulding the site
├── README.md
├── data < ----- day of webscraping from 6th - 21st 
│   ├── 10-8-2022
│   ├── 11-8-2022
│   ├── 12-8-2022
│   ├── 13-8-2022
│   ├── 14-8-2022
│   ├── 15-8-2022
│   ├── 16-8-2022,21:30.csv
│   ├── 17-8-2022.csv
│   ├── 18-8-2022.csv
│   ├── 19-8-2022.csv
│   ├── 2-8-2022
│   ├── 21-8-2022.csv
│   ├── 23-8-2022.csv
│   ├── 3-8-2022.csv
│   ├── 6-8-2022
│   ├── 7-8-2022
│   ├── 8-8-2022
│   ├── 9-8-2022
│   ├── AQAR_TEST.csv
│   ├── ML.csv
│   ├── ML_TEST.csv
│   ├── ML_TEST2.csv
│   ├── aqar.csv
│   ├── from_30-7-2022_To_12-8-2022
│   ├── the 29-7-2022.csv
│   ├── try.csv
│   ├── tryML.csv
│   └── yest.csv
├── model
│   ├── classification.ipynb <----- clasification model
│   └── regression.ipynb
|
└── src
    ├── catboost_info <- for catboost package
    │   ├── catboost_training.json
    │   ├── learn
    │   │   └── events.out.tfevents
    │   ├── learn_error.tsv
    │   ├── test
    │   │   └── events.out.tfevents
    │   ├── test1
    │   │   └── events.out.tfevents
    │   ├── test_error.tsv
    │   ├── time_left.tsv
    │   └── tmp
    ├── class.pkl <----- pkl file to use in app.py for the site 
    ├── cleaning.ipynb <----- cleaning to data set 
    ├── featureEng.ipynb <----- prepare to model 
    ├── features <----- creating features 
    │   ├── onMarket.ipynb
    │   └── timeBeforeRent.ipynb
    ├── info.ipynb <----- info about dataset 
    ├── join.ipynb <----- join data set togather 
    ├── make_dataset.ipynb <----- webscraping
    ├── reg.pkl <----- pkl file to use in app.py for the site  
    └── visualization <----- EDA
        └── EDA.ipynb
```
