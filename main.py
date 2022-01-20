from selenium import webdriver


def solver(flag):
    x = int(driver.find_element_by_id("task_x").text)
    y = int(driver.find_element_by_id("task_y").text)
    op = str(driver.find_element_by_id("task_op").text)
    GameAns = int(driver.find_element_by_id("task_res").text)

    if op == "/" and y == 0:
        FinalAns = None
    else:
        Dict = {"–": x.__sub__, "+": x.__add__, "×": x.__mul__, "/": x.__truediv__}
        FinalAns = Dict[op](y)

    if flag == 0:
        if GameAns == FinalAns:
            driver.find_element_by_id("button_correct").click()
        else:
            driver.find_element_by_id("button_wrong").click()

    else:
        if GameAns == FinalAns:
            driver.find_element_by_id("button_wrong").click()
        else:
            driver.find_element_by_id("button_correct").click()


ask = input('Do you have the link of the website [y/n]: ')

if ask.lower() == 'y':
    website = input('''\nPlease enter the tbot site...
Press Return key to continue by the default website \n''')
else:
    website = "https://tbot.xyz/math/"

print()

while True:
    try:
        ask = int(input('Upto which number would you like to score (enter value in +ve interger): '))
    except ValueError:
        print('\nPlease enter a valid number...')
    else:
        break
    if ask < 0:
        print('\nPlease enter a valid number...')

driver = webdriver.Firefox(executable_path=r'C:\Program Files (x86)\geckodriver.exe')

driver.get(website)

play = driver.find_element_by_id("button_correct").click()

for i in range(0, int(ask)):
    solver(flag=0)

for i in range(0, 3):
    solver(flag=1)
