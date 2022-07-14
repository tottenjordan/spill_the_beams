"""
    Setup for apache beam pipeline.
"""
import setuptools


NAME = 'create_tfrecords'
VERSION = '1.0'
REQUIRED_PACKAGES = [
    'apache-beam[gcp]==2.39.0',
    'tensorflow==2.9.*',
    'gcsfs==2022.5.0',
    # 'workflow'
    ]

setuptools.setup(
    name=NAME,
    version=VERSION,
    install_requires=REQUIRED_PACKAGES,
    packages=setuptools.find_packages(),
    include_package_data=True,
)
