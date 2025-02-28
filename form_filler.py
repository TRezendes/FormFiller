#!/usr/bin/env python3

import argparse
import datetime
import random
import time
from typing import TextIO

from faker import Faker
from faker.providers import date_time, person, phone_number, profile
from faker_education import SchoolProvider
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options as FirefoxOptions

if __name__ == '__main__':

    parser = argparse.ArgumentParser(formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument(
        '-n',
        '--num-subs',
        type=int,
        default=1,
        help='The number of times to fill and submit the form.\ntype: %(type)s\ndefault: %(default)s\n'
    )
    parser.add_argument(
        '-c', '--content',
        type=str,
        default='s',
        choices=['b','s','u'],
        help="""
Select which content with which to fill the form.
b, s, & u use faker to fill plausible data in the short text fields (name, email address, phone number, etc.).
For the 500 character textarea field ('Incident Details') and the optional uploaded files
b uses the Bee Movie transcript,
s uses text from a random Shakespeare play, and
u uses the text of the Universal Declaration of Human Rights.
s & b both fall back to u if their respective API call fails.
g [NOT IMPLEMENTED YET] fills all text fields and the files with randomly generated gibberish.
type: %(type)s
default: %(default)s
        """
    )
    parser.add_argument(
        '-w',
        '--windowed',
        action='store_true',
        help="Set this flag to run selenium browser automation in a browser window. Default is to run headless."
    )
    parser.add_argument(
        '-f',
        '--include-files',
        action='store_true',
        help="[NOT IMPLEMENTED YET] Set this flag to generate and upload 3 5MB files (the form's maximum) with the form submission."
    )

    args = parser.parse_args()

    num_subs:int = args.num_subs
    content_choice: str = args.content
    include_files: bool = args.include_files
    windowed: bool = args.windowed

    form_url: str = 'https://donoharmmedicine.org/share-your-concern/'

    fake = Faker()
    fake.add_provider(date_time)
    fake.add_provider(person)
    fake.add_provider(phone_number)
    fake.add_provider(profile)
    fake.add_provider(SchoolProvider)

    def filler(
        form_url: str=form_url,
        num_subs: int=num_subs,
        content_choice: str=content_choice,
        include_files: bool=include_files,
        windowed: bool=windowed
    ) -> None:
        i: int
        for i in range(num_subs):
            school_name: str = '12345678901234567890123456789012'
            phone_num: str = '12345678901234567890'
            email_address: str = '12345678901234567890'
            while len(school_name) > 30:
                school_dict: dict = fake.school_object()
                school_name = school_dict['school']
            school_state = school_dict['state']
            while len(phone_num) > 15:
                phone_num = fake.phone_number()
            while len(email_address) > 15:
                email_address = fake.profile(fields=['mail'])['mail']


            start_date: datetime.date = datetime.date.today() - datetime.timedelta(weeks=60)
            incident_date: str = datetime.datetime.strftime(fake.date_between_dates(start_date), '%m/%d/%Y')

            input_13_20_value: str = random.choice(['DEI', 'Gender Ideology', 'Other']) # This tip is about...
            input_13_8_value: str = school_name # Doctor, school, hospital, or clinic involved (or “n/a”)
            input_13_9_value: str = school_state # Location of doctor, school, hospital, or clinic involved (or your location)
            input_13_13_value: str = incident_date # Date of incident
            input_13_12_value: str = fake.name_nonbinary()[:30] # Your Name
            input_13_21_value: str = email_address # Your Email Address (Only Used For Incident Follow-Up)
            input_13_10_value: str = phone_num # Your phone number
            input_13_16_value: str = random.choice([
                "Physician (MD; DO; DPM; DDS; DC)",
                "Nurse or Nurse Practitioner/APRN",
                "Other Practitioner/Clinician",
                "Administrator",
                "Concerned Citizen or Patient",
                "Policymaker",
                "Parent",
                "Faculty Member or Academic",
                "Researcher"
            ]) # I am a...

            text_url: str

            if content_choice == 's':
                # Quote Shakespeare at them
                play: str = random.choice(['AWW', 'Ant', 'AYL', 'Err', 'Cor', 'Cym', 'Ham', '1H4', '2H4', 'H5', '1H6', '2H6', '3H6', 'H8', 'JC', 'Jn', 'Lr', 'LLL', 'Mac', 'MM', 'MV', 'Wiv', 'MND', 'Ado', 'Oth', 'Per', 'R2', 'R3', 'Rom', 'Shr', 'Tmp', 'Tim', 'Tit', 'Tro', 'TN', 'TGV', 'TNK', 'WT'])
                text_url = f'https://www.folgerdigitaltexts.org/{play}/text'
                response = requests.get(text_url)
                if response.status_code != 200:
                    content_choice = 'u'

            elif content_choice == 'b':
                # Send them the Bee Movie
                text_url = 'https://benji-lewis.github.io/Bee-Movie-API/'
                response = requests.get(text_url)
                if response.status_code != 200:
                    content_choice = 'u'

            input_13_7_value: str

            f: TextIO
            if content_choice == 'u':
                # Send them to school with the Universal Declaration of Human Rights
                with open('udohr.txt', 'r') as f:
                    input_13_7_value = f.read()
                    input_13_7_value = input_13_7_value[:500] # Incident details (Include As Much Information As Possible)
            else:
                input_13_7_value = response.text.replace('<br/>', '')
                input_13_7_value = input_13_7_value[:500]


            options = FirefoxOptions()
            if not windowed:
                # Run headless
                options.add_argument("-headless")
            browser = webdriver.Firefox(options=options)
            if windowed:
                # Get a good view of the form doing its thing
                browser.maximize_window()
            browser.get(form_url)
            time.sleep(15)

            input_13_20 = browser.find_element(By.ID, 'input_13_20')
            input_13_20.send_keys(input_13_20_value)
            input_13_8 = browser.find_element(By.ID, 'input_13_8') # maxlength = 30
            input_13_8.send_keys(input_13_8_value)
            input_13_9 = browser.find_element(By.ID, 'input_13_9') # maxlength = 30
            input_13_9.send_keys(input_13_9_value)
            input_13_13 = browser.find_element(By.ID, 'input_13_13') # maxlength = 10
            input_13_13.send_keys(input_13_13_value)
            input_13_12 = browser.find_element(By.ID, 'input_13_12') # maxlength = 30
            input_13_12.send_keys(input_13_12_value)
            input_13_21 = browser.find_element(By.ID, 'input_13_21') # maxlength = 15
            input_13_21.send_keys(input_13_21_value)
            input_13_10 = browser.find_element(By.ID, 'input_13_10')
            input_13_10.send_keys(input_13_10_value)
            input_13_16 = browser.find_element(By.ID, 'input_13_16')
            input_13_16.send_keys(input_13_16_value)
            choice_13_15_1 = browser.find_element(By.ID, 'choice_13_15_1')
            click_or_not: int = random.randint(0, 100)
            if click_or_not % 2 == 0:
                choice_13_15_1.click()
            input_13_7 = browser.find_element(By.ID, 'input_13_7') # maxlength = 500
            input_13_7.send_keys(input_13_7_value)
            input_13_17_1 = browser.find_element(By.ID, 'input_13_17_1')
            input_13_17_1.click()
            gform_submit_button_13 = browser.find_element(By.ID, 'gform_submit_button_13')
            gform_submit_button_13.click()

            browser.quit()
            print(f'Done with sub {i + 1}')

        return

    filler()
