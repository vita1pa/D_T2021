from behave import *
import os

from app.DropboxApp import DropboxApp
#


FILES = 'files/'
app = DropboxApp()
last_request = None

@Given('I have a file "{name}"')
def exists(context, name):

	assert os.path.isfile(FILES+name), "EXISTING: File " + name + " does not exist"

@When('I upload file "{name}" to Dropbox')
def uploadToDropbox(context, name):
	global lastRequest
	lastRequest = app.uploadFile(FILES+name);


@Then('I see file "{name}" successfully uploaded')
def isSuccessfullyUploaded(context, name):

	assert app.getLastResponse(FILES+name)['Success'], "UPLOAD FILE: Failed to upload file "+name + " to Dropbox"


@given('I have an uploaded file "{name}"')
def isUploadedBefore(context, name):
	# print(app.getLastResponse(FILES+name))
	assert app.getLastResponse(FILES+name) and app.getLastResponse(FILES+name)['Success'], "IS FILE UPLOADED: \ "  \
		"File " + name + " is not uploaded"


@when('I request metadata of file "{name}" by its id')
def requestFileMetadata(context, name):
	global lastRequest
	lastRequest = app.getFileMetaData(FILES+name)


@then('I receive metadata for file "{name}"')
def isMetadataReceived(context, name):
	assert app.getLastResponse(FILES + name)['Success'],	\
		"RECEIVE FILE METADATA: Failed to get metadata for file " + name


@when('I ask to delete file "{name}"')
def deleteFile(context, name):
	global lastRequest
	lastRequest = app.deleteFile(FILES + name)


@then('I see file "{name}" is successfully deleted')
def isDeletedSuccessfully(context, name):

	assert app.getLastResponse(FILES + name)['Success'], "DELETE FILE: Failed to delete file " + name


@when('I ask for list of files and folders in "{path}"')
def requestForList(context, path):
	global lastRequest
	lastRequest = app.getList(path)


@then("I receive list of files and folders")
def isListReceived(context):

	assert lastRequest['Success'], "RECEIVE LIST: Given wrong path"