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

    if (flag == 0 and game_ans == final_ans) or (flag == 1 and game_ans != final_ans):
        driver.find_element(By.ID, "button_correct").click()
    else:
        driver.find_element(By.ID, "button_wrong").click()

ask = input('Do you have the link to the website? [y/n]: ').strip().lower()

if ask == 'y':
    website = input('Please enter the math solver site URL (press the return key to continue with the default site)\n') or "https://tbot.xyz/math/"
else:
    website = "https://tbot.xyz/math/"

while True:
    try:
        target_score = int(input('Up to which number would you like to score? (Enter a positive integer): '))
        if target_score > 0:
            break
        else:
            print('Please enter a valid positive number.')
    except ValueError:
        print('Please enter a valid number.')

options = webdriver.FirefoxOptions()
driver = webdriver.Firefox(options=options)

driver.get(website)

driver.find_element(By.ID, "button_correct").click()

for _ in range(target_score):
    solver(flag=0)

for _ in range(3):
    solver(flag=1)
