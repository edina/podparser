import re

class PodEntry():

    def __init__(self, line):
        self.line = line
        self.profession = ''
        self.valid = True
        self._parse()

    def _parse(self):
        columns = self.line.split(',')

        if len(columns) > 2:
            self.surname = columns[0]
            self.forename = columns[1]

            if len(columns) == 3:
                self.address = columns[2]
            elif len(columns) == 4:
                # if the third column has a number in it its probably an an address
                if re.search('\d', columns[2]):
                  
                    self.address = '%s,%s' % (columns[2], columns[3])
                    print '* %s %s %s ' % (self.surname, self.forename, self.address)
                else:
                    self.profession = columns[2]
                    self.address = columns[3]
            else:
                # there are more than four columns, use the number in the address to divide them
                remaining = None
                for column in columns[2: len(columns)]:
                    if remaining:
                        remaining = '%s,%s' % (remaining, column)
                    else:
                        remaining = column

                match = re.search('.+(\d)', remaining)
                
                if match:
                    # there is a number get the index
                    num_index = remaining.find(match.group(1))

                    # comma to left of number
                    comma_index = remaining[0: num_index].rfind(',')
                else:
                    # no number just assign the third column to profession and the rest to the address
                    comma_index = remaining.find(',')
                    
                self.profession = remaining[0: comma_index]
                self.address = remaining[comma_index + 1: len(remaining)]
        else:
            # anything with less than 3 columns is invalid
            self.valid = False

    def print_entry(self):
        if self.valid:
            print '%s | %s | %s | %s' % (self.surname, self.forename, self.profession, self.address)
        else:
            print self.line 

class EntryChecker():

    def __init__(self):
        pass

    def clean_up(self, entry):
        #self.entry = entry
        pass