import pandas as pd
import numpy as np
import sys
import os
import math
from pprint import pprint


class Skymaker(object):
	'''[summary]
	
	[description]
	'''
	def __init__(self, **kwargs):
		# super(Skymaker, self).__init__()
		super(Skymaker, self).__init__()
		# self.sexPath = './image.list'
		self.base_dir = "./"
		self.config_name = "sky.conf"
		self.configFile = os.path.join(self.base_dir, self.config_name)

		self.config = self.read_configue

	# @property
	def read_configue(self, configue_context):
		'''[读skymaker配置文件(*.sex)参数信息并转为Dataframe]
		
		[description]
		
		Returns:
			[Dataframe] -- [Dataframe的shape：（配置文件行数，3）
							第一列'line'：对应.sex文件的行号，
							第二列'param'：为参数keyworld
							第三列'value'：为参数取值]
		'''
		conf_list = []

		for index, line in enumerate(configue_context):
			if len(line) < 10 or line[0] == '#' or line.split()[0] == '#':
				pass
			else:
				info = line.split('#')[0].split()
				conf_dict = {}
				# print(line.split('#')[0].split())
				conf_dict['line'] = index
				conf_dict['param'] = info[0]
				conf_dict['value'] = ''.join(info[1:])
				conf_list.append(conf_dict)
		# pprint(conf_list)
		return pd.DataFrame(conf_list, columns=['line', 'param', 'value'])

	def cat_keyworld(self, configue_context, keyworld):
		'''[查看指定参数的信息]
		
		[description]
		
		Arguments:
			keyworld {[str]} -- [参数关键字]
		
		Returns:
			[list] -- [指定参数的信息['line', 'param', 'value']]
		'''
		df = self.read_configue(configue_context)
		infor = df[df.param == keyworld].values.tolist()
		# print(infor)
		return infor

	def set_configue_add_lock(self, config, output_file):
		'''[设置参数]
		
		[description]
		
		Arguments:
			keys {[list]} -- [需修改的参数关键字列表]
			values {[list]} -- [对应的修改的参数取值]
		'''
		with open(self.configFile, 'r') as f:
			context = f.readlines()

		for key, value in config.items():
			line = self.cat_keyworld(context, key)[0][0]
			# print('修改参数所在行', line)
			# print('切的结果', context[line].split('#', 1))
			info, annotation = context[line].split('#', 1)
			column1 = format(key, '<17')
			if len(str(value)) < 15:
				column2 = format(str(value), '<15')
			else:
				column2 = format(str(value), '<%d' % (len(str(value))+2))
			column3 = '#'+annotation
			context[line] = "{}{}{}".format(column1, column2, column3)
			# print('新行', context[line])
		# pprint(context)

		with open(output_file, 'w') as f:
			# fcntl.flock(f, fcntl.LOCK_EX)
			f.write(''.join(context))
			# fcntl.flock(f, fcntl.LOCK_UN)
		
	def call_sky(self, new_config_file, file):
		'''调用skymaker'''
		# 加异常处理
		# os.system('echo %s | sudo -S %s' % (self.password, 'sextractor -c ' + self.configFile + self.file_path))
		os.system('sky %s -c %s' % (file, new_config_file))

	def catalog_file_create(self, file, catalog_set):
		# 创建SExtractor输出文件
		name = os.path.basename(file).split(".list")[0]
		output_file = os.path.join(self.base_dir, 'c'+name+".conf")
		print('########', output_file)
		# catalog_set = {"IMAGE_NAME": name+".fits"}
		self.set_configue_add_lock(catalog_set, output_file)
		return output_file

	def catalog_file_remove(self, file):
		# 删除SExtractor输出文件
		os.remove(file)

	def run(self, file, configs):
		'''提取image.sex文件的坐标和列信息'''
		config_file = self.catalog_file_create(file, configs)
		# self.set_configue_add_lock(configs, config_file)

		try:
			self.call_sky(config_file, file)
		except AttributeError:
			print("Call skymaker Error!")

		# os.remove(config_file)
