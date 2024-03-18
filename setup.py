from setuptools import setup, find_packages

setup(name='gym_safety',
      version='0.0.1',
      install_requires=['gym'],#And any other dependencies required
      packages=find_packages(),  # And any other packages required
)
