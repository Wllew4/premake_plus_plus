import urllib.request
import json
import subprocess

def get_latest_release() -> dict:
	url = 'https://api.github.com/repos/premake/premake-core/releases'
	f = urllib.request.urlopen(url)
	releases = json.loads(f.read().decode('utf-8'))
	return releases[0]

def get_release_version_tag(release: dict) -> str:
	return release['tag_name'][1:]

def get_current_version() -> str:
	try:
		result = subprocess.run(['premake5', '--version'], stdout=subprocess.PIPE).stdout.decode('utf-8')
		return result[str.rindex(result, ')')+2:-2]
	except:
		return ''

def check_for_update() -> tuple[bool, dict, str, str]:
	latest_d = get_latest_release()
	latest_t = get_release_version_tag(latest_d)
	current_t = get_current_version()

	return (
		latest_t == current_t,
		latest_d,
		latest_t,
		current_t)