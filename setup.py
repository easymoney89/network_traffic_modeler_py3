
from setuptools import setup, find_packages

with open("requirements.txt", "r") as fs:
    reqs = [r for r in fs.read().splitlines() if (
        len(r) > 0 and not r.startswith("#"))]

version = '1.0'

setup(
    name='pyNTM',
    version=version,
    py_modules=['pyNTM'],
    packages=find_packages(),
    install_requires=reqs,
    include_package_data=True,
    description='Network traffic modeler API written in Python 3',
    author='Tim Fiola',
    author_email='timothy.fiola@gmail.com',
    url='https://github.com/tim-fiola/network_traffic_modeler_py3',
    download_url='https://github.com/tim-fiola/network_traffic_modeler_py3/tarball/%s' % version,
    keywords=['networking', 'layer3', 'failover', 'modeling', 'model'],
    classifiers=[],
)
