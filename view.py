import streamlit as st


def to_streamlit(data):
    # streamlit configuration
    page_title = 'Hello'
    layout = 'wide'
    sidebar_state = 'expanded'

    st.set_page_config(page_title=page_title, layout=layout, initial_sidebar_state=sidebar_state)
    st.text('Report')
    st.dataframe(data)
