#!/usr/bin/env python

from optparse import OptionParser
import ConfigParser
import yaml


parser = OptionParser()
parser.add_option("-p", "--profile",  dest="profile",  help="use profile")
parser.add_option("-n", "--name",  dest="name",  help="environment name")
parser.add_option("-a", "--action",  dest="action",  help="requested action on env")

(options, argList) = parser.parse_args()

#print "argList:", argList
args = {}
for arg in argList:
    aa = arg.split('=')
    args[aa[0]] = aa[1]
print "args:", args

conf = ConfigParser.SafeConfigParser({})

conf.read("cloudforge.conf")

def usage():
    print "%s: --profile PROFILE --name ENVNAME --action {create|delete} arg1=val1 [arg2=val2 ...]" % (sys.argv[0],)

profileSource = "profiles/%s.yaml" % options.profile
stream = file(profileSource, 'r')
profileContent = stream.read()

profile = yaml.load(profileContent)
#print yaml.dump(profile, default_flow_style=False)

runtimeArgs = profile['instance']
print "runtimeArgs:", runtimeArgs

for paramName, paramKey in runtimeArgs.iteritems():
    #print "arg=%s, val=%s" % (arg, val)
    newContent = profileContent.replace('$(' + paramKey + ')', args[paramName])
    profileContent = newContent

profile = yaml.load(profileContent)
print "******************************************************"
print yaml.dump(profile, default_flow_style=False)

#if options.action == 'create':
