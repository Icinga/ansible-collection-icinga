import re

class Icinga2Parser(object):

    def parse(self, attrs, constants, indent=0):
        def attribute_types(attr):
            if re.search(r'^[a-zA-Z0-9_]+$', attr):
                result = attr
            else:
                result = '"'+ attr + '"'
            return result
            
    
        def value_types(value, indent=2):
            #TODO: Get Constant List from from Moduleparams or AnsibleVars
            # Values without quotes
            if ((r := re.search(r'^-?\d+\.?\d*[dhms]?$', value)) or (r := re.search(r'^(true|false|null)$', value)) or
                ( r := re.search(r'^!?(host|service|user)\.', value))):
                result = value
            elif (r := re.search(r'^(True|False)$', value)):
                result = value.lower()
            elif value in constants:
                # Check if it is a constant
                result = value
            else:
                # Print a normal string
                result = '"' + value + '"'
            return result
    
    
        def parser(row):
            result = ''
    
            # Disable parsing of the value if prefix -:
            if (r := re.search(r'^-:(.*)$', row)):
                #print("Ignore Row: " + row)
                return r.group(1)
    
            # r = re.search(r'^\{{2}(.+)\}{2}$', row)
            if (r := re.search(r'^\{{2}(.+)\}{2}$', row)):
                #Ex. '{{ testfuction in icinga2 }}'
                #print("Im a Function: " + row)
                result += "{{ %s }}" % (r.group(1))
            elif (r := re.search(r'^(.+)\s([\+-]|\*|\/|==|!=|&&|\|{2}|in)\s\{{2}(.+)\}{2}$', row)):
                #print("Im a expression with a function " + row )
                result += "%s %s {{ %s }}" % (parser(r.group(1)), r.group(2), r.group(3))
            elif (r := re.search(r'^(.+)\s([\+-]|\*|\/|==|!=|&&|\|{2}|in)\s(.+)$', row)):
                #print("Im a expression maybe assign " + row)
                result += "%s %s %s" % (parser(r.group(1)), r.group(2), parser(r.group(3)))
            else:
                if (r := re.search(r'^(.+)\((.*)$', row)):
                    #print("Irgendwas mit klammer %s(%s wahrscheinlich match(): " + row)
                    result += "Parser kommt noch"
                    # Alle Params der Funktion werden einzeln ohne Komma dem Parser übergeben und danach wieder zusammengeführt.
                    # result += "%s(%s" % [ $1, $2.split(',').map {|x| parse(x.lstrip)}.join(', ') ]
                elif (r := re.search(r'^ (.*)\)(.+)?$', row)):
                    # TODO: Parse functions
                    print("# closing bracket ) with optional access of an attribute e.g. '.arguments'" +
                          'result += "%s)%s" % [ $1.split(', ').map {|x| parse(x.lstrip)}.join(', '), $2 ]"')
                elif (r := re.search(r'^\((.*)$', row)):
                    result += "(%s" % (parser(r.group(1)))
                elif (r := re.search(r'^\s*\[\s*(.*)\s*\]\s?(.+)?$', row)):
                    #print("Its an array - process it " + row)
                    result += "[ %s]" % (process_array(r.group(1).split(',')))
                    if r.group(2):
                        result += " %s" % (parser(r.group(2)))
                elif (r := re.search(r'^\s*\{\s*(.*)\s*\}\s?(.+)?$', row)):
                    #print("Its an hash " + row)
                    result += "%s" % (process_hash(dict(list(divide_chunks((re.sub('\s*=\s*|\s*,\s*', ',', r.group(1)).split(',')), 2)))))
                    if r.group(2):
                        result += " %s" % (parser(r.group(2)))
                else:
                    result += str(value_types(row.lstrip(' ')))
   
            return result
    
    
        def process_array(items, indent=2):
            result=''
            for item in items:
                if type(item) is dict:
                    result += "\n%s{\n%s%s}, " % ( ' '*indent, process_hash(attrs=item, indent=indent+2), ' '*indent)
                elif type(item) is list:
                    result += "[ %s], " % ( process_array(item.split(','), indent=indent+2))
                else:
                    result += "%s, " % (parser(item))
            return result
    
        def process_hash(attrs, level=3, indent=2, prefix=' '):
            result = ''
            if re.search(r'^\s+$', prefix):
                prefix = prefix * indent
            op = ''
    
            for attr, value in attrs.items():
                if type(value) is dict:
                    if "+" in value:
                        del value['+']
                        op = "+"
                    if not bool(value):
                        #print("Its empty- moving on")
                        if level == 1:
                            result += "%s%s %s={}\n" % (prefix, attr, op)
                        elif level == 2:
                            result += "%s[\"%s\"] %s= {\n%s%s}\n" % (
                            prefix, attr, op, process_hash(attrs=value, indent=indent+2), ' '*indent)
                        else:
                            result += "%s%s %s= {\n%s%s}\n" % (
                            prefix, attribute_types(attr), op, process_hash(attrs=value, indent=indent+2), ' '*indent)
    
                    # "%s%s #{op}= {\n%s%s}\n" % [prefix, attribute_typess(attr), process_hash(value, indent + 2), ' ' * indent]
                    else:
                        #print("Next Level for: " + str(value))
                        #print(indent)
                        indent_char=' '
                        if level == 1:
                            result += process_hash(attrs=value, level=2, indent=indent, prefix=(prefix + attr))
                        elif level == 2:
                            result += "%s[\"%s\"] %s= {\n%s%s}\n" % (
                            prefix, attr, op, process_hash(attrs=value, indent=indent), (indent-2)*indent_char)
                        else:
                            result += "%s%s %s= {\n%s%s}\n" % (
                            prefix, attribute_types(attr), op, process_hash(attrs=value, indent=indent+2), ' '*indent)
                elif type(value) is list:
                    if value[0] == "+":
                        op = "+"
                        value.pop(0)
                    elif value[0] == "-":
                        op = "-"
                        value.pop(0)
                    if level == 2:
                        result += "%s[\"%s\"] %s= [ %s]\n" % (
                        prefix, attribute_types(attr), op, process_array(value))
                    else:
                        result += "%s%s %s= [ %s]\n" % (
                        prefix, attribute_types(attr), op, process_array(value))
                else:
                    if (r := re.search(r'^([\+,-])\s+', value)):
                        operator = r.group(1)
                        value = re.sub(r'^[\+,-]\s+', '', value)
                    else:
                        operator = ''
                    if level > 1:
                        if level == 3:
                            if value != None:
                                result += "%s%s %s= %s\n" % (
                                prefix, attribute_types(attr), operator, parser(value))
                        else:
                            if value != None:
                                result += "%s[\"%s\"] %s= %s\n" % (prefix, attr, operator, parser(value))
                    else:
                        if value != None:
                            result += "%s%s %s= %s\n" % (prefix, attr, operator, parser(value))
    
            return result
    
    
        def divide_chunks(l, n):
            for i in range(0, len(l), n):
                yield l[i:i + n]


        config = ''
        op = ''
    
        for attr, value in attrs.items():
            #if re.search(r'^(assign|ignore) where$', attr):
            if attr == 'assign' or attr == 'ignore':
                for x in value:
                  config += "%s%s %s\n" % (' '*indent, attr+' where', parser(x))
            elif attr == 'vars':
                if type(value) is dict:
                    if "+" in value:
                        del value['+']
                    config += process_hash(attrs=value, indent=indent+2, level=1, prefix=("%s%s." % (' '*indent, attr)))
                elif type(value) is list:
                    for item in value:
                        if type(item) is str:
                            config += "%s%s += %s\n" % (indent*' ', attr, re.sub(r'^[\+,-]\s+/', '', item))
                        else:
                            if "+" in item:
                                del item["+"]
                            if not bool(item):
                                config += "%s%s += {}\n" % ( ' ' * indent, attr)
                            else:
                                config += process_hash(attrs=item, indent=indent+2, level=1, prefix=("%s%s." % (' '*indent, attr)))
                else:
                    if re.search(r'^\+\s+', value):
                        op = '+'
                        value = re.sub(r'^\+\s+', '', str(value))
                    config += "%s%s %s= %s\n" % ( ' ' * indent, attr, op, parser(value) )
            else:
                if type(value) is dict:
                    if "+" in value:
                        op = '+'
                        del value['+']
                    if bool(value):
                        config += "%s%s %s= {\n%s%s}\n" % (' '*indent, attr, op, process_hash(attrs=value, indent=indent+2), ' '*indent)
                    else:
                        config += "%s%s %s= {}\n" % (' '*indent, op, attr)
                elif type(value) is list:
                    if value:
                        if value[0] == "+":
                            op = "+"
                            value.pop(0)
                        elif value[0] == "-":
                            op = "-"
                            value.pop(0)
                    config += "%s%s %s= [ %s]\n" % ( ' ' * indent, attr, op, process_array(value))
                elif value is None:
                    config += ''
                else:
                    if ( r:=re.search(r'^([\+,-])\s+', str(value))):
                        config += "%s%s %s= %s\n" % (' '*indent, attr, r.group(1), parser(re.sub(r'^[\+,-]\s+', '', str(value))))
                    else:
                        config += "%s%s = %s\n" % (' '*indent, attr, parser(str(value)))

        return config
