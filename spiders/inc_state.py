from bs4 import BeautifulSoup
from selenium import webdriver
from operator import itemgetter


browser = webdriver.PhantomJS("/usr/local/lib/phantomjs/bin/phantomjs", service_args=[
                              '--ssl-protocol=any', '--ignore-ssl-errors=true', '--load-images=no'])


def get_income_statement_wsj(country,stock,type):

    browser.get("http://192.168.2.174:8080/st.html")

    html_data = browser.find_element_by_class_name("cr_dataTable").get_attribute('innerHTML')
    table_data = [[cell.text for cell in row("td")] for row in BeautifulSoup(html_data, "lxml")("tr")]

    json = {}
    for i,v in enumerate(table_data):
        if len[v] > 1 and v[1].strip() != "":
            json[i] = v
    return json