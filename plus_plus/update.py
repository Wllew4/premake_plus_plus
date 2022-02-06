import urllib.request
import urllib.parse
import json
import subprocess
import zipfile
import shutil
import os
import platform

def get_latest_version() -> dict:
	url = 'https://api.github.com/repos/premake/premake-core/releases'
	f = urllib.request.urlopen(url)
	releases = json.loads(f.read().decode('utf-8'))
	return releases[0]

def get_currently_installed_version() -> str:
	try:
		result = subprocess.run(['premake5', '--version'], stdout=subprocess.PIPE).stdout.decode('utf-8')
		return result[str.rindex(result, ')')+2:-2]
	except:
		return ''

latest = get_latest_version()

latest_version_tag = latest['tag_name'][1:]
current_version_tag = get_currently_installed_version()

if latest_version_tag == current_version_tag:
	print('All up-to-date! ' + current_version_tag)

else:
	print('Newer version found: ' + latest_version_tag)

	print('Fetching download url...')
	download_url = ''
	for i in latest['assets']:
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

	newly_installed_version_tag = get_currently_installed_version()
	if newly_installed_version_tag == latest_version_tag:
		print('Successfully updated premake to ' + latest_version_tag)
		os.popen('python plus_plus/remove_old_version.py')
	else:
		print('Something went wrong!')
		print('Expected version: ' + latest_version_tag)
		print('Newly installed vestion: ' + newly_installed_version_tag)