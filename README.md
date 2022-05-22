# ScrapingFb
+This project is a Rest API, developed with FastAPI as RESTful API framework and Postgresql as local database, allows to retrieve data and save them in a local database from a public page on Facebook.

+You can run it with Docker by running the command "docker-compose up --build" in the path of the "api" folder.
Then, you can consult the "localhost/fbscrap/" url or you can execute the "Post" HTTP method by sending a json object which contains the following 3 elements:

*pagename : Name of the facebook page, it will be used in the database to identify the origin of each line (publication).

*pagrurl : presents the link of the publications of the chosen facebook page. it is of the form https://www.facebook.com/pg/<url_page_name>/posts/" with <url_page_name> can be obtained by deleting the "https://www.facebook.com/" part of the link of the page.

*scrollnbr : This is the number of times we will scroll down the facebook page to see more posts.
