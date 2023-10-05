
from pywinauto.application import Application
import time


###### Automation Criate a New Project and Importing Data ############


app = Application(backend='uia').start('C:\Program Files (x86)\AquaChem 12\AQC32.exe')
time.sleep(30)
app.connect(title='AquaChem (x86)')

#app.AquaChemX86.print_control_identifiers()

newProject = app.AquaChemX86.child_window(title= 'New project...', auto_id='buttonNewProject', control_type='Button').wrapper_object()
if newProject.is_visible() and newProject.is_enabled():
    newProject.click_input()
#time.sleep(2)

projectName = app.AquaChemX86.child_window(title= 'Project folder', auto_id='textBoxName', control_type='Edit').wrapper_object()
if projectName.is_visible() and projectName.is_enabled():
    projectName.click_input()
    projectName.type_keys('Test Project Basic Template', with_spaces=True)
#time.sleep(2)

nextButton = app.AquaChemX86.child_window(title= 'Next >>', auto_id='buttonNext', control_type='Button').wrapper_object()
if nextButton.is_visible() and nextButton.is_enabled():
    nextButton.click()
#time.sleep(2)

nextButton1 = app.AquaChemX86.child_window(title= 'Next >>', auto_id='buttonNext', control_type='Button').wrapper_object()
if nextButton1.is_visible() and nextButton1.is_enabled():
    nextButton1.click()
#time.sleep(2)

finishButton1 = app.AquaChemX86.child_window(title= 'Finish', auto_id='buttonNext', control_type='Button').wrapper_object()
if finishButton1.is_visible() and finishButton1.is_enabled():
    finishButton1.click()
time.sleep(10)

templateManager = app['AquaChem (x86) [Test Project Basic Template]'].child_window(title= 'Template Manager', control_type='Button').wrapper_object()
if templateManager.is_visible() and templateManager.is_enabled():
    templateManager.click_input()
#time.sleep(2)

templateManagerOkButton = app['AquaChem (x86) [Test Project Basic Template]'].child_window(title= 'OK', auto_id='buttonOK', control_type='Button').wrapper_object()
if templateManagerOkButton.is_visible() and templateManagerOkButton.is_enabled():
    templateManagerOkButton.click()
#time.sleep(10)

######## Aquifer_Code #######

stationTable1 = app['AquaChem (x86) [Test Project Basic Template]'].child_window(title= 'Station', auto_id='[Node] 0, [Node] 0', control_type='DataItem').wrapper_object()
if stationTable1.is_visible() and stationTable1.is_enabled():
    stationTable1.click_input()
#time.sleep(2)

addField1 = app['AquaChem (x86) [Test Project Basic Template]'].child_window(title= 'Add Field', control_type='Button').wrapper_object()
if addField1.is_visible() and addField1.is_enabled():
    addField1.click_input()
#time.sleep(2)

fieldName1 = app['AquaChem (x86) [Test Project Basic Template]'].child_window(title= 'Field name', auto_id='textBoxFieldName', control_type='Edit').wrapper_object()
if fieldName1.is_visible() and fieldName1.is_enabled():
    fieldName1.click_input()
    fieldName1.type_keys('Aquifer_Code', with_spaces=True)
#time.sleep(2)

fieldNameOk1 = app['AquaChem (x86) [Test Project Basic Template]'].child_window(title= 'OK', auto_id='buttonOK', control_type='Button').wrapper_object()
if fieldNameOk1.is_visible() and fieldNameOk1.is_enabled():
    fieldNameOk1.click()

######## Geology #######

stationTable2 = app['AquaChem (x86) [Test Project Basic Template]'].child_window(title= 'Station', auto_id='[Node] 0, [Node] 0', control_type='DataItem').wrapper_object()
if stationTable2.is_visible() and stationTable2.is_enabled():
    stationTable2.click_input()
#time.sleep(2)

addField2 = app['AquaChem (x86) [Test Project Basic Template]'].child_window(title= 'Add Field', control_type='Button').wrapper_object()
if addField2.is_visible() and addField2.is_enabled():
    addField2.click_input()
#time.sleep(2)

fieldName2 = app['AquaChem (x86) [Test Project Basic Template]'].child_window(title= 'Field name', auto_id='textBoxFieldName', control_type='Edit').wrapper_object()
if fieldName2.is_visible() and fieldName2.is_enabled():
    fieldName2.click_input()
    fieldName2.type_keys('Geology', with_spaces=True)
#time.sleep(2)

fieldNameOk2 = app['AquaChem (x86) [Test Project Basic Template]'].child_window(title= 'OK', auto_id='buttonOK', control_type='Button').wrapper_object()
if fieldNameOk2.is_visible() and fieldNameOk2.is_enabled():
    fieldNameOk2.click()

######## Station_Comment #######

stationTable3 = app['AquaChem (x86) [Test Project Basic Template]'].child_window(title= 'Station', auto_id='[Node] 0, [Node] 0', control_type='DataItem').wrapper_object()
if stationTable3.is_visible() and stationTable3.is_enabled():
    stationTable3.click_input()
#time.sleep(2)

addField3 = app['AquaChem (x86) [Test Project Basic Template]'].child_window(title= 'Add Field', control_type='Button').wrapper_object()
if addField3.is_visible() and addField3.is_enabled():
    addField3.click_input()
#time.sleep(2)

fieldName3 = app['AquaChem (x86) [Test Project Basic Template]'].child_window(title= 'Field name', auto_id='textBoxFieldName', control_type='Edit').wrapper_object()
if fieldName3.is_visible() and fieldName3.is_enabled():
    fieldName3.click_input()
    fieldName3.type_keys('Station_Comment', with_spaces=True)
#time.sleep(2)

fieldNameOk3 = app['AquaChem (x86) [Test Project Basic Template]'].child_window(title= 'OK', auto_id='buttonOK', control_type='Button').wrapper_object()
if fieldNameOk3.is_visible() and fieldNameOk3.is_enabled():
    fieldNameOk3.click()

######## Station_Comment #######

stationTable4 = app['AquaChem (x86) [Test Project Basic Template]'].child_window(title= 'Station', auto_id='[Node] 0, [Node] 0', control_type='DataItem').wrapper_object()
if stationTable4.is_visible() and stationTable4.is_enabled():
    stationTable4.click_input()
#time.sleep(2)

addField4 = app['AquaChem (x86) [Test Project Basic Template]'].child_window(title= 'Add Field', control_type='Button').wrapper_object()
if addField4.is_visible() and addField4.is_enabled():
    addField4.click_input()
#time.sleep(2)

fieldName4 = app['AquaChem (x86) [Test Project Basic Template]'].child_window(title= 'Field name', auto_id='textBoxFieldName', control_type='Edit').wrapper_object()
if fieldName4.is_visible() and fieldName4.is_enabled():
    fieldName4.click_input()
    fieldName4.type_keys('Depth_to_Sample_Point', with_spaces=True)
#time.sleep(2)

dataType4 = app['AquaChem (x86) [Test Project Basic Template]'].child_window(title= 'Data type', auto_id='comboBoxDataType', control_type='ComboBox').wrapper_object()
if dataType4.is_visible() and dataType4.is_enabled():
    dataType4.click_input()

doubleDataType4 = app['AquaChem (x86) [Test Project Basic Template]'].child_window(title= 'Double', control_type='ListItem').wrapper_object()
if doubleDataType4.is_visible() and doubleDataType4.is_enabled():
    doubleDataType4.click_input()

fieldNameOk4 = app['AquaChem (x86) [Test Project Basic Template]'].child_window(title= 'OK', auto_id='buttonOK', control_type='Button').wrapper_object()
if fieldNameOk4.is_visible() and fieldNameOk4.is_enabled():
    fieldNameOk4.click()

######## Well_Depth #######

stationTable5 = app['AquaChem (x86) [Test Project Basic Template]'].child_window(title= 'Station', auto_id='[Node] 0, [Node] 0', control_type='DataItem').wrapper_object()
if stationTable5.is_visible() and stationTable5.is_enabled():
    stationTable5.click_input()
#time.sleep(2)

addField5 = app['AquaChem (x86) [Test Project Basic Template]'].child_window(title= 'Add Field', control_type='Button').wrapper_object()
if addField5.is_visible() and addField5.is_enabled():
    addField5.click_input()
#time.sleep(2)

fieldName5 = app['AquaChem (x86) [Test Project Basic Template]'].child_window(title= 'Field name', auto_id='textBoxFieldName', control_type='Edit').wrapper_object()
if fieldName5.is_visible() and fieldName5.is_enabled():
    fieldName5.click_input()
    fieldName5.type_keys('Well_Depth', with_spaces=True)
#time.sleep(2)

dataType5 = app['AquaChem (x86) [Test Project Basic Template]'].child_window(title= 'Data type', auto_id='comboBoxDataType', control_type='ComboBox').wrapper_object()
dataType5.click_input()

doubleDataType5 = app['AquaChem (x86) [Test Project Basic Template]'].child_window(title= 'Double', control_type='ListItem').wrapper_object()
doubleDataType5.click_input()

fieldNameOk5 = app['AquaChem (x86) [Test Project Basic Template]'].child_window(title= 'OK', auto_id='buttonOK', control_type='Button').wrapper_object()
fieldNameOk5.click()

###### Hide Total Dipth ######

#hideTotalDipth = app['AquaChem (x86) [Test Project Basic Template]'].child_window(title= 'Total Depth', auto_id='[Node] 0, [Node] 0, [Node] 6', control_type='DataItem').wrapper_object()
#hideTotalDipth.actions.type_keys('{DOWN 6}') NO attribut mensege
#hideTotalDipth.click_input()
#hideTotalDipth.uncheck_by_click_input()

# Obter um item
#item = hideTotalDipth.get_item(r'[Node] 0, [Node] 0, [Node] 6')
# Selecionar o item
#item.select()
# 
# select('Total Depth', '[Node] 0, [Node] 0, [Node] 6', 'DataItem')
# title= 'Total Depth', auto_id='[Node] 0, [Node] 0, [Node] 6', control_type='DataItem'
#hideTotalDipth.uncheck_by_click_input()

###### Monitoring Event click ######## 

monitoringEvent = app['AquaChem (x86) [Test Project Basic Template]'].child_window(title= 'Monitoring Event', auto_id='[Node] 3', control_type='DataItem').wrapper_object()
monitoringEvent.double_click_input()

##### Sample click ######

sampleClick = app['AquaChem (x86) [Test Project Basic Template]'].child_window(title= 'Sample', auto_id='[Node] 3, [Node] 3', control_type='DataItem').wrapper_object()
sampleClick.double_click_input()

###### WATERTYPE #######

addWaterTypeField = app['AquaChem (x86) [Test Project Basic Template]'].child_window(title= 'Add Field', control_type='Button').wrapper_object()
if addWaterTypeField.is_visible() and addWaterTypeField.is_enabled():
    addWaterTypeField.click_input()
#time.sleep(2)

fildNameWATERTYPE = app['AquaChem (x86) [Test Project Basic Template]'].child_window(title= 'Field name', auto_id='textBoxFieldName', control_type='Edit').wrapper_object()
if fildNameWATERTYPE.is_visible() and fildNameWATERTYPE.is_enabled():
    fildNameWATERTYPE.click_input()
    fildNameWATERTYPE.type_keys('WATERTYPE', with_spaces=True)
#time.sleep(2)

fieldNameWATERTYPEOk = app['AquaChem (x86) [Test Project Basic Template]'].child_window(title= 'OK', auto_id='buttonOK', control_type='Button').wrapper_object()
fieldNameWATERTYPEOk.click()

##### Close Data Base ########

closeDataBase = app['AquaChem (x86) [Test Project Basic Template]'].child_window(title= 'Close', auto_id='buttonClose', control_type='Button').wrapper_object()
closeDataBase.click()

buttonOK = app['AquaChem (x86) [Test Project Basic Template]'].child_window(title= 'OK', auto_id='2', control_type='Button').wrapper_object()
buttonOK.click()

#### Click Import Data ####

clickImportData = app['AquaChem (x86) [Test Project Basic Template]'].child_window(title= 'Import Data', control_type='Button').wrapper_object()
clickImportData.click_input()

#### Select Import Type General ####

generalSelect = app['AquaChem (x86) [Test Project Basic Template]'].child_window(title= 'General', auto_id= 'radioButtonGeneral', control_type='RadioButton').wrapper_object()
generalSelect.click_input()

selectImportTypeOKButton = app['AquaChem (x86) [Test Project Basic Template]'].child_window(title= 'OK', auto_id='buttonOK', control_type='Button').wrapper_object()
selectImportTypeOKButton.click_input()

### Click on Select File #####

selectImportFileName = app['AquaChem (x86) [Test Project Basic Template]'].child_window(title= "", auto_id='buttonBrowse', control_type='Button').wrapper_object()
if selectImportFileName.is_visible() and selectImportFileName.is_enabled():
    selectImportFileName.click_input()
#time.sleep(5)

stationsSelecting = app['AquaChem (x86) [Test Project Basic Template]'].child_window(title= 'Stations.xlsx', auto_id='0', control_type='ListItem').wrapper_object()
if stationsSelecting.is_visible() and stationsSelecting.is_enabled():
    stationsSelecting.double_click_input()
#time.sleep(5)

buttonNextClick = app['AquaChem (x86) [Test Project Basic Template]'].child_window(title= 'Next >>', auto_id='buttonNext', control_type='Button').wrapper_object()
buttonNextClick.click()

### Description Click ###

descriptionClick = app['AquaChem (x86) [Test Project Basic Template]'].child_window(title= 'Description', auto_id='[Node] 0', control_type='DataItem').wrapper_object()
if descriptionClick.is_visible() and descriptionClick.is_enabled():
    descriptionClick.double_click_input()
#time.sleep(5)

### Select Station Check box ###

stationCheckBox = app['AquaChem (x86) [Test Project Basic Template]'].child_window(title= 'Station', auto_id='[Node] 0, [Node] 0', control_type='DataItem').wrapper_object()
#stationCheckBox.send_keys("{SPACE}")
#stationCheckBox.CheckBox() AttributeError: 'ListItemWrapper' object has no attribute 'CheckBox'
#stationCheckBox.toggle()  AttributeError: 'ListItemWrapper' object has no attribute 'toggle'
#stationCheckBox.checkbox.click() #AttributeError: 'ListItemWrapper' object has no attribute 'checkbox'
#stationCheckBox.Options.type_keys('{DOWN 0}') AttributeError: 'ListItemWrapper' object has no attribute 'Options'. Did you mean: 'actions'?
#stationCheckBox.actions.type_keys('{DOWN 0}') AttributeError: '_StandardLogger' object has no attribute 'type_keys'
#stationCheckBox.click_input()
#stationCheckBox.set_focus()
#time.sleep(5)