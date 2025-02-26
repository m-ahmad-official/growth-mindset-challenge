import streamlit as st
import requests

def get_country_info(country_name):
    country_mapping = {
        "china": "china?fullText=true",
        "england": "united kingdom?fullText=true",
        "scotland": "united kingdom?fullText=true",
        "oman": "oman?fullText=true",
        "ireland": "ireland?fullText=true"
    }
    
    if country_name.lower() == "israel":
        return None
    
    query = country_mapping.get(country_name.lower(), country_name)
    url = f"https://restcountries.com/v3.1/name/{query}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()[0]
    return None


st.set_page_config(page_title="Country Info", page_icon="🌍", layout="centered")

st.markdown("<h3 style='text-align: center;'>🚀 Growth Mindset Challenge: Web App with Streamlit</h3>", unsafe_allow_html=True)
st.markdown("---")

st.title("🌍 Country Information App")

if "country_name" not in st.session_state:
    st.session_state.country_name = "Pakistan"

def update_country():
    st.session_state.country_name = st.session_state.input_text
    st.session_state.fetch_data = True

country_name = st.text_input("Enter country name:", st.session_state.country_name, key="input_text", on_change=update_country)

if st.button("Get Info") or st.session_state.get("fetch_data", False):
    country_data = get_country_info(st.session_state.country_name)
    st.session_state.fetch_data = False

    if country_data:
        col1, col2 = st.columns([1, 2])
        
        with col1:
            st.image(country_data['flags']['png'], caption=f"Flag of {country_name}", use_container_width=True)
        
        with col2:
            st.subheader(f"{country_data['name']['common']}")
            st.write(f"**Capital:** {country_data['capital'][0]}")
            st.write(f"**Region:** {country_data['subregion']}")
            st.write(f"**Population:** {country_data['population']:,}")
            st.write(f"**Currency:** {list(country_data['currencies'].keys())[0]} - {list(country_data['currencies'].values())[0]['name']}")
            st.write(f"**Languages:** {', '.join(country_data['languages'].values())}")
    else:
        st.error("Country not found! Please try again.")

st.markdown("---")
st.markdown("<p style='text-align: center; font-size: 14px;'>© 2025 Developed by <span style='font-weight: bold;'>Muhammad Ahmed</span>. All rights reserved. 🌍</p>", unsafe_allow_html=True)