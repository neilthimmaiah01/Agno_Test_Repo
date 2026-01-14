import requests

url = "https://github.com/neilthimmaiah01/Agno_Test_Repo/edit/master/Agno_Test/test_code.py"

try:
    response = requests.get(url)
    
    response.raise_for_status() 
    html_content = response.text
    print(html_content)

except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")
