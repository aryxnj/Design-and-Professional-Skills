def poly_to_lists(poly):
    terms = poly.split(' + ')
    powers = []
    coeffs = []
    for term in terms:
        if term.find('x^') == -1:
            powers.append(0)
            coeffs.append(int(term))
        else:
            power = int(term[term.find('^')+1:])
            powers.append(power)
            coeffs.append(int(term[:term.find('x')]))
    return powers, coeffs