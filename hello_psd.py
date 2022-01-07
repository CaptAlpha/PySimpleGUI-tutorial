import PySimpleGUI as sg

layout = [
    [sg.Text('Hello world!')],
    [sg.Button('OK')]

]

# Create the Window
window = sg.Window('Hello world!', layout)

# Create an Event loop 
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'OK':
        break
window.close()