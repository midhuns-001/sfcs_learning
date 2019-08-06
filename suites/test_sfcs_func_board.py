import unittest
from src.make_move import initial_params
from src.make_move import MakeMove 
from src.sfcs_logger import logger
from src.config_utils import ConfigUtil

class TestSFCSFunctionalBoard(unittest.TestCase):
    '''
        This suite covers all the functional aspects of the Board  parameters and vulnerabilities(if any)
    '''
    @classmethod
    def setUpClass(self):
        logger.info("\n\n ============================================ In SFCS TestSFCSFunctionalBoard setup Class ============================================")
        self.move_obj = MakeMove()
        self.config = ConfigUtil().readConfigurationFile()
        self.url = self.config['TEST_URL']
        self.id = self.config['SESSION_ID']
        self.json_rpc = self.config['JSON_RPC']
        self.playerState = self.config['PLAYER_STATE']
        self.move = "Nc3"
        self.params = {}
        
        '''
            Set the initial state of the board and make the first move here
        '''
        self.params  =  initial_params
        self.initial_state_of_the_board = {}
        self.params['playerState'] =   self.playerState
        self.params['move'] = self.move
   
    @classmethod
    def tearDownClass(self):
        logger.info("\n\n ============================================ In SFCS TestSFCSFunctionalBoard TearDown Class ============================================")

    def test01_sfcs_func_board_invalid_method_negative_01(self):
        """
            Test script to verify board functionality. Script to verify the board when an invalid method is been passed
        """
        logger.info("\n\n test01_sfcs_func_board_invalid_method_negative_01: Script to verify the board when an invalid method is been passed ")
        
        #invalid method
        self.method = "makemove"
        self.initial_state_of_the_board = {"method": self.method,
                                           "params": self.params,
                                           "id": self.id,
                                           "jsonrpc": self.json_rpc}
        result = self.move_obj.make_move(self.initial_state_of_the_board, self.url)
        self.assertTrue(result['error']['message'] == 'Unknown method: makemove', msg= "unknown method passed illegally to invoke a move")
        logger.info('End of case test01_sfcs_func_board_invalid_method_negative_01')

    def test02_sfcs_func_board_invalid_method_negative_02(self):
        """
            Test script to verify board functionality. Script to verify the board when an  method is passed as empty
        """
        logger.info("\n\n test02_sfcs_func_board_invalid_method_negative_02: Script to verify the board when an  method is passed as empty")
        
        #empty method
        self.method = ""
        self.initial_state_of_the_board = {"method": self.method,
                                           "params": self.params,
                                           "id": self.id,
                                           "jsonrpc": self.json_rpc}
        result = self.move_obj.make_move(self.initial_state_of_the_board, self.url)
        self.assertTrue(result['error']['message'] == 'no method specified', msg= "empty method passed illegally to invoke a move")
        logger.info('End of case test02_sfcs_func_board_invalid_method_negative_02')

    def test03_sfcs_func_board_invalid_playerstate_negative_03(self):
        """
            Test script to verify board functionality. Script to verify the invalid player state (W instead of w)
        """
        logger.info("\n\n test03_sfcs_func_board_invalid_playerstate_negative_03: Script to verify the invalid player states")
        self.method = "MakeMove"
        #invalid player state
        self.params['playerState'] =   "W"
        self.initial_state_of_the_board = {"method": self.method,
                                           "params": self.params,
                                           "id": self.id,
                                           "jsonrpc": self.json_rpc}
        result = self.move_obj.make_move(self.initial_state_of_the_board, self.url)
        self.assertTrue(result['error']['message'] == 'Could not create board with given inputs.', msg= "Should be a BoardError given invalid player state")
        logger.info('End of case test03_sfcs_func_board_invalid_playerstate_negative_03')

    def test04_sfcs_func_board_invalid_playerstate_negative_04(self):
        """
            Test script to verify board functionality. Script to verify the invalid player states (B instead of b)
        """
        logger.info("\n\n test04_sfcs_func_board_invalid_playerstate_negative_04: Script to verify the invalid player state")
        self.method = "MakeMove"
        #invalid player state
        self.params['playerState'] =   "B"
        self.initial_state_of_the_board = {"method": self.method,
                                           "params": self.params,
                                           "id": self.id,
                                           "jsonrpc": self.json_rpc}
        result = self.move_obj.make_move(self.initial_state_of_the_board, self.url)
        self.assertTrue(result['error']['message'] == 'Could not create board with given inputs.', msg= "Should be a BoardError given invalid player state")
        logger.info('End of case test04_sfcs_func_board_invalid_playerstate_negative_04') 

    def test05_sfcs_func_board_invalid_playerstate_negative_05(self):
        """
            Test script to verify board functionality. Script to verify the invalid player states (Invalid string passed to player state)
        """
        logger.info("\n\n test05_sfcs_func_board_invalid_playerstate_negative_05: Script to verify the invalid player state")
        self.method = "MakeMove"
        #invalid player state
        self.params['playerState'] =   "X"
        self.initial_state_of_the_board = {"method": self.method,
                                           "params": self.params,
                                           "id": self.id,
                                           "jsonrpc": self.json_rpc}
        result = self.move_obj.make_move(self.initial_state_of_the_board, self.url)
        self.assertTrue(result['error']['message'] == 'Could not create board with given inputs.', msg= "Should be a BoardError given invalid player state")
        logger.info('End of case test05_sfcs_func_board_invalid_playerstate_negative_05') 

    def test06_sfcs_func_board_invalid_playerstate_negative_06(self):
        """
            Test script to verify board functionality. Script to verify the invalid player states (Empty player state passed to player state)
        """
        logger.info("\n\n test06_sfcs_func_board_invalid_playerstate_negative_06: Script to verify the empty player state")
        self.method = "MakeMove"
        #invalid player state
        self.params['playerState'] =   ""
        self.initial_state_of_the_board = {"method": self.method,
                                           "params": self.params,
                                           "id": self.id,
                                           "jsonrpc": self.json_rpc}
        result = self.move_obj.make_move(self.initial_state_of_the_board, self.url)
        self.assertTrue(result['error']['message'] == 'Required param (playerState) missing or null', msg= "Required param (playerState) is not provided")
        logger.info('End of case test06_sfcs_func_board_invalid_playerstate_negative_06') 
      
    def test07_sfcs_func_board_invalid_boardstate_negative_07(self):
        """
            Test script to verify board functionality. Script to verify the empty boardstate 
        """
        logger.info("\n\n test07_sfcs_func_board_invalid_boardstate_negative_07: Script to verify the empty board state")
        self.method = "MakeMove"
        params ={}
        params['playerState'] =   "w"
        #empty board state
        params['boardState'] = []
        self.initial_state_of_the_board = {"method": self.method,
                                           "params": params,
                                           "id": self.id,
                                           "jsonrpc": self.json_rpc}
        result = self.move_obj.make_move(self.initial_state_of_the_board, self.url)
        self.assertTrue(result['error']['message'] == 'Required param (boardState) missing or null', msg= "Required param (boardState) is not provided")
        logger.info('End of case test07_sfcs_func_board_invalid_boardstate_negative_07') 
      
    def test08_sfcs_func_board_invalid_location_negative_08(self):
        """
            Test script to verify board functionality. Script to verify move to a location using invalid coin type  (n instead of N for Knight)
        """ 
        logger.info("\n\n test08_sfcs_func_board_invalid_location_negative_08: Script to verify move to a location using invalid coin type ")
        self.method = "MakeMove"
        #invalid player state
        self.params ={}
        self.params = initial_params
        self.params['playerState'] =   "w"
        self.params['playerState'] =   self.playerState
        #invalid move nc3 instead of Nc3 to move the knight
        self.params['move'] = "nc3"
        self.initial_state_of_the_board = {"method": self.method,
                                           "params": self.params,
                                           "id": self.id,
                                           "jsonrpc": self.json_rpc}
        result = self.move_obj.make_move(self.initial_state_of_the_board, self.url)
        self.assertTrue(result['error']['message'] ==  'Invalid move string.', msg= "Invalid coin type  coin trying to move to the location")
        logger.info('End of case test08_sfcs_func_board_invalid_location_negative_08') 
      
    def test09_sfcs_func_board_invalid_location_negative_09(self):
        """
            Test script to verify board functionality. Script to verify move to a location using invalid coin type  (Pawn movement)
        """
        logger.info("\n\n test09_sfcs_func_board_invalid_location_negative_09: Script to verify move to a location using invalid coin type   ")
        self.method = "MakeMove"
        #invalid player state
        self.params ={}
        self.params = initial_params
        self.params['playerState'] =   "w"
        self.params['playerState'] =   self.playerState
        #invalid move C3 instead of c3 to move the pawn
        self.params['move'] = "C3"
        self.initial_state_of_the_board = {"method": self.method,
                                           "params": self.params,
                                           "id": self.id,
                                           "jsonrpc": self.json_rpc}
        result = self.move_obj.make_move(self.initial_state_of_the_board, self.url)
        self.assertTrue(result['error']['message'] ==  'Invalid move string.', msg= "Invalid location to move pawn trying to move to a location")
        logger.info('End of case test09_sfcs_func_board_invalid_location_negative_09') 
         
    def test10_sfcs_func_board_invalid_location_negative_10(self):
        """
            Test script to verify board functionality. Script to verify an empty move 
        """
        logger.info("\n\n test10_sfcs_func_board_invalid_location_negative_10: Script to verifyempty move ")
        self.method = "MakeMove"
        #invalid player state
        self.params ={}
        self.params = initial_params
        self.params['playerState'] =   "w"
        self.params['playerState'] =   self.playerState
        #invalid move C3 instead of c3 to move the pawn
        self.params['move'] = ""
        self.initial_state_of_the_board = {"method": self.method,
                                           "params": self.params,
                                           "id": self.id,
                                           "jsonrpc": self.json_rpc}
        result = self.move_obj.make_move(self.initial_state_of_the_board, self.url)
        self.assertTrue(result['error']['message'] ==  'Required param (move) missing or null', msg= "Required param (move) is not provided")
        logger.info('End of case test10_sfcs_func_board_invalid_location_negative_10') 
         
if __name__ == "__main__":
    unittest.main()

