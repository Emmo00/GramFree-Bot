from datetime import datetime
from time import sleep
from selenium import webdriver
import bot.constants as const


class Bot(webdriver.Chrome):
    def __init__(self, user_data_dir='C:/webdrivers/mychromedata/'):
        print('automation started')
        options = webdriver.ChromeOptions()
        options.add_argument(f"--user-data-dir={user_data_dir}")
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        print('browser open')
        super().__init__(options=options)
        self.implicitly_wait(20)
        self.maximize_window()
        self.get(const.DASHBOARD)
        sleep(2)

    def free(self):
        print('opening page')
        self.get(const.FREE)
        sleep(3)
        roll_button = self.find_element_by_id('roll-button')
        self.execute_script('arguments[0].click();', roll_button)
        print('done Free')

    def video(self):
        self.get(const.VIDEOS)
        sleep(4)
        watch_btn = self.find_elements_by_class_name('watch-btn')
        if watch_btn:
            for element in watch_btn:
                self.execute_script('arguments[0].click();', element)
                sleep(70)
                self.video()
        else:
            print('No more videos')

    def smart_contracts(self):
        self.get(const.SMART_CONTRACTS)
        self.sign()

    def sign(self):
        contracts = self.find_elements_by_class_name('send-contract')
        for contract in contracts:
            self.execute_script('arguments[0].click();', contract)
            self.confirm_contract()
            sleep(1)
        self.get(const.SMART_CONTRACTS)
        sleep(1)
        take = self.find_element_by_class_name('take-contract')
        self.execute_script('arguments[0].click();', take)
        return

    def confirm_contract(self):
        confirm = self.find_element_by_xpath('/html/body/div[9]/div/div[3]/button[1]')
        self.execute_script('arguments[0].click();', confirm)
        sleep(3)

    def close_window(self):
        self.close()

    def log_balance(self):
        self.get(const.DASHBOARD)
        balance = self.find_element_by_xpath('//*[@id="dashboard-analytics"]/div[4]/div[1]/div/div/div[1]/h2').text
        bal = balance.removesuffix('Gram').strip()
        bal_file = open(const.BAL_LOG, 'w')
        bal_file.write(f'{datetime.now()},{bal}\n')
        bal_file.close()

    def go_home(self):
        self.get(const.DASHBOARD)
