# jina-shortcode-front(covidQA)

This is a simple example using the [Jina](https://github.com/jina-ai/jina/) neural search framework. 
<br>
Data set used: [Covid-QA](https://www.kaggle.com/xhlulu/covidqa) from kaggle
<br>


## If you want to run it in local
## Instructions
This is a shortcode using jinahub's indexer and encoder. You can try running this project with the Run on ainize button.
<hr>
이것은 jina를 쉽게 이해할 수 있도록 jina프레임워크를 사용하여 shortcode로 구성한 프로젝트입니다. covidQA의 news 데이터 셋을 사용하였으며 jinahub에 만들어져있는 encoder와 indexer를 가져와 사용했습니다.
<br> 
jinahub의 pytorchtransformerencoder는 distilbert-base-nli-stsb-mean-tokens모델을 사용하였으며 오타를 입력하더라도 유사한 질문과 답변을 확인하실 수 있습니다. simpleindexer에는 5개의 top_k를 보여줍니다.
<br><br>

<img src="./covidQA.gif">
<br>

[![Run on Ainize](https://ainize.ai/images/run_on_ainize_button.svg)](https://master-jina-shortcode-covid-qa-frontend-msh1273.endpoint.ainize.ai/)

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
