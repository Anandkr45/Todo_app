import Function
import PySimpleGUI as sg

label = sg.Text("Type in the ToDo")
input_box = sg.InputText(tooltip="Enter todo")
add_btn = sg.Button("Add")

window = sg.Window('ToDo_App', layout=[[label], [input_box, add_btn]])
window.read()
print("Hello")
window.close()
