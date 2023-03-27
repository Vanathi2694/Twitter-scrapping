import streamlit as st
import pandas as pd
import snscrape.modules.twitter as snmtwitter
from pymongo import MongoClient
import csv

w = st.text_area("Type word to be scrapped")
date = st.date_input("Give the start date the data to be scrapped(Start date should be low or before the End date):")
date1 = st.date_input("Give the end date the data to be scrapped:")
choice = st.number_input("Mention the tweetcount to be:")
click = st.button("Enter")


tweet_list = []
client = MongoClient("mongodb+srv://vanathisoundararajan:vanso2628@cluster0.cdvekaq.mongodb.net/test")
clientatlas = MongoClient("mongodb+srv://vanathisoundararajan:vanu2628@cluster0.cdvekaq.mongodb.net/?retryWrites=true&w=majority")
newdb = client["twitterscrapping"]
newcol = newdb["datas"]


for i, tweet in enumerate(snmtwitter.TwitterSearchScraper('w').get_items()):
    if i > 1000 and date < date1 and choice >= tweet.retweetCount:
        break
tweet_list.append([tweet.date, tweet.id, tweet.url, tweet.content, tweet.user, tweet.replyCount, tweet.retweetCount, tweet.lang, tweet.source, tweet.likeCount])
tweets_df1 = pd.DataFrame(tweet_list, columns=['Datetime', 'Tweetid', 'Url', 'Content', 'User', 'Replycount', 'Retweetcount', 'Language', 'Source', 'Likecount'])
st.dataframe(tweets_df1)


@st.cache_data
def dwl1(df):
    return df.to_json().encode('utf-8')


json = dwl1(tweets_df1)
if 'Download_json_File' not in st.session_state:
    st.session_state.Download_json_File = True
st.download_button('Download json File', file_name="python_tweetscrap.json", data=json, mime="text/json")
st.write(st.session_state.Download_json_File)

file = open("python_tweetscrap.json", "r")
dfd1 = pd.read_json(file)
data2 = dfd1.to_dict(orient="records")


newcol.insert_many(data2)


@st.cache_data
def dwl(df):
    return df.to_csv().encode('utf-8')


csv = dwl(tweets_df1)
if 'Download_csv_File' not in st.session_state:
    st.session_state.Download_csv_File = True
st.download_button('Download csv File', file_name="python_tweetscrap.csv", data=csv, mime="text/csv")
st.write(st.session_state.Download_csv_File)

data = st.file_uploader("Upload a CSV")

csvfile = open("python_tweetscrap.csv", 'r')
dfd = pd.read_csv(csvfile)
data1 = dfd.to_dict(orient="records")
newcol.insert_many(data1)


print("connection successful")
client.close()
clientatlas.close()
