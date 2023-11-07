import requests
from bs4 import BeautifulSoup

def scrp_fkart(url):
    try:
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36' , "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,/;q=0.8"}
        response = requests.get(url, headers=headers)
        
        soup = BeautifulSoup(response.content, 'html.parser')
        
        product_name = soup.find('span', {'class': 'B_NuCI'}).text.strip()
        product_price = soup.find('div', {'class': '_30jeq3 _16Jk6d'}).text.strip()
        
        print("\n⁙•⁘⁙•⁘⁙•⁘⁙•⁘⁙•⁘⁙•⁘⁙•⁘⁙•⁘⁙•⁘⁙•⁘⁙•⁘⁙•⁘⁙•⁘⁙•⁘⁙•⁘⁙•⁘⁙•⁘⁙•⁘⁙•⁘⁙•⁘⁙•⁘⁙•⁘")
        print('• Product Name :', product_name)
        print('\n⁘ Product Price :', product_price)
        print("⁙•⁘⁙•⁘⁙•⁘⁙•⁘⁙•⁘⁙•⁘⁙•⁘⁙•⁘⁙•⁘⁙•⁘⁙•⁘⁙•⁘⁙•⁘⁙•⁘⁙•⁘⁙•⁘⁙•⁘⁙•⁘⁙•⁘⁙•⁘⁙•⁘⁙•⁘")
    except Exception as e:
        print('Error:', str(e))

if __name__ == "__main__":
    url = input("Enter Flipkart URL of the product (press Ctrl+C to stop) » ")
    scrp_fkart(url)