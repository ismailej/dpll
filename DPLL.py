import sys
import copy

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
output.close()
 


  
