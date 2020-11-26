from parsers.all_content_of_a_page import WebPage
from database.database_manipulation import *
from robot.robot import RobotFileChecker


DB_PROJECT_NAME = 'Enter a name for your Database: '
ASK_URL = "Enter a url or '0' to stop: "
ASK_USER_NAME = "Enter your name: "
running = True
USER_CHOISES = """(a) Select to enter your name 
(b) Show the objective of the program 
(c) A keyword (can be numbers, letters, or both. NOT case sensitive) 
(d) execute your choice: """


def prompt_db_name():
    global DB_PROJECT_NAME
    result = input(DB_PROJECT_NAME).strip(' ')
    return result


def prompt_user_name():
    global ASK_USER_NAME
    result = input(ASK_USER_NAME)
    return result


def prompt_user_url():
    global ASK_URL
    result = input(ASK_URL)
    return result


def program_objectives(objectives):
    print(objectives)


def prompt_keyword():
    pass


def execute_btm():
    pass


user_choices = {
    'a': prompt_user_name,
    'b': program_objectives,
    'c': prompt_keyword,
    'd': execute_btm

}


def menu():
    while user_input != '0':
        user_input = input(USER_CHOISES)
        if user_input in user_choices.keys():
            user_choices[user_input]()
        else:
            print('Please choose a valid command.')
        user_input = input(USER_CHOISES)
    else:
        global running
        running = False


if __name__ == "__main__" and running:
    DB_PROJECT_NAME = 'x'  # TODO 01.prompt_db_name()
    create_table_webpages_if_not_exist(DB_PROJECT_NAME)
    create_table_keywords_if_not_exist(DB_PROJECT_NAME)
    search_if_db_empty(DB_PROJECT_NAME)
    promped_url = 'https://books.toscrape.com/'  # prompt_user_url()
    current_page = WebPage(promped_url)  # TODO 02. replace url with prompt_url
    url_title = WebPage.grab_title
    roboCheck = RobotFileChecker(promped_url)
    print(roboCheck.check_fetch_page)

