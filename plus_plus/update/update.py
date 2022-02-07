from install_release import install_release
import version_check

update_check = version_check.check_for_update()
if update_check[0]:
	print('All up-to-date! You have version ' + update_check[3])
else:
	print('Newer version found: ' + update_check[2])
	install_release(update_check[1])