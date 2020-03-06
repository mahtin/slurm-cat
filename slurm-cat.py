#!/usr/bin/env python3
""" slurm-cat - RFC8416 SLURM"""

import sys
import json

def read_file(filename):
	""" read a JSON file - exit if it fails"""
	try:
		fd = open(filename, 'r')
	except:
		sys.exit('%s: failed to read file' % filename)
	try:
		j = json.load(fd)
	except:
		sys.exit('%s: file has bad json format' % filename)
	fd.close()
	return j

def doit(args):
	""" sum SLURM files and output results"""

	# build resulting summation into this structure
	result = {
		'slurmVersion': 1,
		'validationOutputFilters': {
			'prefixFilters': [],
			'bgpsecFilters': []
		},
		'locallyAddedAssertions': {
			'prefixAssertions': [],
			'bgpsecAssertions': []
		}
	}

	for filename in args:
		# basic test for JSON success done here
		j = read_file(filename)

		# This code is for SMURM version 1
		if j['slurmVersion'] != 1:
			sys.exit('%s: SLURM file is not version 1' % filename)

		# This mainly confirms the SLURM format is correct as per RFC8416
		# each section MUST exist
		try:
			validationOutputFilters = j['validationOutputFilters']
			prefixFilters = validationOutputFilters['prefixFilters']
			bgpsecFilters = validationOutputFilters['bgpsecFilters']

			locallyAddedAssertions = j['locallyAddedAssertions']
			prefixAssertions = locallyAddedAssertions['prefixAssertions']
			bgpsecAssertions = locallyAddedAssertions['bgpsecAssertions']
		except:
			sys.exit('%s: SLURM file has bad format' % filename)

		# if the section is empty - nothing is summed
		for element in prefixFilters:
			result['validationOutputFilters']['prefixFilters'] += [element]
		for element in bgpsecFilters:
			result['validationOutputFilters']['bgpsecFilters'] += [element]
		for element in prefixAssertions:
			result['locallyAddedAssertions']['prefixAssertions'] += [element]
		for element in bgpsecAssertions:
			result['locallyAddedAssertions']['bgpsecAssertions'] += [element]

	# the no sorting option could help with debug
	print(json.dumps(result, indent=4, sort_keys=False))

def main(args=None):
	""" slurm-cat - RFC8416 SLURM"""
	if args is None:
		args = sys.argv[1:]
	if len(args) == 0:
		sys.exit('slurm-cat: usage: slurm-cat filename [filename ...]')

	doit(args)

if __name__ == '__main__':
	main()
