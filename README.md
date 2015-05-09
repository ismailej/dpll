SAT-solver 

This is a boolean satisfiability solver that takes a
set of variables and connectives in CNF and returns either a satisfying
assignment that would make the CNF sentence true or determines that no
satisfying assignment is possible. This is an implementation of DPLL algorithm 

Sample Input

['and', ['or', ['not', 'P'], ['not', 'R']], ['or', ['not', 'P'], 'R'], ['or', 'Q', 'R']]


