def abbrev_name(name):
    return '.'.join([x[0].upper() for x in name.split()])


assert abbrev_name("Sam Harris") == "S.H"
assert abbrev_name("patrick feenan") == "P.F"
assert abbrev_name("Evan C") == "E.C"
assert abbrev_name("P Favuzzi") == "P.F"
assert abbrev_name("David Mendieta") == "D.M"