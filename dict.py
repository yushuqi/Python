people = {
	'alice': {
		'phone': '234341',
		'addr':'Foo drive 23'
	},

	'beth': {
		'phone': '2495',
		'addr':'bar street 53'
	},
	
	'cecil': {
		'phone': '0959',
		'addr':'baz avenue 90'
	}
}

labels = {
	'phone': 'phone number',
	'addr': 'address'
}

name = input('name: ')

request = input('Phone number (p) or adress(a)? ')

if request == 'p': key = 'phone'
if request == 'a': key = 'addr'

if name in people: print("%s's %s is %s." % \
	(name, labels[key], people[name][key]))
