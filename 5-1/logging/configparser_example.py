import configparser
config = configparser.ConfigParser()

config.read('example.cfg')
print(config.sections())

# 안에 있는 값 접근하려면 for loop
# print(config['SectionThree'])
for key in config['SectionOne']:
    value = config['SectionOne'][key]
    print("{0} : {1}".format(key, value))
