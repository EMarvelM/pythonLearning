#!/home/vagrant/pythonLearning/phaseIII/bin/python3
import cowsay
import sys

if len(sys.argv) == 2:
    cowsay.trex("Hello, " + sys.argv[1])
else:
    cowsay.cow("Hello, World!")