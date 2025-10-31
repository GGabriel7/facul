import pyautogui
screenWidth, screenHeight = pyautogui.size()
currentMouseX, currentMouseY = pyautogui.position()
pyautogui.moveTo(100, 150)
pyautogui.click()
pyautogui.click(100, 200)
pyautogui.move(0, 10)
pyautogui.doubleClick()
pyautogui.moveTo(500, 500, duration=2, tween=pyautogui.easeInOutQuad)
pyautogui.write('Olá, Mundo!', interval=0.25)
pyautogui.press('esc')
pyautogui.keyDown('shift')
pyautogui.press(['left', 'left', 'left', 'left'])
pyautogui.keyUp('shift')
pyautogui.hotkey('ctrl', 'c')
pyautogui.alert('Esta é a mensagem para Tela.')

# PyAutoGUI é uma biblioteca Python que permite a automação de interações com a interface gráfica do usuário (GUI), como mover o mouse, clicar, digitar texto e capturar screenshots. É amplamente utilizada para testes automatizados, automação de tarefas repetitivas e criação de bots para interagir com aplicações desktop.