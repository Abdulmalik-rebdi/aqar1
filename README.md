in this Repositorie there are 5 files each file is step to prepare the data 

the first file is the webscpaing : Webdcraping.ipynb 

in this file a gather the information in sa.aqar.fm the information a gathered is apartment in riyadh that are rented yearly  and everyday i ran this file to gather more inforamtion 

after that the next step is cleaning  after i finsh web scraping clean the data (edit the format from second to date  , split columns to havve more features , drop zero-varince features) all this happen in (cleaning.ipynb)

then next step is joining the dataframe into one dataframe (each day we have new csv file and we have to merge it with prevoius dataframes  ) this happen in file called join.ipynb

then the forth step is is adding new feature which indicate how long was the post availble untill it was sold  i added this feature in file called updateDate.ipynb 

now the data are Ready for the EDA

but i made extra file that will till me how many post from 2/08/2022 are still there (not sold) and how many post are removed(sold) just to have more data scince the first webscrapped i did was in 2/08/2022 i'm still not sure if am goning to use it . it is in check.ipynb file 




after cleaning this is the data i will be workimg on are 28 columns

1- beds: how many bedrooms are there

2 - livings : how many leving room are there

3- wc: no of water closet

4- user_id : each user has his own id

5- id : each post/ad has it own id (this is unique)

6- title : title of the post

7 - content : content in the page of each post

8- imgs : list contain the images of each post

9- create_time : the creation of the page

10 - refresh : last time it was upddated

11 - district : neighborhood name

12 - street_width : the width of the street

13 - age : how old is the apartment

(14,15,16) - ketchen , ac , furnished : does the apartment contain this facilitys or not

17 - location : the lat and mag of the apartment (if needed i will seperate them)

(18 , 19 )width , length = is the width and the length

20 - area = the area of the apartment

21 - advertiser_type = what type of dealler

22 - review = the reviews for the advertiser 23 - profileImg = TRUE / false 24 - UserName = the user name 25 - iam_verified = TRUE / false 26 - path = inddcate the path from the home page to the post (it will be helpful becouse we can know if it is in the north-east - west -center ... of riyadh ) 27 - last_update :last_update time 28 -the price of the apartment
