import streamlit as st
import pandas as pd
import joblib
df = pd.read_csv('./data/ML.csv')
L1 = list(df.district.unique())
L2 = list(df.advertiser_type.unique())
L3 = list(df.zone.unique())
# Title
st.header("Streamlit Machine Learning App")

# Input bar 1
user_id  = st.text_input('write your user id if you have one' , placeholder  = "1495817")
# txt = st.text_area('Text to analyze')
# st.write('Sentiment:', run_sentiment_analysis(txt))
# height = st.slider("Enter Height", 75, 95, 75)
len_of_title  = st.text_input("write the title you want to pu in the site " , placeholder  = 'شقة للإيجار في شارع إبراهيم بن الأحمدي')
len_of_content = st.text_area('enter the content that you want to put in the site ') 
img_in_post = st.slider('how many image you want to put  ', 1, 30, 8)
age =    st.slider('how old is your apartment  note that 0 indicate new', 0, 40, 2)
beds =  st.slider('how many bedrooms does your apartment have ', 1, 7, 1)
livings = st.slider('how many living room does your apartment have ', 0, 5, 1)
wc =    st.slider('how many water closet  does your apartment have ', 0, 5, 1)
area = st.number_input("what is the area of the apartment  ")
street_width = st.number_input("what is the street width of the apartment  ")
# age = st.number_input("how old is your apartment  " )
price  = st.number_input("Enter price you want to  ")

ketchen1 = st.radio(
     "does the apartment has  ketchen ",
     ('YES', 'NO'))
if ketchen1 == 'YES':
    ketchen = 1 
else :
    ketchen = 0 
ac1 = st.radio("does the apartment has  ac ON ",
     ('YES', 'NO'))
if ac1 == 'YES':
    ac = 1 
else :
    ac = 0 
furnished1  = st.radio(
     "is the apartment furnished ",
     ('YES', 'NO'))
if furnished1 == 'YES':
    furnished = 1 
else :
    furnished = 0 

profileImg1 =  st.radio(
     "do you have profile image ",
     ('YES', 'NO'))
if profileImg1 == 'YES':
    profileImg = 1 
else :
    profileImg = 0 
iam_verified1  =   st.radio(
     "are you varified user ",
     ('YES', 'NO'))
if iam_verified1 == 'YES':
    iam_verified = 1 
else :
    iam_verified = 0 
zone =  st.selectbox(
     'what is the location of  the apartment ',
     (L3))
district = st.selectbox(
     'How would you like to be contacted?',
     (L1))
advertiser_type = st.selectbox(
     'what is your status in the site ',
     (L2))
review =   st.number_input("your review in the site  " , min_value=1 , max_value=5)
# createYEAR = 
# createMONTH  = 
# createDAY = 
if st.button("Submit"):
    len_of_title = len(len_of_title)
    len_of_content = len(len_of_content)
    # # Unpickle classifier
    clf = joblib.load("./src/class.pkl")
    
    # # Store inputs into dataframe
    X = pd.DataFrame([[user_id, len_of_title, price ,len_of_content , img_in_post ,  beds , livings , wc , area , street_width , age , ketchen1 ,ac1 ,furnished , district , advertiser_type , review , profileImg , iam_verified , zone ]], 
                     columns = ['user_id', 'len_of_title', 'len_of_content' , 'img_in_poss' , 'price' , 'beds' , 'livings' , 'wc' , 'area' , 'street_width' , 'age' , 'ketchen' ,'ac' ,'furnished' , 'district' , 'advertiser_type' , 'review' , 'profileImg' , 'iam_verified' , 'zone'])
    X = X.replace(["YES", "NO"], [1, 0])
  
    # # Get prediction
    prediction = clf.predict(X)[0]
    if prediction == True:
        clf1 = joblib.load("./src/reg.pkl")
        prediction1 = clf1.predict(X)[0]
        round(prediction1)
    # Output prediction
    # for col in X:
        st.text(f"This apartment will be rented in {round(prediction1)} days")
    else:
        st.text(f"This apartment will not be rented ")