# LushaSite
Welcome to Jony and Oren in Lusha site

# Pre-Installation pip
Before you begin please install the requirements file with:

```
pip3 install -r bin/requirements.txt
``` 

# Pre-Installation selenium
now let's install the selenium drivers file with:

```
sudo ./core_infra/drivers/install.sh
``` 

# Running the tests
From the Main directory in the command line please run: 
```
pytest --alluredir=allure-results lusha_test.py
```

# viewing the resuls in allure
From the Main directory in the command line please run:
```
allure serve
```
