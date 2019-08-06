import os
import yaml
from src.sfcs_logger import logger

class ConfigUtil(object):
    '''
         Reads the configuration file and writes the content to a dictionary
    '''
    #className = None
    def readConfigurationFile(self, dict_or_object={}):
        if type(dict_or_object) == type(dict()):
            kwargs = dict_or_object
        else:
            kwargs = dict_or_object.__dict__
        
        try:
          
            tb_file = str(os.getenv("testconfig_file"))
            # Load YAML Value    
            default_dict = yaml.load(open(tb_file))
            
        except:
            raise RuntimeError("testconfig_file IS NOT SET IN ENVIRONMENT OR GIVEN CONFIG FILE DOES NOT EXIST. PLEASE SET export testconfig_file='/Location/FileName' ")
        
        default_dict.update(kwargs)
        
        TEST_URL = default_dict['TEST_URL'] if "TEST_URL" in default_dict \
        else self.__raise_exception("CONFIG FILE DOES NOT HAVE 'TEST_URL' VARIABLE , PLEASE DEFINE LIKE TEST_URL=http://chesstest.solidfire.net:8080/json-rpc")
        default_dict['TEST_URL'] = kwargs.get('TEST_URL', TEST_URL)
        default_dict['JSON_RPC'] = default_dict.get('JSON_RPC', "2.0")
        default_dict['SESSION_ID'] = default_dict.get('SESSION_ID', 1)
        default_dict['TEST_METHOD'] = default_dict.get('TEST_METHOD', " MakeMove")
        default_dict['PLAYER_STATE'] = default_dict.get('PLAYER_STATE',"w")

        logger.info("Reading test config file \n\n")
        logger.info(default_dict)
        return default_dict
