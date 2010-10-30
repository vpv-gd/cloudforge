#!/usr/bin/env python

from optparse import OptionParser
import yaml


parser = OptionParser()
parser.add_option("-p", "--profile",  dest="profile",  help="use profile")
parser.add_option("-n", "--name",  dest="name",  help="environment name")
parser.add_option("-a", "--action",  dest="action",  help="requested action on env")
parser.add_option("-r", "--raw",  dest="rawparam",  help="raw overwrite parameters file")

(options, argList) = parser.parse_args()

#print "argList:", argList
args = {}
for arg in argList:
    aa = arg.split('=')
    args[aa[0]] = aa[1]
print "args:", args


configfile = "cloudforge.yaml"
stream = file(configfile, 'r')
conf = yaml.load(stream)
stream.close()
#print "CONFIG"
#print yaml.dump(conf, default_flow_style=False)

profileSource = "profiles/%s.yaml" % options.profile
stream = file(profileSource, 'r')
profileContent = stream.read()
stream.close()

profile = yaml.load(profileContent)
#print yaml.dump(profile, default_flow_style=False)

instanceArgs = profile['instance']
print "instanceArgs:", instanceArgs

for paramName, paramKey in instanceArgs.iteritems():
    #print "arg=%s, val=%s" % (arg, val)
    newContent = profileContent.replace('$(' + paramKey + ')', args[paramName])
    profileContent = newContent

profile = yaml.load(profileContent)
print "******************************************************"
print yaml.dump(profile, default_flow_style=False)

for m in finditer("\$\{.+\}",profileContent):
    print m

#if options.action == 'create':
