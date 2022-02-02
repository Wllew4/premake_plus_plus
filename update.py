import urllib.request
import urllib.parse
import json
import subprocess
import zipfile
import shutil
import os

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

# print(latest_version_tag)
# print(current_version_tag)

if latest_version_tag == current_version_tag:
	print('All up-to-date!')
else:
	print('Newer version found: ' + latest_version_tag)
	download_url = ''
	for i in latest['assets']:
		if 'windows' in i['name']:
			download_url = i['browser_download_url']
	if download_url != '':
		print('Downloading ' + download_url)
		download = urllib.request.urlopen(download_url)
		open('download.zip','wb').write(download.read())
		zipfile.ZipFile('download.zip', 'r').extractall('download')
		shutil.copyfile('download/premake5.exe', 'premake5.exe')
		shutil.rmtree('download')
		os.remove('download.zip')
	else:
		print('Could not find windows download')