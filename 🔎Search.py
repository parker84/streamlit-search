import os
import streamlit as st

st.set_page_config(
    page_title="Streamlit Search",
    page_icon="🔍"
)

st.title("Streamlit Search")

clean_page = None

pages = sorted(os.listdir('pages'))
page2cleanpage = {
    page: ' '.join(page.split('_')[1:]).replace('.py', '')
    for page in pages
}
cleanpage2page = {
    cleanpage: page for page, cleanpage in page2cleanpage.items()
}

clean_pages = [page2cleanpage[page] for page in pages]
clean_page = st.selectbox(
    '🔎 Search for a Dashboard',
    options=clean_pages,
    index=None,
    placeholder='start typing...',
)
if clean_page is not None:
    st.switch_page(
        f'pages/{cleanpage2page[clean_page]}'
    )