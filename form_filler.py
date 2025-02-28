#!/usr/bin/env python3

import argparse
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
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

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

    form_url: str = 'https://enddei.ed.gov/'

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
            school_name: str = '123456789012345678901234567890123456789012345678901'
            email_address: str = '123456789012345678901234567890123456789012345678901'
            while len(school_name) > 50:
                school_dict: dict = fake.school_object()
                rint: int = random.randint(1,2)
                if rint == 1:
                    school_name = school_dict['school']
                else:
                    school_name = school_dict['district']
            while len(email_address) > 50:
                email_address = fake.profile(fields=['mail'])['mail']

            email_value: str = email_address # Your email (50 char max)
            location_value: str = school_name # School or school district (50 char max)
            zipcode_value: str = fake.postcode()[:5] # School or school district ZIP Code 5 char max)

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

            description_value: str

            f: TextIO
            if content_choice == 'u':
                # Send them to school with the Universal Declaration of Human Rights
                with open('udohr.txt', 'r') as f:
                    description_value = f.read()
                    description_value = ' '.join(description_value.split()[:450]) # Incident details (Include As Much Information As Possible)
            else:
                description_value = response.text.replace('<br/>', '')
                description_value = ' '.join(description_value.split()[:450])


            options = FirefoxOptions()
            if not windowed:
                # Run headless
                options.add_argument("-headless")
            browser = webdriver.Firefox(options=options)
            if windowed:
                # Get a good view of the form doing its thing
                browser.maximize_window()
            browser.get(form_url)
            sleep_time: int = random.randint(2,30)
            print(f'sleeping for {sleep_time} seconds...')
            time.sleep(sleep_time)
            print('Annnnd...GO!')

            email_input = browser.find_element(By.ID, 'email')
            email_input.send_keys(email_value)
            location_input = browser.find_element(By.ID, 'location')
            location_input.send_keys(location_value)
            zipcode_input = browser.find_element(By.ID, 'zipcode')
            zipcode_input.send_keys(zipcode_value)
            description_input = browser.find_element(By.ID, 'description')
            description_input.send_keys(description_value)
            submit_button = browser.find_element(By.ID, 'submitButton')

            WebDriverWait(browser, 20).until(EC.element_to_be_clickable(submit_button)).click()

            submit_button.click()

            browser.quit()
            print(f'Done with sub {i + 1}')

        return

    filler()
