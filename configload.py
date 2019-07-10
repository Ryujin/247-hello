import cfg_load
fig = cfg_load.load('config.ini')
print(type(fig))
for section in fig:
    print(section)
print(fig['pickup'])
for entry in fig['pickup'] :
    print(entry)               #PRINTS THE KEYS
print(fig['tab']['x'])
print(fig['tab']['y'])
print(type(fig['tab']['y']))
yari1 = int(fig['tab']['y'])
print(type(yari1))
'''
Writing configuration ¶
import os
configfile_name = "config.ini"

# Check if there is already a configuration file
if not os.path.isfile(configfile_name):
    # Create the configuration file as it doesn't exist yet
    cfgfile = open(configfile_name, 'w')
#BUT: WE ALSO WANT TO OVERWRITE IT, IF IT DOES EXIST, FOR RECONFIGURATION, NO?
    # Add content to the file
    Config = ConfigParser.ConfigParser()
    Config.add_section('mysql')
    Config.set('mysql', 'host', 'localhost')
    Config.set('mysql', 'user', 'root')
    Config.set('mysql', 'passwd', 'my secret password')
    Config.set('mysql', 'db', 'write-math')
    Config.add_section('other')
    Config.set('other',
               'preprocessing_queue',
               ['preprocessing.scale_and_center',
                'preprocessing.dot_reduction',
                'preprocessing.connect_lines'])
    Config.set('other', 'use_anonymous', True)
    Config.write(cfgfile)
    cfgfile.close()
results in
[mysql]
host = localhost
user = root
passwd = my secret password
db = write-math

[other]
preprocessing_queue = ['preprocessing.scale_and_center', 'preprocessing.dot_reduction', 'preprocessing.connect_lines']
use_anonymous = True
'''