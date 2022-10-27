# -*- coding: utf-8 -*-
"""
Created on Wed Oct 26 13:54:19 2022

@author: jshaffer
"""

import Assignment_6 as BA

def list_equal(list1, list2):
    
    for item in list1:
        if not item in list2:
            return False
    for item in list2:
        if not item in list1:
            return False
    return True


def test_problem_1():
    
    dna = ['cctcttacccaaggggtaccgaggagcataccctttcagaaagtgggatg',
     'cagtaagaagggtaatcaactaagagaatctgcaacaaggttcaggtatg',
     'tccgatctttctgacggaaccatcgggacacaagggtacattaaactatg',
     'ttaccggcaatcaatttatcaactcatgacgattctcagaaaggggccgg',
     'gtttgaggggatgcctttataacgggttgtctccacgttgcgaactgtgc',
     'aggatactagaaggctgcaaaagtgccccttcagcaccccgggatatgca',
     'ctcatcttgtaggacaacaggtggagcccgcgtcgcgtagtacaagagcg',
     'aaacgagatggggaccagtcgatcagtccaggcaggctaatgaagggagt',
     'gcccgagttatagggggtgggtggctcttcaccgagggcgggctcgagat',
     'tagtctggaagaagaggaccagtgcccgggacatgctcttcagagttgta']
    
    
    assert BA.median_string(dna, 8) == 'agaagggg'
    
def test_problem_2():
        
     
    dna = ['cctcttacccaaggggtaccgaggagcataccctttcagaaagtgggatg',
     'cagtaagaagggtaatcaactaagagaatctgcaacaaggttcaggtatg',
     'tccgatctttctgacggaaccatcgggacacaagggtacattaaactatg',
     'ttaccggcaatcaatttatcaactcatgacgattctcagaaaggggccgg',
     'gtttgaggggatgcctttataacgggttgtctccacgttgcgaactgtgc',
     'aggatactagaaggctgcaaaagtgccccttcagcaccccgggatatgca',
     'ctcatcttgtaggacaacaggtggagcccgcgtcgcgtagtacaagagcg',
     'aaacgagatggggaccagtcgatcagtccaggcaggctaatgaagggagt',
     'gcccgagttatagggggtgggtggctcttcaccgagggcgggctcgagat',
     'tagtctggaagaagaggaccagtgcccgggacatgctcttcagagttgta']
    
    assert list_equal(BA.greedy_motif_search(dna, 8 , 10), ['ccaagggg', 'agaagggt', 'acaagggt','agaaaggg','ataacggg','agaaggct','acaacagg','agatgggg','ataggggg','agaagagg'])
        
def test_problem_3():
            
    
    dna = ['cctcttacccaaggggtaccgaggagcataccctttcagaaagtgggatg',
     'cagtaagaagggtaatcaactaagagaatctgcaacaaggttcaggtatg',
     'tccgatctttctgacggaaccatcgggacacaagggtacattaaactatg',
     'ttaccggcaatcaatttatcaactcatgacgattctcagaaaggggccgg',
     'gtttgaggggatgcctttataacgggttgtctccacgttgcgaactgtgc',
     'aggatactagaaggctgcaaaagtgccccttcagcaccccgggatatgca',
     'ctcatcttgtaggacaacaggtggagcccgcgtcgcgtagtacaagagcg',
     'aaacgagatggggaccagtcgatcagtccaggcaggctaatgaagggagt',
     'gcccgagttatagggggtgggtggctcttcaccgagggcgggctcgagat',
     'tagtctggaagaagaggaccagtgcccgggacatgctcttcagagttgta']
    
    result = BA.randomized_motif_search(dna, 8)
    
    assert (len(result) == 10 and BA.hamming_distance('aaaagggg', BA.consensus(result)) <= 8)
            
def test_problem_4():
      dna = ['cctcttacccaaggggtaccgaggagcataccctttcagaaagtgggatg',
       'cagtaagaagggtaatcaactaagagaatctgcaacaaggttcaggtatg',
       'tccgatctttctgacggaaccatcgggacacaagggtacattaaactatg',
       'ttaccggcaatcaatttatcaactcatgacgattctcagaaaggggccgg',
       'gtttgaggggatgcctttataacgggttgtctccacgttgcgaactgtgc',
       'aggatactagaaggctgcaaaagtgccccttcagcaccccgggatatgca',
       'ctcatcttgtaggacaacaggtggagcccgcgtcgcgtagtacaagagcg',
       'aaacgagatggggaccagtcgatcagtccaggcaggctaatgaagggagt',
       'gcccgagttatagggggtgggtggctcttcaccgagggcgggctcgagat',
       'tagtctggaagaagaggaccagtgcccgggacatgctcttcagagttgta']   
    
    
      result = BA.gibbs_sampler(dna, 8, 100)
    
      assert (len(result) == 10 and BA.hamming_distance('aaaagggg', BA.consensus(result)) <= 8)