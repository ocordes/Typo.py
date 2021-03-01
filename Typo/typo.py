"""

Typo.py/typo.py

written by: Oliver Cordes 2021-03-01
changed by: Oliver Cordes 2021-03-01

"""

import os, sys
import re

import io

from pkg_resources import resource_filename

dict_dir = 'dictionaries'

class Typo(object):
    def __init__(self, lang, affData=None, wordData=None):
        self.flag = {}
        if not affData:
            filename = resource_filename(__name__, os.path.join(f'{dict_dir}/{lang}/{lang}.aff'))
            affData = self.readDataFile(filename)
        if not wordData:
            filename = resource_filename(__name__, os.path.join(f'{dict_dir}/{lang}/{lang}.dic'))
            wordData = self.readDataFile(filename)

        self.rules = self.parseAFF(affData)



    def readDataFile(self, filename):
        lines = []
        with io.open(filename, 'r', encoding='utf-8') as f:
            for line in f:
                line = re.sub(r"(?i)( )* #.*$", "", line.strip())  # remove the comments
                if line != '':
                    lines.append(line)

        return lines


    def parseRuleCodes(self, textCodes):
        if not textCodes:
            return []
        elif 'FLAG' not in self.flags:
            print('parseRuleCodes check FLAG')
            return textCodes.split()
        elif self.flags['FLAG'] == 'long':
            flags = []
            for i in range(len(textCodes)//2):
                flags.append(textCodes[i*2:(i+1)*2])

            return flags
        elif self.flags['FLAG'] == 'num':
            return textCodes.split(',')
        else:
            print('parseRuleCodes ending')
            
        return None
        


    def parseAFF(self, lines):
        i = 0
        while i < len(lines):
            line = lines[i]
            definitionsParts = line.split()

            ruleType = definitionsParts[0]

            if (ruleType == 'PFX') or (ruleType == 'SFX'):
                ruleCode = definitionsParts[1]
                combineable = definitionsParts[2]
                numEntries = int(definitionsParts[3])

                entries = []

                for j in range(i+1, i+1+numEntries):
                    subline = lines[j]

                    lineParts = subline.split()
                    charactersToRemove = lineParts[2]
                    additionParts = lineParts[3].split('/')

                    charactersToAdd = additionParts[0]
                    if (charactersToAdd == '0'):
                        charactersToAdd = ''

                    continuationClasses = this.parseRuleCodes(additionParts[1])

                    regexToMatch = lineParts[4]

                    entry = {}
                    entry.add = charactersToAdd




            # next line
            i++



    def check(self, word):
        return True


    def suggest(self, word):
        return []
