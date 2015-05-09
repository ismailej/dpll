import sys
import copy

#Sentence = ["and", ]
#sentence = ["and", "R", ["not", "B"], "W"]
#sentence = ["and", ["or", "P", ["not", "R"]], ["or", ["not", "Q"], ["not", "R"], "P"], ["not", "P"]]
#sentence = ["not", "p"]
#sentence = ["and", "p", ["not", "p"]]
#sentence = ["and", ["or", "p", "q"], ["or", ["not", "p"], "r"], ["or", ["not", "r"], ["not", "p"]], ["or", ["not", "q"], "s", ["not", "t"]], "t"]
#sentence = ["and", ["not", "p"], "p"]
#next is for backtracking
#sentence = ["and", ["or", ["not", "p"], "q"], ["or", ["not", "q"], ["not", "p"]], ["or", "p", ["not", "q"]]]
#sentence = ["not", "p"]

#sentence = ["and", ["or", "p", "q"], ["or", ["not", "p"], ["not", "q"]]]
#sentence = ["and", ["or", ["not", "p"], "q"], ["or", ["not", "q"], ["not", "p"]], ["or", "p", ["not", "q"]]]
#sentence = ["and", ["or", ["not", "p"], "q"], "p"] 
#sentence=["and",["or","a","b", "q"],["or",["not","a"],["not","b"], "p"],["or","p","q"],["or",["not","p"],["not","q"]]]
#sentence = ["and", "a", "a", "b"]
#sentence = ["and",["or","a","b","a"],["or","b","a"],["or","c","b",["not","d"]],["or","b","c","b",["not","d"]],"c","c"]
#sentence = "A"
#sentence = ['and', ['or', 'E', 'G', ['not', 'P'], 'K', 'J', ['not', 'H'], 'I', ['not', 'L'], ['not', 'A'], ['not', 'B'], ['not', 'C'], ['not', 'D'], ['not', 'F']], ['or', 'E', 'D', 'G', ['not', 'P'], 'K', ['not', 'H'], 'I', ['not', 'J'], ['not', 'L'], ['not', 'A'], ['not', 'B'], ['not', 'C'], ['not', 'F']], ['or', 'G', 'F', ['not', 'P'], 'J', ['not', 'H'], 'I', ['not', 'L'], ['not', 'A'], ['not', 'B'], ['not', 'C'], ['not', 'D'], ['not', 'E']], ['or', 'G', 'F', ['not', 'P'], 'J', ['not', 'H'], 'I', ['not', 'K'], ['not', 'L'], ['not', 'A'], ['not', 'B'], ['not', 'C'], ['not', 'D']], ['or', 'D', 'G', 'F', ['not', 'P'], ['not', 'H'], 'I', ['not', 'J'], ['not', 'L'], ['not', 'A'], ['not', 'B'], ['not', 'C'], ['not', 'E']], ['or', 'D', 'G', 'F', ['not', 'P'], ['not', 'H'], 'I', ['not', 'J'], ['not', 'K'], ['not', 'L'], ['not', 'A'], ['not', 'B'], ['not', 'C']], ['or', 'E', ['not', 'P'], 'K', 'J', 'L', 'I', ['not', 'A'], ['not', 'B'], ['not', 'C'], ['not', 'D'], ['not', 'F'], ['not', 'G']], ['or', 'E', ['not', 'P'], 'H', 'K', 'J', 'I', ['not', 'A'], ['not', 'B'], ['not', 'C'], ['not', 'D'], ['not', 'F'], ['not', 'G']], ['or', 'E', 'D', ['not', 'P'], 'K', 'L', 'I', ['not', 'J'], ['not', 'A'], ['not', 'B'], ['not', 'C'], ['not', 'F'], ['not', 'G']], ['or', 'E', 'D', ['not', 'P'], 'H', 'K', 'I', ['not', 'J'], ['not', 'A'], ['not', 'B'], ['not', 'C'], ['not', 'F'], ['not', 'G']], ['or', 'A', 'B', 'E', 'G', ['not', 'P'], 'K', 'J', ['not', 'H'], ['not', 'L'], ['not', 'C'], ['not', 'D'], ['not', 'F']], ['or', 'B', 'E', 'G', ['not', 'P'], 'K', 'J', ['not', 'H'], ['not', 'I'], ['not', 'L'], ['not', 'C'], ['not', 'D'], ['not', 'F']], ['or', 'A', 'B', 'E', 'D', 'G', ['not', 'P'], 'K', ['not', 'H'], ['not', 'J'], ['not', 'L'], ['not', 'C'], ['not', 'F']], ['or', 'B', 'E', 'D', 'G', ['not', 'P'], 'K', ['not', 'H'], ['not', 'I'], ['not', 'J'], ['not', 'L'], ['not', 'C'], ['not', 'F']], ['or', 'C', 'E', 'D', 'G', ['not', 'P'], 'K', 'J', ['not', 'H'], 'I', ['not', 'L'], ['not', 'A'], ['not', 'B'], ['not', 'F']], ['or', 'C', 'E', 'D', 'G', ['not', 'P'], 'K', ['not', 'H'], 'I', ['not', 'L'], ['not', 'A'], ['not', 'B'], ['not', 'D'], ['not', 'F']], ['or', 'C', 'E', 'G', ['not', 'P'], 'K', 'J', ['not', 'H'], 'I', ['not', 'J'], ['not', 'L'], ['not', 'A'], ['not', 'B'], ['not', 'F']], ['or', 'C', 'E', 'G', ['not', 'P'], 'K', ['not', 'H'], 'I', ['not', 'J'], ['not', 'L'], ['not', 'A'], ['not', 'B'], ['not', 'D'], ['not', 'F']], ['or', 'F', ['not', 'P'], 'J', 'L', 'I', ['not', 'A'], ['not', 'B'], ['not', 'C'], ['not', 'D'], ['not', 'E'], ['not', 'G']], ['or', 'F', ['not', 'P'], 'H', 'J', 'I', ['not', 'A'], ['not', 'B'], ['not', 'C'], ['not', 'D'], ['not', 'E'], ['not', 'G']], ['or', 'F', ['not', 'P'], 'J', 'L', 'I', ['not', 'K'], ['not', 'A'], ['not', 'B'], ['not', 'C'], ['not', 'D'], ['not', 'G']], ['or', 'F', ['not', 'P'], 'H', 'J', 'I', ['not', 'K'], ['not', 'A'], ['not', 'B'], ['not', 'C'], ['not', 'D'], ['not', 'G']], ['or', 'D', 'F', ['not', 'P'], 'L', 'I', ['not', 'J'], ['not', 'A'], ['not', 'B'], ['not', 'C'], ['not', 'E'], ['not', 'G']], ['or', 'D', 'F', ['not', 'P'], 'H', 'I', ['not', 'J'], ['not', 'A'], ['not', 'B'], ['not', 'C'], ['not', 'E'], ['not', 'G']], ['or', 'D', 'F', ['not', 'P'], 'L', 'I', ['not', 'J'], ['not', 'K'], ['not', 'A'], ['not', 'B'], ['not', 'C'], ['not', 'G']], ['or', 'D', 'F', ['not', 'P'], 'H', 'I', ['not', 'J'], ['not', 'K'], ['not', 'A'], ['not', 'B'], ['not', 'C'], ['not', 'G']], ['or', 'A', 'B', 'G', 'F', ['not', 'P'], 'J', ['not', 'H'], ['not', 'L'], ['not', 'C'], ['not', 'D'], ['not', 'E']], ['or', 'B', 'G', 'F', ['not', 'P'], 'J', ['not', 'H'], ['not', 'I'], ['not', 'L'], ['not', 'C'], ['not', 'D'], ['not', 'E']], ['or', 'A', 'B', 'G', 'F', ['not', 'P'], 'J', ['not', 'H'], ['not', 'K'], ['not', 'L'], ['not', 'C'], ['not', 'D']], ['or', 'B', 'G', 'F', ['not', 'P'], 'J', ['not', 'H'], ['not', 'I'], ['not', 'K'], ['not', 'L'], ['not', 'C'], ['not', 'D']], ['or', 'A', 'B', 'D', 'G', 'F', ['not', 'P'], ['not', 'H'], ['not', 'J'], ['not', 'L'], ['not', 'C'], ['not', 'E']], ['or', 'B', 'D', 'G', 'F', ['not', 'P'], ['not', 'H'], ['not', 'I'], ['not', 'J'], ['not', 'L'], ['not', 'C'], ['not', 'E']], ['or', 'A', 'B', 'D', 'G', 'F', ['not', 'P'], ['not', 'H'], ['not', 'J'], ['not', 'K'], ['not', 'L'], ['not', 'C']], ['or', 'B', 'D', 'G', 'F', ['not', 'P'], ['not', 'H'], ['not', 'I'], ['not', 'J'], ['not', 'K'], ['not', 'L'], ['not', 'C']], ['or', 'A', 'B', 'E', ['not', 'P'], 'K', 'J', 'L', ['not', 'C'], ['not', 'D'], ['not', 'F'], ['not', 'G']], ['or', 'B', 'E', ['not', 'P'], 'K', 'J', 'L', ['not', 'I'], ['not', 'C'], ['not', 'D'], ['not', 'F'], ['not', 'G']], ['or', 'A', 'B', 'E', ['not', 'P'], 'H', 'K', 'J', ['not', 'C'], ['not', 'D'], ['not', 'F'], ['not', 'G']], ['or', 'B', 'E', ['not', 'P'], 'H', 'K', 'J', ['not', 'I'], ['not', 'C'], ['not', 'D'], ['not', 'F'], ['not', 'G']], ['or', 'A', 'B', 'E', 'D', ['not', 'P'], 'K', 'L', ['not', 'J'], ['not', 'C'], ['not', 'F'], ['not', 'G']], ['or', 'B', 'E', 'D', ['not', 'P'], 'K', 'L', ['not', 'I'], ['not', 'J'], ['not', 'C'], ['not', 'F'], ['not', 'G']], ['or', 'A', 'B', 'E', 'D', ['not', 'P'], 'H', 'K', ['not', 'J'], ['not', 'C'], ['not', 'F'], ['not', 'G']], ['or', 'B', 'E', 'D', ['not', 'P'], 'H', 'K', ['not', 'I'], ['not', 'J'], ['not', 'C'], ['not', 'F'], ['not', 'G']], ['or', 'C', 'D', 'G', 'F', ['not', 'P'], 'J', ['not', 'H'], 'I', ['not', 'L'], ['not', 'A'], ['not', 'B'], ['not', 'E']], ['or', 'C', 'D', 'G', 'F', ['not', 'P'], ['not', 'H'], 'I', ['not', 'L'], ['not', 'A'], ['not', 'B'], ['not', 'D'], ['not', 'E']], ['or', 'C', 'D', 'G', 'F', ['not', 'P'], 'J', ['not', 'H'], 'I', ['not', 'K'], ['not', 'L'], ['not', 'A'], ['not', 'B']], ['or', 'C', 'D', 'G', 'F', ['not', 'P'], ['not', 'H'], 'I', ['not', 'K'], ['not', 'L'], ['not', 'A'], ['not', 'B'], ['not', 'D']], ['or', 'C', 'G', 'F', ['not', 'P'], 'J', ['not', 'H'], 'I', ['not', 'J'], ['not', 'L'], ['not', 'A'], ['not', 'B'], ['not', 'E']], ['or', 'C', 'G', 'F', ['not', 'P'], ['not', 'H'], 'I', ['not', 'J'], ['not', 'L'], ['not', 'A'], ['not', 'B'], ['not', 'D'], ['not', 'E']], ['or', 'C', 'G', 'F', ['not', 'P'], 'J', ['not', 'H'], 'I', ['not', 'J'], ['not', 'K'], ['not', 'L'], ['not', 'A'], ['not', 'B']], ['or', 'C', 'G', 'F', ['not', 'P'], ['not', 'H'], 'I', ['not', 'J'], ['not', 'K'], ['not', 'L'], ['not', 'A'], ['not', 'B'], ['not', 'D']], ['or', 'C', 'E', 'D', ['not', 'P'], 'K', 'J', 'L', 'I', ['not', 'A'], ['not', 'B'], ['not', 'F'], ['not', 'G']], ['or', 'C', 'E', 'D', ['not', 'P'], 'K', 'L', 'I', ['not', 'A'], ['not', 'B'], ['not', 'D'], ['not', 'F'], ['not', 'G']], ['or', 'C', 'E', 'D', ['not', 'P'], 'H', 'K', 'J', 'I', ['not', 'A'], ['not', 'B'], ['not', 'F'], ['not', 'G']], ['or', 'C', 'E', 'D', ['not', 'P'], 'H', 'K', 'I', ['not', 'A'], ['not', 'B'], ['not', 'D'], ['not', 'F'], ['not', 'G']], ['or', 'C', 'E', ['not', 'P'], 'K', 'J', 'L', 'I', ['not', 'J'], ['not', 'A'], ['not', 'B'], ['not', 'F'], ['not', 'G']], ['or', 'C', 'E', ['not', 'P'], 'K', 'L', 'I', ['not', 'J'], ['not', 'A'], ['not', 'B'], ['not', 'D'], ['not', 'F'], ['not', 'G']], ['or', 'C', 'E', ['not', 'P'], 'H', 'K', 'J', 'I', ['not', 'J'], ['not', 'A'], ['not', 'B'], ['not', 'F'], ['not', 'G']], ['or', 'C', 'E', ['not', 'P'], 'H', 'K', 'I', ['not', 'J'], ['not', 'A'], ['not', 'B'], ['not', 'D'], ['not', 'F'], ['not', 'G']], ['or', 'A', 'C', 'B', 'E', 'D', 'G', ['not', 'P'], 'K', 'J', ['not', 'H'], ['not', 'L'], ['not', 'F']], ['or', 'A', 'C', 'B', 'E', 'D', 'G', ['not', 'P'], 'K', ['not', 'H'], ['not', 'L'], ['not', 'D'], ['not', 'F']], ['or', 'C', 'B', 'E', 'D', 'G', ['not', 'P'], 'K', 'J', ['not', 'H'], ['not', 'I'], ['not', 'L'], ['not', 'F']], ['or', 'C', 'B', 'E', 'D', 'G', ['not', 'P'], 'K', ['not', 'H'], ['not', 'I'], ['not', 'L'], ['not', 'D'], ['not', 'F']], ['or', 'A', 'C', 'B', 'E', 'G', ['not', 'P'], 'K', 'J', ['not', 'H'], ['not', 'J'], ['not', 'L'], ['not', 'F']], ['or', 'A', 'C', 'B', 'E', 'G', ['not', 'P'], 'K', ['not', 'H'], ['not', 'J'], ['not', 'L'], ['not', 'D'], ['not', 'F']], ['or', 'C', 'B', 'E', 'G', ['not', 'P'], 'K', 'J', ['not', 'H'], ['not', 'I'], ['not', 'J'], ['not', 'L'], ['not', 'F']], ['or', 'C', 'B', 'E', 'G', ['not', 'P'], 'K', ['not', 'H'], ['not', 'I'], ['not', 'J'], ['not', 'L'], ['not', 'D'], ['not', 'F']], ['or', 'A', 'B', 'F', ['not', 'P'], 'J', 'L', ['not', 'C'], ['not', 'D'], ['not', 'E'], ['not', 'G']], ['or', 'B', 'F', ['not', 'P'], 'J', 'L', ['not', 'I'], ['not', 'C'], ['not', 'D'], ['not', 'E'], ['not', 'G']], ['or', 'A', 'B', 'F', ['not', 'P'], 'H', 'J', ['not', 'C'], ['not', 'D'], ['not', 'E'], ['not', 'G']], ['or', 'B', 'F', ['not', 'P'], 'H', 'J', ['not', 'I'], ['not', 'C'], ['not', 'D'], ['not', 'E'], ['not', 'G']], ['or', 'A', 'B', 'F', ['not', 'P'], 'J', 'L', ['not', 'K'], ['not', 'C'], ['not', 'D'], ['not', 'G']], ['or', 'B', 'F', ['not', 'P'], 'J', 'L', ['not', 'I'], ['not', 'K'], ['not', 'C'], ['not', 'D'], ['not', 'G']], ['or', 'A', 'B', 'F', ['not', 'P'], 'H', 'J', ['not', 'K'], ['not', 'C'], ['not', 'D'], ['not', 'G']], ['or', 'B', 'F', ['not', 'P'], 'H', 'J', ['not', 'I'], ['not', 'K'], ['not', 'C'], ['not', 'D'], ['not', 'G']], ['or', 'A', 'B', 'D', 'F', ['not', 'P'], 'L', ['not', 'J'], ['not', 'C'], ['not', 'E'], ['not', 'G']], ['or', 'B', 'D', 'F', ['not', 'P'], 'L', ['not', 'I'], ['not', 'J'], ['not', 'C'], ['not', 'E'], ['not', 'G']], ['or', 'A', 'B', 'D', 'F', ['not', 'P'], 'H', ['not', 'J'], ['not', 'C'], ['not', 'E'], ['not', 'G']], ['or', 'B', 'D', 'F', ['not', 'P'], 'H', ['not', 'I'], ['not', 'J'], ['not', 'C'], ['not', 'E'], ['not', 'G']], ['or', 'A', 'B', 'D', 'F', ['not', 'P'], 'L', ['not', 'J'], ['not', 'K'], ['not', 'C'], ['not', 'G']], ['or', 'B', 'D', 'F', ['not', 'P'], 'L', ['not', 'I'], ['not', 'J'], ['not', 'K'], ['not', 'C'], ['not', 'G']], ['or', 'A', 'B', 'D', 'F', ['not', 'P'], 'H', ['not', 'J'], ['not', 'K'], ['not', 'C'], ['not', 'G']], ['or', 'B', 'D', 'F', ['not', 'P'], 'H', ['not', 'I'], ['not', 'J'], ['not', 'K'], ['not', 'C'], ['not', 'G']], ['or', 'C', 'D', 'F', ['not', 'P'], 'J', 'L', 'I', ['not', 'A'], ['not', 'B'], ['not', 'E'], ['not', 'G']], ['or', 'C', 'D', 'F', ['not', 'P'], 'L', 'I', ['not', 'A'], ['not', 'B'], ['not', 'D'], ['not', 'E'], ['not', 'G']], ['or', 'C', 'D', 'F', ['not', 'P'], 'H', 'J', 'I', ['not', 'A'], ['not', 'B'], ['not', 'E'], ['not', 'G']], ['or', 'C', 'D', 'F', ['not', 'P'], 'H', 'I', ['not', 'A'], ['not', 'B'], ['not', 'D'], ['not', 'E'], ['not', 'G']], ['or', 'C', 'D', 'F', ['not', 'P'], 'J', 'L', 'I', ['not', 'K'], ['not', 'A'], ['not', 'B'], ['not', 'G']], ['or', 'C', 'D', 'F', ['not', 'P'], 'L', 'I', ['not', 'K'], ['not', 'A'], ['not', 'B'], ['not', 'D'], ['not', 'G']], ['or', 'C', 'D', 'F', ['not', 'P'], 'H', 'J', 'I', ['not', 'K'], ['not', 'A'], ['not', 'B'], ['not', 'G']], ['or', 'C', 'D', 'F', ['not', 'P'], 'H', 'I', ['not', 'K'], ['not', 'A'], ['not', 'B'], ['not', 'D'], ['not', 'G']], ['or', 'C', 'F', ['not', 'P'], 'J', 'L', 'I', ['not', 'J'], ['not', 'A'], ['not', 'B'], ['not', 'E'], ['not', 'G']], ['or', 'C', 'F', ['not', 'P'], 'L', 'I', ['not', 'J'], ['not', 'A'], ['not', 'B'], ['not', 'D'], ['not', 'E'], ['not', 'G']], ['or', 'C', 'F', ['not', 'P'], 'H', 'J', 'I', ['not', 'J'], ['not', 'A'], ['not', 'B'], ['not', 'E'], ['not', 'G']], ['or', 'C', 'F', ['not', 'P'], 'H', 'I', ['not', 'J'], ['not', 'A'], ['not', 'B'], ['not', 'D'], ['not', 'E'], ['not', 'G']], ['or', 'C', 'F', ['not', 'P'], 'J', 'L', 'I', ['not', 'J'], ['not', 'K'], ['not', 'A'], ['not', 'B'], ['not', 'G']], ['or', 'C', 'F', ['not', 'P'], 'L', 'I', ['not', 'J'], ['not', 'K'], ['not', 'A'], ['not', 'B'], ['not', 'D'], ['not', 'G']], ['or', 'C', 'F', ['not', 'P'], 'H', 'J', 'I', ['not', 'J'], ['not', 'K'], ['not', 'A'], ['not', 'B'], ['not', 'G']], ['or', 'C', 'F', ['not', 'P'], 'H', 'I', ['not', 'J'], ['not', 'K'], ['not', 'A'], ['not', 'B'], ['not', 'D'], ['not', 'G']], ['or', 'A', 'C', 'B', 'D', 'G', 'F', ['not', 'P'], 'J', ['not', 'H'], ['not', 'L'], ['not', 'E']], ['or', 'A', 'C', 'B', 'D', 'G', 'F', ['not', 'P'], ['not', 'H'], ['not', 'L'], ['not', 'D'], ['not', 'E']], ['or', 'C', 'B', 'D', 'G', 'F', ['not', 'P'], 'J', ['not', 'H'], ['not', 'I'], ['not', 'L'], ['not', 'E']], ['or', 'C', 'B', 'D', 'G', 'F', ['not', 'P'], ['not', 'H'], ['not', 'I'], ['not', 'L'], ['not', 'D'], ['not', 'E']], ['or', 'A', 'C', 'B', 'D', 'G', 'F', ['not', 'P'], 'J', ['not', 'H'], ['not', 'K'], ['not', 'L']], ['or', 'A', 'C', 'B', 'D', 'G', 'F', ['not', 'P'], ['not', 'H'], ['not', 'K'], ['not', 'L'], ['not', 'D']], ['or', 'C', 'B', 'D', 'G', 'F', ['not', 'P'], 'J', ['not', 'H'], ['not', 'I'], ['not', 'K'], ['not', 'L']], ['or', 'C', 'B', 'D', 'G', 'F', ['not', 'P'], ['not', 'H'], ['not', 'I'], ['not', 'K'], ['not', 'L'], ['not', 'D']], ['or', 'A', 'C', 'B', 'G', 'F', ['not', 'P'], 'J', ['not', 'H'], ['not', 'J'], ['not', 'L'], ['not', 'E']], ['or', 'A', 'C', 'B', 'G', 'F', ['not', 'P'], ['not', 'H'], ['not', 'J'], ['not', 'L'], ['not', 'D'], ['not', 'E']], ['or', 'C', 'B', 'G', 'F', ['not', 'P'], 'J', ['not', 'H'], ['not', 'I'], ['not', 'J'], ['not', 'L'], ['not', 'E']], ['or', 'C', 'B', 'G', 'F', ['not', 'P'], ['not', 'H'], ['not', 'I'], ['not', 'J'], ['not', 'L'], ['not', 'D'], ['not', 'E']], ['or', 'A', 'C', 'B', 'G', 'F', ['not', 'P'], 'J', ['not', 'H'], ['not', 'J'], ['not', 'K'], ['not', 'L']], ['or', 'A', 'C', 'B', 'G', 'F', ['not', 'P'], ['not', 'H'], ['not', 'J'], ['not', 'K'], ['not', 'L'], ['not', 'D']], ['or', 'C', 'B', 'G', 'F', ['not', 'P'], 'J', ['not', 'H'], ['not', 'I'], ['not', 'J'], ['not', 'K'], ['not', 'L']], ['or', 'C', 'B', 'G', 'F', ['not', 'P'], ['not', 'H'], ['not', 'I'], ['not', 'J'], ['not', 'K'], ['not', 'L'], ['not', 'D']], ['or', 'A', 'C', 'B', 'E', 'D', ['not', 'P'], 'K', 'J', 'L', ['not', 'F'], ['not', 'G']], ['or', 'A', 'C', 'B', 'E', 'D', ['not', 'P'], 'K', 'L', ['not', 'D'], ['not', 'F'], ['not', 'G']], ['or', 'C', 'B', 'E', 'D', ['not', 'P'], 'K', 'J', 'L', ['not', 'I'], ['not', 'F'], ['not', 'G']], ['or', 'C', 'B', 'E', 'D', ['not', 'P'], 'K', 'L', ['not', 'I'], ['not', 'D'], ['not', 'F'], ['not', 'G']], ['or', 'A', 'C', 'B', 'E', 'D', ['not', 'P'], 'H', 'K', 'J', ['not', 'F'], ['not', 'G']], ['or', 'A', 'C', 'B', 'E', 'D', ['not', 'P'], 'H', 'K', ['not', 'D'], ['not', 'F'], ['not', 'G']], ['or', 'C', 'B', 'E', 'D', ['not', 'P'], 'H', 'K', 'J', ['not', 'I'], ['not', 'F'], ['not', 'G']], ['or', 'C', 'B', 'E', 'D', ['not', 'P'], 'H', 'K', ['not', 'I'], ['not', 'D'], ['not', 'F'], ['not', 'G']], ['or', 'A', 'C', 'B', 'E', ['not', 'P'], 'K', 'J', 'L', ['not', 'J'], ['not', 'F'], ['not', 'G']], ['or', 'A', 'C', 'B', 'E', ['not', 'P'], 'K', 'L', ['not', 'J'], ['not', 'D'], ['not', 'F'], ['not', 'G']], ['or', 'C', 'B', 'E', ['not', 'P'], 'K', 'J', 'L', ['not', 'I'], ['not', 'J'], ['not', 'F'], ['not', 'G']], ['or', 'C', 'B', 'E', ['not', 'P'], 'K', 'L', ['not', 'I'], ['not', 'J'], ['not', 'D'], ['not', 'F'], ['not', 'G']], ['or', 'A', 'C', 'B', 'E', ['not', 'P'], 'H', 'K', 'J', ['not', 'J'], ['not', 'F'], ['not', 'G']], ['or', 'A', 'C', 'B', 'E', ['not', 'P'], 'H', 'K', ['not', 'J'], ['not', 'D'], ['not', 'F'], ['not', 'G']], ['or', 'C', 'B', 'E', ['not', 'P'], 'H', 'K', 'J', ['not', 'I'], ['not', 'J'], ['not', 'F'], ['not', 'G']], ['or', 'C', 'B', 'E', ['not', 'P'], 'H', 'K', ['not', 'I'], ['not', 'J'], ['not', 'D'], ['not', 'F'], ['not', 'G']], ['or', 'A', 'C', 'B', 'D', 'F', ['not', 'P'], 'J', 'L', ['not', 'E'], ['not', 'G']], ['or', 'A', 'C', 'B', 'D', 'F', ['not', 'P'], 'L', ['not', 'D'], ['not', 'E'], ['not', 'G']], ['or', 'C', 'B', 'D', 'F', ['not', 'P'], 'J', 'L', ['not', 'I'], ['not', 'E'], ['not', 'G']], ['or', 'C', 'B', 'D', 'F', ['not', 'P'], 'L', ['not', 'I'], ['not', 'D'], ['not', 'E'], ['not', 'G']], ['or', 'A', 'C', 'B', 'D', 'F', ['not', 'P'], 'H', 'J', ['not', 'E'], ['not', 'G']], ['or', 'A', 'C', 'B', 'D', 'F', ['not', 'P'], 'H', ['not', 'D'], ['not', 'E'], ['not', 'G']], ['or', 'C', 'B', 'D', 'F', ['not', 'P'], 'H', 'J', ['not', 'I'], ['not', 'E'], ['not', 'G']], ['or', 'C', 'B', 'D', 'F', ['not', 'P'], 'H', ['not', 'I'], ['not', 'D'], ['not', 'E'], ['not', 'G']], ['or', 'A', 'C', 'B', 'D', 'F', ['not', 'P'], 'J', 'L', ['not', 'K'], ['not', 'G']], ['or', 'A', 'C', 'B', 'D', 'F', ['not', 'P'], 'L', ['not', 'K'], ['not', 'D'], ['not', 'G']], ['or', 'C', 'B', 'D', 'F', ['not', 'P'], 'J', 'L', ['not', 'I'], ['not', 'K'], ['not', 'G']], ['or', 'C', 'B', 'D', 'F', ['not', 'P'], 'L', ['not', 'I'], ['not', 'K'], ['not', 'D'], ['not', 'G']], ['or', 'A', 'C', 'B', 'D', 'F', ['not', 'P'], 'H', 'J', ['not', 'K'], ['not', 'G']], ['or', 'A', 'C', 'B', 'D', 'F', ['not', 'P'], 'H', ['not', 'K'], ['not', 'D'], ['not', 'G']], ['or', 'C', 'B', 'D', 'F', ['not', 'P'], 'H', 'J', ['not', 'I'], ['not', 'K'], ['not', 'G']], ['or', 'C', 'B', 'D', 'F', ['not', 'P'], 'H', ['not', 'I'], ['not', 'K'], ['not', 'D'], ['not', 'G']], ['or', 'A', 'C', 'B', 'F', ['not', 'P'], 'J', 'L', ['not', 'J'], ['not', 'E'], ['not', 'G']], ['or', 'A', 'C', 'B', 'F', ['not', 'P'], 'L', ['not', 'J'], ['not', 'D'], ['not', 'E'], ['not', 'G']], ['or', 'C', 'B', 'F', ['not', 'P'], 'J', 'L', ['not', 'I'], ['not', 'J'], ['not', 'E'], ['not', 'G']], ['or', 'C', 'B', 'F', ['not', 'P'], 'L', ['not', 'I'], ['not', 'J'], ['not', 'D'], ['not', 'E'], ['not', 'G']], ['or', 'A', 'C', 'B', 'F', ['not', 'P'], 'H', 'J', ['not', 'J'], ['not', 'E'], ['not', 'G']], ['or', 'A', 'C', 'B', 'F', ['not', 'P'], 'H', ['not', 'J'], ['not', 'D'], ['not', 'E'], ['not', 'G']], ['or', 'C', 'B', 'F', ['not', 'P'], 'H', 'J', ['not', 'I'], ['not', 'J'], ['not', 'E'], ['not', 'G']], ['or', 'C', 'B', 'F', ['not', 'P'], 'H', ['not', 'I'], ['not', 'J'], ['not', 'D'], ['not', 'E'], ['not', 'G']], ['or', 'A', 'C', 'B', 'F', ['not', 'P'], 'J', 'L', ['not', 'J'], ['not', 'K'], ['not', 'G']], ['or', 'A', 'C', 'B', 'F', ['not', 'P'], 'L', ['not', 'J'], ['not', 'K'], ['not', 'D'], ['not', 'G']], ['or', 'C', 'B', 'F', ['not', 'P'], 'J', 'L', ['not', 'I'], ['not', 'J'], ['not', 'K'], ['not', 'G']], ['or', 'C', 'B', 'F', ['not', 'P'], 'L', ['not', 'I'], ['not', 'J'], ['not', 'K'], ['not', 'D'], ['not', 'G']], ['or', 'A', 'C', 'B', 'F', ['not', 'P'], 'H', 'J', ['not', 'J'], ['not', 'K'], ['not', 'G']], ['or', 'A', 'C', 'B', 'F', ['not', 'P'], 'H', ['not', 'J'], ['not', 'K'], ['not', 'D'], ['not', 'G']], ['or', 'C', 'B', 'F', ['not', 'P'], 'H', 'J', ['not', 'I'], ['not', 'J'], ['not', 'K'], ['not', 'G']], ['or', 'C', 'B', 'F', ['not', 'P'], 'H', ['not', 'I'], ['not', 'J'], ['not', 'K'], ['not', 'D'], ['not', 'G']]]
#sentence = ['and', ['or', 'C', 'B', 'F', ['not', 'P'], 'H', ['not', 'I'], ['not', 'J'], ['not', 'A'], ['not', 'D'], ['not', 'E'], ['not', 'G']], ['or', 'C', 'B', ['not', 'P'], 'H', 'J', ['not', 'I'], ['not', 'A'], ['not', 'D'], ['not', 'E'], ['not', 'F'], ['not', 'G']], ['or', 'B', 'F', ['not', 'P'], 'H', 'I', ['not', 'J'], ['not', 'A'], ['not', 'C'], ['not', 'D'], ['not', 'E'], ['not', 'G']], ['or', 'B', ['not', 'P'], 'H', 'J', 'I', ['not', 'A'], ['not', 'C'], ['not', 'D'], ['not', 'E'], ['not', 'F'], ['not', 'G']], ['or', 'A', 'C', 'F', ['not', 'P'], 'H', ['not', 'I'], ['not', 'J'], ['not', 'B'], ['not', 'D'], ['not', 'E'], ['not', 'G']], ['or', 'A', 'C', ['not', 'P'], 'H', 'J', ['not', 'I'], ['not', 'B'], ['not', 'D'], ['not', 'E'], ['not', 'F'], ['not', 'G']], ['or', 'A', 'F', ['not', 'P'], 'H', 'I', ['not', 'J'], ['not', 'B'], ['not', 'C'], ['not', 'D'], ['not', 'E'], ['not', 'G']], ['or', 'A', ['not', 'P'], 'H', 'J', 'I', ['not', 'B'], ['not', 'C'], ['not', 'D'], ['not', 'E'], ['not', 'F'], ['not', 'G']], ['or', 'C', 'B', 'D', 'F', ['not', 'P'], 'H', 'I', ['not', 'J'], ['not', 'A'], ['not', 'E'], ['not', 'G']], ['or', 'B', 'I', 'D', 'F', ['not', 'P'], 'H', ['not', 'I'], ['not', 'J'], ['not', 'A'], ['not', 'E'], ['not', 'G']], ['or', 'C', 'B', 'D', ['not', 'P'], 'H', 'J', 'I', ['not', 'A'], ['not', 'E'], ['not', 'F'], ['not', 'G']], ['or', 'B', 'I', 'D', ['not', 'P'], 'H', 'J', ['not', 'I'], ['not', 'A'], ['not', 'E'], ['not', 'F'], ['not', 'G']], ['or', 'C', 'B', 'D', 'F', ['not', 'P'], 'H', ['not', 'J'], ['not', 'A'], ['not', 'C'], ['not', 'E'], ['not', 'G']], ['or', 'B', 'D', 'F', ['not', 'P'], 'H', ['not', 'I'], ['not', 'J'], ['not', 'A'], ['not', 'C'], ['not', 'E'], ['not', 'G']], ['or', 'C', 'B', 'D', ['not', 'P'], 'H', 'J', ['not', 'A'], ['not', 'C'], ['not', 'E'], ['not', 'F'], ['not', 'G']], ['or', 'B', 'D', ['not', 'P'], 'H', 'J', ['not', 'I'], ['not', 'A'], ['not', 'C'], ['not', 'E'], ['not', 'F'], ['not', 'G']], ['or', 'A', 'C', 'D', 'F', ['not', 'P'], 'H', 'I', ['not', 'J'], ['not', 'B'], ['not', 'E'], ['not', 'G']], ['or', 'A', 'I', 'D', 'F', ['not', 'P'], 'H', ['not', 'I'], ['not', 'J'], ['not', 'B'], ['not', 'E'], ['not', 'G']], ['or', 'A', 'C', 'D', ['not', 'P'], 'H', 'J', 'I', ['not', 'B'], ['not', 'E'], ['not', 'F'], ['not', 'G']], ['or', 'A', 'I', 'D', ['not', 'P'], 'H', 'J', ['not', 'I'], ['not', 'B'], ['not', 'E'], ['not', 'F'], ['not', 'G']], ['or', 'A', 'C', 'D', 'F', ['not', 'P'], 'H', ['not', 'J'], ['not', 'B'], ['not', 'C'], ['not', 'E'], ['not', 'G']], ['or', 'A', 'D', 'F', ['not', 'P'], 'H', ['not', 'I'], ['not', 'J'], ['not', 'B'], ['not', 'C'], ['not', 'E'], ['not', 'G']], ['or', 'A', 'C', 'D', ['not', 'P'], 'H', 'J', ['not', 'B'], ['not', 'C'], ['not', 'E'], ['not', 'F'], ['not', 'G']], ['or', 'A', 'D', ['not', 'P'], 'H', 'J', ['not', 'I'], ['not', 'B'], ['not', 'C'], ['not', 'E'], ['not', 'F'], ['not', 'G']], ['or', 'C', 'B', 'E', 'F', ['not', 'P'], 'H', 'J', ['not', 'I'], ['not', 'A'], ['not', 'D'], ['not', 'G']], ['or', 'C', 'B', 'E', ['not', 'P'], 'H', 'J', ['not', 'I'], ['not', 'J'], ['not', 'A'], ['not', 'D'], ['not', 'G']], ['or', 'C', 'B', 'E', 'F', ['not', 'P'], 'H', ['not', 'I'], ['not', 'A'], ['not', 'D'], ['not', 'F'], ['not', 'G']], ['or', 'C', 'B', 'E', ['not', 'P'], 'H', ['not', 'I'], ['not', 'J'], ['not', 'A'], ['not', 'D'], ['not', 'F'], ['not', 'G']], ['or', 'B', 'E', 'F', ['not', 'P'], 'H', 'J', 'I', ['not', 'A'], ['not', 'C'], ['not', 'D'], ['not', 'G']], ['or', 'B', 'E', ['not', 'P'], 'H', 'J', 'I', ['not', 'J'], ['not', 'A'], ['not', 'C'], ['not', 'D'], ['not', 'G']], ['or', 'B', 'E', 'F', ['not', 'P'], 'H', 'I', ['not', 'A'], ['not', 'C'], ['not', 'D'], ['not', 'F'], ['not', 'G']], ['or', 'B', 'E', ['not', 'P'], 'H', 'I', ['not', 'J'], ['not', 'A'], ['not', 'C'], ['not', 'D'], ['not', 'F'], ['not', 'G']], ['or', 'A', 'C', 'E', 'F', ['not', 'P'], 'H', 'J', ['not', 'I'], ['not', 'B'], ['not', 'D'], ['not', 'G']], ['or', 'A', 'C', 'E', ['not', 'P'], 'H', 'J', ['not', 'I'], ['not', 'J'], ['not', 'B'], ['not', 'D'], ['not', 'G']], ['or', 'A', 'C', 'E', 'F', ['not', 'P'], 'H', ['not', 'I'], ['not', 'B'], ['not', 'D'], ['not', 'F'], ['not', 'G']], ['or', 'A', 'C', 'E', ['not', 'P'], 'H', ['not', 'I'], ['not', 'J'], ['not', 'B'], ['not', 'D'], ['not', 'F'], ['not', 'G']], ['or', 'A', 'E', 'F', ['not', 'P'], 'H', 'J', 'I', ['not', 'B'], ['not', 'C'], ['not', 'D'], ['not', 'G']], ['or', 'A', 'E', ['not', 'P'], 'H', 'J', 'I', ['not', 'J'], ['not', 'B'], ['not', 'C'], ['not', 'D'], ['not', 'G']], ['or', 'A', 'E', 'F', ['not', 'P'], 'H', 'I', ['not', 'B'], ['not', 'C'], ['not', 'D'], ['not', 'F'], ['not', 'G']], ['or', 'A', 'E', ['not', 'P'], 'H', 'I', ['not', 'J'], ['not', 'B'], ['not', 'C'], ['not', 'D'], ['not', 'F'], ['not', 'G']], ['or', 'C', 'B', 'E', 'D', 'F', ['not', 'P'], 'H', 'J', 'I', ['not', 'A'], ['not', 'G']], ['or', 'C', 'B', 'E', 'D', ['not', 'P'], 'H', 'J', 'I', ['not', 'J'], ['not', 'A'], ['not', 'G']], ['or', 'B', 'E', 'D', 'F', ['not', 'P'], 'H', 'J', ['not', 'I'], 'I', ['not', 'A'], ['not', 'G']], ['or', 'B', 'E', 'D', ['not', 'P'], 'H', 'J', ['not', 'I'], ['not', 'J'], 'I', ['not', 'A'], ['not', 'G']], ['or', 'C', 'B', 'E', 'D', 'F', ['not', 'P'], 'H', 'I', ['not', 'A'], ['not', 'F'], ['not', 'G']], ['or', 'C', 'B', 'E', 'D', ['not', 'P'], 'H', 'I', ['not', 'J'], ['not', 'A'], ['not', 'F'], ['not', 'G']], ['or', 'B', 'E', 'D', 'F', ['not', 'P'], 'H', ['not', 'I'], 'I', ['not', 'A'], ['not', 'F'], ['not', 'G']], ['or', 'B', 'E', 'D', ['not', 'P'], 'H', ['not', 'I'], ['not', 'J'], 'I', ['not', 'A'], ['not', 'F'], ['not', 'G']], ['or', 'C', 'B', 'E', 'D', 'F', ['not', 'P'], 'H', 'J', ['not', 'A'], ['not', 'C'], ['not', 'G']], ['or', 'C', 'B', 'E', 'D', ['not', 'P'], 'H', 'J', ['not', 'J'], ['not', 'A'], ['not', 'C'], ['not', 'G']], ['or', 'B', 'E', 'D', 'F', ['not', 'P'], 'H', 'J', ['not', 'I'], ['not', 'A'], ['not', 'C'], ['not', 'G']], ['or', 'B', 'E', 'D', ['not', 'P'], 'H', 'J', ['not', 'I'], ['not', 'J'], ['not', 'A'], ['not', 'C'], ['not', 'G']], ['or', 'C', 'B', 'E', 'D', 'F', ['not', 'P'], 'H', ['not', 'A'], ['not', 'C'], ['not', 'F'], ['not', 'G']], ['or', 'C', 'B', 'E', 'D', ['not', 'P'], 'H', ['not', 'J'], ['not', 'A'], ['not', 'C'], ['not', 'F'], ['not', 'G']], ['or', 'B', 'E', 'D', 'F', ['not', 'P'], 'H', ['not', 'I'], ['not', 'A'], ['not', 'C'], ['not', 'F'], ['not', 'G']], ['or', 'B', 'E', 'D', ['not', 'P'], 'H', ['not', 'I'], ['not', 'J'], ['not', 'A'], ['not', 'C'], ['not', 'F'], ['not', 'G']], ['or', 'A', 'C', 'E', 'D', 'F', ['not', 'P'], 'H', 'J', 'I', ['not', 'B'], ['not', 'G']], ['or', 'A', 'C', 'E', 'D', ['not', 'P'], 'H', 'J', 'I', ['not', 'J'], ['not', 'B'], ['not', 'G']], ['or', 'A', 'E', 'D', 'F', ['not', 'P'], 'H', 'J', ['not', 'I'], 'I', ['not', 'B'], ['not', 'G']], ['or', 'A', 'E', 'D', ['not', 'P'], 'H', 'J', ['not', 'I'], ['not', 'J'], 'I', ['not', 'B'], ['not', 'G']], ['or', 'A', 'C', 'E', 'D', 'F', ['not', 'P'], 'H', 'I', ['not', 'B'], ['not', 'F'], ['not', 'G']], ['or', 'A', 'C', 'E', 'D', ['not', 'P'], 'H', 'I', ['not', 'J'], ['not', 'B'], ['not', 'F'], ['not', 'G']], ['or', 'A', 'E', 'D', 'F', ['not', 'P'], 'H', ['not', 'I'], 'I', ['not', 'B'], ['not', 'F'], ['not', 'G']], ['or', 'A', 'E', 'D', ['not', 'P'], 'H', ['not', 'I'], ['not', 'J'], 'I', ['not', 'B'], ['not', 'F'], ['not', 'G']], ['or', 'A', 'C', 'E', 'D', 'F', ['not', 'P'], 'H', 'J', ['not', 'B'], ['not', 'C'], ['not', 'G']], ['or', 'A', 'C', 'E', 'D', ['not', 'P'], 'H', 'J', ['not', 'J'], ['not', 'B'], ['not', 'C'], ['not', 'G']], ['or', 'A', 'E', 'D', 'F', ['not', 'P'], 'H', 'J', ['not', 'I'], ['not', 'B'], ['not', 'C'], ['not', 'G']], ['or', 'A', 'E', 'D', ['not', 'P'], 'H', 'J', ['not', 'I'], ['not', 'J'], ['not', 'B'], ['not', 'C'], ['not', 'G']], ['or', 'A', 'C', 'E', 'D', 'F', ['not', 'P'], 'H', ['not', 'B'], ['not', 'C'], ['not', 'F'], ['not', 'G']], ['or', 'A', 'C', 'E', 'D', ['not', 'P'], 'H', ['not', 'J'], ['not', 'B'], ['not', 'C'], ['not', 'F'], ['not', 'G']], ['or', 'A', 'E', 'D', 'F', ['not', 'P'], 'H', ['not', 'I'], ['not', 'B'], ['not', 'C'], ['not', 'F'], ['not', 'G']], ['or', 'A', 'E', 'D', ['not', 'P'], 'H', ['not', 'I'], ['not', 'J'], ['not', 'B'], ['not', 'C'], ['not', 'F'], ['not', 'G']]]
##sentence =  ['and', ['not', 'P'], ['or', 'I', ['not', 'A'], ['not', 'B']], ['or', 'K', 'E', ['not', 'F']], ['or', ['not', 'H'], ['not', 'L'], 'G'], ['or', 'A', 'B'], ['or', ['not', 'I'], 'B'], ['or', 'J', ['not', 'C'], ['not', 'D']], ['or', ['not', 'J'], ['not', 'C'], 'D'], ['or', ['not', 'E'], 'F'], ['or', ['not', 'K'], 'F'], ['or', 'L', ['not', 'G']], ['or', 'H', ['not', 'G']], ['or', 'C', 'J', 'D'], ['or', 'C', ['not', 'D'], 'D'], ['or', ['not', 'J'], 'J', 'C'], ['or', ['not', 'J'], ['not', 'D'], 'C']]
#['and', ['not', 'P'], ['or', 'J', ['not', 'C'], ['not', 'D']], ['or', ['not', 'J'], ['not', 'C'], 'D'], ['or', 'H', ['not', 'G']], ['or', 'L', ['not', 'V'], ['not', 'G']], ['or', 'V', ['not', 'L'], ['not', 'G']], ['or', 'A', ['not', 'B'], 'M'], ['or', ['not', 'I'], ['not', 'B'], 'M'], ['or', 'A', 'B', ['not', 'M']], ['or', ['not', 'I'], 'B', ['not', 'M']], ['or', 'I', ['not', 'A'], 'B', 'M'], ['or', 'I', ['not', 'A'], 'M', ['not', 'M']], ['or', 'I', ['not', 'A'], ['not', 'B'], 'B'], ['or', 'I', ['not', 'A'], ['not', 'B'], ['not', 'M']], ['or', 'C', 'J', 'D'], ['or', 'C', ['not', 'D'], 'D'], ['or', ['not', 'J'], 'J', 'C'], ['or', ['not', 'J'], ['not', 'D'], 'C'], ['or', 'U', ['not', 'E'], ['not', 'F']], ['or', ['not', 'K'], 'U', ['not', 'F']], ['or', 'F', ['not', 'E'], ['not', 'U']], ['or', ['not', 'K'], ['not', 'U'], 'F'], ['or', 'E', 'K', 'U', 'F'], ['or', 'E', 'K', 'U', ['not', 'U']], ['or', 'K', 'E', ['not', 'F'], 'F'], ['or', 'K', 'E', ['not', 'U'], ['not', 'F']], ['or', ['not', 'H'], 'L', 'G', 'V'], ['or', ['not', 'H'], 'G', ['not', 'V'], 'V'], ['or', ['not', 'H'], ['not', 'L'], 'L', 'G'], ['or', ['not', 'H'], ['not', 'L'], 'G', ['not', 'V']]]
#sentence = ['and', ['or', 'a', 'b'], 'a']

#sentence = ['and', ['or', 'a', 'c', 'b', 'f'], ['or', 'c', 'd', 'f'], ['or', 'a', 'b', 'd', 'f'], ['or', 'd', 'f']]
#sentence = ['and', ['or', 'a', 'c', 'e'], ['or', 'c', 'b', 'e'], ['or', 'a', 'c', 'e', 'f'], ['or', 'c', 'b', 'e', 'f'], ['or', 'a', 'e', 'd'], ['or', 'b', 'e', 'd'], ['or', 'a', 'e', 'd', 'f'], ['or', 'b', 'e', 'd', 'f']]
#sentence = ['and', ['not', 'P'], ['or', 'I', ['not', 'A'], ['not', 'B']], ['or', 'K', 'E', ['not', 'F']], ['or', ['not', 'H'], ['not', 'L'], 'G'], ['or', 'A', 'B'], ['or', ['not', 'I'], 'B'], ['or', 'J', ['not', 'C'], ['not', 'D']], ['or', ['not', 'J'], ['not', 'C'], 'D'], ['or', ['not', 'E'], 'F'], ['or', ['not', 'K'], 'F'], ['or', 'L', ['not', 'G']], ['or', 'H', ['not', 'G']], ['or', 'C', 'J', 'D'], ['or', 'C', ['not', 'D'], 'D'], ['or', ['not', 'J'], 'J', 'C'], ['or', ['not', 'J'], ['not', 'D'], 'C']]
#sentence = ['and', 'C', 'B', 'E', 'F']
#sentence = ['and', ['not', 'P'], ['or', 'I', ['not', 'A'], ['not', 'B']], ['or', 'K', 'E', ['not', 'F']], ['or', ['not', 'H'], ['not', 'L'], 'G'], ['or', 'A', 'B'], ['or', ['not', 'I'], 'B'], ['or', 'J', ['not', 'C'], ['not', 'D']], ['or', ['not', 'J'], ['not', 'C'], 'D'], ['or', ['not', 'E'], 'F'], ['or', ['not', 'K'], 'F'], ['or', 'L', ['not', 'G']], ['or', 'H', ['not', 'G']], ['or', 'C', 'J', 'D'], ['or', 'C', ['not', 'D'], 'D'], ['or', ['not', 'J'], 'J', 'C'], ['or', ['not', 'J'], ['not', 'D'], 'C']]sentence = ['and', ['not', 'P'], ['or', 'I', ['not', 'A'], ['not', 'B']], ['or', 'K', 'E', ['not', 'F']], ['or', ['not', 'H'], ['not', 'L'], 'G'], ['or', 'A', 'B'], ['or', ['not', 'I'], 'B'], ['or', 'J', ['not', 'C'], ['not', 'D']], ['or', ['not', 'J'], ['not', 'C'], 'D'], ['or', ['not', 'E'], 'F'], ['or', ['not', 'K'], 'F'], ['or', 'L', ['not', 'G']], ['or', 'H', ['not', 'G']], ['or', 'C', 'J', 'D'], ['or', 'C', ['not', 'D'], 'D'], ['or', ['not', 'J'], 'J', 'C'], ['or', ['not', 'J'], ['not', 'D'], 'C']]
sentence = ['and', ['or', ["not",'E'], 'G', ['not', 'P'], 'K', 'J', ['not', 'H'], 'I', ['not', 'L'], ['not', 'A'], ['not', 'B'], ['not', 'C'], ['not', 'D'], ['not', 'F']], ['or', 'E', 'D', 'G', ['not', 'P'], 'K', ['not', 'H'], 'I', ['not', 'J'], ['not', 'L'], ['not', 'A'], ['not', 'B'], ['not', 'C'], ['not', 'F']], ['or', 'G', 'F', ['not', 'P'], 'J', ['not', 'H'], 'I', ['not', 'L'], ['not', 'A'], ['not', 'B'], ['not', 'C'], ['not', 'D'], ['not', 'E']], ['or', 'G', 'F', ['not', 'P'], 'J', ['not', 'H'], 'I', ['not', 'K'], ['not', 'L'], ['not', 'A'], ['not', 'B'], ['not', 'C'], ['not', 'D']], ['or', 'D', 'G', 'F', ['not', 'P'], ['not', 'H'], 'I', ['not', 'J'], ['not', 'L'], ['not', 'A'], ['not', 'B'], ['not', 'C'], ['not', 'E']], ['or', 'D', 'G', 'F', ['not', 'P'], ['not', 'H'], 'I', ['not', 'J'], ['not', 'K'], ['not', 'L'], ['not', 'A'], ['not', 'B'], ['not', 'C']], ['or', 'E', ['not', 'P'], 'K', 'J', 'L', 'I', ['not', 'A'], ['not', 'B'], ['not', 'C'], ['not', 'D'], ['not', 'F'], ['not', 'G']], ['or', 'E', ['not', 'P'], 'H', 'K', 'J', 'I', ['not', 'A'], ['not', 'B'], ['not', 'C'], ['not', 'D'], ['not', 'F'], ['not', 'G']], ['or', 'E', 'D', ['not', 'P'], 'K', 'L', 'I', ['not', 'J'], ['not', 'A'], ['not', 'B'], ['not', 'C'], ['not', 'F'], ['not', 'G']], ['or', 'E', 'D', ['not', 'P'], 'H', 'K', 'I', ['not', 'J'], ['not', 'A'], ['not', 'B'], ['not', 'C'], ['not', 'F'], ['not', 'G']], ['or', 'A', 'B', 'E', 'G', ['not', 'P'], 'K', 'J', ['not', 'H'], ['not', 'L'], ['not', 'C'], ['not', 'D'], ['not', 'F']], ['or', 'B', 'E', 'G', ['not', 'P'], 'K', 'J', ['not', 'H'], ['not', 'I'], ['not', 'L'], ['not', 'C'], ['not', 'D'], ['not', 'F']], ['or', 'A', 'B', 'E', 'D', 'G', ['not', 'P'], 'K', ['not', 'H'], ['not', 'J'], ['not', 'L'], ['not', 'C'], ['not', 'F']], ['or', 'B', 'E', 'D', 'G', ['not', 'P'], 'K', ['not', 'H'], ['not', 'I'], ['not', 'J'], ['not', 'L'], ['not', 'C'], ['not', 'F']], ['or', 'C', 'E', 'D', 'G', ['not', 'P'], 'K', 'J', ['not', 'H'], 'I', ['not', 'L'], ['not', 'A'], ['not', 'B'], ['not', 'F']], ['or', 'C', 'E', 'D', 'G', ['not', 'P'], 'K', ['not', 'H'], 'I', ['not', 'L'], ['not', 'A'], ['not', 'B'], ['not', 'D'], ['not', 'F']], ['or', 'C', 'E', 'G', ['not', 'P'], 'K', 'J', ['not', 'H'], 'I', ['not', 'J'], ['not', 'L'], ['not', 'A'], ['not', 'B'], ['not', 'F']], ['or', 'C', 'E', 'G', ['not', 'P'], 'K', ['not', 'H'], 'I', ['not', 'J'], ['not', 'L'], ['not', 'A'], ['not', 'B'], ['not', 'D'], ['not', 'F']], ['or', 'F', ['not', 'P'], 'J', 'L', 'I', ['not', 'A'], ['not', 'B'], ['not', 'C'], ['not', 'D'], ['not', 'E'], ['not', 'G']], ['or', 'F', ['not', 'P'], 'H', 'J', 'I', ['not', 'A'], ['not', 'B'], ['not', 'C'], ['not', 'D'], ['not', 'E'], ['not', 'G']], ['or', 'F', ['not', 'P'], 'J', 'L', 'I', ['not', 'K'], ['not', 'A'], ['not', 'B'], ['not', 'C'], ['not', 'D'], ['not', 'G']], ['or', 'F', ['not', 'P'], 'H', 'J', 'I', ['not', 'K'], ['not', 'A'], ['not', 'B'], ['not', 'C'], ['not', 'D'], ['not', 'G']], ['or', 'D', 'F', ['not', 'P'], 'L', 'I', ['not', 'J'], ['not', 'A'], ['not', 'B'], ['not', 'C'], ['not', 'E'], ['not', 'G']], ['or', 'D', 'F', ['not', 'P'], 'H', 'I', ['not', 'J'], ['not', 'A'], ['not', 'B'], ['not', 'C'], ['not', 'E'], ['not', 'G']], ['or', 'D', 'F', ['not', 'P'], 'L', 'I', ['not', 'J'], ['not', 'K'], ['not', 'A'], ['not', 'B'], ['not', 'C'], ['not', 'G']], ['or', 'D', 'F', ['not', 'P'], 'H', 'I', ['not', 'J'], ['not', 'K'], ['not', 'A'], ['not', 'B'], ['not', 'C'], ['not', 'G']], ['or', 'A', 'B', 'G', 'F', ['not', 'P'], 'J', ['not', 'H'], ['not', 'L'], ['not', 'C'], ['not', 'D'], ['not', 'E']], ['or', 'B', 'G', 'F', ['not', 'P'], 'J', ['not', 'H'], ['not', 'I'], ['not', 'L'], ['not', 'C'], ['not', 'D'], ['not', 'E']], ['or', 'A', 'B', 'G', 'F', ['not', 'P'], 'J', ['not', 'H'], ['not', 'K'], ['not', 'L'], ['not', 'C'], ['not', 'D']], ['or', 'B', 'G', 'F', ['not', 'P'], 'J', ['not', 'H'], ['not', 'I'], ['not', 'K'], ['not', 'L'], ['not', 'C'], ['not', 'D']], ['or', 'A', 'B', 'D', 'G', 'F', ['not', 'P'], ['not', 'H'], ['not', 'J'], ['not', 'L'], ['not', 'C'], ['not', 'E']], ['or', 'B', 'D', 'G', 'F', ['not', 'P'], ['not', 'H'], ['not', 'I'], ['not', 'J'], ['not', 'L'], ['not', 'C'], ['not', 'E']], ['or', 'A', 'B', 'D', 'G', 'F', ['not', 'P'], ['not', 'H'], ['not', 'J'], ['not', 'K'], ['not', 'L'], ['not', 'C']], ['or', 'B', 'D', 'G', 'F', ['not', 'P'], ['not', 'H'], ['not', 'I'], ['not', 'J'], ['not', 'K'], ['not', 'L'], ['not', 'C']], ['or', 'A', 'B', 'E', ['not', 'P'], 'K', 'J', 'L', ['not', 'C'], ['not', 'D'], ['not', 'F'], ['not', 'G']], ['or', 'B', 'E', ['not', 'P'], 'K', 'J', 'L', ['not', 'I'], ['not', 'C'], ['not', 'D'], ['not', 'F'], ['not', 'G']], ['or', 'A', 'B', 'E', ['not', 'P'], 'H', 'K', 'J', ['not', 'C'], ['not', 'D'], ['not', 'F'], ['not', 'G']], ['or', 'B', 'E', ['not', 'P'], 'H', 'K', 'J', ['not', 'I'], ['not', 'C'], ['not', 'D'], ['not', 'F'], ['not', 'G']], ['or', 'A', 'B', 'E', 'D', ['not', 'P'], 'K', 'L', ['not', 'J'], ['not', 'C'], ['not', 'F'], ['not', 'G']], ['or', 'B', 'E', 'D', ['not', 'P'], 'K', 'L', ['not', 'I'], ['not', 'J'], ['not', 'C'], ['not', 'F'], ['not', 'G']], ['or', 'A', 'B', 'E', 'D', ['not', 'P'], 'H', 'K', ['not', 'J'], ['not', 'C'], ['not', 'F'], ['not', 'G']], ['or', 'B', 'E', 'D', ['not', 'P'], 'H', 'K', ['not', 'I'], ['not', 'J'], ['not', 'C'], ['not', 'F'], ['not', 'G']], ['or', 'C', 'D', 'G', 'F', ['not', 'P'], 'J', ['not', 'H'], 'I', ['not', 'L'], ['not', 'A'], ['not', 'B'], ['not', 'E']], ['or', 'C', 'D', 'G', 'F', ['not', 'P'], ['not', 'H'], 'I', ['not', 'L'], ['not', 'A'], ['not', 'B'], ['not', 'D'], ['not', 'E']], ['or', 'C', 'D', 'G', 'F', ['not', 'P'], 'J', ['not', 'H'], 'I', ['not', 'K'], ['not', 'L'], ['not', 'A'], ['not', 'B']], ['or', 'C', 'D', 'G', 'F', ['not', 'P'], ['not', 'H'], 'I', ['not', 'K'], ['not', 'L'], ['not', 'A'], ['not', 'B'], ['not', 'D']], ['or', 'C', 'G', 'F', ['not', 'P'], 'J', ['not', 'H'], 'I', ['not', 'J'], ['not', 'L'], ['not', 'A'], ['not', 'B'], ['not', 'E']], ['or', 'C', 'G', 'F', ['not', 'P'], ['not', 'H'], 'I', ['not', 'J'], ['not', 'L'], ['not', 'A'], ['not', 'B'], ['not', 'D'], ['not', 'E']], ['or', 'C', 'G', 'F', ['not', 'P'], 'J', ['not', 'H'], 'I', ['not', 'J'], ['not', 'K'], ['not', 'L'], ['not', 'A'], ['not', 'B']], ['or', 'C', 'G', 'F', ['not', 'P'], ['not', 'H'], 'I', ['not', 'J'], ['not', 'K'], ['not', 'L'], ['not', 'A'], ['not', 'B'], ['not', 'D']], ['or', 'C', 'E', 'D', ['not', 'P'], 'K', 'J', 'L', 'I', ['not', 'A'], ['not', 'B'], ['not', 'F'], ['not', 'G']], ['or', 'C', 'E', 'D', ['not', 'P'], 'K', 'L', 'I', ['not', 'A'], ['not', 'B'], ['not', 'D'], ['not', 'F'], ['not', 'G']], ['or', 'C', 'E', 'D', ['not', 'P'], 'H', 'K', 'J', 'I', ['not', 'A'], ['not', 'B'], ['not', 'F'], ['not', 'G']], ['or', 'C', 'E', 'D', ['not', 'P'], 'H', 'K', 'I', ['not', 'A'], ['not', 'B'], ['not', 'D'], ['not', 'F'], ['not', 'G']], ['or', 'C', 'E', ['not', 'P'], 'K', 'J', 'L', 'I', ['not', 'J'], ['not', 'A'], ['not', 'B'], ['not', 'F'], ['not', 'G']], ['or', 'C', 'E', ['not', 'P'], 'K', 'L', 'I', ['not', 'J'], ['not', 'A'], ['not', 'B'], ['not', 'D'], ['not', 'F'], ['not', 'G']], ['or', 'C', 'E', ['not', 'P'], 'H', 'K', 'J', 'I', ['not', 'J'], ['not', 'A'], ['not', 'B'], ['not', 'F'], ['not', 'G']], ['or', 'C', 'E', ['not', 'P'], 'H', 'K', 'I', ['not', 'J'], ['not', 'A'], ['not', 'B'], ['not', 'D'], ['not', 'F'], ['not', 'G']], ['or', 'A', 'C', 'B', 'E', 'D', 'G', ['not', 'P'], 'K', 'J', ['not', 'H'], ['not', 'L'], ['not', 'F']], ['or', 'A', 'C', 'B', 'E', 'D', 'G', ['not', 'P'], 'K', ['not', 'H'], ['not', 'L'], ['not', 'D'], ['not', 'F']], ['or', 'C', 'B', 'E', 'D', 'G', ['not', 'P'], 'K', 'J', ['not', 'H'], ['not', 'I'], ['not', 'L'], ['not', 'F']], ['or', 'C', 'B', 'E', 'D', 'G', ['not', 'P'], 'K', ['not', 'H'], ['not', 'I'], ['not', 'L'], ['not', 'D'], ['not', 'F']], ['or', 'A', 'C', 'B', 'E', 'G', ['not', 'P'], 'K', 'J', ['not', 'H'], ['not', 'J'], ['not', 'L'], ['not', 'F']], ['or', 'A', 'C', 'B', 'E', 'G', ['not', 'P'], 'K', ['not', 'H'], ['not', 'J'], ['not', 'L'], ['not', 'D'], ['not', 'F']], ['or', 'C', 'B', 'E', 'G', ['not', 'P'], 'K', 'J', ['not', 'H'], ['not', 'I'], ['not', 'J'], ['not', 'L'], ['not', 'F']], ['or', 'C', 'B', 'E', 'G', ['not', 'P'], 'K', ['not', 'H'], ['not', 'I'], ['not', 'J'], ['not', 'L'], ['not', 'D'], ['not', 'F']], ['or', 'A', 'B', 'F', ['not', 'P'], 'J', 'L', ['not', 'C'], ['not', 'D'], ['not', 'E'], ['not', 'G']], ['or', 'B', 'F', ['not', 'P'], 'J', 'L', ['not', 'I'], ['not', 'C'], ['not', 'D'], ['not', 'E'], ['not', 'G']], ['or', 'A', 'B', 'F', ['not', 'P'], 'H', 'J', ['not', 'C'], ['not', 'D'], ['not', 'E'], ['not', 'G']], ['or', 'B', 'F', ['not', 'P'], 'H', 'J', ['not', 'I'], ['not', 'C'], ['not', 'D'], ['not', 'E'], ['not', 'G']], ['or', 'A', 'B', 'F', ['not', 'P'], 'J', 'L', ['not', 'K'], ['not', 'C'], ['not', 'D'], ['not', 'G']], ['or', 'B', 'F', ['not', 'P'], 'J', 'L', ['not', 'I'], ['not', 'K'], ['not', 'C'], ['not', 'D'], ['not', 'G']], ['or', 'A', 'B', 'F', ['not', 'P'], 'H', 'J', ['not', 'K'], ['not', 'C'], ['not', 'D'], ['not', 'G']], ['or', 'B', 'F', ['not', 'P'], 'H', 'J', ['not', 'I'], ['not', 'K'], ['not', 'C'], ['not', 'D'], ['not', 'G']], ['or', 'A', 'B', 'D', 'F', ['not', 'P'], 'L', ['not', 'J'], ['not', 'C'], ['not', 'E'], ['not', 'G']], ['or', 'B', 'D', 'F', ['not', 'P'], 'L', ['not', 'I'], ['not', 'J'], ['not', 'C'], ['not', 'E'], ['not', 'G']], ['or', 'A', 'B', 'D', 'F', ['not', 'P'], 'H', ['not', 'J'], ['not', 'C'], ['not', 'E'], ['not', 'G']], ['or', 'B', 'D', 'F', ['not', 'P'], 'H', ['not', 'I'], ['not', 'J'], ['not', 'C'], ['not', 'E'], ['not', 'G']], ['or', 'A', 'B', 'D', 'F', ['not', 'P'], 'L', ['not', 'J'], ['not', 'K'], ['not', 'C'], ['not', 'G']], ['or', 'B', 'D', 'F', ['not', 'P'], 'L', ['not', 'I'], ['not', 'J'], ['not', 'K'], ['not', 'C'], ['not', 'G']], ['or', 'A', 'B', 'D', 'F', ['not', 'P'], 'H', ['not', 'J'], ['not', 'K'], ['not', 'C'], ['not', 'G']], ['or', 'B', 'D', 'F', ['not', 'P'], 'H', ['not', 'I'], ['not', 'J'], ['not', 'K'], ['not', 'C'], ['not', 'G']], ['or', 'C', 'D', 'F', ['not', 'P'], 'J', 'L', 'I', ['not', 'A'], ['not', 'B'], ['not', 'E'], ['not', 'G']], ['or', 'C', 'D', 'F', ['not', 'P'], 'L', 'I', ['not', 'A'], ['not', 'B'], ['not', 'D'], ['not', 'E'], ['not', 'G']], ['or', 'C', 'D', 'F', ['not', 'P'], 'H', 'J', 'I', ['not', 'A'], ['not', 'B'], ['not', 'E'], ['not', 'G']], ['or', 'C', 'D', 'F', ['not', 'P'], 'H', 'I', ['not', 'A'], ['not', 'B'], ['not', 'D'], ['not', 'E'], ['not', 'G']], ['or', 'C', 'D', 'F', ['not', 'P'], 'J', 'L', 'I', ['not', 'K'], ['not', 'A'], ['not', 'B'], ['not', 'G']], ['or', 'C', 'D', 'F', ['not', 'P'], 'L', 'I', ['not', 'K'], ['not', 'A'], ['not', 'B'], ['not', 'D'], ['not', 'G']], ['or', 'C', 'D', 'F', ['not', 'P'], 'H', 'J', 'I', ['not', 'K'], ['not', 'A'], ['not', 'B'], ['not', 'G']], ['or', 'C', 'D', 'F', ['not', 'P'], 'H', 'I', ['not', 'K'], ['not', 'A'], ['not', 'B'], ['not', 'D'], ['not', 'G']], ['or', 'C', 'F', ['not', 'P'], 'J', 'L', 'I', ['not', 'J'], ['not', 'A'], ['not', 'B'], ['not', 'E'], ['not', 'G']], ['or', 'C', 'F', ['not', 'P'], 'L', 'I', ['not', 'J'], ['not', 'A'], ['not', 'B'], ['not', 'D'], ['not', 'E'], ['not', 'G']], ['or', 'C', 'F', ['not', 'P'], 'H', 'J', 'I', ['not', 'J'], ['not', 'A'], ['not', 'B'], ['not', 'E'], ['not', 'G']], ['or', 'C', 'F', ['not', 'P'], 'H', 'I', ['not', 'J'], ['not', 'A'], ['not', 'B'], ['not', 'D'], ['not', 'E'], ['not', 'G']], ['or', 'C', 'F', ['not', 'P'], 'J', 'L', 'I', ['not', 'J'], ['not', 'K'], ['not', 'A'], ['not', 'B'], ['not', 'G']], ['or', 'C', 'F', ['not', 'P'], 'L', 'I', ['not', 'J'], ['not', 'K'], ['not', 'A'], ['not', 'B'], ['not', 'D'], ['not', 'G']], ['or', 'C', 'F', ['not', 'P'], 'H', 'J', 'I', ['not', 'J'], ['not', 'K'], ['not', 'A'], ['not', 'B'], ['not', 'G']], ['or', 'C', 'F', ['not', 'P'], 'H', 'I', ['not', 'J'], ['not', 'K'], ['not', 'A'], ['not', 'B'], ['not', 'D'], ['not', 'G']], ['or', 'A', 'C', 'B', 'D', 'G', 'F', ['not', 'P'], 'J', ['not', 'H'], ['not', 'L'], ['not', 'E']], ['or', 'A', 'C', 'B', 'D', 'G', 'F', ['not', 'P'], ['not', 'H'], ['not', 'L'], ['not', 'D'], ['not', 'E']], ['or', 'C', 'B', 'D', 'G', 'F', ['not', 'P'], 'J', ['not', 'H'], ['not', 'I'], ['not', 'L'], ['not', 'E']], ['or', 'C', 'B', 'D', 'G', 'F', ['not', 'P'], ['not', 'H'], ['not', 'I'], ['not', 'L'], ['not', 'D'], ['not', 'E']], ['or', 'A', 'C', 'B', 'D', 'G', 'F', ['not', 'P'], 'J', ['not', 'H'], ['not', 'K'], ['not', 'L']], ['or', 'A', 'C', 'B', 'D', 'G', 'F', ['not', 'P'], ['not', 'H'], ['not', 'K'], ['not', 'L'], ['not', 'D']], ['or', 'C', 'B', 'D', 'G', 'F', ['not', 'P'], 'J', ['not', 'H'], ['not', 'I'], ['not', 'K'], ['not', 'L']], ['or', 'C', 'B', 'D', 'G', 'F', ['not', 'P'], ['not', 'H'], ['not', 'I'], ['not', 'K'], ['not', 'L'], ['not', 'D']], ['or', 'A', 'C', 'B', 'G', 'F', ['not', 'P'], 'J', ['not', 'H'], ['not', 'J'], ['not', 'L'], ['not', 'E']], ['or', 'A', 'C', 'B', 'G', 'F', ['not', 'P'], ['not', 'H'], ['not', 'J'], ['not', 'L'], ['not', 'D'], ['not', 'E']], ['or', 'C', 'B', 'G', 'F', ['not', 'P'], 'J', ['not', 'H'], ['not', 'I'], ['not', 'J'], ['not', 'L'], ['not', 'E']], ['or', 'C', 'B', 'G', 'F', ['not', 'P'], ['not', 'H'], ['not', 'I'], ['not', 'J'], ['not', 'L'], ['not', 'D'], ['not', 'E']], ['or', 'A', 'C', 'B', 'G', 'F', ['not', 'P'], 'J', ['not', 'H'], ['not', 'J'], ['not', 'K'], ['not', 'L']], ['or', 'A', 'C', 'B', 'G', 'F', ['not', 'P'], ['not', 'H'], ['not', 'J'], ['not', 'K'], ['not', 'L'], ['not', 'D']], ['or', 'C', 'B', 'G', 'F', ['not', 'P'], 'J', ['not', 'H'], ['not', 'I'], ['not', 'J'], ['not', 'K'], ['not', 'L']], ['or', 'C', 'B', 'G', 'F', ['not', 'P'], ['not', 'H'], ['not', 'I'], ['not', 'J'], ['not', 'K'], ['not', 'L'], ['not', 'D']], ['or', 'A', 'C', 'B', 'E', 'D', ['not', 'P'], 'K', 'J', 'L', ['not', 'F'], ['not', 'G']], ['or', 'A', 'C', 'B', 'E', 'D', ['not', 'P'], 'K', 'L', ['not', 'D'], ['not', 'F'], ['not', 'G']], ['or', 'C', 'B', 'E', 'D', ['not', 'P'], 'K', 'J', 'L', ['not', 'I'], ['not', 'F'], ['not', 'G']], ['or', 'C', 'B', 'E', 'D', ['not', 'P'], 'K', 'L', ['not', 'I'], ['not', 'D'], ['not', 'F'], ['not', 'G']], ['or', 'A', 'C', 'B', 'E', 'D', ['not', 'P'], 'H', 'K', 'J', ['not', 'F'], ['not', 'G']], ['or', 'A', 'C', 'B', 'E', 'D', ['not', 'P'], 'H', 'K', ['not', 'D'], ['not', 'F'], ['not', 'G']], ['or', 'C', 'B', 'E', 'D', ['not', 'P'], 'H', 'K', 'J', ['not', 'I'], ['not', 'F'], ['not', 'G']], ['or', 'C', 'B', 'E', 'D', ['not', 'P'], 'H', 'K', ['not', 'I'], ['not', 'D'], ['not', 'F'], ['not', 'G']], ['or', 'A', 'C', 'B', 'E', ['not', 'P'], 'K', 'J', 'L', ['not', 'J'], ['not', 'F'], ['not', 'G']], ['or', 'A', 'C', 'B', 'E', ['not', 'P'], 'K', 'L', ['not', 'J'], ['not', 'D'], ['not', 'F'], ['not', 'G']], ['or', 'C', 'B', 'E', ['not', 'P'], 'K', 'J', 'L', ['not', 'I'], ['not', 'J'], ['not', 'F'], ['not', 'G']], ['or', 'C', 'B', 'E', ['not', 'P'], 'K', 'L', ['not', 'I'], ['not', 'J'], ['not', 'D'], ['not', 'F'], ['not', 'G']], ['or', 'A', 'C', 'B', 'E', ['not', 'P'], 'H', 'K', 'J', ['not', 'J'], ['not', 'F'], ['not', 'G']], ['or', 'A', 'C', 'B', 'E', ['not', 'P'], 'H', 'K', ['not', 'J'], ['not', 'D'], ['not', 'F'], ['not', 'G']], ['or', 'C', 'B', 'E', ['not', 'P'], 'H', 'K', 'J', ['not', 'I'], ['not', 'J'], ['not', 'F'], ['not', 'G']], ['or', 'C', 'B', 'E', ['not', 'P'], 'H', 'K', ['not', 'I'], ['not', 'J'], ['not', 'D'], ['not', 'F'], ['not', 'G']], ['or', 'A', 'C', 'B', 'D', 'F', ['not', 'P'], 'J', 'L', ['not', 'E'], ['not', 'G']], ['or', 'A', 'C', 'B', 'D', 'F', ['not', 'P'], 'L', ['not', 'D'], ['not', 'E'], ['not', 'G']], ['or', 'C', 'B', 'D', 'F', ['not', 'P'], 'J', 'L', ['not', 'I'], ['not', 'E'], ['not', 'G']], ['or', 'C', 'B', 'D', 'F', ['not', 'P'], 'L', ['not', 'I'], ['not', 'D'], ['not', 'E'], ['not', 'G']], ['or', 'A', 'C', 'B', 'D', 'F', ['not', 'P'], 'H', 'J', ['not', 'E'], ['not', 'G']], ['or', 'A', 'C', 'B', 'D', 'F', ['not', 'P'], 'H', ['not', 'D'], ['not', 'E'], ['not', 'G']], ['or', 'C', 'B', 'D', 'F', ['not', 'P'], 'H', 'J', ['not', 'I'], ['not', 'E'], ['not', 'G']], ['or', 'C', 'B', 'D', 'F', ['not', 'P'], 'H', ['not', 'I'], ['not', 'D'], ['not', 'E'], ['not', 'G']], ['or', 'A', 'C', 'B', 'D', 'F', ['not', 'P'], 'J', 'L', ['not', 'K'], ['not', 'G']], ['or', 'A', 'C', 'B', 'D', 'F', ['not', 'P'], 'L', ['not', 'K'], ['not', 'D'], ['not', 'G']], ['or', 'C', 'B', 'D', 'F', ['not', 'P'], 'J', 'L', ['not', 'I'], ['not', 'K'], ['not', 'G']], ['or', 'C', 'B', 'D', 'F', ['not', 'P'], 'L', ['not', 'I'], ['not', 'K'], ['not', 'D'], ['not', 'G']], ['or', 'A', 'C', 'B', 'D', 'F', ['not', 'P'], 'H', 'J', ['not', 'K'], ['not', 'G']], ['or', 'A', 'C', 'B', 'D', 'F', ['not', 'P'], 'H', ['not', 'K'], ['not', 'D'], ['not', 'G']], ['or', 'C', 'B', 'D', 'F', ['not', 'P'], 'H', 'J', ['not', 'I'], ['not', 'K'], ['not', 'G']], ['or', 'C', 'B', 'D', 'F', ['not', 'P'], 'H', ['not', 'I'], ['not', 'K'], ['not', 'D'], ['not', 'G']], ['or', 'A', 'C', 'B', 'F', ['not', 'P'], 'J', 'L', ['not', 'J'], ['not', 'E'], ['not', 'G']], ['or', 'A', 'C', 'B', 'F', ['not', 'P'], 'L', ['not', 'J'], ['not', 'D'], ['not', 'E'], ['not', 'G']], ['or', 'C', 'B', 'F', ['not', 'P'], 'J', 'L', ['not', 'I'], ['not', 'J'], ['not', 'E'], ['not', 'G']], ['or', 'C', 'B', 'F', ['not', 'P'], 'L', ['not', 'I'], ['not', 'J'], ['not', 'D'], ['not', 'E'], ['not', 'G']], ['or', 'A', 'C', 'B', 'F', ['not', 'P'], 'H', 'J', ['not', 'J'], ['not', 'E'], ['not', 'G']], ['or', 'A', 'C', 'B', 'F', ['not', 'P'], 'H', ['not', 'J'], ['not', 'D'], ['not', 'E'], ['not', 'G']], ['or', 'C', 'B', 'F', ['not', 'P'], 'H', 'J', ['not', 'I'], ['not', 'J'], ['not', 'E'], ['not', 'G']], ['or', 'C', 'B', 'F', ['not', 'P'], 'H', ['not', 'I'], ['not', 'J'], ['not', 'D'], ['not', 'E'], ['not', 'G']], ['or', 'A', 'C', 'B', 'F', ['not', 'P'], 'J', 'L', ['not', 'J'], ['not', 'K'], ['not', 'G']], ['or', 'A', 'C', 'B', 'F', ['not', 'P'], 'L', ['not', 'J'], ['not', 'K'], ['not', 'D'], ['not', 'G']], ['or', 'C', 'B', 'F', ['not', 'P'], 'J', 'L', ['not', 'I'], ['not', 'J'], ['not', 'K'], ['not', 'G']], ['or', 'C', 'B', 'F', ['not', 'P'], 'L', ['not', 'I'], ['not', 'J'], ['not', 'K'], ['not', 'D'], ['not', 'G']], ['or', 'A', 'C', 'B', 'F', ['not', 'P'], 'H', 'J', ['not', 'J'], ['not', 'K'], ['not', 'G']], ['or', 'A', 'C', 'B', 'F', ['not', 'P'], 'H', ['not', 'J'], ['not', 'K'], ['not', 'D'], ['not', 'G']], ['or', 'C', 'B', 'F', ['not', 'P'], 'H', 'J', ['not', 'I'], ['not', 'J'], ['not', 'K'], ['not', 'G']], ['or', 'C', 'B', 'F', ['not', 'P'], 'H', ['not', 'I'], ['not', 'J'], ['not', 'K'], ['not', 'D'], ['not', 'G']]]
#sentence = ['and', ['or', 'C', 'B', 'F', ['not', 'P'], 'H', ['not', 'I'], ['not', 'J'], ['not', 'A'], ['not', 'D'], ['not', 'E'], ['not', 'G']], ['or', 'C', 'B', ['not', 'P'], 'H', 'J', ['not', 'I'], ['not', 'A'], ['not', 'D'], ['not', 'E'], ['not', 'F'], ['not', 'G']], ['or', 'B', 'F', ['not', 'P'], 'H', 'I', ['not', 'J'], ['not', 'A'], ['not', 'C'], ['not', 'D'], ['not', 'E'], ['not', 'G']], ['or', 'B', ['not', 'P'], 'H', 'J', 'I', ['not', 'A'], ['not', 'C'], ['not', 'D'], ['not', 'E'], ['not', 'F'], ['not', 'G']], ['or', 'A', 'C', 'F', ['not', 'P'], 'H', ['not', 'I'], ['not', 'J'], ['not', 'B'], ['not', 'D'], ['not', 'E'], ['not', 'G']], ['or', 'A', 'C', ['not', 'P'], 'H', 'J', ['not', 'I'], ['not', 'B'], ['not', 'D'], ['not', 'E'], ['not', 'F'], ['not', 'G']], ['or', 'A', 'F', ['not', 'P'], 'H', 'I', ['not', 'J'], ['not', 'B'], ['not', 'C'], ['not', 'D'], ['not', 'E'], ['not', 'G']], ['or', 'A', ['not', 'P'], 'H', 'J', 'I', ['not', 'B'], ['not', 'C'], ['not', 'D'], ['not', 'E'], ['not', 'F'], ['not', 'G']], ['or', 'C', 'B', 'D', 'F', ['not', 'P'], 'H', 'I', ['not', 'J'], ['not', 'A'], ['not', 'E'], ['not', 'G']], ['or', 'B', 'I', 'D', 'F', ['not', 'P'], 'H', ['not', 'I'], ['not', 'J'], ['not', 'A'], ['not', 'E'], ['not', 'G']], ['or', 'C', 'B', 'D', ['not', 'P'], 'H', 'J', 'I', ['not', 'A'], ['not', 'E'], ['not', 'F'], ['not', 'G']], ['or', 'B', 'I', 'D', ['not', 'P'], 'H', 'J', ['not', 'I'], ['not', 'A'], ['not', 'E'], ['not', 'F'], ['not', 'G']], ['or', 'C', 'B', 'D', 'F', ['not', 'P'], 'H', ['not', 'J'], ['not', 'A'], ['not', 'C'], ['not', 'E'], ['not', 'G']], ['or', 'B', 'D', 'F', ['not', 'P'], 'H', ['not', 'I'], ['not', 'J'], ['not', 'A'], ['not', 'C'], ['not', 'E'], ['not', 'G']], ['or', 'C', 'B', 'D', ['not', 'P'], 'H', 'J', ['not', 'A'], ['not', 'C'], ['not', 'E'], ['not', 'F'], ['not', 'G']], ['or', 'B', 'D', ['not', 'P'], 'H', 'J', ['not', 'I'], ['not', 'A'], ['not', 'C'], ['not', 'E'], ['not', 'F'], ['not', 'G']], ['or', 'A', 'C', 'D', 'F', ['not', 'P'], 'H', 'I', ['not', 'J'], ['not', 'B'], ['not', 'E'], ['not', 'G']], ['or', 'A', 'I', 'D', 'F', ['not', 'P'], 'H', ['not', 'I'], ['not', 'J'], ['not', 'B'], ['not', 'E'], ['not', 'G']], ['or', 'A', 'C', 'D', ['not', 'P'], 'H', 'J', 'I', ['not', 'B'], ['not', 'E'], ['not', 'F'], ['not', 'G']], ['or', 'A', 'I', 'D', ['not', 'P'], 'H', 'J', ['not', 'I'], ['not', 'B'], ['not', 'E'], ['not', 'F'], ['not', 'G']], ['or', 'A', 'C', 'D', 'F', ['not', 'P'], 'H', ['not', 'J'], ['not', 'B'], ['not', 'C'], ['not', 'E'], ['not', 'G']], ['or', 'A', 'D', 'F', ['not', 'P'], 'H', ['not', 'I'], ['not', 'J'], ['not', 'B'], ['not', 'C'], ['not', 'E'], ['not', 'G']], ['or', 'A', 'C', 'D', ['not', 'P'], 'H', 'J', ['not', 'B'], ['not', 'C'], ['not', 'E'], ['not', 'F'], ['not', 'G']], ['or', 'A', 'D', ['not', 'P'], 'H', 'J', ['not', 'I'], ['not', 'B'], ['not', 'C'], ['not', 'E'], ['not', 'F'], ['not', 'G']], ['or', 'C', 'B', 'E', 'F', ['not', 'P'], 'H', 'J', ['not', 'I'], ['not', 'A'], ['not', 'D'], ['not', 'G']], ['or', 'C', 'B', 'E', ['not', 'P'], 'H', 'J', ['not', 'I'], ['not', 'J'], ['not', 'A'], ['not', 'D'], ['not', 'G']], ['or', 'C', 'B', 'E', 'F', ['not', 'P'], 'H', ['not', 'I'], ['not', 'A'], ['not', 'D'], ['not', 'F'], ['not', 'G']], ['or', 'C', 'B', 'E', ['not', 'P'], 'H', ['not', 'I'], ['not', 'J'], ['not', 'A'], ['not', 'D'], ['not', 'F'], ['not', 'G']], ['or', 'B', 'E', 'F', ['not', 'P'], 'H', 'J', 'I', ['not', 'A'], ['not', 'C'], ['not', 'D'], ['not', 'G']], ['or', 'B', 'E', ['not', 'P'], 'H', 'J', 'I', ['not', 'J'], ['not', 'A'], ['not', 'C'], ['not', 'D'], ['not', 'G']], ['or', 'B', 'E', 'F', ['not', 'P'], 'H', 'I', ['not', 'A'], ['not', 'C'], ['not', 'D'], ['not', 'F'], ['not', 'G']], ['or', 'B', 'E', ['not', 'P'], 'H', 'I', ['not', 'J'], ['not', 'A'], ['not', 'C'], ['not', 'D'], ['not', 'F'], ['not', 'G']], ['or', 'A', 'C', 'E', 'F', ['not', 'P'], 'H', 'J', ['not', 'I'], ['not', 'B'], ['not', 'D'], ['not', 'G']], ['or', 'A', 'C', 'E', ['not', 'P'], 'H', 'J', ['not', 'I'], ['not', 'J'], ['not', 'B'], ['not', 'D'], ['not', 'G']], ['or', 'A', 'C', 'E', 'F', ['not', 'P'], 'H', ['not', 'I'], ['not', 'B'], ['not', 'D'], ['not', 'F'], ['not', 'G']], ['or', 'A', 'C', 'E', ['not', 'P'], 'H', ['not', 'I'], ['not', 'J'], ['not', 'B'], ['not', 'D'], ['not', 'F'], ['not', 'G']], ['or', 'A', 'E', 'F', ['not', 'P'], 'H', 'J', 'I', ['not', 'B'], ['not', 'C'], ['not', 'D'], ['not', 'G']], ['or', 'A', 'E', ['not', 'P'], 'H', 'J', 'I', ['not', 'J'], ['not', 'B'], ['not', 'C'], ['not', 'D'], ['not', 'G']], ['or', 'A', 'E', 'F', ['not', 'P'], 'H', 'I', ['not', 'B'], ['not', 'C'], ['not', 'D'], ['not', 'F'], ['not', 'G']], ['or', 'A', 'E', ['not', 'P'], 'H', 'I', ['not', 'J'], ['not', 'B'], ['not', 'C'], ['not', 'D'], ['not', 'F'], ['not', 'G']], ['or', 'C', 'B', 'E', 'D', 'F', ['not', 'P'], 'H', 'J', 'I', ['not', 'A'], ['not', 'G']], ['or', 'C', 'B', 'E', 'D', ['not', 'P'], 'H', 'J', 'I', ['not', 'J'], ['not', 'A'], ['not', 'G']], ['or', 'B', 'E', 'D', 'F', ['not', 'P'], 'H', 'J', ['not', 'I'], 'I', ['not', 'A'], ['not', 'G']], ['or', 'B', 'E', 'D', ['not', 'P'], 'H', 'J', ['not', 'I'], ['not', 'J'], 'I', ['not', 'A'], ['not', 'G']], ['or', 'C', 'B', 'E', 'D', 'F', ['not', 'P'], 'H', 'I', ['not', 'A'], ['not', 'F'], ['not', 'G']], ['or', 'C', 'B', 'E', 'D', ['not', 'P'], 'H', 'I', ['not', 'J'], ['not', 'A'], ['not', 'F'], ['not', 'G']], ['or', 'B', 'E', 'D', 'F', ['not', 'P'], 'H', ['not', 'I'], 'I', ['not', 'A'], ['not', 'F'], ['not', 'G']], ['or', 'B', 'E', 'D', ['not', 'P'], 'H', ['not', 'I'], ['not', 'J'], 'I', ['not', 'A'], ['not', 'F'], ['not', 'G']], ['or', 'C', 'B', 'E', 'D', 'F', ['not', 'P'], 'H', 'J', ['not', 'A'], ['not', 'C'], ['not', 'G']], ['or', 'C', 'B', 'E', 'D', ['not', 'P'], 'H', 'J', ['not', 'J'], ['not', 'A'], ['not', 'C'], ['not', 'G']], ['or', 'B', 'E', 'D', 'F', ['not', 'P'], 'H', 'J', ['not', 'I'], ['not', 'A'], ['not', 'C'], ['not', 'G']], ['or', 'B', 'E', 'D', ['not', 'P'], 'H', 'J', ['not', 'I'], ['not', 'J'], ['not', 'A'], ['not', 'C'], ['not', 'G']], ['or', 'C', 'B', 'E', 'D', 'F', ['not', 'P'], 'H', ['not', 'A'], ['not', 'C'], ['not', 'F'], ['not', 'G']], ['or', 'C', 'B', 'E', 'D', ['not', 'P'], 'H', ['not', 'J'], ['not', 'A'], ['not', 'C'], ['not', 'F'], ['not', 'G']], ['or', 'B', 'E', 'D', 'F', ['not', 'P'], 'H', ['not', 'I'], ['not', 'A'], ['not', 'C'], ['not', 'F'], ['not', 'G']], ['or', 'B', 'E', 'D', ['not', 'P'], 'H', ['not', 'I'], ['not', 'J'], ['not', 'A'], ['not', 'C'], ['not', 'F'], ['not', 'G']], ['or', 'A', 'C', 'E', 'D', 'F', ['not', 'P'], 'H', 'J', 'I', ['not', 'B'], ['not', 'G']], ['or', 'A', 'C', 'E', 'D', ['not', 'P'], 'H', 'J', 'I', ['not', 'J'], ['not', 'B'], ['not', 'G']], ['or', 'A', 'E', 'D', 'F', ['not', 'P'], 'H', 'J', ['not', 'I'], 'I', ['not', 'B'], ['not', 'G']], ['or', 'A', 'E', 'D', ['not', 'P'], 'H', 'J', ['not', 'I'], ['not', 'J'], 'I', ['not', 'B'], ['not', 'G']], ['or', 'A', 'C', 'E', 'D', 'F', ['not', 'P'], 'H', 'I', ['not', 'B'], ['not', 'F'], ['not', 'G']], ['or', 'A', 'C', 'E', 'D', ['not', 'P'], 'H', 'I', ['not', 'J'], ['not', 'B'], ['not', 'F'], ['not', 'G']], ['or', 'A', 'E', 'D', 'F', ['not', 'P'], 'H', ['not', 'I'], 'I', ['not', 'B'], ['not', 'F'], ['not', 'G']], ['or', 'A', 'E', 'D', ['not', 'P'], 'H', ['not', 'I'], ['not', 'J'], 'I', ['not', 'B'], ['not', 'F'], ['not', 'G']], ['or', 'A', 'C', 'E', 'D', 'F', ['not', 'P'], 'H', 'J', ['not', 'B'], ['not', 'C'], ['not', 'G']], ['or', 'A', 'C', 'E', 'D', ['not', 'P'], 'H', 'J', ['not', 'J'], ['not', 'B'], ['not', 'C'], ['not', 'G']], ['or', 'A', 'E', 'D', 'F', ['not', 'P'], 'H', 'J', ['not', 'I'], ['not', 'B'], ['not', 'C'], ['not', 'G']], ['or', 'A', 'E', 'D', ['not', 'P'], 'H', 'J', ['not', 'I'], ['not', 'J'], ['not', 'B'], ['not', 'C'], ['not', 'G']], ['or', 'A', 'C', 'E', 'D', 'F', ['not', 'P'], 'H', ['not', 'B'], ['not', 'C'], ['not', 'F'], ['not', 'G']], ['or', 'A', 'C', 'E', 'D', ['not', 'P'], 'H', ['not', 'J'], ['not', 'B'], ['not', 'C'], ['not', 'F'], ['not', 'G']], ['or', 'A', 'E', 'D', 'F', ['not', 'P'], 'H', ['not', 'I'], ['not', 'B'], ['not', 'C'], ['not', 'F'], ['not', 'G']], ['or', 'A', 'E', 'D', ['not', 'P'], 'H', ['not', 'I'], ['not', 'J'], ['not', 'B'], ['not', 'C'], ['not', 'F'], ['not', 'G']], "p", ["not", "p"]]#sentence = ["and", ["or", "p", "q"], ["or", ["not", "p"], "r"], ["or", ["not", "r"], ["not", "p"]], ["or", ["not", "q"], "s", ["not", "t"]], "t", "p", ["not", "p"]]
#sentence = ["and", ["or", ["not", "p"], "q", ["not", "k"]],["or", "p", ["not", "q"], "k"], ["not", "p"]]
#sentence = ["and", "a", ["or", "b", ["not", "a"]]]
sentence = ["and", ["or", "p",["not", "q"]], ["or", ["not", "p"], "q"], ["or", ["not", "p"], ["not", "q"]]]
sentence = ["and", ["or", ["not", "p"], "q"], ["or", ["not", "q"], ["not", "p"]], ["or", "p", ["not", "q"]]]
#Global symbols
symbols = {}
results = {}
li = []

# Goal test true :- If the sentence is empty, the sentence is satisfiable
def goal_test_true():
    global li
    if not li:
        return True
    return False

# Goal test false :- If there is an empty clause, the present configuration is not satisfiable
def goal_test_false():
    global li
    for a in li:
        if a == "":
            return True
    
    return False
 
""" Extract Symbols the clauses are converted to a string for ease of handling,
    for example : the clause [or, a, b, [not, c], d, [not, e]] will be converted to ab~d~e
"""
def extract_symbols(sentence): 
    global symbols, results
    st = ""
    if sentence[0] == "not" and len(sentence) == 2:
        not_item = "~" + sentence[1]
        st = st + not_item
        if not_item in symbols:
            symbols[not_item] += 1
        else:
            symbols[not_item] = 1
            results[not_item] = -1
    
        return st 
        
    for item in sentence:
        print"Item is", item
        if isinstance(item, list):
            if item[0] == "not":
                not_item = "~" + item[1]
                st = st + not_item
                if not_item in symbols:
                    symbols[not_item] += 1
                else:
                    symbols[not_item] = 1
                    results[not_item] = -1
        else:
            if item != "or":
                st = st + item
                elem = item
                if elem in symbols:
                    symbols[elem] += 1
                else:
                    symbols[elem] = 1
                    results[elem] = -1
    
    return st         
                           
 
#Driver for extract_symbols            
def find_terms_new(sentence):
    global li
    if sentence[0] == "or":
        sentence = sentence[1:]
        li.append(extract_symbols(sentence))
    elif sentence[0] == "and":
        
        for elem in sentence:
            print elem
            if elem != "and":
                li.append(extract_symbols(elem))
    else:
        #["not", "p"]
        li.append(extract_symbols(sentence))
        
    
    print "the converted list is", li
    print "the symbol dict is,", symbols
    print "the result dict is,", results
    

""" Finding the pure symbols in the sentence if any if pure symbol is found the symbol is returned else
    False
"""
def find_pure_symbols(): 
    global symbols
    for keys in symbols:
        if symbols[keys] > 0:
            
            if len(keys) == 2:
                not_keys = keys[1]
            else:
                not_keys = "~" + keys
            if not_keys in symbols:
                if symbols[not_keys] == 0:
                    return keys
            else:
                return keys
    
    return False

""" Finding the unit clauses in the sentence if any, if unit clause is found the index of the 
    unit clause in the sentence is returned else -1
"""
def find_unit_clauses():
    global li
    for index, item in enumerate(li):
        if len(item) == 1:
            return index
        elif len(item) == 2:
            if "~" in item:
                return index
    
    return -1

""" Finding the first term in the sentence for the splitting rule, the first term is returned from here
"""
def find_first_term():
    global li
    item = li[0]
    if item[0] != "~":
        return item[0]
    else:
        return item[0] + item[1]   

def remove_clause(index):
    global li, symbols
    item = li[index]
    #item = li[index]
    i = 0
    while(i < len(item)):
        if item[i] != "~":
            if i!= 0:
                if item[i - 1] == "~":
                    new = item[i - 1] + item[i]
                    symbols[new] -= 1
                else:
                    symbols[item[i]] -= 1
            else:
                symbols[item[i]] -= 1
        i += 1
  
""" The value of the term is set here, also all the clauses containing the term is removed and not term is removed
    from all the clauses
"""
def set_value(sym):
    global li, results, symbols
    not_sym = "~" + sym if len(sym) == 1 else sym[1]
    results[sym] = "true"
    new_list = []
    for index, item in enumerate(li):
        if len(sym) == 2 and sym in item:
              remove_clause(index)
        
        elif len(sym) == 1 and sym in item:
            #Two cases check if item is available and also check if not item is available
            inde = item.find(sym)
            if (inde == -1):
                #item not available nothing to do
                li[index] = item
            else:
                if inde != 0:
                    if (item[inde - 1] == "~"):
                        #this is not_sym check again with the rest of the item if sym is available
                        if (index < len(item) - 1):
                            ind = item[inde+1:].find(sym)
                            if (ind == -1):
                                #the sym is not present only not_sym is present,  just remove that from the item..
                                elem = li[index]
                                elem = elem.replace(not_sym,"")
                                symbols[not_sym] -= 1
                                li[index] = elem
                                new_list.append(li[index])
                            else:
                                #we have the sym here pop the element
                                remove_clause(index)
                        else:
                                #the sym is not present only not_sym is present,  just remove that from the item..
                                elem = li[index]
                                elem = elem.replace(not_sym,"")
                                symbols[not_sym] -= 1
                                li[index] = elem
                                new_list.append(li[index])
                                  
                    else:
                        remove_clause(index)
                else:
                    remove_clause(index)
                            
        
        elif len(sym) == 2 and not_sym in item:
            elem = li[index]
            elem = elem.replace(not_sym,"")
            symbols[not_sym] -= 1
            li[index] = elem
            new_list.append(li[index])
        
        else:
            new_list.append(li[index])
        
    li = new_list

""" DPLL implemenation as in lecture slide 
"""
def dpll():
    global li
    global results
    global symbols
    
    if (goal_test_true()):
        return True
    if (goal_test_false()):
        return False
    
    pure_symbol = find_pure_symbols()
    if (pure_symbol):
        print "The pure symbol is ",pure_symbol
        set_value(pure_symbol)
        return dpll()

    unit_clause = find_unit_clauses() 
    if (unit_clause != -1):
        print "Got unit clause", li[unit_clause]
        set_value(li[unit_clause])
        return dpll()
    
    #Backup all the values because we are going to guess, guess may go wrong
    backup = copy.deepcopy(li)
    results_backup = copy.deepcopy(results)
    symbols_backup = copy.deepcopy(symbols)
    
    first = find_first_term()
    
    set_value(first)
    if (dpll()):
        return True
    else:
          #Guess was wrong, copy the backed up values
        li = copy.deepcopy(backup)
        results = copy.deepcopy(results_backup)
        symbols = copy.deepcopy(symbols_backup)
        
        if len(first) == 1:
            first = "~" + first
        else:
            first = first[1]
        set_value(first)
        if (dpll()):
            return True
        else:
            return False
    

""" Formatting of the results is done here
"""
def get_results(value):
    global results
    if value:
        res = ["true"]
        for keys in results:
                if len(keys) == 2:
                    a = []
                    a.append(keys[1] +"=false")
                    a.append(keys[1] +"=true")
                    if a[1] not in res and a[0] not in res and (keys[1] not in results or results[keys[1]])!="true":
                            st = keys[1]+"=false"  
                            res.append(st)    
                else:
                    a = []
                    a.append(keys +"=false")
                    a.append(keys +"=true")
                    if a[1] not in res and a[0] not in res and ("~" + keys not in results or results["~" + keys])!="true":
                            st = keys+"=true"  
                            res.append(st)
                                 
        return res
    else:
        return ["false"]

"""
input = open(sys.argv[2]).readlines()
number = int(input[0]) + 1
output = open("CNF_satisfiability.txt", 'w')
print "the number is ", number

for i in xrange(1, number):
    global symbols 
    global results 
    global li 
    global sentence 
    symbols = {}
    results = {}
    li = []
    sentence = eval(input[i])
    print "the input sentence is ",sentence
    find_terms_new(sentence) 
    value = dpll()     
    res = get_results(value)
    print "results", res
    output.write(str(res) + '\n')
"""  

""" 
sentence = 
find_terms_new(sentence)
value = dpll()
value = get_results(value)
print value  
"""


input = open("cnf_sentences", "r").readlines()
number = int(input[0]) + 1
output = open("dpll_output2", 'w')
print "the number is ", number

for i in xrange(1, number):
    global symbols 
    global results 
    global li 
    global sentence 
    symbols = {}
    results = {}
    li = []
    sentence = eval(input[i])
    print "the input sentence is ",sentence
    find_terms_new(sentence) 
    value = dpll()     
    res = get_results(value)
    print "results", res
    output.write(str(res) + '\n')
  
