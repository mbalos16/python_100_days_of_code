# Exercise 48.2. Fill a sign up form and submit

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import random

STORE_SECONDS = 5
COOKIE_SECONDS = 600
DRIVERS_PATH = "/Users/Maria/Desktop/Python/Python Exercises/assets/chrome_driver"
COOKIECLICKER_URL = "http://orteil.dashnet.org/experiments/cookie/"
random.seed(7)


# Check on time.
class Timer:
    def __init__(self) -> None:
        self.start_time = None
        self.seconds = None

    def start(self, seconds):
        self.start_time = time.time()
        self.seconds = seconds

    def restart(self):
        self.start(self.seconds)

    def check(self):
        time_now = time.time()
        diff = time_now - self.start_time
        if diff >= self.seconds:
            return True
        else:
            return False


def launch_chrome(path):
    """This function defines Chrome options specifying
    the path of the drivers. Then it creates the driver
    with specified options."""
    opt = webdriver.ChromeOptions()
    opt.binary_location = path
    driver = webdriver.Chrome(opt)
    return driver


def find_available_items(driver):
    store = driver.find_element(By.ID, "store")
    items = store.find_elements(By.XPATH, "./div")

    # Check the available items in the store.
    available_items = [
        item for item in items if item.get_attribute("class") != "grayed"
    ]
    return available_items


def buy_most_expensive_item(driver, available_items=None):
    if available_items is None:
        available_items = find_available_items(driver)
    # ------------ Method 1 ------------
    # max_cost = 0
    # most_expensive_item = None
    # for item in available_items:
    #     item_b = item.find_element(By.TAG_NAME, "b")
    #     item_text = item_b.text.split(" - ")
    #     item_cost = int(item_text[1].replace(",", ""))
    #     if item_cost > max_cost:
    #         max_cost = item_cost
    #         most_expensive_item = item
    # if most_expensive_item is not None:
    # most_expensive_item.click()

    # ------------ Method 2 ------------
    most_expensive_item = available_items[-1] if len(available_items) > 0 else None
    if most_expensive_item is not None:
        most_expensive_item.click()


def recursively_buy_most_expensive_item(driver):
    available_items = find_available_items(driver)
    while len(available_items) > 0:
        buy_most_expensive_item(driver, available_items=available_items)
        time.sleep(100 / 1000)
        available_items = find_available_items(driver)


def buy_random_item(driver, available_items=None):
    if available_items is None:
        available_items = find_available_items(driver)
    random_item = random.choice(available_items) if len(available_items) > 0 else None
    if random_item is not None:
        random_item.click()


def recursively_buy_random_item(driver):
    available_items = find_available_items(driver)
    while len(available_items) > 0:
        buy_random_item(driver, available_items=available_items)
        time.sleep(100 / 1000)
        available_items = find_available_items(driver)


def random_strategy(driver):
    strategies = [
        buy_most_expensive_item,
        recursively_buy_most_expensive_item,
        buy_random_item,
        recursively_buy_random_item,
    ]
    strategy = random.choice(strategies)
    strategy(driver)


def run_game(driver, buying_strategy, store_check_period, game_duration):
    # Find the cookie within the website.
    cookie = driver.find_element(By.ID, "cookie")

    # Timmer set to check on the store and buy improvements
    store_timer = Timer()
    store_timer.start(store_check_period)

    # Timer set to check the seconds record and improve, every time
    cookie_timer = Timer()
    cookie_timer.start(game_duration)

    game_on = True
    while game_on:
        # Find the central cookie and click on it
        cookie.click()

        # Check if the store timer has passed to buy items
        store_timer_finished = store_timer.check()

        if store_timer_finished:
            buying_strategy(driver)
            # restart the timer
            store_timer.restart()

        # Check on the cookies timer for cookies/seconds
        cookie_timer_finished = cookie_timer.check()

        # Check on the cookies/seconds avaibalbe
        if cookie_timer_finished:
            # stop the game to check on cookies/seconds time.
            game_on = False
            cookie_sec = driver.find_element(By.ID, "cps")
            print(cookie_sec.text)
            cookie_timer.restart()


if __name__ == "__main__":
    # -------- Method 1: Run the code with an indivual strategy
    # driver = launch_chrome(path=DRIVERS_PATH)
    # driver.get(COOKIECLICKER_URL)
    # run_game(
    #     driver=driver,
    #     buying_strategy=random_strategy,
    #     store_check_period=STORE_SECONDS,
    #     game_duration=COOKIE_SECONDS,
    # )

    # -------- Method 2: Run the code with all the strategies to see which one is the best.
    strategies = [
        buy_most_expensive_item,
        recursively_buy_most_expensive_item,
        buy_random_item,
        recursively_buy_random_item,
        random_strategy,
    ]
    for strategy in strategies:
        print(f"Testing strategy {strategy.__name__}")
        driver = launch_chrome(path=DRIVERS_PATH)
        driver.get(COOKIECLICKER_URL)
        run_game(
            driver=driver,
            buying_strategy=strategy,
            store_check_period=STORE_SECONDS,
            game_duration=COOKIE_SECONDS,
        )
        driver.close()

    # -------- Results:
    #     Testing strategy buy_most_expensive_item
    #     cookies/second : 164
    #     Testing strategy recursively_buy_most_expensive_item
    #     cookies/second : 133
    #     Testing strategy buy_random_item
    #     cookies/second : 174.6
    #     Testing strategy recursively_buy_random_item
    #     cookies/second : 98.8
    #     Testing strategy random_strategy
    #     cookies/second : 131.8

    # When the program stops the page will remain open for 4 seconds.
    time.sleep(4000)
