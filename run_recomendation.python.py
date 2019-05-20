# -*- coding: utf-8 -*-
"""
Created on Mon May 20 14:22:56 2019

@author: Pai
"""
from recsys.recsys import SkuReco as sr

#load sku data
sku_data=sr('data_source/reco-sku-test-data.json')



while True:

    
    #return all the list of recommended sku
    try:
        SKU = raw_input("What is the SKU name? ")
        TOP_N = raw_input("How manyrecommended SKU? ")
        if SKU == 'exit' or TOP_N == 'exit':
            break
        get_rec_sku = sku_data.get_reco(SKU)
        
    except Exception as e:
        print type(e).__name__#, e.args
        continue
    #rethrive the input sku
    input_sku = get_rec_sku.loc[aa.index == SKU]
    print "Selected SKU and attributes: "
    print input_sku
    
    #filter for only top n list
    result = get_rec_sku.loc[aa.index != SKU].sort_values\
                (['rank','alphabetical_score'],\
                ascending=False).head(int(TOP_N))
    print "\n Recommended SKU: "
    print result