from database.DAO import DAO

mydeo = DAO()
"""countries = DAO.getAllCountries()
for c in countries:
    print(c)"""
confini = DAO.getContiguityByYear(2000)
confini.sort()
for c in confini:
    print(f" {c[0]} - Vicini: {c[1]}")
