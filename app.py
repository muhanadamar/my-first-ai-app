
import streamlit as st
import requests

st.set_page_config(
    page_title="My AI World",
    page_icon="🤖"
)

st.title("🤖 My AI World")
st.write("Welcome! Ask me anything.")

question = st.text_input("What would you like to ask?")

if st.button("Ask AI") and question.strip():
    try:
        token = st.secrets["CLOUDFLARE_API_TOKEN"]
        account_id = st.secrets["CLOUDFLARE_ACCOUNT_ID"]

        url = (
            f"https://api.cloudflare.com/client/v4/accounts/"
            f"{account_id}/ai/run/@cf/moonshotai/kimi-k2.7-code"
        )

        headers = {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json"
        }

        data = {
            "messages": [
                {
                    "role": "system",
                    "content": "You are a friendly, helpful assistant."
                },
                {
                    "role": "user",
                    "content": question
                }
            ]
        }

        with st.spinner("Thinking..."):
            response = requests.post(
                url,
                headers=headers,
                json=data,
                timeout=60
            )

        if response.ok:
            result = response.json()
            answer = result.get("result", {}).get("response")

            if answer:
                st.success(answer)
            else:
                st.error("The AI returned an unexpected response.")
        else:
            st.error(
                f"Cloudflare returned error {response.status_code}. "
                "Please check your settings."
            )

    except Exception:
        st.error(
            "I couldn't connect to the AI. "
            "Please check your Secrets and try again."
        )
