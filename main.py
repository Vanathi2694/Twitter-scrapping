import streamlit as st
import pandas as pd
import snscrape.modules.twitter as snmtwitter
from pymongo import MongoClient
import csv
import json

w = st.text_area("Type word to be scrapped")
date = st.date_input("Give the start date the data to be scrapped(Start date should be low or before the End date):")
date1 = st.date_input("Give the end date the data to be scrapped:")
choice = st.number_input("Mention the tweetcount to be:")
click = st.button("Enter")

def twitter_scrapping(name_to_search):
    try:
        tweet_list = []
        client = MongoClient("mongodb+srv://vanathisoundararajan:vanso2628@cluster0.cdvekaq.mongodb.net/test")
        clientatlas = MongoClient("mongodb+srv://vanathisoundararajan:vanu2628@cluster0.cdvekaq.mongodb.net/?retryWrites=true&w=majority")
        newdb = client["twitterscrapping"]
        newcol = newdb["datas"]

        for i,tweet in enumerate(snmtwitter.TwitterSearchScraper(w).get_items()):
            if i>1000 and date<date1 and choice>=tweet.retweetCount:
                break
        tweet_list.append([tweet.date,tweet.id,tweet.url,tweet.content,tweet.user,tweet.replyCount,tweet.retweetCount,tweet.lang,tweet.source,tweet.likeCount])
        tweets_df1=pd.DataFrame(tweet_list,columns=['Datetime','Tweetid','Url','Content','User','Replycount','Retweetcount','Language','Source','Likecount'])
        #print(tweets_df1.head())
        st.dataframe(tweets_df1)

        tweets_df1.to_json("python_tweetscrap.json",index=None)
        file = open( "python_tweetscrap.json", "r")
        tweets_df1.to_csv("python_tweetscrap.csv", index=None)
        file1 = open("python_tweetscrap.csv", "r")
       # x = json.loads(file)

        csvfile=open("python_tweetscrap.csv",'r')
        reader=csv.DictReader(csvfile)
        for i in reader:
            row = {}
            for j in tweets_df1:
                row[j]=i[j]
                newcol.insert_many(row)
       # x=newcol.insert_one(file1)
        #newdb.newcol.find()
       # ins_id = x.inserted_id
        dwl()


        upl()
        print(j)
        j.find()

     #   print(ins_id)
      #  ins_id.find()
        print("connection successful")
        client.close()
        clientatlas.close()
        #newcol.find(tweet_list)
    except:
        print("Give the word to be scrapped")
twitter_scrapping(w)

@st.cache_data
def upl(self):
    data = st.file_uploader("Upload a CSV")
    return data
@st.cache_data
def dwl(self):
    st.download_button("Download json File", file)
    st.download_button("Download csv File", file1)

# return name_to_search

