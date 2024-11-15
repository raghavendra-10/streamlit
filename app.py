import streamlit as st
import requests
import json

# Streamlit app
st.title("BH Coordination Follow-Up API")

# Input prompt
st.header("Provide the details for the API call")
prompt = st.text_area("Prompt", "Enter your prompt here...")

if st.button("Submit"):
    if prompt.strip() == "":
        st.error("Please provide a valid prompt!")
    else:
        # API endpoint
        url = "https://dr9gvhct3f.execute-api.us-west-2.amazonaws.com/dev/chat"

        # Payload
        payload = {"prompt": prompt}

        # Headers
        headers = {
            "Content-Type": "application/json"
        }

        # API call
        try:
            response = requests.post(url, headers=headers, data=json.dumps(payload))
            if response.status_code == 200:
                st.success("API call successful!")
                result = response.json()
                st.json(result)
            else:
                st.error(f"API call failed with status code {response.status_code}")
                st.error(response.text)
        except Exception as e:
            st.error(f"An error occurred: {e}")
