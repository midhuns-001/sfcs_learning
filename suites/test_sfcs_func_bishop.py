import unittest
from src.make_move import initial_params
from src.make_move import MakeMove 
from src.sfcs_logger import logger
from src.config_utils import ConfigUtil

class TestSFCSFunctionalBishop(unittest.TestCase):
    '''
        This suite covers all the functional aspects of the coin Bishop on the chess board. Movements, conditions & illegal actions
    '''
    @classmethod
    def setUpClass(self):
        logger.info("\n\n ============================================ In SFCS TestSFCSFunctionalBishop setup Class ============================================")
        self.move_obj = MakeMove()
        self.config = ConfigUtil().readConfigurationFile()
        self.url = self.config['TEST_URL']
        self.id = self.config['SESSION_ID']
        self.json_rpc = self.config['JSON_RPC']
        self.method = self.config['TEST_METHOD']
        self.playerState = self.config['PLAYER_STATE']
        self.move = "e4"
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
        logger.info("\n\n ============================================ In SFCS TestSFCSFunctionalBishop TearDown Class ============================================")

    def test01_func_sfcs_bishop_movements_positive_01(self):
        """
            Test script to verify Bishop movements diagnoal (forward) and get killed

        """
        logger.info("\n\n test01_func_sfcs_bishop_movements_positive_01: verify Bishop movements horizontal and vertical (forward) and get killed ")
        movement_list = ['Nf6', 'Bc4', 'e5', 'Bxf7' , 'Kxf7']
        self.next_move = {"method": self.method, "params":{}, "id": self.id, "jsonrpc": self.json_rpc}
        self.move_obj.make_iter_moves_for_game_action( (self.player_state, self.game_state, self.board_state), self.next_move,  movement_list, self.url, error_flag= True)
        logger.info('End of case test01_func_sfcs_bishop_movements_positive_01')
    
    
    def test02_func_sfcs_bishop_movements_positive_02(self):
        """
            Test script to verify bishop movements diagonal and kill a bishop

        """
        logger.info("\n\n test02_func_sfcs_bishop_movements_positive_02: Test script to verify bishop movements horizontal and vertical  and kill a bishop")
        self.params['move'] = 'g3'
        self.initial_state_of_the_board = {"method": self.method,
                                           "params": self.params,
                                           "id": self.id,
                                           "jsonrpc": self.json_rpc}
        movement_list = [ 'Nf6', 'Bh3', 'Nc6', 'b3', 'h5', 'Ba3', 'g5', 'Bxe7', 'Kxe7', 'Bxd7', 'Bg7', 'Bxc8', 'Rxc8']
        logger.info("Make initial move on the board")
        result = self.move_obj.make_move(self.initial_state_of_the_board, self.url)
        (self.player_state, self.game_state, self.board_state) = self.move_obj.get_states_from_last_move(result)
        
        self.next_move = {"method": self.method, "params":{}, "id": self.id, "jsonrpc": self.json_rpc}
        self.move_obj.make_iter_moves_for_game_action( (self.player_state, self.game_state, self.board_state), self.next_move,  movement_list, self.url, error_flag= True)
        logger.info('End of case test02_func_sfcs_bishop_movements_positive_02')
    

    def test03_func_sfcs_bishop_movements_positive_03(self):
        """
            Test script to verify bishop movements diagonal  backwards

        """
        logger.info("\n\n test03_func_sfcs_bishop_movements_positive_03: verify bishop movements diagonal  backwards")
        self.params['move'] = 'e3'
        self.initial_state_of_the_board = {"method": self.method,
                                           "params": self.params,
                                           "id": self.id,
                                           "jsonrpc": self.json_rpc}
        movement_list = [ 'e6', 'Bd3', 'h5', 'Bb5', 'a6', 'Bd3', 'g5', 'Be4', 'Nc6', 'Bd3', 'f5', 'b3', 'd6', 'Ba3', 'h4', 'Bxd6']
        logger.info("Make initial move on the board")
        result = self.move_obj.make_move(self.initial_state_of_the_board, self.url)
        (self.player_state, self.game_state, self.board_state) = self.move_obj.get_states_from_last_move(result)
        
        self.next_move = {"method": self.method, "params":{}, "id": self.id, "jsonrpc": self.json_rpc}
        self.move_obj.make_iter_moves_for_game_action( (self.player_state, self.game_state, self.board_state), self.next_move,  movement_list, self.url, error_flag= True)
        logger.info('End of case test03_func_sfcs_bishop_movements_positive_03')
        
    def test04_func_sfcs_bishop_movements_negative_01(self):
        """
            Test script to verify bishop movements in L shape. Illegal move

        """
        logger.info("\n\n test04_func_sfcs_bishop_movements_negative_01: Test script to verify bishop movements in L shape. Illegal move")

        movement_list = [ 'Be3']
        self.next_move = {"method": self.method, "params":{}, "id": self.id, "jsonrpc": self.json_rpc}
        result = self.move_obj.make_iter_moves_for_game_action( (self.player_state, self.game_state, self.board_state), self.next_move,  movement_list, self.url, error_flag= False)
        self.assertTrue(result['error']['message']=='Move cannot be made.', msg='Bishop has made an illegal move. Possible bug')
        logger.info('End of case test04_func_sfcs_bishop_movements_negative_01')
        
    def test05_func_sfcs_bishop_movements_negative_02(self):
        """
            Test script to verify bishop movements in horizontal shape. Illegal move

        """
        logger.info("\n\n test05_func_sfcs_bishop_movements_negative_02: Test script to verify bishop movements in diagonal shape. Illegal move")

        movement_list = [ 'Bf3']
        self.next_move = {"method": self.method, "params":{}, "id": self.id, "jsonrpc": self.json_rpc}
        result = self.move_obj.make_iter_moves_for_game_action( (self.player_state, self.game_state, self.board_state), self.next_move,  movement_list, self.url, error_flag= False)
        self.assertTrue(result['error']['message']=='Move cannot be made.', msg='Bishop has made an illegal move. Possible bug')
        logger.info('End of case test05_func_sfcs_bishop_movements_negative_02')
        
    def test06_func_sfcs_bishop_movements_negative_03(self):
        """
            Test script to verify bishop movements to an already occupied location. Illegal move

        """
        logger.info("\n\n test06_func_sfcs_bishop_movements_negative_03: Test script to verify bishop movements to an already occupied location. Illegal move")

        movement_list = [ 'Be2']
        self.next_move = {"method": self.method, "params":{}, "id": self.id, "jsonrpc": self.json_rpc}
        result = self.move_obj.make_iter_moves_for_game_action( (self.player_state, self.game_state, self.board_state), self.next_move,  movement_list, self.url, error_flag= False)
        self.assertTrue(result['error']['message']=='Move cannot be made.', msg='Bishop has made an illegal move. Possible bug')
        logger.info('End of case test06_func_sfcs_bishop_movements_negative_03')    

if __name__ == "__main":
    unittest.main()