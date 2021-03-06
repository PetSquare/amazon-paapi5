import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name='amazon-paapi5',
    version='1.1.2',
    author='Celine Bursztein'    ,
    description='Amazon Product Advertising API 5.0 wrapper for Python',
    long_description=long_description,
    long_description_content_type='text/markdown',
    license='GPL-3.0',
    packages=setuptools.find_packages(),
    install_requires=['amightygirl.paapi5-python-sdk'],
    classifiers=[
        'Programming Language :: Python',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: OS Independent',
    ],
    python_requires='>=2.7',
)
