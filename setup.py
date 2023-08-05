from setuptools import setup, find_packages 

setup(
name="hyperclip", 
version = "1.0.0", 
description="Hyperbolic CLIP", 
#package_dir={"":"blsc"}, 
#packages = find_packages(where="blsc"), 
packages = find_packages(exclude=["tests", "logs" ,  "docs", "data"]), 
python_requires=">=3.7, <4",
#url='https://github.com/Simon1V/Hyperclip',
entry_points={"console_scripts": ["hyperclip=hyperclip.main:main"]},
)
 