from setuptools import setup, find_packages

setup(
    name='my_project',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'gymnasium',
        'stable-baselines3',
        'numpy',
        'pybullet',
        'gym-pybullet-drones',
    ],
)
