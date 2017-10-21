try:
	from setuptools import setup
except ImportError:
	from distutils.core import setup
	
config = {
	'description':'Firstproject',
	'author':'sunao',
	'url':'URL to get it at.',
	'download_url':'Where to download it.',
	'author_email':'402920965@qq.com',
	'version':'0.1',
	'install_requires':['nose'],
	'packages':['firstpackage'],
	'scripts':[],
	'name':'firstpackage'
	}
	
setup(**config)