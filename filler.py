import datetime
import json
import random
import time

from dateutil.relativedelta import relativedelta
from mockaroo import Client
import requests
from selenium.webdriver.common.by import By
from selenium import webdriver

# Get a free Mockaroo API key by signing up at https://mockaroo.com
with open('config.json', 'r') as config:
    mockaroo_key = json.load(config)['MOCKAROO_KEY']

with open('field_spec.json', 'r') as f:
    field_spec = json.load(f)

form_url = 'https://faith-freedom.com/savegirlssports'
data_request_url = 'https://api.mockaroo.com/api/generate.json'

mock_client = Client(mockaroo_key)

mock_data = mock_client.generate(count=5000, fields=field_spec)

for record in mock_data:
    student_first_name_value = mock_data['student_first_name']
    student_last_name_value = mock_data['student_last_name']
    date_of_birth = mock_data['birth_date'].split('-')
    birth_month_value = date_of_birth[1]
    birth_day_value = date_of_birth[2]
    birth_year_value = date_of_birth[0]
    today = datetime.date.today()
    dob = datetime.datetime.strptime(mock_data['birth_date'], '%Y-%m-%d')
    age = relativedelta(today, dob).years
    if age == 5:
        grade_choices = ['Kindergarten']
    elif age == 6:
        grade_choices = ['Kindergarten', '1st']
    elif age == 7:
        grade_choices = ['1st', '2nd']
    elif age == 8:
        grade_choices = ['2nd', '3rd']
    elif age == 9:
        grade_choices = ['3rd', '4th']
    elif age == 10:
        grade_choices = ['4th', '5th']
    elif age == 11:
        grade_choices = ['5th', '6th']
    elif age == 12:
        grade_choices = ['6th', '7th']
    elif age == 13:
        grade_choices = ['7th', '8th']
    elif age == 14:
        grade_choices = ['8th', '9th']
    elif age == 15:
        grade_choices = ['9th', '10th']
    elif age == 16:
        grade_choices = ['10th', '11th']
    elif age == 17:
        grade_choices = ['11th', '12th']
    elif age == 18:
        grade_choices = ['12th']
    else:
        grade_choices = ['Kindergarten', '1st', '2nd', '3rd', '4th', '5th', '6th', '7th', '8th', '9th', '10th', '11th', '12th']
    grade_level_value = random.choice(grade_choices)
    student_phone = mock_data['student_phone_number'].split('-')
    student_area_code_value = student_phone[0]
    student_phone_exchange_value = student_phone[1]
    student_phone_line_value = student_phone[2]
    student_email_value = mock_data['student_email']
    # school_district_value =
    # school_name_value =
    # school_type_value =
    what_sport_value = mock_data['what_sport']
    are_you_outing_a_teammate_value = mock_data['are_you_outing_a_teammate']
    or_are_you_outing_an_opponent_value = mock_data['or_are_you_outing_an_opponent']
    are_you_a_sore_loser_value = mock_data['are_you_a_sore_loser']

    # # Would you like to quote Shakespeare at them? Unquote the two lines below
    play = random.choice(['AWW', 'Ant', 'AYL', 'Err', 'Cor', 'Cym', 'Ham', '1H4', '2H4', 'H5', '1H6', '2H6', '3H6', 'H8', 'JC', 'Jn', 'Lr', 'LLL', 'Mac', 'MM', 'MV', 'Wiv', 'MND', 'Ado', 'Oth', 'Per', 'R2', 'R3', 'Rom', 'Shr', 'Tmp', 'Tim', 'Tit', 'Tro', 'TN', 'TGV', 'TNK', 'WT'])
    text_url = f'https://www.folgerdigitaltexts.org/{play}/text'

    # # Prefer the Bee Movie Script? Unquote the next line for that instead.
    # text_url = 'https://benji-lewis.github.io/Bee-Movie-API/'

    response = requests.get(text_url)

    # If the API request fails, default to the Universal Declaration of Human Rights
    if response.status_code != 200:
        with open('udohr.txt', 'r') as f:
            explain_why_youre_such_a_whiner_baby_value = f.read()
    else:
        explain_why_youre_such_a_whiner_baby_value = response.text.replace('<br/>', '')
    parent_relation_value = mock_data['parent_relation']
    parent_first_name_value = mock_data['parent_first_name']
    parent_last_name_value = mock_data['parent_last_name']
    parent_email_value = mock_data['parent_email']
    parent_phone = mock_data['parent_phone_number'].split('-')
    parent_area_code_value = parent_phone[0]
    parent_phone_exchange_value = parent_phone[1]
    parent_phone_line_value = parent_phone[2]
    student_acknowledgement_value = mock_data['student_acknowledgement']
    parent_acknowledgement_value = mock_data['parent_acknowledgement']


browser = webdriver.Firefox()

# # Uncomment the next three lines to run headless
# options = webdriver.FirefoxOptions()
# options.add_argument("-headless")
# driver = webdriver.Firefox(options=options)

# # Uncomment the next line if you want a good view of the form doing its thing
browser.maximize_window()

browser.get(form_url)
time.sleep(5)

student_first_name = browser.find_element(By.XPATH, '/fieldset[@id="name-ee367545-38c6-4d3f-adef-27b3a5222961"]/div/label/input[@name="fname"]') # max-length: 30
student_last_name = browser.find_element(By.XPATH, '/fieldset[@id="name-ee367545-38c6-4d3f-adef-27b3a5222961"]/div/label/input[@name="lname"]') # max-length: 30
birth_month = browser.find_element(By.CSS_SELECTOR, 'input[data-title="Month"]') # max-length: 2
birth_day = browser.find_element(By.CSS_SELECTOR, 'input[data-title="Day"]') # max-length: 2
birth_year = browser.find_element(By.CSS_SELECTOR, 'input[data-title="Year"]') # max-length: 4
grade_level = browser.find_element(By.ID, 'select-d028169d-5994-4f8f-a99b-a4136bbf5b99-field')
student_area_code = browser.find_element(By.XPATH, '/fieldset[@id="phone-64f8a1c8-a0c7-42ad-a853-9d0ee175907c"]/div/label/input[@data-title="Areacode"]') # max-length: 3
student_phone_exchange = browser.find_element(By.XPATH, '/fieldset[@id="phone-64f8a1c8-a0c7-42ad-a853-9d0ee175907c"]/div/label/input[@data-title="Prefix"]') # max-length: 3
student_phone_line = browser.find_element(By.XPATH, '/fieldset[@id="phone-64f8a1c8-a0c7-42ad-a853-9d0ee175907c"]/div/label/input[@data-title="Line"]') # max-length: 4
student_email = browser.find_element(By.ID, 'email-f5dd562d-fdef-40bc-970a-b7e725e331d2-field')
school_district = browser.find_element(By.ID, 'text-4e1582df-c6ee-484f-b95c-b1b0bbaebd9b-field')
school_name = browser.find_element(By.ID, 'text-ab1bef83-3d2c-4997-bbb5-5fad296aaccd-field')
school_type = browser.find_element(By.ID, 'select-4b04c9f9-23a0-41af-8632-6bfe3805057f-field')
what_sport = browser.find_element(By.ID, 'lect-5233d989-d6a9-480f-beee-51574f401f84-field')
are_you_outing_a_teammate = browser.find_element(By.ID, 'select-bcd3d894-968d-479a-a9b2-6ddf7a76190c-field')
or_are_you_outing_an_opponent = browser.find_element(By.ID, 'select-7aa80927-b034-4fa8-bb62-23d23bc85bf4-field')
are_you_a_sore_loser = browser.find_element(By.ID, 'select-d0916576-8c5a-45fb-8bd8-3516463fc4fb-field')
explain_why_youre_such_a_whiner_baby = browser.find_element(By.ID, 'textarea-61bfe773-3ba8-4016-a165-4be0d876c57f-field')
parent_relation = browser.find_element(By.ID, 'select-2e6db164-bb16-459b-9d8c-5f887bd82c61-field')
parent_first_name = browser.find_element(By.XPATH, '/fieldset[@id="name-yui_3_17_2_1_1693613454290_9239"]/div/label/input[@name="fname"]') # max-length: 30
parent_last_name = browser.find_element(By.XPATH, '/fieldset[@id="name-yui_3_17_2_1_1693613454290_9239"]/div/label/input[@name="lname"]') # max-length: 30
parent_email = browser.find_element(By.ID, 'email-dd630fb5-766f-4b7e-968c-644cb378a927-field')
parent_area_code = browser.find_element(By.XPATH, '/fieldset[@id="phone-b7c1fc30-9c7e-475f-bb65-9badd1ffc72a"]/div/label/input[@data-title="Areacode"]') # max-length: 3
parent_phone_exchange = browser.find_element(By.XPATH, '/fieldset[@id="phone-b7c1fc30-9c7e-475f-bb65-9badd1ffc72a"]/div/label/input[@data-title="Prefix"]') # max-length: 3
parent_phone_line = browser.find_element(By.XPATH, '/fieldset[@id="phone-b7c1fc30-9c7e-475f-bb65-9badd1ffc72a"]/div/label/input[@data-title="Line"]') # max-length: 4
student_acknowledgement = browser.find_element(By.ID, 'ee937708-36a0-4d26-b894-326710667749-field')
parent_acknowledgement = browser.find_element(By.ID, 'text-726b8518-a80e-4dbc-b0c6-8f3ae030179c-field')
submit = browser.find_element(By.CSS_SELECTOR, 'input[value="Submit"]')
