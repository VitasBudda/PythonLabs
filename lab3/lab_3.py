n = int(input('n = '))

country_cities = dict()

for _ in range(n):
    words = input().split()
    country_cities[words[0]] = words[1:]

m = int(input('m = '))

result = []

for _ in range(m):
    city = input()
    for country, cities in country_cities.items():
        if city in cities:
            result.append(country)
            break

print(*result, sep='\n')
