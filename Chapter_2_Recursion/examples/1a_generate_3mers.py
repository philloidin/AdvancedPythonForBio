def generate_trimers():
    bases = ['A', 'T', 'G', 'C']
    result = []
    for base1 in bases:
        for base2 in bases:
            for base3 in bases:
                result.append(base1 + base2 + base3)
    for i in result:
        answer = i + " "
        print 'Some trimer', answer

generate_trimers()