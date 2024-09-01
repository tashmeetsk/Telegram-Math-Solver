from selenium import webdriver
from selenium.webdriver.common.by import By


def solver(flag):
    x = int(driver.find_element(By.ID, "task_x").text)
    y = int(driver.find_element(By.ID, "task_y").text)
    op = str(driver.find_element(By.ID, "task_op").text)
    game_ans = int(driver.find_element(By.ID, "task_res").text)

    if op == "/" and y == 0:    # We don't want the program to divide by 0
        final_ans = None
    else:
        operation = {"–": x.__sub__, "+": x.__add__, "×": x.__mul__, "/": x.__truediv__}
        final_ans = operation[op](y)

    if flag == 0:
        if game_ans == final_ans:
            driver.find_element(By.ID, "button_correct").click()
        else:
            driver.find_element(By.ID, "button_wrong").click()

    else:
        if game_ans == final_ans:
            driver.find_element(By.ID, "button_wrong").click()
        else:
            driver.find_element(By.ID, "button_correct").click()


ask = input('Do you have the link of the website [y/n]: ')

if ask.lower() == 'y':
    website = input('''\nPlease enter the math solver site...
Press Return key to continue by the default website \n''')
else:
    website = "https://tbot.xyz/math/"

print()

while True:
    try:
        ask = int(input('Up to which number would you like to score (enter value in +ve integer): '))
    except ValueError:
        print('\nPlease enter a valid number...')
    else:
        break
    if ask < 0:
        print('\nPlease enter a valid number...')

option = webdriver.FirefoxOptions()
driver = webdriver.Firefox(options = option)

driver.get(website)

play = driver.find_element(By.ID, "button_correct").click()

for i in range(0, int(ask)):
    solver(flag=0)

for i in range(0, 3):
    solver(flag=1)
