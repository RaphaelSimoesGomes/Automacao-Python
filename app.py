import pyautogui 
from time import sleep

pyautogui.click(968,597, duration=0.7)

pyautogui.click(1017,540, duration=0.7)
pyautogui.write("raphael")

pyautogui.click(1010,564, duration=0.7)
pyautogui.write("1234")

pyautogui.click(867,599, duration=0.7)


pyautogui.click(1017,540, duration=0.7)
pyautogui.write("raphael")

pyautogui.click(1010,564,duration=0.7)
pyautogui.write("1234")

pyautogui.click(867,599, duration=0.7)

with open('produtos.txt','r') as arquivo:
    for line in arquivo:
        produto = line.split(',')[0]
        quantidade = line.split(',')[1]
        preço = line.split(',')[2]

        pyautogui.click(712,528,duration=0.2)
        pyautogui.write(produto)
        pyautogui.click(713,552, duration=0.2)
        pyautogui.write(quantidade)
        pyautogui.click(712,581,duration=0.2)
        pyautogui.write(preço)
        pyautogui.click(591,737,duration=0.2)