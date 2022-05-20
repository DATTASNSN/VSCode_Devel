from calendar import c


def tournamentWinner(competitions, results):
    # Write your code here.
	winners_dict = {}
	count=0
	for home_team,away_team in competitions:
		if results[count] == 0:
			if away_team in winners_dict:
				winners_dict[away_team] += 3
			else:
				winners_dict[away_team] = 3
		elif results[count] == 1:
			if home_team in winners_dict:
				winners_dict[home_team] += 3
			else:
				winners_dict[home_team] = 3
		count+=1
	fin_max = max(winners_dict, key=winners_dict.get)
	return fin_max


competitions= [
  ["HTML", "C#"],
  ["C#", "Python"],
  ["Python", "HTML"]
]
results= [0, 0, 1]
print(tournamentWinner(competitions, results))

# {
#   "competitions": [
#     ["HTML", "Java"],
#     ["Java", "Python"],
#     ["Python", "HTML"]
#   ],
#   "results": [0, 1, 1]
# }