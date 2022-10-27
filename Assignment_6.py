# -*- coding: utf-8 -*-
"""
Created on Wed Oct 26 13:53:36 2022

@author: jshaffer
"""


#Note that adding additional imported packages will result in the autograder to fail. pytest in your own terminal may still work.
import random
import numpy as np
import itertools

"""
Function for randomly mutating a sequence at d locations - use this to help you test your code
"""
def mutate_sequence(seq, d):
    bases = ['a', 't', 'c', 'g']
    p = random.sample(list(range(0,len(seq))), d)
    
    out = list(seq)
    
    for i in p:
        temp = [x for x in bases if x != out[i]]
        out[i] = random.choice(temp)
        
    
    return ''.join(out)

"""
Function for generating a set of n sequences of length k that include a given motif with at most d mutations - use this to help you test your code
"""
def generate_mutated_motif_samples(motif, n, k, d):
    out = []
    bases = ['a', 't', 'c', 'g']
      
    for i in range(n):
        random_seq = random.choices(bases, k=k)
        
        p = random.randint(0,k-len(motif))
        random_seq[p:p+len(motif)] = list(mutate_sequence(motif, d))
        
        out.append(''.join(random_seq))
    
    return out

"""
Function for getting all k-mers
"""
def get_all_kmers(k):
    bases = ['a', 'c', 'g', 't']
    return [''.join(p) for p in itertools.product(bases, repeat=k)]

"""
Function for calculating the Hamming distance between two sequences
"""
def hamming_distance(seq_a, seq_b):
    #Check that the lengths are the same - Hamming distance only works for equal length strings
    if len(seq_a) != len(seq_b):
        return None
    
    #Initialize distance to 0
    distance = 0
    
    #Count the number of letter mismatches that are present between the strings
    for a,b in zip(seq_a, seq_b):
        if a != b:
            distance += 1
    
    return distance

"""
Utility function for getting the consensus string for a given list of motifs
"""
def consensus(motifs):
    cts = counts(motifs)
    consensus = []
    for i in range(len(motifs[0])):
        max_count = max([cts[x][i] for x in cts.keys()])
        #print(max_count)
        for b in cts.keys():
            #print(cts[b])
            if cts[b][i] == max_count:
                consensus.append(b)
                break
        
    return ''.join(consensus)
#%%

def d(pattern, motifs):
   return 0


def median_string(dna, k):
    return 0


#%%

def counts(motifs):
    return 0

def profile(motifs):
    return 0

def score(motifs):
    return 0

def pr(motif, profile):
    return 0

def most_probable_kmer(text,k, profile):
    
   return 0


def greedy_motif_search(dna, k):
    
   return 0
#%%


def get_most_probable_motifs(dna,k, profile):
    
    return 0

def randomized_motif_search(dna, k):
    
    return 0


#%%

def get_profile_random_kmer(text, k, profile):
    
    return 0

def gibbs_sampler(dna, k , n):
    
    return 0