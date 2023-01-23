# The Movie DB scraper
Project to practice web scraping by getting movies, tv shows, and people information from The Movie DB site using Python, Selenium and the Page Object Model design pattern.

## Installation
    
  1. Clone or download the repository:

  `git clone https://github.com/betofleitass/themoviedb-scraper`

  2. Go to the project directory

  `cd themoviedb-scraper`

  3. Create a virtual environment and activate it:

      PowerShell:
      ```
       python -m venv venv
       venv\Scripts\Activate.ps1
      ```

      Linux:
      ```
      python3 -m venv venv
      source venv/bin/activate
      ```

  4. Install dependencies:

  `pip install -r requirements.txt`
  
  
## Running the tests

1. Go to the project directory: `cd themoviedb-scraper`

2. Run the following command (e.g.):  

  ` py .\test_get_movies.py `

  This will run the test case that scrapes a list of movies.

  ` py .\smoke_test.py `

  This will run the all tests that are in the test suite.
  
3. Go to the reports folder to view the test results

## Project Structure

    themoviedb-scraper/
        ├── pages/
        │   ├── __init__.py
        │   ├── home_page.py
        │   ├── movies_list_page.py
        │   ├── people_list_page.py
        │   └── tv_shows_list_page.py
        ├── reports
        ├── requirements.txt
        ├── smoke_test.py
        ├── test_get_movies.py
        ├── test_get_people.py
        ├── test_get_tv_shows.py
        └── test_home_page.py


-   `pages`: This directory contains the Page Object Model classes that represent the different pages of the The Movie DB website.
-   `reports`: This directory contains the results of the tests.
-   `smoke_test`: This file contains a test suite with all the tests.

