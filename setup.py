from setuptools import setup


def readme():
    with open("README.md", "r") as fh:
        long_description = fh.read()
        return long_description


setup(
    name='ANCIENT_INVASION',
    version='1',
    packages=['ANCIENT_INVASION'],
    url='https://github.com/NativeApkDev/ANCIENT_INVASION',
    license='MIT',
    author='NativeApkDev',
    author_email='nativeapkdev2021@gmail.com',
    description='This package contains implementation of the offline turn-based strategy RPG '
                '"ANCIENT_INVASION" on command line interface.',
    long_description=readme(),
    long_description_content_type="text/markdown",
    include_package_data=True,
    install_requires=[],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7"
    ],
    entry_points={
        "console_scripts": [
            "ANCIENT_INVASION=ANCIENT_INVASION.ancient_invasion:main",
        ]
    }
)