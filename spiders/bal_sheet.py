from bs4 import BeautifulSoup
from . import browser


def get_balance_sheet_wsj(country,stock,type):

    browser.get("http://192.168.2.174:8080/bal_sheet.html")

    html_data = browser.find_element_by_class_name("cr_dataTable").get_attribute('innerHTML')
    table_data = [[cell.text for cell in row("td")] for row in BeautifulSoup(html_data, "lxml")("tr")]
    json_data = {}
    for i,v in enumerate(table_data):
        if len(v) > 1 and v[1].strip() != "":
            json_data[i] = v
    return json_data