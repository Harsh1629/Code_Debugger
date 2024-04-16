from openai import OpenAI
import streamlit as st
import json

# f=open("keys/.api_key.txt")
# key=f.read()
client=OpenAI(api_key="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")

def code_review(code_input):
    response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[ 
        {"role": "system", "content": """ 
        You are a friendly AI Assistant. You take a python code as an input from the user.
        Your job is to explain the bugs and generate the fixed code as an output.
        Your output is a JSON with the following structure:
        {"Bugs": "review_on_code", "Code": '```python fixed_code```'}
        """},
        {"role": "user", "content": f"Fix and explain the bugs in the following python code: {code_input}"}
        ],
    temperature=0.5
)
    print("Response content:", response.choices[0].message.content)
    review=json.loads(response.choices[0].message.content)
    return review["Bugs"], review["Code"]

def main():
    st.title("Python Code Review App")
    st.write("Submit your Python code for review and receive feedback on potential bugs along with suggestions for fixes.")

   
    code_input = st.text_area("Enter your Python code here:")

    if st.button("Generate"):
        if code_input:
            
            bug_report, fixed_code = code_review(code_input)

           
            st.subheader("Bug Report")
            st.write(bug_report)

            st.subheader("Fixed Code")
            st.code(fixed_code, language='python')
        else:
            st.warning("Please enter some Python code!")

if __name__ == "__main__":
    main()
