from countryinfo import CountryInfo

country = CountryInfo(input("Enter Country Name:"))

print("Country Name:", country.name())
print("Capital:", country.capital())
print("Population:", country.population())
print("Area (in square kilometers):", country.area())
print("Region:", country.region())
print("Subregion:", country.subregion())
print("Demonym:", country.demonym())
print("Currency:", country.currencies())
print("Languages:", country.languages())
print("Borders:", country.borders())