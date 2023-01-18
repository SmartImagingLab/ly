# 1.先给一组初始参数
# 2.要有个循环，循环里边改参数
import os
from SkyCall import Skymaker
from skymaker import getlist

if __name__ == '__main__':
	dir_path = "./"

	Sky = Skymaker()

	# nums为参数修改次数
	nums = 2

	for i in range(nums):
		list_name = "%d.list" % i
		file = os.path.join(dir_path, list_name)
		print(list_name, file)
		list_file = getlist(file)
		config = {
			"IMAGE_NAME": str(i)+".fits",
			'MAG_ZEROPOINT': 20,
			'SEEING_FWHM': 0.7}
		Sky.run(file, config)
