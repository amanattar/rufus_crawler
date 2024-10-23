from setuptools import setup, find_packages

setup(
    name="rufus",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "beautifulsoup4",
        "openai",
        "selenium",
        "requests",
        "webdriver-manager",
    ],
    entry_points={
        'console_scripts': [
            'run_rufus=scripts.run_rufus:main',  # Allow `run_rufus` as a command-line script
        ],
    },
)
