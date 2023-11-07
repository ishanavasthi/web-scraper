# Import necessary modules
import os

# Function to run AmazonScraper.py
def run_amazon():
    os.system('python scrapers/AmazonScraper.py')

# Function to run FlipkartScraper.py
def run_flipkart():
    os.system('python scrapers/FlipkartScraper.py')

# Function to run Snapdeal.py
def run_snapdeal():
    os.system('python scrapers/SnapdealScraper.py')

# Function to handle user input
def main():
    print("--------------------------------------------------------------------------------")
    print("Welcome to the Web Scraper made by Ishan Avasthi. Visit https://ishanavasthi.in")
    print("--------------------------------------------------------------------------------")

    while True:
        print("\nEnter 1 to run Amazon Scraping")
        print("Enter 2 to run Flipkart Scraping")
        print("Enter 3 to run Snapdeal Scraping")
        print("Enter 4 to exit")
        
        user_input = input("\nPlease enter your choice » ")

        if user_input == '1':
            run_amazon()
        elif user_input == '2':
            run_flipkart()
        elif user_input == '3':
            run_snapdeal()
        elif user_input == '4':
            print("\nThank You! for trying my Web Scraper. You can always run it back again by typing 'python Main.py' on the terminal.")
            print("\n")
            break
        else:
            print("Invalid input. Please try again.")

if __name__ == '__main__':
    main()
