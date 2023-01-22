from HtmlTestRunner import HTMLTestRunner  # para generar el reporte
from unittest import TestLoader, TestSuite
from test_home_page import HomePageTest
from test_get_movies import GetMoviesTest
from test_get_tv_shows import GetTVShowsTest
from test_get_people import GetPeopleTest

test_home_page = TestLoader().loadTestsFromTestCase(HomePageTest)
test_get_movies = TestLoader().loadTestsFromTestCase(GetMoviesTest)
test_get_tv_shows = TestLoader().loadTestsFromTestCase(GetTVShowsTest)
test_get_people = TestLoader().loadTestsFromTestCase(GetPeopleTest)

# Create the test suite
smoke_test = TestSuite([test_home_page, test_get_movies,
                       test_get_tv_shows, test_get_people])


# To generate the reports
kwargs = {
    "output": "reports/smoke-report",
    "report_name": "smoke-report",
    "report_name": "Smoke Report",
    "combine_reports": True
}

runner = HTMLTestRunner(**kwargs)

# Run the test suite
runner.run(smoke_test)
