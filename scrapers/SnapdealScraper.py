import requests
from bs4 import BeautifulSoup

def scrp_snpdl(url):
    try:
        response = requests.get(url)
        
        soup = BeautifulSoup(response.content, 'html.parser')
        
        product_name = soup.find('h1', {'class': 'pdp-e-i-head'}).text.strip()
        product_price = soup.find('span', {'class': 'payBlkBig'}).text.strip()
        
        print("\n⁙•⁘⁙•⁘⁙•⁘⁙•⁘⁙•⁘⁙•⁘⁙•⁘⁙•⁘⁙•⁘⁙•⁘⁙•⁘⁙•⁘⁙•⁘⁙•⁘⁙•⁘⁙•⁘⁙•⁘⁙•⁘⁙•⁘⁙•⁘⁙•⁘⁙•⁘")
        print('• Product Name :', product_name)
        print('\n⁘ Product Price : ₹', product_price)
        print("⁙•⁘⁙•⁘⁙•⁘⁙•⁘⁙•⁘⁙•⁘⁙•⁘⁙•⁘⁙•⁘⁙•⁘⁙•⁘⁙•⁘⁙•⁘⁙•⁘⁙•⁘⁙•⁘⁙•⁘⁙•⁘⁙•⁘⁙•⁘⁙•⁘⁙•⁘")
    except Exception as e:
        print('Error:', str(e))

if __name__ == "__main__":
    url = input("Enter Snapdeal URL of the product (press Ctrl+C to stop) » ")
    scrp_snpdl(url)
