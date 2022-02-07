import platform
import urllib.request
import zipfile
import shutil
import os

import version_check

def install_release(release: dict):

	print('Fetching download url...')
	download_url = ''
	for i in release['assets']:
		if platform.system() == 'Windows' and 'windows' in i['name']:
			download_url = i['browser_download_url']
		elif platform.system() == 'Linux' and 'linux' in i['name']:
			download_url = i['browser_download_url']
		elif platform.system() == 'Darwin' and 'macosx' in i['name']:
			download_url = i['browser_download_url']
	if download_url == '':
		print('Something went wrong, could not find the download url for your system.')
		exit(1)
	print('Got it!')

	print('Downloading ' + download_url)
	download = urllib.request.urlopen(download_url)
	open('download.zip','wb').write(download.read())
	print('Download success')

	print('Extracting...')
	zipfile.ZipFile('download.zip', 'r').extractall('download')
	print('Successfully extracted')

	print('Cleaning up...')
	try:
		os.rename('premake5.exe', 'premake5-old.exe')
	except:
		pass
	shutil.copyfile('download/premake5.exe', 'premake5.exe')
	shutil.rmtree('download')
	os.remove('download.zip')
	print('All done!')

	update_check = version_check.check_for_update()
	if update_check[0]:
		print('Successfully updated Premake to ' + update_check[2])
		os.popen('python plus_plus/update/remove_old_version.py')
	else:
		print('Something went wrong!')
		print('Expected version: ' + update_check[3])
		print('Newly installed vestion: ' + update_check[4])