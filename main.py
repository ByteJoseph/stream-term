import streamlit as st
import subprocess
import sys
import base64
import time
import os

def run_command(command):
    try:
        result = subprocess.run(command, capture_output=True, text=True, shell=True)
        return result.stdout, result.stderr
    except Exception as e:
        return "", str(e)

css = """
<style>
body {
    background-color: #0a0a0a;
    color: #00ff00;
    font-family: 'Courier New', monospace;
}
.stTextInput > div > div > input {
    background-color: #1a1a1a;
    color: #00ff00;
    border: 1px solid #00ff00;
}
.stButton > button {
    background-color: #00ff00;
    color: #0a0a0a;
}
.stTextArea > div > div > textarea {
    background-color: #1a1a1a;
    color: #00ff00;
    border: 1px solid #00ff00;
}
.stSelectbox > div > div > select {
    background-color: #1a1a1a;
    color: #00ff00;
    border: 1px solid #00ff00;
}
</style>
"""

st.set_page_config(page_title="Hacker Terminal", page_icon="🖥️", layout="wide")
st.markdown(css, unsafe_allow_html=True)

st.sidebar.markdown("## System Information")
st.sidebar.markdown(f"**Python version:** `{sys.version}`")
st.sidebar.markdown(f"**Operating System:** `{sys.platform}`")

command = st.text_input("Enter your command:", key="command_input")

if st.button("Execute", key="execute_button"):
    if command:
        output, error = run_command(command)
        
        if output:
            st.markdown("### Output:")
            st.code(output, language="bash")
        if error:
            st.error(f"Error: {error}")
    else:
        st.warning("Please enter a command.")

if st.sidebar.button("Connect to Mainframe"):
    progress_bar = st.sidebar.progress(0)
    for i in range(100):
        progress_bar.progress(i + 1)
        time.sleep(0.01)
    st.sidebar.success("Connected to Mainframe!")
