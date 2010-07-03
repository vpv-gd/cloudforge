#!/usr/bin/env python

from optparse import OptionParser
import ConfigParser
import yaml


parser = OptionParser()
parser.add_option("-p", "--profile",  dest="profile",  help="use profile")
parser.add_option("-n", "--name",  dest="name",  help="environment name")

(options, args) = parser.parse_args()

conf = ConfigParser.SafeConfigParser({})

conf.read("cloudforge.conf")

def usage():
	print "%s: --profile PROFILE arg1=val1 [arg2=val2 ...]" % (sys.argv[0],)

profileSource = "profiles/%s.yaml" % options.profile
stream = file(profileSource, 'r')
profile = yaml.load(stream)

print yaml.dump(profile, default_flow_style=False)

