
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
- Create a virtual environment for the app
- Activate the virtual environment
- Go to the project
- Install the application requirements
- Make django migrations
- Run django migrations
- Run the application
- Open the applciation in your browser
- Observe on your terminal how sent events are logged.

# Issues encountered
- The link to (i) given on the wiki is broken; due to the fact that it was deprecated for some reason. This (i) file has to be added to the S3 bucket. Inorder to solve this, I went to a previous commit to get the (i) file and it worked.

# Next steps
- I am currently looking at ways to proceed with enrichment up to the data visualisation; so I have a 360 degrees understanding of how this works.