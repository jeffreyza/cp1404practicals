from prac_06.guitar_specs import GuitarSpecs

guitar = GuitarSpecs('Gibson L-5 CES', 1922, 16035.40)
other_guitar = GuitarSpecs('Ibanez JBM-27', 2012, 3000)

print("{} get_age() - Expected {}. Got {}".format(guitar.name, 99, guitar.get_age()))
print("{} get_age() - Expected {}. Got {}".format(other_guitar.name, 9, other_guitar.get_age()))
print('{} is_vintage() - Expected True. Got {}'.format(guitar.name, guitar.is_vintage()))
print('{} is_vintage() - Expected False. Got {}'.format(other_guitar.name, other_guitar.is_vintage()))
