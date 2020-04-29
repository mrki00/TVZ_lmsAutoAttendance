from selenium import webdriver
from selenium.webdriver.chrome.options import Options

CHROME_OPTIONS = Options()
CHROME_OPTIONS.add_argument("--headless")
PATH_TO_CHROMEDRIVER = 'PATH'  # replace PATH with your path to chrome webdriver
browser = webdriver.Chrome(chrome_options=CHROME_OPTIONS, executable_path=PATH_TO_CHROMEDRIVER)  # noqa


def login():
    url = 'https://lms.tvz.hr/login/index.php'
    browser.get(url)
    while True:
        username = input('Upisi korisnicko ime: ')
        password = input('Upisi lozinku: ')
        browser.find_element_by_id('username').send_keys(username)
        browser.find_element_by_id('password').send_keys(password)
        browser.find_element_by_id('loginbtn').click()
        try:
            browser.find_element_by_class_name('error')
        except:  # noqa
            break


def submit_attendance(password, url):
    browser.get(url)
    browser.find_element_by_xpath("//*[text()='Submit attendance']").click()
    browser.find_element_by_id('id_studentpassword').send_keys(password)
    browser.find_element_by_xpath(
        '/html/body/div[4]/div/div/div/section/div/form/fieldset[1]/div/div[2]/fieldset/span[1]/input').click()  # noqa
    browser.find_element_by_id('id_submitbutton').click()


def elpo():
    url = 'https://lms.tvz.hr/course/view.php?id=139'
    browser.get(url)
    password = browser.find_element_by_xpath(
        '/html/body/div[4]/div/div/div/section/div/div/ul/li[1]/div[3]/ul/li[8]/div/div/div[2]/div[2]/div/div/p[2]').text  # noqa
    url = 'https://lms.tvz.hr/mod/attendance/view.php?id=15337'
    submit_attendance(password, url)


def trkom():
    url = 'https://lms.tvz.hr/course/view.php?id=199'
    browser.get(url)
    password = browser.find_element_by_xpath(
        '/html/body/div[4]/div/div/div/section/div/div/ul/li[1]/div[3]/ul/li[5]/div/div/div[2]/div[2]/div/div/p').text  # noqa
    url = 'https://lms.tvz.hr/mod/attendance/view.php?id=15342'
    submit_attendance(password, url)


def main():
    kolegij = input(
        'Upisi \"elpo\" za elektronicko poslovanje ili \"trkom\" za trzisne komunikacije: ')  # noqa
    while(kolegij != 'elpo' and kolegij != 'trkom'):
        print('Upis nije valjan, pokusajte ponovno')
        kolegij = input(
            'Upisi \"elpo\" za elektronicko poslovanje ili \"trkom\" za trzisne komunikacije: ')  # noqa
    login()
    if(kolegij == "elpo"):
        elpo()
    elif(kolegij == "trkom"):
        trkom()


if __name__ == "__main__":
    main()
