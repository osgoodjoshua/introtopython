glossary = {
    'variable' : 'A thing that can be assigned a value.',
    'value' : 'A string, number, boolean, etc that can define an item.',
    'list' : 'Using brackets, you can group items or elements into one thing.',
    'for loops' : 'A way to loop through information to gain results or move data.',
    'conditional testing' : 'Using certain criteria to determine whether data matches or has different value'
    }

for i in glossary:
    print('\n' + i.title() + ': \n' + glossary[i])