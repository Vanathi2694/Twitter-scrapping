import streamlit as st
import pandas as pd
import snscrape.modules.twitter as snmtwitter
from altair.examples.pyramid import df
from pymongo import MongoClient


st.write("Twitter Data Scrapping")
choice = st.selectbox("Pick One", ["Keyword", "Hastag"])
w = st.text_area("Type " + choice + " to be scrapped")
date = st.date_input("Give the start date the data to be scrapped(Start date should be low or before the End date):")
date1 = st.date_input("Give the end date the data to be scrapped:")
choice = st.number_input("Mention the tweetcount to be:")
click = st.button("Enter")

tweets_df1 = pd.DataFrame()
tweet_list = []
client = MongoClient("mongodb+srv://vanathisoundararajan:vanso2628@cluster0.cdvekaq.mongodb.net/test")
clientatlas = MongoClient("mongodb+srv://vanathisoundararajan:vanu2628@cluster0.cdvekaq.mongodb.net/?retryWrites=true&w=majority")
newdb = client["twitterscrapping"]
newcol = newdb["datas"]


if w:
    if choice == "keyword":
        for i, tweet in enumerate(snmtwitter.TwitterSearchScraper(f'{w} since:{date} until:{date1}').get_items()):
            if i > 1000 and date < date1 and choice >= tweet.retweetCount:
                break
            tweet_list.append([tweet.date, tweet.id, tweet.url, tweet.content, tweet.user, tweet.replyCount, tweet.retweetCount, tweet.lang, tweet.source, tweet.likeCount])
        tweets_df1 = pd.DataFrame(tweet_list, columns=['Datetime', 'Tweetid', 'Url', 'Content', 'User', 'Replycount', 'Retweetcount', 'Language', 'Source', 'Likecount'])
        st.dataframe(tweets_df1)
    else:
        for i, tweet in enumerate(snmtwitter.TwitterHashtagScraper(f'{w} since:{date} until:{date1}').get_items()):
            if i > 1000 and date < date1 and choice >= tweet.retweetCount:
                break
            tweet_list.append(
                        [tweet.date, tweet.id, tweet.url, tweet.content, tweet.user, tweet.replyCount, tweet.retweetCount, tweet.lang, tweet.source, tweet.likeCount])
        tweets_df1 = pd.DataFrame(tweet_list, columns=['Datetime', 'Tweetid', 'Url', 'Content', 'User', 'Replycount', 'Retweetcount', 'Language', 'Source', 'Likecount'])
        st.dataframe(tweets_df1)
else:
    st.warning("Enter the Keyword or Hashtag to be scrapped")


@st.cache_data
def dwl1(df):
    return df.to_json().encode('utf-8')


def downloading_json_file():
    json = dwl1(tweets_df1)
    if 'Download_json_File' not in st.session_state:
        st.session_state.Download_json_File = True
    st.download_button('Download json File', file_name="python_tweetscrap.json", data=json, mime="text/json")
    st.write(st.session_state.Download_json_File)


def json_file_open_insert():
    file = open("python_tweetscrap.json", "r")
    dfd1 = pd.read_json(file)
    data2 = dfd1.to_dict(orient="records")
    newcol.insert_many(data2)


@st.cache_data
def dwl(df):
    return df.to_csv().encode('utf-8')


def downloading_csv_file():
    csv = dwl(tweets_df1)
    if 'Download_csv_File' not in st.session_state:
        st.session_state.Download_csv_File = True
    st.download_button('Download csv File', file_name="python_tweetscrap.csv", data=csv, mime="text/csv")
    st.write(st.session_state.Download_csv_File)


def csv_file_open_insert():
    csvfile = open("python_tweetscrap.csv", 'r')
    dfd = pd.read_csv(csvfile)
    data1 = dfd.to_dict(orient="records")
    newcol.insert_many(data1)


def upl():
    data = st.file_uploader("Upload the data")
    return data


downloading_json_file()
json_file_open_insert()
downloading_csv_file()
csv_file_open_insert()
upl()
st.success("Data scrapped and collected successfully")
st.snow()
client.close()
clientatlas.close()
