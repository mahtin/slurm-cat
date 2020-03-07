#!/usr/bin/env python3
""" slurm-cat - RFC8416 SLURM"""

import sys
import json

def read_file(filename):
	""" read a JSON file - exit if it fails"""
	try:
		if filename == '-':
			fd = sys.stdin
		else:
			fd = open(filename, 'r')
	except (FileNotFoundError,PermissionError) as e:
		sys.exit('%s: %s' % (filename, e))
	try:
		j = json.load(fd)
	except Exception as e:
		sys.exit('%s: %s' % (filename, e))
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

		# This code is for SLURM version 1
		try:
			if j['slurmVersion'] != 1:
				sys.exit('%s: SLURM file is not version 1' % filename)
		except KeyError as e:
			sys.exit('%s: SLURM file has bad format, %s missing' % (filename, e))

		# This mainly confirms the SLURM format is correct as per RFC8416
		# each section MUST exist
		try:
			validationOutputFilters = j['validationOutputFilters']
			prefixFilters = validationOutputFilters['prefixFilters']
			bgpsecFilters = validationOutputFilters['bgpsecFilters']
			locallyAddedAssertions = j['locallyAddedAssertions']
			prefixAssertions = locallyAddedAssertions['prefixAssertions']
			bgpsecAssertions = locallyAddedAssertions['bgpsecAssertions']
		except KeyError as e:
			sys.exit('%s: SLURM file has bad format, %s missing' % (filename, e))

		# throw these values into the result
		result['validationOutputFilters']['prefixFilters'] += prefixFilters
		result['validationOutputFilters']['bgpsecFilters'] += bgpsecFilters
		result['locallyAddedAssertions']['prefixAssertions'] += prefixAssertions
		result['locallyAddedAssertions']['bgpsecAssertions'] += bgpsecAssertions

	# the no sorting option could help with debug
	print(json.dumps(result, indent=4, sort_keys=False))

def main(args=None):
	""" slurm-cat - RFC8416 SLURM"""
	if args is None:
		args = sys.argv[1:]
	if len(args) == 0:
		# just like cat - use stdin
		args = ['-']

	doit(args)

if __name__ == '__main__':
	main()
