# jina-shortcode-front(covidQA)

This is a simple example using the [Jina](https://github.com/jina-ai/jina/) neural search framework. 
<br>
Data set used: [Covid-QA](https://www.kaggle.com/xhlulu/covidqa) from kaggle
<br>


## If you want to run it in local
## Instructions
This is a shortcode using jinahub's indexer and encoder. You can try running this project with the Run on ainize button.
<br>
[![Run on Ainize](https://ainize.ai/images/run_on_ainize_button.svg)]()

### Clone this repo

```shell
git clone https://github.com/msh1273/jina-shortcode-covidQA-frontend.git
cd jina-shortcode-covidQA-frontend
```

### Create a virtual environment (optional)

We wouldn't want our project clashing with our system libraries, now would we?

```shell
virtualenv env --python=python3.8 # Python versions >= 3.7 work fine
source env/bin/activate
```

### Install everything

Make sure you're in your virtual environment first!

```shell
pip install -r requirements.txt
```

### Run your app

```shell
streamlit run front.py
```
## FAQ

### Why this dataset?

Ask any questions you have about Corona. jina will show you the desired result even if you type a typo.
