
# Snowplow technical exercise
Full description of the exercise:
https://gist.github.com/goodits/0fce9ac581fd13f769124c570bc82f82

# About the application
This is a simple blog application written in django 2.2 with the following functionalities:
- List all articles on the application
- View a single article on a Page
- Comment on an article

# System requirements
- Python version: 3.7.7
- Django version: 2.2
- Ubuntu 18.04 (I haven't tested on other Operating systems or other versions of Ubuntu)

# Local deployment
- Clone the github repo

`git clone https://github.com/mikael19/sp_tech.git`

- Create a virtual environment for the app

`mkdir v_env`

`virtualenv --python=/usr/bin/python3.7 v_env/`

- Activate the virtual environment

`source v_env/bin/activate`

- Go to the project

`cd sp_tech`

- Install the application requirements

`pip install -r requirements.txt `

- Make django migrations
No need to do this. I pushed the code with migrations
- Run django migrations
No need to do this I push the sqlite database too.

- Run the application

`python manage.py runserver`

- Open the application in your browser
```
Open your browser
Go to: http://127.0.0.1:8000```

- Observe on your terminal how sent events are logged.

- Example log in snowplow micro

```[
   {
      "event": {
         "api": {
            "vendor": "com.snowplowanalytics.snowplow",
            "version": "tp1"
         },
         "parameters": {
            "e": "pv",
            "eid": "92f1e8e7-a510-4241-b75f-e8a3f75214e9",
            "url": "http://127.0.0.1:8000/",
            "stm": "1588950207000",
            "tv": "py-0.8.3",
            "p": "pc",
            "dtm": "1588950207030"
         },
         "contentType": null,
         "source": {
            "name": "ssc-0.15.0-stdout$",
            "encoding": "UTF-8",
            "hostname": "0.0.0.0"
         },
         "context": {
            "timestamp": "2020-05-08T15:03:27.042Z",
            "ipAddress": "172.17.0.1",
            "useragent": "python-requests/2.23.0",
            "refererUri": null,
            "headers": [
               "Host: 0.0.0.0:9090",
               "User-Agent: python-requests/2.23.0",
               "Accept-Encoding: gzip, deflate",
               "Accept: */*",
               "Connection: keep-alive",
               "Timeout-Access: <function1>"
            ],
            "userId": "a3c5605d-c1ed-4b83-bef6-9c45057c340a"
         }
      },
      "eventType": "pv",
      "schema": null,
      "contexts": null
   }
]```

# Issues encountered
- The link to (i) given on the wiki is broken; due to the fact that it was deprecated for some reason. This (i) file has to be added to the S3 bucket. Inorder to solve this, I went to a previous commit to get the (i) file and it worked.

# Next steps
- I am currently looking at ways to proceed with enrichment up to the data visualisation; so I have a 360 degrees understanding of how this works.