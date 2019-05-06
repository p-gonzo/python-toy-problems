def r_p_s(num):
    options = ['r', 'p', 's']
    permutations = []

    def construct_candidate_solutions(candidate_solution):
        if len(candidate_solution) == num:
            permutations.append(candidate_solution)
            return
        else:
            for option in options:
                construct_candidate_solutions(candidate_solution + option)
    construct_candidate_solutions('')
    return permutations

print(r_p_s(4))