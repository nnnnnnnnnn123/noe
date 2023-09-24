name: Streamlit App Deployment

on:
  push:
    branches:
      - main  # Adjust this to your main branch name

jobs:
  deploy:
    runs-on: ubuntu-latest

    steps:
    - name: Checkout repository
      uses: actions/checkout@v2

    - name: Set up Python
      uses: actions/setup-python@v2
      with:
        python-version: 3.9  # Adjust the Python version as needed

    - name: Install dependencies
      run: pip install -r requirements.txt

    - name: Run Streamlit app
      run: streamlit run noe.py  # Replace with your script name
