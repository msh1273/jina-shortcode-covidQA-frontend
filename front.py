import streamlit as st
import requests

# Set up some defaults
endpoint = 'https://master-jina-shortcode-covid-qa-msh1273.endpoint.ainize.ai/search'

def get_data(query: str, endpoint: str) -> dict:
    headers = {
        "Content-Type": "application/json",
    }

    data = '{"mode":"search","data":["' + query + '"]}'

    response = requests.post(endpoint, headers=headers, data=data)
    content = response.json()

    matches = content["data"]["docs"][0]["matches"]

    return matches


# layout
max_width = 1200
padding = 2


st.markdown(
    f"""
<style>
    .reportview-container .main .block-container{{
        max-width: {max_width}px;
        padding-top: {padding}rem;
        padding-right: {padding}rem;
        padding-left: {padding}rem;
        padding-bottom: {padding}rem;
    }}
    .reportview-container .main {{
        color: "#111";
        background-color: "#eee";
    }}
</style>
""",
    unsafe_allow_html=True,
)

# Setup sidebar
st.sidebar.title("Settings")
endpoint = st.sidebar.text_input(label="Endpoint", value=endpoint)
output_format = st.sidebar.selectbox(label="Output format", options=["Plain text", "JSON"])

st.title("Simple Jina Search about COVID-QA")

query = st.text_input(
    label="Your search term"
)

if st.button(label="Search"):
    if not query:
        st.markdown("Please enter a query")
    else:

        matches = get_data(query=query, endpoint=endpoint)
        if output_format == "JSON":
            st.json(matches)
        elif output_format == "Plain text":
            for match in matches:
                st.markdown(f"- {match['text']}")
                st.write(match['tags']['answer'])