#!/usr/bin/env python3
import sys
import json
assert sys.version_info >= (3,9), "This script requires at least Python 3.9"


game1 = open('keepbreathing.JSON')
game2 = open('kingandcountry.JSON')
client = "yes"
option = ""

while(True):
	client.lower().strip()
	if client == 'yes':
		while(True):
			print("Welcome to Jarus Game Client. Please choose which game to play.")
			print("a for Keep Breathing")
			print("b for King and Country")
			print("q to quit Game Client")
			r = input()
			r = r.lower().strip()
			if r == "a":
				world = json.load(game1)
				option = "breathing"
				break
			elif r == "b":
				world = json.load(game2)
				option = "king"
				break
			elif r == "q":
				print("please come again,")
				break
			else:
				print("Please try again")

		# ----------------------------------------------------------------

		def find_current_location(location_label):
			if "passages" in world:
				for passage in world["passages"]:
					if location_label == passage["name"]:
						return passage
			return {}

		# ----------------------------------------------------------------
		if option == "breathing":
			def render(current_location, oxygen, moves):
				if "name" in current_location and "cleanText" in current_location:
					print("You are at the " + str(current_location["name"]))
					print(current_location["cleanText"] + "\n")
					print("Moves: {m}, oxygen: {s}".format(m = moves, s = oxygen))
					# print("Moves: " + str(moves) + ", oxygen: " + str(oxygen))

			def get_input():
				response = input("What do you want to do? ")
				response = response.lower().strip()
				return response

			def update(current_location, location_label, response):
				if response == "":
					return location_label
				if "links" in current_location:
					for link in current_location["links"]:
						if link["linkText"] == response:
							return link["passageName"]
				print("I don't understand what you are trying to do. Try again.")
				return location_label


			# ----------------------------------------------------------------

			location_label = "Prison Cell"
			current_location = {}
			response = ""
			oxygen = 100
			moves = 0

			while True:


				if response == "QUIT" or "win" in current_location or oxygen == 0:
					finalScore = oxygen + moves
					break
				location_label = update(current_location, location_label, response)
				current_location = find_current_location(location_label)
				if "oxygen" in current_location:
					oxygen += current_location["oxygen"]
				render(current_location, oxygen, moves)
				response = get_input()
				


			print("Your Final Score is ", str(finalScore), "Thanks for playing!")

		elif option == "king":

			def render(current_location, exp):
				if "name" in current_location and "cleanText" in current_location:
					print("You are at the " + str(current_location["name"]))
					print(current_location["cleanText"] + "\n")
					print("Exp: {s}".format(s = exp))

			def get_input():
				response = input("What do you want to do? ")
				response = response.lower().strip()
				return response

			def update(current_location, location_label, response):
				if response == "":
					return location_label
				if "links" in current_location:
					for link in current_location["links"]:
						if link["linkText"] == response:
							return link["passageName"]
				print("I don't understand what you are trying to do. Try again.")
				return location_label


			# ----------------------------------------------------------------

			location_label = "Start"
			current_location = {}
			response = ""
			exp = 0

			while True:


				if response == "QUIT" or "win" in current_location:
					print("You have won. Good Job!")
					break
				if "dead" in current_location:
					print("You have died")
					break
				location_label = update(current_location, location_label, response)
				current_location = find_current_location(location_label)
				if "exp" in current_location:
					exp += current_location["exp"]
				render(current_location, exp)
				response = get_input()
			
			print("Your Final Score is ", str(exp), "Thanks for playing!")
	elif client == "no":
		print("Goodbye!")
		break
	else:
		print("Not Applicable Please try again")

	print("Would you like to keep playing in the game client? Yes or No")
	client = input()
	client = client.lower().strip()
