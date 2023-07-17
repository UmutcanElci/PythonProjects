from googlesearch import search
import requests

a = input("Question:")

sites = [
    "https://www.geeksforgeeks.org",
    "https://stackoverflow.com/",
    "https://realpython.com/",
    "https://www.w3schools.com/",
    "https://www.tutorialspoint.com/",
    "https://medium.com/",
    "https://www.w3resource.com/",
    
]
search_results = []

for site in sites:
    search_result = search(a + "site:" + site, num_results=5)
    search_results.append(search_result)
    

for result in search_result:
    print(result)
    
selected_site = input("Which site you want to choose ? ")
get_site = search_results.index(selected_site)
requests.get(selected_site)
