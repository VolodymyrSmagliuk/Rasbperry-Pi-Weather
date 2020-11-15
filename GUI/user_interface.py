from PySimpleGUI import PySimpleGUI as sg

layout = [
    [sg.Text('Latitude'), sg.InputText()
     ],
    [sg.Text('Longitude'), sg.InputText()
     ],
    [sg.Output(size=(88, 20))],
    [sg.Submit(), sg.Cancel()]
]
window = sg.Window('Local weather search', layout)
while True:                             # The Event Loop
    event, values = window.read()
    # print(event, values) #debug
    if event in (None, 'Exit', 'Cancel'):
        break
