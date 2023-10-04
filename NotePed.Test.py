from pywinauto.application import Application


#app = Application(backend='uia').start('notepad.exe')
#app = Application(backend='uia').connect(title='Untitled - Notepad', timeout=15)
app = Application(backend='uia').start('notepad.exe').connect(title='Untitled - Notepad', timeout=15)
#app.UntitledNotepad.print_control_identifiers()

textEditor = app.UntitledNotepad.child_window(title='Text Editor', auto_id='15', control_type='Edit').wrapper_object()
textEditor.type_keys('Subscribe to the channel Its free I mean it!', with_spaces=True)

fileMenu = app.UntitledNotepad.child_window(title='File', control_type='MenuItem').wrapper_object()
fileMenu.click_input()
app.UntitledNotepad.print_control_identifiers()

