# -*- coding: utf-8 -*-
"""
Created on Sat May 18 16:08:24 2019

@author: Pai
"""
import config as cf


import json
import pandas as pd

pd.set_option('display.max_columns', None)


class SkuReco():          
    
    def __init__(self, data_source):

        self._df_weight = pd.Series(cf.WEIGHT)
        self._df = self._load_source(data_source)

    def get_reco(self, sku):
        main_sku_attr = self._sku_get_attr(sku)
        match_search = self._match_search(main_sku_attr)
        
        match_search_count = self._match_search_count(match_search)
        alphabetical_score = self._alphabetical_score(match_search)
        
        return self._add_ranking_data(self._df,
                                   match_search_count,
                                   alphabetical_score
                                   )

    def _add_ranking_data(self, df_main,
                    df_match_count,
                    df_alphabetical_rank
                    ):
        
        df_rank = pd.concat([df_main, df_match_count], axis=1, sort=False)
        df_rank = pd.concat([df_rank, df_alphabetical_rank], axis=1, sort=False)
        return df_rank
        #return df_rank.sort_values(['rank','alphabetical_score'],ascending=False).head(top_n)
       
    def _load_source(self,path):
        """
        input path : json file dir
        return : dataframe
        """
        with open(path) as json_file:  
            skus = json.load(json_file)
        return pd.DataFrame(skus).T
    
    def _sku_get_attr(self, sku):
        """
        filter for the selected sku and return a the list of its attributes
        """
        sku_input = self._df[self._df.index==sku]
        return sku_input.values[0] #convert into a python list
        
    def _match_search(self, sku_attr_list):
        """
        input as a list of sku's attributes
        """
        return self._df.isin(sku_attr_list)
    
    def _match_search_count(self, df_match_search):
        """
        input from _match_search()
        to count the number of attributes matched
        """
        df_match_count = df_match_search.apply(sum,axis=1).sort_values(ascending=False)
        return pd.DataFrame(df_match_count, columns=['rank'])
    
    def _alphabetical_score(self, df_match_search):
        df = df_match_search*self._df_weight
        df = df.apply(sum, axis=1)
        return pd.DataFrame(df, columns=['alphabetical_score'])
    
