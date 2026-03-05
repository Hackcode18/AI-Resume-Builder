import streamlit as st
from openai import OpenAI

client = OpenAI(api_key="YOUR_API_KEY")

st.title("AI Resume Builder")

name = st.text_input("Enter your name")
skills = st.text_area("Enter your skills")
education = st.text_area("Education")
projects = st.text_area("Projects")
experience = st.text_area("Experience")

if st.button("Generate Resume"):

    prompt = f"""
    Create a professional resume for:

    Name: {name}
    Skills: {skills}
    Education: {education}
    Projects: {projects}
    Experience: {experience}
    """

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[{"role":"user","content":prompt}]
    )

    resume = response.choices[0].message.content

    st.subheader("Generated Resume")
    st.write(resume)
