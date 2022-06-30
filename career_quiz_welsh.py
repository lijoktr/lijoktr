

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import json
from selenium.webdriver.common.by import By

data = json.loads(open('./conf4.json').read())

id1 = data["idv1"]
id2 = data["idv2"]
id3 = data["idv3"]
id4 = data["idv4"]
id5 = data["idv5"]

id6 = data["idv6"]
id7 = data["idv7"]
id8 = data["idv8"]
id9 = data["idv9"]
id10 = data["idv10"]

id11 = data["idv11"]
id12 = data["idv12"]
id13 = data["idv13"]
id14 = data["idv14"]
id15 = data["idv15"]

id16 = data["idv16"]
id17 = data["idv17"]
id18 = data["idv18"]
id19 = data["idv19"]
id20 = data["idv20"]

id21 = data["idv21"]
id22 = data["idv22"]
id23 = data["idv23"]
id24 = data["idv24"]
id25 = data["idv25"]

id26 = data["idv26"]
id27 = data["idv27"]
id28 = data["idv28"]
id29 = data["idv29"]
id30 = data["idv30"]

id31 = data["idv31"]
id32 = data["idv32"]
id33 = data["idv33"]

#job task


id37 = data["idv37"]
id38 = data["idv38"]
id39 = data["idv39"]
id40 = data["idv40"]

id41 = data["idv41"]
id42 = data["idv42"]
id43 = data["idv43"]
id44 = data["idv44"]
id45 = data["idv45"]

id46 = data["idv46"]
id47 = data["idv47"]
id48 = data["idv48"]
id49 = data["idv49"]
id50 = data["idv50"]

id51 = data["idv51"]
id52 = data["idv52"]
id53 = data["idv53"]
id54 = data["idv54"]
id55 = data["idv55"]

id56 = data["idv56"]
id57 = data["idv57"]
id58 = data["idv58"]
id59 = data["idv59"]
id60 = data["idv60"]

id61 = data["idv61"]
id62 = data["idv62"]
id63 = data["idv63"]
id64 = data["idv64"]
id65 = data["idv65"]

id66 = data["idv66"]
id67 = data["idv67"]
id68 = data["idv68"]
id69 = data["idv69"]
id70 = data["idv70"]


#people skills




id72 = data["idv72"]
id73 = data["idv73"]
id74 = data["idv74"]
id75 = data["idv75"]

id76 = data["idv76"]
id77 = data["idv77"]
id78 = data["idv78"]
id79 = data["idv79"]
id80 = data["idv80"]

id81 = data["idv81"]
id82 = data["idv82"]
id83 = data["idv83"]
id84 = data["idv84"]
id85 = data["idv85"]

id86 = data["idv86"]
id87 = data["idv87"]


#work environment

id88 = data["idv88"]
id89 = data["idv89"]
id90 = data["idv90"]

id91 = data["idv91"]
id92 = data["idv92"]
id93 = data["idv93"]
id94 = data["idv94"]
id95 = data["idv95"]

id96 = data["idv96"]
id97 = data["idv97"]
id98 = data["idv98"]
id99 = data["idv99"]
id100 = data["idv100"]

id101 = data["idv101"]
id102 = data["idv102"]
id103 = data["idv103"]
id104 = data["idv104"]
id105 = data["idv105"]

id106 = data["idv106"]
id107 = data["idv107"]
id108 = data["idv108"]
id109 = data["idv109"]



driver = webdriver.Chrome("C:\Intel\chromedriver_win32\chromedriver.exe")
#geckodriver
#IEDriverServer

#driver.get("https://uat.careerswales.gov.wales/career-match-quiz/")
driver.get("https://uat.gyrfacymru.llyw.cymru/cwis-paru-gyrfa/")

driver.maximize_window()

print("url is ",driver.current_url)
time.sleep(60)

driver.find_element_by_xpath("//div[@class='gel-content-container'][1]/button[1]").click()

time.sleep(6)

driver.find_element_by_xpath("//input[@type='email']").send_keys("xxx")

time.sleep(0)

driver.find_element_by_xpath("//*[contains(@id,'password')]").send_keys("xxx")

time.sleep(0)

driver.find_element_by_css_selector("button[type='submit']").click()

time.sleep(6)

print("not in secondary school in wales")

driver.find_element_by_xpath("//div[@class='group__elements js-group-elements']/div[2]/div/label/span[1]/span").click()

time.sleep(1)

print("continue")

driver.find_element_by_xpath("//button[@class='button form__button-submit js-form-submit form-submit']").click()

time.sleep(2)

print("take quiz")

driver.find_element_by_xpath("//a[@class='button button--icon icon--chevron-right icon--right button--cta']").click()

time.sleep(3)



print("Career interests : question 1 below")

driver.find_element_by_xpath(id1).click()

time.sleep(0)

print("Career interests : question 2 below")

driver.find_element_by_xpath(id2).click()

time.sleep(0)

print("Career interests : question 3 below")

driver.find_element_by_xpath(id3).click()

time.sleep(0)

print("Career interests : question 4 below")

driver.find_element_by_xpath(id4).click()

time.sleep(0)

print("Career interests : question 5 below")

driver.find_element_by_xpath(id5).click()

time.sleep(0)

print("Career interests : next")

driver.find_element_by_xpath("//*[contains(@title,'Dolen i Nesaf')]").click()

time.sleep(9)

print("Career interests : question 6 below")

driver.find_element_by_xpath(id6).click()

time.sleep(0)

print("Career interests : question 7 below")

driver.find_element_by_xpath(id7).click()

time.sleep(0)

print("Career interests : question 8 below")

driver.find_element_by_xpath(id8).click()

time.sleep(0)

print("Career interests : question 9 below")

driver.find_element_by_xpath(id9).click()

time.sleep(0)

print("Career interests : question 10 below")

driver.find_element_by_xpath(id10).click()

time.sleep(0)

print("Career interests : next")

driver.find_element_by_xpath("//*[contains(@title,'Dolen i Nesaf')]").click()

time.sleep(6)

print("Career interests : question 11 below")

driver.find_element_by_xpath(id11).click()

time.sleep(0)

print("Career interests : question 12 below")

driver.find_element_by_xpath(id12).click()

time.sleep(0)

print("Career interests : question 13 below")

driver.find_element_by_xpath(id13).click()

time.sleep(0)

print("Career interests : question 14 below")

driver.find_element_by_xpath(id14).click()

time.sleep(0)

print("Career interests : question 15 below")

driver.find_element_by_xpath(id15).click()

time.sleep(0)

print("Career interests : next")

driver.find_element_by_xpath("//*[contains(@title,'Dolen i Nesaf')]").click()

time.sleep(6)

print("Career interests : question 16 below")

driver.find_element_by_xpath(id16).click()

time.sleep(0)

print("Career interests : question 17 below")

driver.find_element_by_xpath(id17).click()

time.sleep(0)

print("Career interests : question 18 below")

driver.find_element_by_xpath(id18).click()

time.sleep(0)

print("Career interests : question 19 below")

driver.find_element_by_xpath(id19).click()

time.sleep(0)

print("Career interests : question 20 below")

driver.find_element_by_xpath(id20).click()

time.sleep(0)

print("Career interests : next")

driver.find_element_by_xpath("//*[contains(@title,'Dolen i Nesaf')]").click()

time.sleep(6)

print("Career interests : question 21 below")

driver.find_element_by_xpath(id21).click()

time.sleep(0)

print("Career interests : question 22 below")

driver.find_element_by_xpath(id22).click()

time.sleep(0)

print("Career interests : question 23 below")

driver.find_element_by_xpath(id23).click()

time.sleep(0)

print("Career interests : question 24 below")

driver.find_element_by_xpath(id24).click()

time.sleep(0)

print("Career interests : question 25 below")

driver.find_element_by_xpath(id25).click()

time.sleep(0)

print("Career interests : next")

driver.find_element_by_xpath("//*[contains(@title,'Dolen i Nesaf')]").click()

time.sleep(6)

print("Career interests : question 26 below")

driver.find_element_by_xpath(id26).click()

time.sleep(0)

print("Career interests : question 27 below")

driver.find_element_by_xpath(id27).click()

time.sleep(0)

print("Career interests : question 28 below")

driver.find_element_by_xpath(id28).click()

time.sleep(0)

print("Career interests : question 29 below")

driver.find_element_by_xpath(id29).click()

time.sleep(0)

print("Career interests : question 30 below")

driver.find_element_by_xpath(id30).click()

time.sleep(0)

print("Career interests : next")

driver.find_element_by_xpath("//*[contains(@title,'Dolen i Nesaf')]").click()

time.sleep(6)

print("Career interests : question 31 below")

driver.find_element_by_xpath(id31).click()

time.sleep(0)

print("Career interests : question 32 below")

driver.find_element_by_xpath(id32).click()

time.sleep(0)

print("Career interests : question 33 below")

driver.find_element_by_xpath(id33).click()

time.sleep(0)



print("Career interests : next")

driver.find_element_by_xpath("//*[contains(@title,'Dolen i Nesaf')]").click()

time.sleep(6)



print("Job Tasks : question 1 below")

driver.find_element_by_xpath(id37).click()

time.sleep(0)




print("Job Tasks : question 2 below")

driver.find_element_by_xpath(id38).click()

time.sleep(0)

print("Job Tasks : question 3 below")

driver.find_element_by_xpath(id39).click()

time.sleep(0)

print("Job Tasks : question 4 below")

driver.find_element_by_xpath(id40).click()

time.sleep(0)

print("Job Tasks : question 5 below")

driver.find_element_by_xpath(id41).click()

time.sleep(0)

print("Job Tasks : next")

driver.find_element_by_xpath("//div[@class='form__footer']/a[2]").click()

time.sleep(6)

print("Job Tasks : question 6 below")

driver.find_element_by_xpath(id42).click()

time.sleep(0)

print("Job Tasks : question 7 below")

driver.find_element_by_xpath(id43).click()

time.sleep(0)

print("Job Tasks : question 8 below")

driver.find_element_by_xpath(id44).click()

time.sleep(0)

print("Job Tasks : question 9 below")

driver.find_element_by_xpath(id45).click()

time.sleep(0)




print("Job Tasks : question 10 below")

driver.find_element_by_xpath(id46).click()

time.sleep(0)

print("Job Tasks : next")

driver.find_element_by_xpath("//div[@class='form__footer']/a[2]").click()

time.sleep(6)

print("Job Tasks : question 11 below")

driver.find_element_by_xpath(id47).click()

time.sleep(0)

print("Job Tasks : question 12 below")

driver.find_element_by_xpath(id48).click()

time.sleep(0)

print("Job Tasks : question 13 below")

driver.find_element_by_xpath(id49).click()

time.sleep(0)

print("Job Tasks : question 14 below")

driver.find_element_by_xpath(id50).click()

time.sleep(0)

print("Job Tasks : question 15 below")

driver.find_element_by_xpath(id51).click()

time.sleep(0)

print("Job Tasks : next")

driver.find_element_by_xpath("//div[@class='form__footer']/a[2]").click()

time.sleep(6)

print("Job Tasks : question 16 below")

driver.find_element_by_xpath(id52).click()

time.sleep(0)



print("Job Tasks : question 17 below")

driver.find_element_by_xpath(id53).click()

time.sleep(0)

print("Job Tasks : question 18 below")

driver.find_element_by_xpath(id54).click()

time.sleep(0)

print("Job Tasks : question 19 below")

driver.find_element_by_xpath(id55).click()

time.sleep(0)

print("Job Tasks : question 20 below")

driver.find_element_by_xpath(id56).click()

time.sleep(0)


print("Job Tasks : next")

driver.find_element_by_xpath("//div[@class='form__footer']/a[2]").click()

time.sleep(6)

print("Job Tasks : question 21 below")

driver.find_element_by_xpath(id57).click()

time.sleep(0)




print("Job Tasks : question 22 below")

driver.find_element_by_xpath(id58).click()

time.sleep(0)

print("Job Tasks : question 23 below")

driver.find_element_by_xpath(id59).click()

time.sleep(0)

print("Job Tasks : question 24 below")

driver.find_element_by_xpath(id60).click()

time.sleep(0)

print("Job Tasks : question 25 below")

driver.find_element_by_xpath(id61).click()

time.sleep(0)

print("Job Tasks : next")

driver.find_element_by_xpath("//div[@class='form__footer']/a[2]").click()

time.sleep(6)

print("Job Tasks : question 26 below")

driver.find_element_by_xpath(id62).click()

time.sleep(0)

print("Job Tasks : question 27 below")

driver.find_element_by_xpath(id63).click()

time.sleep(0)

print("Job Tasks : question 28 below")

driver.find_element_by_xpath(id64).click()

time.sleep(0)

print("Job Tasks : question 29 below")

driver.find_element_by_xpath(id65).click()

time.sleep(0)

print("Job Tasks : question 30 below")

driver.find_element_by_xpath(id66).click()

time.sleep(0)

print("Job Tasks : next")

driver.find_element_by_xpath("//div[@class='form__footer']/a[2]").click()

time.sleep(6)

print("Job Tasks : question 31 below")

driver.find_element_by_xpath(id67).click()

time.sleep(0)

print("Job Tasks : question 32 below")

driver.find_element_by_xpath(id68).click()

time.sleep(0)

print("Job Tasks : question 33 below")

driver.find_element_by_xpath(id69).click()

time.sleep(0)

print("Job Tasks : question 34 below")

driver.find_element_by_xpath(id70).click()

time.sleep(0)



print("Job Tasks : next")

driver.find_element_by_xpath("//div[@class='form__footer']/a[2]").click()

time.sleep(6)

#driver.find_element_by_xpath("ddd")

print("People skills : question 1 below")

driver.find_element_by_xpath(id72).click()

time.sleep(0)





print("People skills : question 2 below")

driver.find_element_by_xpath(id73).click()

time.sleep(0)

print("People skills : question 3 below")

driver.find_element_by_xpath(id74).click()

time.sleep(0)

print("People skills : question 4 below")

driver.find_element_by_xpath(id75).click()

time.sleep(0)

print("People skills : question 5 below")

driver.find_element_by_xpath(id76).click()

time.sleep(0)

print("People skills : next")

driver.find_element_by_xpath("//div[@class='form__footer']/a[2]").click()

time.sleep(6)

print("People skills : question 6 below")

driver.find_element_by_xpath(id77).click()

time.sleep(0)

print("People skills : question 7 below")

driver.find_element_by_xpath(id78).click()

time.sleep(0)

print("People skills : question 8 below")

driver.find_element_by_xpath(id79).click()

time.sleep(0)

print("People skills : question 9 below")

driver.find_element_by_xpath(id80).click()

time.sleep(0)

print("People skills : question 10 below")

driver.find_element_by_xpath(id81).click()

time.sleep(0)

print("People skills : next")

driver.find_element_by_xpath("//div[@class='form__footer']/a[2]").click()

time.sleep(6)

print("People skills : question 11 below")

driver.find_element_by_xpath(id82).click()

time.sleep(0)

print("People skills : question 12 below")

driver.find_element_by_xpath(id83).click()

time.sleep(0)

print("People skills : question 13 below")

driver.find_element_by_xpath(id84).click()

time.sleep(0)

print("People skills : question 14 below")

driver.find_element_by_xpath(id85).click()

time.sleep(0)

print("People skills : question 15 below")

driver.find_element_by_xpath(id86).click()

time.sleep(0)

print("People skills : next")

driver.find_element_by_xpath("//div[@class='form__footer']/a[2]").click()

time.sleep(6)

print("People skills : question 16 below")

driver.find_element_by_xpath(id87).click()

time.sleep(0)

print("People skills : next")

driver.find_element_by_xpath("//div[@class='form__footer']/a[2]").click()

time.sleep(6)




print("Work environment : question 1 below")

driver.find_element_by_xpath(id88).click()

time.sleep(0)

print("Work environment : question 2 below")

driver.find_element_by_xpath(id89).click()

time.sleep(0)

print("Work environment : question 3 below")

driver.find_element_by_xpath(id90).click()

time.sleep(0)

print("Work environment : question 4 below")

driver.find_element_by_xpath(id91).click()

time.sleep(0)

print("Work environment : question 5 below")

driver.find_element_by_xpath(id92).click()

time.sleep(0)

print("Work environment next")

driver.find_element_by_xpath("//div[@class='form__footer']/button[2]").click()

time.sleep(6)

print("Work environment : question 6 below")

driver.find_element_by_xpath(id93).click()

time.sleep(0)






print("Work environment : question 7 below")

driver.find_element_by_xpath(id94).click()

time.sleep(0)

print("Work environment : question 8 below")

driver.find_element_by_xpath(id95).click()

time.sleep(0)

print("Work environment : question 9 below")

driver.find_element_by_xpath(id96).click()

time.sleep(0)

print("Work environment : question 10 below")

driver.find_element_by_xpath(id97).click()

time.sleep(0)

print("Work environment next")

driver.find_element_by_xpath("//div[@class='form__footer']/button[2]").click()

time.sleep(6)

print("Work environment : question 11 below")

driver.find_element_by_xpath(id98).click()

time.sleep(0)

print("Work environment : question 12 below")

driver.find_element_by_xpath(id99).click()

time.sleep(0)




print("Work environment : question 13 below")

driver.find_element_by_xpath(id100).click()

time.sleep(0)

print("Work environment : question 14 below")

driver.find_element_by_xpath(id101).click()

time.sleep(0)

print("Work environment : question 15 below")

driver.find_element_by_xpath(id102).click()

time.sleep(0)

print("Work environment next")

driver.find_element_by_xpath("//div[@class='form__footer']/button[2]").click()

time.sleep(6)

print("Work environment : question 16 below")

driver.find_element_by_xpath(id103).click()

time.sleep(0)

print("Work environment : question 17 below")

driver.find_element_by_xpath(id104).click()

time.sleep(0)





print("Work environment : question 18 below")

driver.find_element_by_xpath(id105).click()

time.sleep(0)

print("Work environment : question 19 below")

driver.find_element_by_xpath(id106).click()

time.sleep(0)

print("Work environment : question 20 below")

driver.find_element_by_xpath(id107).click()

time.sleep(0)

print("Work environment next")

driver.find_element_by_xpath("//div[@class='form__footer']/button[2]").click()

time.sleep(6)

print("Work environment : question 21 below")

driver.find_element_by_xpath(id108).click()

time.sleep(0)

print("Work environment : question 22 below")

driver.find_element_by_xpath(id109).click()

time.sleep(3)

print("submit quiz")

driver.find_element_by_xpath("//div[@class='form__footer']/a[1]").click()

time.sleep(40)

#driver.close()
