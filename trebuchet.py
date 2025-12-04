# Author: Hemanth Bathini
# Date: 10/08/24
# Description: This Python program tracks and ranks the top three farthest distances recorded from multiple trials.
# It prompts the user to enter the distance for each trial and
# keeps updating the top three distances as new values are input.
top_three_distances = [0, 0, 0]
top_three_trials = [0, 0, 0]

continue_input = "Y"
trial_number = 1

while continue_input.upper() == "Y":
    distance = int(input(f"Enter the distance for trial {trial_number}: "))
    if distance > top_three_distances[0]:
        top_three_distances[2] = top_three_distances[1]
        top_three_trials[2] = top_three_trials[1]
        top_three_distances[1] = top_three_distances[0]
        top_three_trials[1] = top_three_trials[0]
        top_three_distances[0] = distance
        top_three_trials[0] = trial_number
    elif distance > top_three_distances[1]:
        top_three_distances[2] = top_three_distances[1]
        top_three_trials[2] = top_three_trials[1]
        top_three_distances[1] = distance
        top_three_trials[1] = trial_number
    elif distance > top_three_distances[2]:
        top_three_distances[2] = distance
        top_three_trials[2] = trial_number

    continue_input = input("Would you like to enter another trial? (Y/N): ").strip().upper()
    trial_number += 1

print("\nTop 3 Farthest Distances:")
print(f"{'Trial':<10} {'Distance'}")
for i in range(3):
    if top_three_distances[i] > 0:
        print(f"{top_three_trials[i]:<10} {top_three_distances[i]}")

