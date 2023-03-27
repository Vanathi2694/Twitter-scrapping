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
for i,tweet in enumerate(snmtwitter.TwitterSearchScraper('w').get_items()):
        if i > 1000 and date < date1 and choice >= tweet.retweetCount:
            break
tweet_list.append([tweet.date, tweet.id, tweet.url, tweet.content, tweet.user, tweet.replyCount, tweet.retweetCount, tweet.lang, tweet.source, tweet.likeCount])
tweets_df1 = pd.DataFrame(tweet_list, columns=['Datetime', 'Tweetid', 'Url', 'Content', 'User', 'Replycount', 'Retweetcount', 'Language', 'Source', 'Likecount'])
#print(tweets_df1.head())
st.dataframe(tweets_df1)

#tweets_df1.to_json("python_tweetscrap.json",index=True)
#st.download_button("Download json File", "python_tweetscrap.json")
#file = open("python_tweetscrap.json", "r")

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

#newdb.newcol.insert_one({"name":"vanu"})
newcol.insert_many(data2)


#x = json.loads(file)
#newdb.newcol.insert_many(file)

@st.cache_data
def dwl(df):
    return df.to_csv().encode('utf-8')


csv = dwl(tweets_df1)
if 'Download_csv_File' not in st.session_state:
    st.session_state.Download_csv_File = True
st.download_button('Download csv File', file_name="python_tweetscrap.csv", data=csv, mime="text/csv")
st.write(st.session_state.Download_csv_File)

data = st.file_uploader("Upload a CSV")
#file1 = open("python_tweetscrap.csv", "r")

csvfile = open("python_tweetscrap.csv", 'r')
dfd = pd.read_csv(csvfile)
data1 = dfd.to_dict(orient="records")
newdb.newcol.insert_many(data1)


#reader=csv.DictReader(csvfile)
#for i in reader:
#        row = {}
#for j in tweets_df1:
#       row[j]=i[j]
#newcol.insert_many(row)
#x = newcol.insert_one(csvfile)
#newdb.newcol.find()
# ins_id = x.inserted_id
# print(x)
#x.find()
#   print(ins_id)
#  ins_id.find()
print("connection successful")
client.close()
clientatlas.close()
#newcol.find(tweet_list)


# return name_to_search

#csvfile=open("python_tweet_scrap.csv",'r')
#      reader=csv.DictReader(csvfile)
#     for i in reader:
#        row = {}
#       for j in tweets_df1:
#          row[j]=i[j]
#         newcol.insert_many(row)"""
