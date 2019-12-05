## It is a one-shot command-line RSS reader by Zviger.
### Installation
Install [Python3.8](https://www.python.org/downloads/)

Install [pip](https://pip.pypa.io/en/stable/installing/)

Install GIT.
This [link](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) 
may be useful in this matter.
Clone this repository in the folder you need using this command
```text
git clone https://github.com/Zviger/PythonHomework
```
after change the branch to the project branch and run
```text
git checkout final_proj
```
Now you can install the application itself using this command from the application folder
```text
pip install . --user
```
You will also need MongoDB. You can install and run
MongoDB on your system using this [link](https://docs.mongodb.com/manual/installation/).
But you can install [Docker](https://docs.docker.com/install/) and
[Docker-Compose](https://docs.docker.com/compose/install/).


To start the container with MongoDB, run the following command in the application folder
```text
docker-compose up
```
* The application and database are connected through port 27017.

You can stop container with MongoDB by command
```text
docker-compose stop
```
and run again
```text
docker-compose start
```
You can execute the command
```text
docker-compose down
```
but you will lose all saved data from the database.


Congratulations!

Run
```text
rss-reader --help
```
to learn about the features of the application and start using it.
### User interface
```text
usage: rss-reader [-h] [--version] [-l LIMIT] [--verbose] [--json] [--length LENGTH] [--date DATE] [--to_html PATH] [--to_fb2 PATH] [--colorize] source

positional arguments:
  source                RSS URL

optional arguments:
  -h, --help            show this help message and exit
  --version             Print version info
  -l LIMIT, --limit LIMIT
                        Limit news topics if this parameter provided
  --verbose             Print result as JSON in stdout
  --json                Outputs verbose status messages
  --length LENGTH       Sets the length of each line of news output
  --date DATE           Search past news by date in format yeardaymonth (19991311)
  --to_html PATH        Save news by path in html format
  --to_fb2 PATH         Save news by path in fb2 format
  --colorize            Make console text display colorful
```

### Json structure
```json
[
  {
    "title": "Yahoo News - Latest News & Headlines",
    "link": "https://www.yahoo.com/news",
    "items":
      [
        {
          "title": "Sorry, Hillary: Democrats don&#39;t need a savior",
          "link": "https://news.yahoo.com/sorry-hillary-democrats-dont-need-a-savior-194253123.html",
          "author": "no author",
          "published_parsed": [2019, 11, 13, 19, 42, 53, 2, 317, 0],
          "description": "With the Iowa caucuses fast approaching, Hillary Clinton is just the latest in the colorful cast of characters who seem to have surveyed the sprawling Democratic field, sensed something lacking and decided that \u201csomething\u201d might be them.",
          "img_links":
            [
              "http://l.yimg.com/uu/api/res/1.2/xq3Ser6KXPfV6aeoxbq9Uw--/YXBwaWQ9eXRhY2h5b247aD04Njt3PTEzMDs-/https://media-mbst-pub-ue1.s3.amazonaws.com/creatr-uploaded-images/2019-11/14586fd0-064d-11ea-b7df-7288f8d8c1a7"
            ]
        }
      ]
  }
]
```
### Cashing
The news is saved to the database when news output commands are executed. MongoDB is used as a database management system.
When the --date parameter is used, news is downloaded from the database by the entered date and the entered RSS link.

Features:
* The --limit parameter affects the amount of data loaded into the database.
* Date must be written in the yearmonthday (example - 19991113) format.

### Saving in files
Using the "--to_html" and "--to_fb2" parameters, you can save files at a given path.
The path should be written in the style of UNIX systems (example: ./some/folder).
File names are formed using the "feed[index].[format]" template (example: feed13.html).
File indices go sequentially and a new file fills this sequence or is set to the end.
What does this mean: if, for example, there are files "feed1.html" and "feed3.html",
a new file will be created with the name "feed2.html".