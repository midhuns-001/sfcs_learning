import unittest
from src.make_move import initial_params
from src.make_move import MakeMove 
from src.sfcs_logger import logger
from src.config_utils import ConfigUtil

class TestSFCSFunctionalQueen(unittest.TestCase):
    '''
        This suite covers all the functional aspects of the coin Queen on the chess board. Movements, conditions & illegal actions
    '''
    @classmethod
    def setUpClass(self):
        logger.info("\n\n ============================================ In SFCS TestSFCSFunctionalQueen setup Class ============================================")
        self.move_obj = MakeMove()
        self.config = ConfigUtil().readConfigurationFile()
        self.url = self.config['TEST_URL']
        self.id = self.config['SESSION_ID']
        self.json_rpc = self.config['JSON_RPC']
        self.method = self.config['TEST_METHOD']
        self.playerState = self.config['PLAYER_STATE']
        self.move = "Na3"
        self.params = {}
        '''
            Set the initial state of the board and make the first move here
        '''
        self.params  =  initial_params
        self.initial_state_of_the_board = {}
        self.params['playerState'] =   self.playerState
        self.params['move'] = self.move
        self.initial_state_of_the_board = {"method": self.method,
                                           "params": self.params,
                                           "id": self.id,
                                           "jsonrpc": self.json_rpc}
        
        logger.info("SetupClass: Make the initial move on the chess board")
        result = self.move_obj.make_move(self.initial_state_of_the_board, self.url)
        (self.player_state, self.game_state, self.board_state) = self.move_obj.get_states_from_last_move(result)    

    
    @classmethod
    def tearDownClass(self):
        logger.info("\n\n ============================================ In SFCS TestSFCSFunctionalQueen TearDown Class ============================================")

    def test01_func_sfcs_queen_movements_positive_01(self):
        """
            Test script to verify queen movements horizontal and vertical (forward) and get killed

        """
        logger.info("\n\n test01_func_sfcs_queen_movements_positive_01: Test script to verify queen movements horizontal and vertical and get killed ")
        movement_list = ['Nf6', 'd4', 'h5', 'Qd3' , 'c6', 'Qb3', 'Nd5', 'Qxb7', 'Bxb7']
        self.next_move = {"method": self.method, "params":{}, "id": self.id, "jsonrpc": self.json_rpc}
        self.move_obj.make_iter_moves_for_game_action( (self.player_state, self.game_state, self.board_state), self.next_move,  movement_list, self.url, error_flag= True)
        logger.info('End of case test01_func_sfcs_queen_movements_positive_01')

    def test02_func_sfcs_queen_movements_positive_02(self):
        """
            Test script to verify queen movements diagonal (forward) and issue a check

        """
        logger.info("\n\n test02_func_sfcs_queen_movements_positive_02: Test script to verify queen movements diagonal (forward) and issue a check")
        movement_list = [ 'Nf6', 'c3', 'd6' , 'Qb3', 'Nc6', 'Qxf7']
        logger.info("Make initial move on the board")
        result = self.move_obj.make_move(self.initial_state_of_the_board, self.url)
        (self.player_state, self.game_state, self.board_state) = self.move_obj.get_states_from_last_move(result)
        
        self.next_move = {"method": self.method, "params":{}, "id": self.id, "jsonrpc": self.json_rpc}
        self.game_state = self.move_obj.make_iter_moves_for_game_action( (self.player_state, self.game_state, self.board_state), self.next_move,  movement_list, self.url, error_flag= False)
        self.assertTrue(self.game_state == 'check', msg= "Queen couldnt issue a check")
        logger.info('End of case test02_func_sfcs_queen_movements_positive_02')
        
    def test03_func_sfcs_queen_movements_positive_03(self):
        """
            Test script to verify queen movements killing moves in diagonal, horizontal and vertical . Issue check

        """
        logger.info("\n\n test03_func_sfcs_queen_movements_positive_03: Test script to verify queen movements killing moves in diagonal, horizontal and vertical . Issue check")
        movement_list = [ 'Nf6', 'd4', 'h5' , 'e4', 'c6', 'd5', 'd6', 'Qd3', 'Bd7', 'dxc6', 'Qb6', 'c7', 'Ng4', 'Qxd6', 'Qxf2']
        logger.info("Make initial move on the board")
        result = self.move_obj.make_move(self.initial_state_of_the_board, self.url)
        (self.player_state, self.game_state, self.board_state) = self.move_obj.get_states_from_last_move(result)
        
        self.next_move = {"method": self.method, "params":{}, "id": self.id, "jsonrpc": self.json_rpc}
        self.game_state = self.move_obj.make_iter_moves_for_game_action( (self.player_state, self.game_state, self.board_state), self.next_move,  movement_list, self.url, error_flag= False)
        self.assertTrue(self.game_state == 'check', msg= "Queen couldnt issue a check")
        logger.info('End of case test03_func_sfcs_queen_movements_positive_03')

    def test04_func_sfcs_queen_movements_positive_04(self):
        """
            Test script to verify queen movements backwards in diagonal, horizontal and vertical.

        """
        logger.info("\n\n test04_func_sfcs_queen_movements_positive_04: Test script to verify queen movements backwards in diagonal, horizontal and vertical.")
        movement_list = [ 'e5', 'd4', 'd5' , 'Qd3', 'Nd7', 'Qf5', 'Nh6', 'Qf3', 'Nb6', 'Qh5', 'Be6', 'Qh4', 'Qxh4', 'Nf3', 'Qd8']
        logger.info("Make initial move on the board")
        result = self.move_obj.make_move(self.initial_state_of_the_board, self.url)
        (self.player_state, self.game_state, self.board_state) = self.move_obj.get_states_from_last_move(result)
        
        self.next_move = {"method": self.method, "params":{}, "id": self.id, "jsonrpc": self.json_rpc}
        self.move_obj.make_iter_moves_for_game_action( (self.player_state, self.game_state, self.board_state), self.next_move,  movement_list, self.url, error_flag= True)
        logger.info('End of case test04_func_sfcs_queen_movements_positive_04')
    
    def test05_func_sfcs_queen_movements_negative_01(self):
        """
            Test script to verify queen movements in L shape. Illegal move

        """
        logger.info("\n\n test05_func_sfcs_queen_movements_negative_01: Test script to verify queen movements in L shape. Illegal move")
        movement_list = [ 'Qe6']
        logger.info("Make initial move on the board")
        result = self.move_obj.make_move(self.initial_state_of_the_board, self.url)
        (self.player_state, self.game_state, self.board_state) = self.move_obj.get_states_from_last_move(result)
        
        self.next_move = {"method": self.method, "params":{}, "id": self.id, "jsonrpc": self.json_rpc}
        result  = self.move_obj.make_iter_moves_for_game_action( (self.player_state, self.game_state, self.board_state), self.next_move,  movement_list, self.url, error_flag= False)
        self.assertTrue(result['error']['message']=='Move cannot be made.', msg='Queen has made an illegal move. Possible bug')
        logger.info('End of case test05_func_sfcs_queen_movements_negative_01')
    
    def test06_func_sfcs_queen_movements_negative_02(self):
        """
            Test script to verify queen movements to an invalid location

        """
        logger.info("\n\n test06_func_sfcs_queen_movements_negative_02: Test script to verify queen movements to an invalid location")
        movement_list = [ 'Qd9']
        logger.info("Make initial move on the board")
        result = self.move_obj.make_move(self.initial_state_of_the_board, self.url)
        (self.player_state, self.game_state, self.board_state) = self.move_obj.get_states_from_last_move(result)
        
        self.next_move = {"method": self.method, "params":{}, "id": self.id, "jsonrpc": self.json_rpc}
        result  = self.move_obj.make_iter_moves_for_game_action( (self.player_state, self.game_state, self.board_state), self.next_move,  movement_list, self.url, error_flag= False)
        self.assertTrue(result['error']['message'] == 'Invalid move string.', msg= "Illegal move made by the Queen to invalid location")       
        logger.info('End of case test06_func_sfcs_queen_movements_negative_02')

    def test07_func_sfcs_queen_movements_negative_03(self):
        """
            Test script to verify queen movements to an already occupied location

        """
        logger.info("\n\n test07_func_sfcs_queen_movements_negative_03: Test script to verify queen movements to an already occupied location")
        movement_list = [ 'Qd7']
        logger.info("Make initial move on the board")
        result = self.move_obj.make_move(self.initial_state_of_the_board, self.url)
        (self.player_state, self.game_state, self.board_state) = self.move_obj.get_states_from_last_move(result)
        
        self.next_move = {"method": self.method, "params":{}, "id": self.id, "jsonrpc": self.json_rpc}
        result  = self.move_obj.make_iter_moves_for_game_action( (self.player_state, self.game_state, self.board_state), self.next_move,  movement_list, self.url, error_flag= False)
        self.assertTrue(result['error']['message'] == 'Move cannot be made.', msg='Queen has made an illegal move to already occupied location. Possible bug')       
        logger.info('End of case test07_func_sfcs_queen_movements_negative_03')    

if __name__ == "__main":
    unittest.main()