from selenium import webdriver

class CityCodeCrawler():
    def __init__(self):
        self.url = 'https://flight.qunar.com/'
        self.headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.62 Safari/537.36'}

    def getDomesticCities(self):
        driver = webdriver.PhantomJS()
        driver.get(url = self.url)
        driver.find_element_by_class_name("textbox").click()
        CityInfo = []
        elems = driver.find_elements_by_class_name("m-hct-lst")
        for elem in elems:
            if elem.get_attribute("data-panel-id") == "dfh-国内热门":
                continue
            if elem.get_attribute("data-panel-id") == "dfh-国际▪港澳台":
                continue
            print(elem.get_attribute("data-panel-id"))
            elems2 = driver.find_elements_by_tag_name("span")
            for elem2 in elems2:
                if elem2.get_attribute("data-tab-id") == elem.get_attribute("data-panel-id"):
                    print(elem2.get_attribute("data-tab"))
                    elem2.click()
                    break
            cities = elem.find_elements_by_class_name("js-hotcitylist")
            for city in cities:
                cityinfo = {"country": city.get_attribute('data.country'), "cityname": city.text, "citycode": city.get_attribute("data-code")}
                CityInfo.append({cityinfo["cityname"]:cityinfo["citycode"]})
                print("国家：%s" % city.get_attribute(
                    'data-country') + " 城市名：%s" % city.text + " 代码：%s" % city.get_attribute("data-code"))
        return CityInfo


    def getInternationalCities(self):
        driver = webdriver.PhantomJS()
        driver.get(url = self.url)
        button1 = driver.find_element_by_id("js_inter_tab")
        button1.click()
        buttons = driver.find_elements_by_class_name("textbox")
        # button.click()
        for button in buttons:
            print(button.get_attribute("data-track"))
            if button.get_attribute("data-track") == "key=101030004&val=到达城市":
            # if button.get_attribute("name") == "ptoCity":
                button.click()
                break
        CityInfo = []
        elems = driver.find_elements_by_class_name("m-hct-lst")
        for elem in elems:
            if elem.get_attribute("data-panel-id") == "dfh-国际▪港澳台" or elem.get_attribute("data-panel-id") == "dfh-国内热门":
                continue
            print(elem.get_attribute("data-panel-id"))
            elems2 = driver.find_elements_by_tag_name("span")
            for elem2 in elems2:
                if elem2.get_attribute("data-tab-id") == elem.get_attribute("data-panel-id"):
                    print(elem2.get_attribute("data-tab"))
                    elem2.click()
                    break
            cities = elem.find_elements_by_class_name("js-hotcitylist")
            for city in cities:
                cityinfo = {"country": city.get_attribute('data.country'), "cityname": city.text, "citycode": city.get_attribute("data-code")}
                if cityinfo["country"] == cityinfo["cityname"]:
                    continue
                CityInfo.append(cityinfo)
                print("国家：%s" % city.get_attribute(
                    'data-country') + " 城市名：%s" % city.text + " 代码：%s" % city.get_attribute("data-code"))
        return CityInfo