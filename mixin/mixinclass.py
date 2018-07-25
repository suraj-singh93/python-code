class strmixin(object):


    def __attrnames(self):
        result = ''
        for attr in dir(self):
            if attr[:2] == '__' and attr[-2:] == '__':
                result += '\t{}\n'.format(attr)
            else:
                result += '\t{}={}\n'.format(attr,getattr(self,attr))
        return result

    def __str__(self):
        return 'Instanceof: {0}\n address: {1}\n attributes: {2}'.format(self.__class__.__name__, id(self), self.__attrnames())


class test(strmixin):
     def __init__(self,topt):
         self.topt = topt


a = test(2)


print(a)