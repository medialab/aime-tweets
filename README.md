# AIME Tweets

Collect latest tweets related to Bruno Latour and ModesOfExistence.org for display on the website.


## Install

Clone this repository, then create a Python2.7 virtualenv, for instance using [pyenv](https://github.com/pyenv/pyenv-installer):

```
git clone --recursive https://github.com/medialab/aime-tweets
cd aime-tweets
pyenv install 2.7.15
pyenv virtualenv 2.7.15 aime-tweets
pyenv activate aime-tweets
pip install -r got/requirements.txt
```

## Run 

Using the virtualenv:

```
./collect_tweets.py
```

