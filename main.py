import selenium

from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

import time 

from classes.classes import MainPage, GridPage, JobTitlePage
from constants import *

#Авторизуємось, page надалі - наш основний об'єкт, з яким ми будемо працювати
page = MainPage()
page = page.authorize()

#Відразу переходимо на сторінку з таблицею Job Titles
page.get('https://opensource-demo.orangehrmlive.com/index.php/admin/viewJobTitleList')

#GridPage - об'єкт сторінки з таблицею Job Titles. Тут нам знадобляться лише "функції"
gr_page = GridPage(page)
gr_page.press_add()

#JobTitlePage - об'єкт сторінки на якій ми будемо взазувати інформацію про Job Title. 
# Тут нам необхідно буде вводити інформацію / підтверджувати зміни
jt_page = JobTitlePage(page)
jt_page.set_job_title(TITLE)
jt_page.set_job_description(DESCRIPTION1)
jt_page.set_note(NOTE)
jt_page.enter_button_click()

#Перевіряємо правильність запису 
gr_page.check(jt_page.get_job_title())


# Модифікуємо наш запис 
gr_page.edit(gr_page.get_link(TITLE))
jt_page.press_edit()
jt_page.modify_job_description(DESCRIPTION2)
jt_page.enter_button_click()

#Перевіряємо правильність модифікації 
gr_page.check(jt_page.get_job_title())

#Вибираємо в таблиці наш запис та натискаємо DELETE, тобто видаляємо 
gr_page.click_box(jt_page.get_job_title())
gr_page.delete()

#Перевіряємо правильність видалення
gr_page.check(TITLE)

time.sleep(5)

page.quit()










