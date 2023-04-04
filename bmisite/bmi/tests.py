from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BMIFormTest(LiveServerTestCase):

  def testform(self):
    selenium = webdriver.Safari()
    selenium.get('http://127.0.0.1:8000/')
    
    # Find user input elements by ID
    user_pounds = selenium.find_element(By.ID, 'id_pounds')
    user_feet = selenium.find_element(By.ID, 'id_feet')
    user_inches = selenium.find_element(By.ID, 'id_inches')
    submit = selenium.find_element(By.ID, 'submitBMI_button')

    # Pass values to UI
    user_pounds.send_keys('200')
    user_feet.send_keys('6')
    user_inches.send_keys('0')

    # Submit the form and wait for the result to appear
    submit.send_keys(Keys.RETURN)
    WebDriverWait(selenium, 10).until(lambda selenium: selenium.find_element(By.ID, 'bmioutput').text.strip() != '')


    #check result; page source looks at entire html document
    assert '27.78; Overweight.' in selenium.page_source