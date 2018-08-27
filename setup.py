from setuptools import setup, find_packages
setup(
    name = 'youtube-download',
    version = '1.0',
    packages = find_packages(),
    scripts = ['download-youtbe.py'],
    install_requires = ['Click','youtube-dl'],
    author = 'Jenish'
)
