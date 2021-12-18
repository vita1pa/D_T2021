import json
import os.path

import requests

class DropboxApp():

	def __init__(self):

		self.oauth_key = 'sl.A-azIKCRPY7ZiVq-zh_sdPbDosHXD-1Gnbbk68ZAEG227IYwmYbOlIm0g7CO1H2NDS52Bup6rlPhCqDwQx3vXiQOHcyY8WvNgQTwxe0XNf0or4Ud5ec-qLs_9toHbomnfUq061DH'
		self.last_responses = dict()


	def uploadFile(self, file):

		request = requests.post("https://content.dropboxapi.com/2/files/upload",
					headers={
						"Dropbox-API-Arg": "{\"path\": \"/" + file + "\",\"mode\": \"add\",\"autorename\": true,\"mute\": false,\"strict_conflict\": false}",
						"Content-Type":"application/octet-stream",
						"Authorization":"Bearer "+self.oauth_key
					},
					data=open(file, 'rb').read()
		    	)
		request_json = request.json()
		request_json['Success'] = request.ok


		return self.last_responses.update({os.path.abspath(file) : request_json
			}
		)

	def getFileMetaData(self, file):

		request = requests.post("https://api.dropboxapi.com/2/sharing/get_file_metadata",
					headers={
						"Content-Type":"application/json",
						"Authorization":"Bearer "+self.oauth_key
					},
					data="{\r\n    \"file\": \""
						+self.getFileId(file)
						+ "\",\r\n    \"actions\": []\r\n}"
	    		)
		request_json = request.json()
		request_json['Success'] = request.ok

		return self.last_responses.update({os.path.abspath(file): request_json
	   })

	def deleteFile(self, file):

		request = requests.post("https://api.dropboxapi.com/2/files/delete_v2",
					headers={
						"Content-Type":"application/json",
						"Authorization":"Bearer "+self.oauth_key
					},
					data="{\r\n    \"path\": \"/" + file + "\"\r\n}"
	    		)
		request_json = request.json()
		request_json['Success'] = request.ok

		return self.last_responses.update({os.path.abspath(file): request_json
	    })

	def getList(self, path):

		request = requests.post("https://api.dropboxapi.com/2/files/list_folder",
			headers={
				"Content-Type":"application/json",
				"Authorization":"Bearer "+self.oauth_key
			},
			data="{\r\n    \"path\": \"" + path +"\",\r\n    \"recursive\": false,\r\n    \"include_media_info\": false,\r\n    \"include_deleted\": false,\r\n    \"include_has_explicit_shared_members\": false,\r\n    \"include_mounted_folders\": true,\r\n    \"include_non_downloadable_files\": true\r\n}"
	    )

		request_json = request.json()
		request_json['Success'] = request.ok

		return request_json

	def getFileId(self, file):

		return self.last_responses.get(os.path.abspath(file))['id']

	def getLastResponse(self, file):

		return self.last_responses.get(os.path.abspath(file))



