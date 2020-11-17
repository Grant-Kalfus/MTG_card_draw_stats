# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import random as rand
import csv
import pandas as pd
import matplotlib.pyplot as plt

#from collections import defaaultdict

class stat_gener():
    def __init__(self, deck_size=99, num_cards_of_interest=36):
        self.deck_size = deck_size
        self.num_cards_of_interest = num_cards_of_interest
        
        self.shuffle_cards()
        
        self.cards_of_interest_list = [c for c in range(0, num_cards_of_interest)]
        
    def shuffle_cards(self):
        self.deck_list = [c for c in range(0, self.deck_size)]
        rand.shuffle(self.deck_list)
        
    def draw_card(self):
        return self.deck_list.pop(0)
    
    def draw_and_check(self, draw_num = 7):
        hits = 0
        for i in range(0, draw_num):
            try:  
                if(self.draw_card() in self.cards_of_interest_list): hits += 1
            except IndexError:
                break
        return hits

    def gen_histogram(self, samples=1000, draw_num=7, message="Gen histogram", reshuffle=True, hist_percents=True):
        card_histogram = [0 for i in range(0, draw_num+1)]
        temp = 0
        downsampler = samples / 10
        
        for i in range(0, int(samples)):
            if(reshuffle): self.shuffle_cards()
            temp = self.draw_and_check(draw_num)
            card_histogram[temp] += 1
            
            if(i >= downsampler):
                print("%s, %i%% complete" % (message, i/samples * 100))
                downsampler += samples / 10
                
        print("%s, 100%% complete" % message)

        if(hist_percents):
            for i in range(0, draw_num+1):
                card_histogram[i] = round((card_histogram[i] / samples * 100), 2)
        
        return card_histogram;
                
            
if __name__ == "__main__":
    COI = 10
    
    
    test = stat_gener(deck_size = 99,
                      num_cards_of_interest = COI)
    total = 0

    data_dict = {}
    str_id = ""

    for i in range(0, 26):
        str_id = "%i_draws_at_COI_%i" % (i, COI)
        data_dict[str_id] = test.gen_histogram(samples=1e3, draw_num=i, message=str_id, hist_percents=True)
    
    #Need to make all lists the same size
    #for key in data_dict.items():
        
    
    
    #df = pd.DataFrame(data_dict)
    
    
    
    with open('output2.csv', 'w+') as output:
        writer = csv.writer(output)
        for key, value_list in data_dict.items():
            values = ",".join(str(x) for x in value_list)
            writer.writerow([key, values])
    
    
    
    
    
    
