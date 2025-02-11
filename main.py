import streamlit as st
from script import (scrape_website,
split_dom_content, clean_body_content,extract_body_content,
)

from parse import parse_with_ollama
st.title("AI WEB SCRAPER")

url = st.text_input("Enter the URL to scrape:")

if st.button("Scrape"):
        st.write("Scraping....")
        # Here you would call your scraping function
        # For example: results = scrape(url)
        # Then display the results
        # st.write(results)
        result = scrape_website(url)
        body_content = extract_body_content(result)
        cleaned_content = clean_body_content(body_content)

        st.session_state.dom_content = cleaned_content

        with st.expander("View DOM Content"):
                st.text_area("DOM Content",cleaned_content, height=300)
        print(result)

if "dom_content" in st.session_state:
        parse_description = st.text_area("Describe what you want to look for")
if st.button("Parse"):
        if parse_description:
                st.write("Parsing....")

                dom_chunks = split_dom_content(st.session_state.dom_content)
                result = parse_with_ollama(dom_chunks, parse_description)
                st.write(result)
if st.button("Amazon") in st.session_state:   
        if parse_description:
                st.write("Parsing....")