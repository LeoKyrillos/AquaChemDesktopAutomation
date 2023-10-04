
from pywinauto.application import Application
import time



app = Application(backend='uia').start('C:\Program Files (x86)\AquaChem 12\AQC32.exe')
time.sleep(1)
app.connect(title='AquaChem (x86)', timeout=15)

#app.AquaChemX86.print_control_identifiers()

newProject = app.AquaChemX86.child_window(title= 'New project...', auto_id='buttonNewProject', control_type='Button').wrapper_object()
newProject.click_input()
time.sleep(2)

projectName = app.AquaChemX86.child_window(title= 'Project folder', auto_id='textBoxName', control_type='Edit').wrapper_object()
projectName.click_input()
time.sleep(3)
projectName.type_keys("Test Project Advanced", with_spaces=True)

    #def test_text():
    #assert app.AquaChemX86.child_window(title= 'New project...', auto_id='buttonNewProject').window_text() == 'Test Project Advanced', 'O texto capturado é o mesmo'

nextButton = app.AquaChemX86.child_window(title= 'Next >>', auto_id='buttonNext', control_type='Button').wrapper_object()
nextButton.click()
time.sleep(2)

selectTemplates = app.AquaChemX86.child_window(title= 'Select a Template', auto_id='comboBoxTemplates', control_type='ComboBox').wrapper_object()
selectTemplates.click_input()
time.sleep(2)

advancedTemplates= app.AquaChemX86.child_window(title= 'Advanced').wrapper_object()
advancedTemplates.select()
time.sleep(2)

nextButton1 = app.AquaChemX86.child_window(title= 'Next >>', auto_id='buttonNext', control_type='Button').wrapper_object()
nextButton1.click()
time.sleep(2)

#finishButton1 = app.AquaChemX86.child_window(title= 'Finish', auto_id='buttonNext', control_type='Button').wrapper_object()
#finishButton1.click()
#time.sleep(2)