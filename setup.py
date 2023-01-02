import setuptools

install_requires = open('requirements.txt').read().splitlines()

setuptools.setup(
    name="g8",
    version="1.0",
    packages=setuptools.find_packages(),
    install_requires=install_requires,
    entry_points={
        'console_scripts': [
            'g8 = src.g8:g8.main',
        ],
    },
    include_package_data=True,
)
