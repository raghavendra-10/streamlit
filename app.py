import streamlit as st
import requests
import json

# Streamlit app
st.title("BH Coordination Follow-Up API")

# Input prompt
st.header("Provide the details for the API call")
prompt = st.text_area("Prompt", "Enter your prompt here...")
static = "Question: Based on the conversation, analyze the patient's concerns and provide structured insights in the following format:-Issues: (Object with key-value pairs) Identify the top three issues the patient has explicitly mentioned or implied during the conversation. These should be concise statements or direct quotes that accurately reflect their primary concerns. Ensure clarity and specificity.-Assessments: (Object with key-value pairs) Recommend the most appropriate behavioral health assessments based on the discussion. Each assessment should align with the patient’s identified concerns and provide a rationale for its relevance.-Technique: (Object with key-value pairs) Suggest only one evidence-based therapy technique that directly addresses the identified concerns. Provide a brief yet comprehensive definition, sourced from a validated knowledge base, explaining how this technique will be implemented in future sessions.-Questions: (Array of strings) Provide the top three relevant follow-up questions that align with the suggested therapy technique. These questions should be specific, open-ended, and designed to guide the next conversation toward uncovering deeper insights or tracking progress.-Emotions: (Object with key-value pairs) Identify the top four emotions, thoughts, feelings, or behaviors from the following predefined list or their synonyms:Distress, stress, anger, frustration, anxiety, depression, low self-confidence, low self-esteem, feelings of loneliness, loss of purpose, grief, sorrow, anguish, pain, agony, discomfort, upset, worry, fretfulness, perturbation, gloom, melancholy, dejection, downheartedness, low spirits, discouragement, disengagement, tearfulness, dispiritedness, pessimism, dullness, weakness, disappointment, defeat, burden.If it is difficult to extract emotions from the conversation, provide a template with placeholders for manual input. Note: based on the conversation if it is difficult to identify these then just give a basic template with these keys Please provide the response in JSON format with the keys  \"issues\", \"assessments\", \"technique\",\"questions\" and \"emotions\"."
final_prompt = f"{prompt}\n\n{static}"
if st.button("Submit"):
    if prompt.strip() == "":
        st.error("Please provide a valid prompt!")
    else:
        # API endpoint
        url = "https://em8fhimio3.execute-api.us-west-2.amazonaws.com/dev"

        # Payload
        payload = {"prompt": final_prompt}

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
