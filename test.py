from ga import Individual, TeamIndividual, GeneticAlgorithm


# ## Individual
# print("-------------------------------------------")
# ind1 = Individual()
# print(ind1)


# ## TeamIndividual
# print("-------------------------------------------")
# team = TeamIndividual()
# print(team)
# print("-------------------------------------------")
# team.initialize_random_team()
# print(team)


## GeneticAlgorithm
print("-------------------------------------------")

ag = GeneticAlgorithm()

# print("-------------------------------------------")
# # print(ag.oponent_team)
# ag.initialize_oponent_team()
# # # print(ag.oponent_team)
# # print("-------------------------------------------")
# # print(ag.population)
# ag.initialize_population()
# print("-------------------------------------------")
# # for x in ag.population:
# #     print(x)
# # #     print("-------------------------------------------")
# # #     print(len(x.team))
# # #     for y in x.team:
# # #         print(y)
# # # print(len(ag.population))
# # print("-------------------------------------------")
# # print(ag.fittest_team)
# # print("-------------------------------------------")
# # print(ag.historical_fitness)
# # print(ag.oponent_team)
# # print("-------------------------------------------")
# # for x in ag.population:
# #     print(x.fitness)
#     # print(x.fitness_list)
# # print("-------------------------------------------")
# # print(ag.global_gen_fitness)
# # print("-------------------------------------------")
# # print(ag.roulette_wheel_selection())

# print("-------------------------------------------")
# # print(ag.reproduce(ag.population))
# print("-------------------------------------------")
# # for x in (ag.population):
# #     print(x)
# # for x in ag.reproduce(ag.population):
# #     print(x)

# # print([ag.roulette_wheel_selection() for _ in range(ag.population_size)])

# for x in [ag.roulette_wheel_selection() for _ in range(ag.population_size)]:
#     print(x)
# print("-------------------------------------------")
ag.run()

# ag.initialize_oponent_team()
# ag.initialize_population()
# ag.calculate_population_fitness()
# for generation in range(3):
#     print(generation)
#     # selected_individuals = ag.tournament_selection() # for tournament selection
#     selected_individuals = [ag.roulette_wheel_selection() for _ in range(ag.population_size)]
#     for x in selected_individuals:
#         print(x)
#     new_population = ag.reproduce(selected_individuals, 0.1)
#     ag.population = new_population
#     ag.calculate_population_fitness()
#     ag.calculate_global_fitness()

#     fittest_team = ag.best_team_population(ag.population)
#     ag.historical_fitness.append(fittest_team.fitness)
#     ag.best_team(fittest_team)

#     print(f"Generation {generation}: Fittest individual has fitness {fittest_team.fitness}")
#     # if self.fittest_team >= 100:
#     #     print("Terminating because fittest individual has reached maximum fitness")
#     #     break