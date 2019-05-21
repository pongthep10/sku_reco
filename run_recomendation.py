# -*- coding: utf-8 -*-
"""
Created on Mon May 20 14:22:56 2019

@author: Pai
"""
from recsys.recsys import SkuReco as sr
import os

current_path = os.path.dirname(os.path.realpath(__file__))

#load sku data
sku_data=sr(os.path.join(current_path,'data_source/reco-sku-test-data.json'))



while True:

    
    #return all the list of recommended sku
    try:
        SKU = input("What is the SKU name? ")
        TOP_N = input("How many recommended SKU? (1-20) ")
        if SKU == 'exit' or TOP_N == 'exit':
            break
        if int(TOP_N) < 1 or int(TOP_N) > 20:
            print("The number of SKU output out of bound")
            continue
        get_rec_sku = sku_data.get_reco(SKU)
        
    except Exception as e:
        print(str(e))
        continue
    
    
    
    try:
        #rethrive the input sku
        input_sku = get_rec_sku.loc[get_rec_sku.index == SKU]

        
        #filter for only top n list
        result = get_rec_sku.loc[get_rec_sku.index != SKU].sort_values\
                    (['rank','alphabetical_score'],\
                    ascending=False).head(int(TOP_N))
                    
        print("Selected SKU and attributes: ")
        #print only first 10 col of attributes
        print(input_sku[input_sku.columns[:10]])
        print("\n Recommended SKU: ")
        print(result)
    except Exception as e:
        print(str(e))
        continue