#!/usr/bin/env python

from optparse import OptionParser
import ConfigParser


parser = OptionParser()
parser.add_option("-p", "--profile",  dest="profile",  help="used profile")
#parser.add_option("-n", "--name",  dest="name",  help="environment name")
#parser.add_option("-b", "--build", dest="build", help="build number")

(options, args) = parser.parse_args()

conf = ConfigParser.SafeConfigParser({})

conf.read("cloudforge.conf")

def usage():
	print "%s: --profile PROFILE arg1=val1 [arg2=val2 ...]" % (sys.argv[0],)



