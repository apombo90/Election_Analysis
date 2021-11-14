# counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
# for county, voters in counties_dict.items():
#     message = f"{county} county has {voters} registered voters."
#     print(message)

voting_data = [{"county":"Arapahoe", "registered_voters": 422829}, {"county":"Denver", "registered_voters": 463353}, {"county":"Jefferson", "registered_voters": 432438}]
for dic in voting_data:
    message = f"{dic.get('county')} county has {dic.get('registered_voters'):,.0f} registered voters."
    print(message)