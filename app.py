from parsers.all_content_of_a_page import WebPage
from database.database_manipulation import *
from robot.robot import RobotFileChecker


OBJECTIVES = "Scrape a website, get the words contained and classify them by significance."
DB_PROJECT_NAME = 'Enter a name for your Database: '
ASK_URL = "Enter a url or : "
ASK_USER_NAME = "Enter your name: "
USER_CHOISES = """Options:
(a) Select to enter your name 
(b) Enter a url of a website to scrape or website content
(c) A keyword (can be numbers, letters, or both. NOT case sensitive) 
(d) Enter to show objectives of the website.
(f) Print all words from the page
(q) Type q to quit
Please select an option: """
running = True


def prompt_user_name():
    global ASK_USER_NAME
    result = input(ASK_USER_NAME)
    return result


def prompt_user_url():
    global ASK_URL, DB_PROJECT_NAME
    url = input(ASK_URL)
    page = WebPage(url)
    try:
        add_to_webpages(DB_PROJECT_NAME, url, page.grab_title)
        for word, count, significance in page.words_count_significance:
            add_to_keywords(DB_PROJECT_NAME, 1, word, count, significance)
    except AttributeError:
        print("You have to enter a valid website url!")


def program_objectives():
    global OBJECTIVES
    return OBJECTIVES


def prompt_keyword():
    keyword = input("Please enter 1 keyword to check if it is on the website: ")
    return search_keyword(DB_PROJECT_NAME, keyword)


def all_words():
    return search_all_words(DB_PROJECT_NAME)


user_choices = {
    'a': prompt_user_name,
    'b': prompt_user_url,
    'c': prompt_keyword,
    'd': program_objectives,
    'f': all_words,

}


def menu():
    user_input = input(USER_CHOISES)
    if user_input != 'q':
        if user_input in user_choices.keys():
            print(user_choices[user_input]())
        else:
            print('Please choose a valid command.')
        menu()
    else:
        global running
        running = 'q'
        return running


def prompt_database_name():
    global DB_PROJECT_NAME
    DB_PROJECT_NAME = input(DB_PROJECT_NAME)
    try: delete_database(DB_PROJECT_NAME)
    except FileNotFoundError: pass
    create_table_webpages_if_not_exist(DB_PROJECT_NAME)
    create_table_keywords_if_not_exist(DB_PROJECT_NAME)


if __name__ == "__main__":
    prompt_database_name()

    if running != 'q':
        menu()
    else:
        print("Thank you for using the program.")


