# Twitter-scrapping
Skills:

      Python scripting
      MongoDb
      Streamlit
      Snscrape
      
      
Domain:

      Social Media
      
      
Results:

      To scrape the twitter data and store it in the database and allow the user to upload and download the data in multiple formats
      
      
GUI used in streamlit:

      SelectBox for Keyword or Hashtag to be searched
      Text area for keyword or hashtag
      Start Date
      End Date
      Number Input For Tweet Count
      Button To Enter
      2 Download Buttons For CSV and json File Format to Download
      Upload Button
      Warning Box if word is not typed
      Success Box
      Snowflake
      
      
Process:

      *Type the keyword or hashtag to be searched using streamlit
      *After entering the date and tweetcount using streamlit, the twitter data will be scrapped using snscrape
      *We can download the data either as csv or json format using streamlit
      *Connection is given for python and MongoDb cluster or MongoclientAtlas
      *The data will be inserted into MongoDb and MongoClientAtlas
      *We can upload the data using upload button
      *The success box and snoflake will appear after succefull scrapping


Install in python:

        pip install streamlit
        pip install snscrape
        pip install pymongo
        pip install pandas


Run:

        Streamlit run filename
        Pandas run filename
        Snscrape run filename
        Pymongo run filename
        
        
The code will be executed in streamlit browser after clicking the url after running streamlit
      
[Your Link Here](https://www.linkedin.com/posts/vanathi-soundararajan-04289726btwitter-scrapping-activity-7046501839210434560-8opL?utm_source=share&utm_medium=member_android)
