import streamlit as st
import geemap.foliumap as geemap

st.set_page_config(layout="wide")

# Customize the sidebar
markdown = """

"""

st.sidebar.title("About")
st.sidebar.info(markdown)
logo = "https://i.imgur.com/UbOXYAU.png"
st.sidebar.image(logo)

# Customize page title
st.title("Earth Engine Web App")

st.markdown(
    """
 
    """
)

st.header("Instructions")

markdown = """

"""

st.markdown(markdown)

m = geemap.Map()
m.add_basemap("OpenTopoMap")
m.to_streamlit(height=500)
