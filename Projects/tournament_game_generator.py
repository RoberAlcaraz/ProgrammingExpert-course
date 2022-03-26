
# Number of teams
number_of_teams = input('Enter the number of teams: ')

while True:
    if number_of_teams.isdigit():
        number_of_teams = int(number_of_teams)
        if number_of_teams < 2:
            print('The minimum number of teams is 2, try again.')
            number_of_teams = input('Enter the number of teams: ')
        else:
            break
    else:
        print('Please enter a valid number.')
        number_of_teams = input('Enter the number of teams: ')

# Team names
team_names = []

for i in range(1, number_of_teams+1):
    team_name = input(f'Enter the name for team #{i}: ')
    while len(team_name.split(' ')) > 2 or len(team_name) < 2:
        if len(team_name.split(' ')) > 2:
            print('Team names may have at most 2 words, try again.')
        else:
            print('Team names must have at least 2 characters, try again.')
        team_name = input(f'Enter the name for team #{i}: ')

    team_names.append(team_name)

# Number of games played:
number_of_games = int(input('Enter the number of games played by each team: '))
while number_of_games < number_of_teams - 1:
    print('Invalid number of games. Each team plays each other at least once in the regular season, try again.')
    number_of_games = int(
        input('Enter the number of games played by each team: '))

# Number of wins
number_of_wins = {}
for team in team_names:
    number_of_wins[team] = int(
        input(f'Enter the number of wins Team {team} had: '))
    while number_of_wins[team] < 0 or number_of_wins[team] > number_of_games:
        if number_of_wins[team] < 0:
            print('The minimum number of wins is 0, try again.')
        else:
            print('The maximum number of wins is 6, try again.')
        number_of_wins[team] = int(
            input(f'Enter the number of wins Team {team} had: '))

# Generating the games to be played:

print('Generating the games to be played in the first round of the tournament...')
team_order = {k: v for k, v in sorted(
    number_of_wins.items(), key=lambda item: item[1])}
team_order = [key for key in team_order.keys()]
for _ in range(int(number_of_teams/2)):
    print(f'Home: {team_order[0]} VS Away: {team_order[len(team_order) - 1]}')
    team_order.pop(0)
    team_order.pop(len(team_order) - 1)
