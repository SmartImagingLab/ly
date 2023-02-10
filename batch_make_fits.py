# 1.先给一组初始参数
# 2.要有个循环，循环里边改参数
import os
import random
from SkyCall import Skymaker
from skymaker import getlist

if __name__ == '__main__':
	dir_path = "./images"

	Sky = Skymaker()

	# nums为参数修改次数
	nums = 10
	for i in range(nums):
		list_name = "%d.list" % i
		SEEING_FWHM = random.uniform(0.5, 1)
		READOUT_NOISE = random.uniform(0, 4)
		file = os.path.join(dir_path, list_name)
		print(list_name, file)
		list_file = getlist(file)
		config = {

			"IMAGE_NAME": str(i)+".fits",
			'SEEING_FWHM': SEEING_FWHM,
			'READOUT_NOISE': READOUT_NOISE,

		}
		Sky.run(file, config)
