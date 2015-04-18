import json
from pprint import pprint

with open('example.json') as data_file:
	data = json.load(data_file)

blueprint = data["blueprint"].split()

alias = open(blueprint[0], 'w')

# Function declration.
alias.write('#!/usr/bin/env bash\n\n' + blueprint[0] + '() {')

# Obtaining alias arguments.
alias.write('\n\tparameters=(${@:1:$(($#-($#-' + str(len(data['arguments'])) + ')))})')

alias.write('\n\n\tcase ${#parameters[@]} in')

for number_of_arguments in range(0, len(data['arguments']) + 1):
	alias.write('\n\t\t' + str(number_of_arguments) + ' ) ')

	for index, argument in enumerate(data['arguments']):
		alias.write(argument + 'Set=')

		if index < number_of_arguments:
			alias.write('true')
		else:
			alias.write('false')

		alias.write('\n\t\t\t\t')

	alias.write(';;\n');

alias.write('\tesac')

alias.write('\n\n\techo');
for argument in data['arguments']:
	alias.write(' $' + argument + 'Set')
alias.write('\n')

for index, argument in enumerate(data['arguments']):
	alias.write('\n\tif $' + argument + '; then\n\t\t')
	if data['blueprint'][data['blueprint'].index(argument) - 1] == '*':
		alias.write(argument + '=${parameters[' + str(index) + ']}')
	else:
		alias.write('case ${parameters[' + str(index) + ']} in')

		for value in data['arguments'][argument]['values']:
			if value != 'default':
				alias.write('\n\t\t\t"' + value + '" ) ' + argument + '="' + data['arguments'][argument]['values'][value] + '";;\n')

		invalidValueError = data['arguments'][argument]['errors']['invalid']
		for invalidValueErrorArgumentIndex, invalidValueErrorArgument in enumerate(data['arguments']):
			invalidValueError = invalidValueError.replace('{' + invalidValueErrorArgument + '}', '${parameters[' + str(invalidValueErrorArgumentIndex) + ']}')

		alias.write('\n\t\t\t* )' + ' echo "' + invalidValueError + '";;')

		alias.write('\n\t\tesac')

	alias.write('\n\telse')
	alias.write('\n\t\t' + argument + '="' + data['arguments'][argument]['values']['default'] + '"')
	alias.write('\n\tfi')

	alias.write('\n')

# Generate command from blueprint and data.
command = data['blueprint']

# Call the blueprint's command.
# alias.write('\n' + str(command))

# Close the function declration.
alias.write('\n}')

# Call the function...
alias.write('\n\n' + blueprint[0] + ' $@')

alias.close()
