def importAs(module_name):
    return __import__(module_name)

sys = importAs('sys')
print sys.path