import webbrowser, pyautogui, time, cv2, pytesseract
pytesseract.pytesseract.tesseract_cmd = (r'C:\Program Files\Tesseract-OCR\tesseract.exe')
firefox = "C:/Program Files/Mozilla Firefox/firefox.exe %s"
webbrowser.get(firefox).open_new("https://bit.ly/3dI9XPt")

time.sleep(1)
pyautogui.click(r'Play.png')
pyautogui.move(500,0)

def solver():
      
    time.sleep(0.3)
    pyautogui.screenshot('equation.png', region = (482, 244, 375, 155))
    
    time.sleep(1)
    img = cv2.imread('equation.png')
    img2 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    (thresh, blackAndWhiteImage) = cv2.threshold(img2, 175, 255, cv2.THRESH_BINARY)
    blackAndWhiteImage2 = cv2.bitwise_not(blackAndWhiteImage)

    result = pytesseract.image_to_string(blackAndWhiteImage2)
    print(result)

    dict1 = {'§':'5', '%':'x', '—':'-'} 
    for i in dict1.keys():
        if i in result:
            result = result.replace(i, dict1[i])

    numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    op = ['+', '-', 'x', '/', '=']

    a,b,c,f = ([] for i in range(4))

    x = list(result)

    f = [i for i in x if i in op or i in numbers]  

    flag = 0
    for i in f:
        if i not in op and flag == 0:
            a.append(i)
        elif i not in op and flag == 1:
            b.append(i)
        elif i not in op and flag == 2:
            c.append(i)
        else:
            if i == '=':
                flag = 2
            else:
                flag = 1
                opt = i

    y = int(''.join(a))
    z = int(''.join(b))
    w = int(''.join(c))

    def calc(l,m,n):
        isEqual = False
        check = [l+m, l-m, l*m, l/m]
        if n in check:
            isEqual = True
        return isEqual

    check = calc(y,z,w)
    print(check)

    if check == True:
        pyautogui.click(r'Correct.png')
    else:
        pyautogui.click(r'Incorrect.png')
        
    pyautogui.move(500,0)
    
while True:
    solver()
