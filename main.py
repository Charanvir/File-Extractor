import PySimpleGUI as sg
from functions import extract_archive as extract

select_file_text = sg.Text("Select Archive: ")
select_destination_text = sg.Text("Select Destination: ")
file_input = sg.Input()
destination_input = sg.Input()
file_choose_button = sg.FileBrowse("Choose", key="file_button")
destination_choose_button = sg.FolderBrowse("Choose", key="destination_button")
extract_button = sg.Button("Extract", key="extract")
output_message = sg.Text(key="output", text_color="green")

layout = [
    [select_file_text, file_input, file_choose_button],
    [select_destination_text, destination_input, destination_choose_button],
    [extract_button, output_message]
]

window = sg.Window("File Extractor", layout)

while True:
    event, values = window.read()
    archive_file = values["file_button"]
    destination_path = values["destination_button"]
    match event:
        case "extract":
            extract(archive_file, destination_path)
            window["output"].update("Archive Extracted")
        case sg.WINDOW_CLOSED:
            break

window.close()
