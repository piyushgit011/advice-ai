import os
import openai
import streamlit as st

st.title("Advice Generator")


profile = st.text_input("Enter your profile:")
interest = st.text_input("Enter your area of interest:")
api = st.text_input("Enter your API key:")

openai.api_key = api

if st.button("Get Advice"):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": "you are one of the best market advisor and mentor for the people of different areas of interest."
            },
            {
                "role": "user",
                "content": f"hi i am {profile} i need an advice for {interest}. please give me some detailed advice to be relevant in the industry."
            },
        ],
        temperature=1,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    st.subheader("Advice:")
    print(response.choices[0].message.content)
    st.write(response.choices[0].message.content)  

  