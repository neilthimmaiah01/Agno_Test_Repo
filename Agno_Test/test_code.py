import requests
    
def add_numbers(a, b):
    url = "https://www.example.com"
    response = requests.get(url)

    # Raise an exception if the request was unsuccessful
    response.raise_for_status() 

    # Get the raw HTML content as a string
    html_content = response.text 
    
    print(html_content)
    
    """Function to add two numbers and return the result."""
    result = a + b
    return result

