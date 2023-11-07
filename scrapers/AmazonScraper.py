# Importing the necessary modules
import requests  # Module to send HTTP requests
from bs4 import BeautifulSoup  # Module for pulling data out of HTML and XML files
import sys  # Module for system-specific parameters and functions

# Function to scrape product information from Amazon website
def scrp_amzn(url):
    try:
        # Defining a custom user agent for the request headers
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36', "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,/;q=0.8"}
        status_code=503  # Setting an initial status code value to 503 for the while loop
        print("\nPlease wait...")

        # Loop to handle server errors until a 200 status code is received
        while(status_code!=200):
            # Sending a GET request to the provided URL with the custom headers
            response = requests.get(url, headers=headers)

            # Checking if the response status code is 200 (OK)
            if response.status_code==200:
                # Parsing the HTML content of the page using BeautifulSoup
                soup = BeautifulSoup(response.content, 'html.parser')

                # Finding the product name from the HTML using the specific class name
                product_name = soup.find('span', class_='a-size-large product-title-word-break')

                # Finding the product price from the HTML using the specific class name
                price_element = soup.find('span', class_='a-price-whole')

                # Printing the product name and price if found, and breaking the loop
                if price_element:
                    print("------------------------------------------------------------------------------------")
                    print("• Product Name : " + product_name.get_text().strip())
                    print("\n⁘ Product Price : ₹" + price_element.get_text().strip())
                    print("------------------------------------------------------------------------------------")
                    print("\n")
                    break

    # Handling the KeyboardInterrupt exception
    except KeyboardInterrupt:
        print("\nSorry to see you go! You can always run it back by typing 'python Main.py' in the terminal.")
        sys.exit()

    # Handling any other exceptions that might occur during the scraping process
    except Exception as e:
        return f"Error: {str(e)}"

# Prompting the user to enter the URL of the product on Amazon
Url = input("Enter Amazon URL of the product (press Ctrl+C to stop) » ")

# Calling the function to scrape the product information from the provided URL
scrp_amzn(Url)
