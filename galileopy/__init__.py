import pandas as pd
import os

def help():
    '''
    In the future, this will be more helpful.
    '''
    print('Set the GO_PDS_PATH environment variable in your shell profile/rc file.')
    print('    Bash: export GO_PDS_PATH="User/myname/data/GO"')
    print('Get the index for a volume of data.')
    print('    mag_index = go.Index("GO-J-MAG-3-RDR-HIGHRES-V1.0")')
    return None

class Index(dict):
    '''
    The index of a dataset is somewhat special.
    A pandas DataFrame handles it nicely though.
    But it ought to have the other attributes in the LBL file as well.
    So it will be a dict.
    It's kind of a special case of a Product with a table object.
    In which the table is very easy to find and read.
    '''
    def __init__(self, dataset):
        if 'GO_PDS_PATH' in os.environ:
            self.read_index_tab(os.path.join(os.environ['GO_PDS_PATH'],dataset,'INDEX/INDEX.TAB'))
            [attributes_keys, attributes, pointers_keys, pointers, objects] = _parse_odl(
                os.path.join(os.environ['GO_PDS_PATH'],dataset,'INDEX/INDEX.LBL'))
        else:
            _scream_go_path_env()
        return None
    
    def read_index_tab(self, index_tab):
        go_index = pd.read_csv(index_tab)
        go_index.columns = go_index.columns.str.strip()
        for k in go_index.keys():
            go_index[k] = go_index[k].str.strip() 
        self.index = go_index
        return None

class Product(dict):
    '''
    There are lots of different kinds of Products in a PDS dataset.
    But they all have attributes.
    So I think a dict is general enough for that.
    '''

def _scream_go_path_env():
    print("galileopy: We've gotta know where your data is! "
           "Please set the GO_PDS_PATH environment variable to the path "
           "where you'll keep your datasets.")
    return None
    
def _parse_odl(lbl_file):
    '''
    An (incomplete) parser for ODL (Object Definition Language).
    For specifications see https://pds.jpl.nasa.gov/documents/sr/Chapter12.pdf
    The idea is to parse it all into something python can use to make a dict.
    So, separate out keys from the attributes themselves
    and sort them into dicts
    find the pointers for each object
    And in particular, handle Objects by making a dict for them
    most attributes are one line
    many are not though, eg lists and descriptions
    so when we read a line, the decisions we must make are:
    1) Do I need to read more lines to finish this attribute?
    2) If not, is this a pointer to a file in the dataset?
    3) If so, append the key to pointers_keys and the path to pointers.
    4) If I don't need to read more lines and this isn't a pointer,
       is this a reserved identifier?
    5) If not, append the key to attributes_keys and the attribute to attributes.
    6) If it is a RI then I need to treat accordingly.
    '''
    reserved_identifiers = ['END','END_GROUP','END_OBJECT','GROUP','OBJECT','BEGIN_OBJECT']
    
    attributes_keys = []
    attributes = []
    pointers_keys = []
    pointers = []
    objects = []
    
    return [attributes_keys, attributes, pointers_keys, pointers, objects]

def _attach_labels(self,stuff):
    '''
    This function is for attaching the stuff that was parsed out of the LBL file
    onto a Product or Index
    '''
#    for k in range(len(attributes_keys)):
#        self.[attributes_keys[k]] = attributes[k]
    return None
