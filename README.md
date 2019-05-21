# SKU Reccomendation Engine


### Prerquisite
- Python version 3.6+ 
- Pip (comes with Python)
- Download all the codes and save it to your local directory

### Installation Guide
1. Install package "pandas" with **pip**
> pip install pandas

or install with pip from requirements.txt
> pip install -r /path/to/requirements.txt

2. Go to the location where the scripts located
> cd /path/to/script/folder

### Execution

1. Run the Python script run_recomendation.py

>  python run_recomendation.py

![alt text](https://github.com/pongthep10/sku_reco/blob/master/img/1.png)

2. The prompt text is showed asking **What is the SKU name?**. We need to put the answer in the format of "sku-{number}". In this example we have input sku-1

> sku-1

3. After that the second prompt text asking **"How many recommended SKU? (1-20)"**. We have to input the number between 1-20. In this example we have input 3

> 3

4. Now the result is returned


## SKU data Changes
This project comes with sample data in json format. It's located in the folder **data_source**. 

To change the data source, edit the file **run_recomendation.py** in line 13.

> 13 > sku_data=sr(os.path.join(current_path,'data_source/reco-sku-test-data.json'))


## Attribute Weight Configuration 
The SKU attributes are weighed in alphabetical order which is configured in the config.py and to change this, editing the file and adjust the weight for each attribute (larger number has higher priority)

This approach is similar to the CSS Specificity which we can specify weight for priority in making order.


>            'att-a': 1000000000,
>            'att-b': 100000000,
>            'att-c': 10000000,
>            'att-d': 1000000,
>            'att-e': 100000,
>            'att-f': 10000,
>            'att-g': 1000,
>            'att-h': 100,
>            'att-i': 10,
>            'att-j': 1 }


