""" 
================================================
          Advanced Dictionary
================================================

Topic Covered"
 1. Frequecy Count
 2. First Non-repeating
 3. Group Problem
 
 Author: Mohammad Faizan
 Date: 23/03/2026
 
 """
 
from typing import List, Dict
 
 #=================================================
 # Frequency Count
 #=================================================

def freq_count(text: str)-> Dict[str, int]:
    """ return frequency of each character in string """
    
    freq = {}
    
    for ch in text:
        freq[ch] = freq.get(ch, 0) + 1
        
    return freq
 
#============================================================
#  2. First Non Repeating 
#============================================================

def first_non_repeating(role: str)-> str | None:
    """ return first non repeating character """
    
    
    freq = {}
    
    for ch in role:
        freq[ch] = freq.get(ch, 0) + 1
    for ch in role:
        if freq[ch] == 1:
            return ch
           
    return None

#=====================================================================
# 3. Group Anagram
#=====================================================================

def group_anagrams(words: List[str])-> List[List[str]]:
    """ group words that are  anagam """
    
    group = {}
    
    for word in words:
        freq = [0] * 26
        for ch in word:
            freq[ord(ch) - ord('a')] +=1
            
        key = tuple(freq)
        group.setdefault(key, []).append(word)
            
    return list(group.values())

#==================================================================          
# Main Guard
#==================================================================

if __name__ == "__main__":
    
    print("\n==========TESTING=========")
    
    # Frequency Count 
    text = "backenddeveloper"
    print("\nInput ->", text)
    print("Frequency Count: ",freq_count(text))
    
    # First Non Repeating 
    role = "pythondeveloper"
    print("\nInput ->", role)
    print("First Non Repeating Character ->",first_non_repeating(role))
    
    # Group Anagram
    words = ["eat", "tea", "ate", "tan", "nat", "bat", "cat", "tab"]
    print("\nInput ->",words)
    
    result = group_anagrams(words)
    
    print("Group Anagram")
    for group in result:
        print(group)
    
   