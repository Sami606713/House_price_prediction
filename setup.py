from setuptools import setup, find_packages
from typing import List
HIFEN="-e ."
def get_packages(file_path:str)->List[str]:
    """
    This will return a list of functions
    """
    pckages=[]
    with open(file_path) as f:
        packages=f.readlines()
        # remove the escape squence char("\n")
        packages=[pkg.strip() for pkg in packages]
        if(HIFEN in packages):
            packages.remove(HIFEN)
    return packages

# Set up 
setup(
    name="US House Price Prediction",
    version="3.12.0",
    author='Samiullah',
    author_email='sami606713@gmail.com',
    description='Build a end to end project on house price prediction with complete dash-board and webapp',
    url='https://github.com/Sami606713/House_price_prediction.git',
    packages=find_packages(),
    install_requires=get_packages("requirements.txt")

)
