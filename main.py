from selenium import webdriver


def solver(flag):
    x = int(driver.find_element_by_id("task_x").text)
    y = int(driver.find_element_by_id("task_y").text)
    op = str(driver.find_element_by_id("task_op").text)
    game_ans = int(driver.find_element_by_id("task_res").text)

    if op == '/' and y == 0:   #we don't want the program to divide by 0
        final_ans = None
    else:
        dict1 = {'–': x - y, '+': x + y, '×': x * y, '/': x / y}
        final_ans = dict1[op]

    if flag == 0:
        if game_ans == final_ans:
            driver.find_element_by_id("button_correct").click()
        else:
            driver.find_element_by_id("button_wrong").click()

    else:
        if game_ans == final_ans:
            driver.find_element_by_id("button_wrong").click()
        else:
            driver.find_element_by_id("button_correct").click()


website = input('''Please enter the tbot site...
Press Return/Spacebar to continue by the default website \n''')

print()

ask = int(input('Upto which number would you like to score (enter value in +ve interger): '))

driver = webdriver.Firefox(executable_path=r'C:\Program Files (x86)\geckodriver.exe')

if website == '' or website == ' ':
    driver.get("https://tbot.xyz/math/")
else:
    driver.get(website)

play = driver.find_element_by_id("button_correct").click()

for i in range(0, ask):
    solver(flag=0)

for i in range(0, 3):
    solver(flag=1)
