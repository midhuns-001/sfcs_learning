import unittest
from src.make_move import initial_params
from src.make_move import MakeMove 
from src.sfcs_logger import logger
from src.config_utils import ConfigUtil

class TestSFCSFunctionalPawn(unittest.TestCase):
    '''
        This suite covers all the functional aspects of the coin Pawn on the chess board. Movements, conditions & illegal actions
    '''
    @classmethod
    def setUpClass(self):
        logger.info("\n\n ============================================ In SFCS TestSFCSFunctionalPawn setup Class ============================================")
        self.move_obj = MakeMove()
        self.config = ConfigUtil().readConfigurationFile()
        self.url = self.config['TEST_URL']
        self.id = self.config['SESSION_ID']
        self.json_rpc = self.config['JSON_RPC']
        self.method = self.config['TEST_METHOD']
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
        self.initial_state_of_the_board = {"method": self.method,
                                           "params": self.params,
                                           "id": self.id,
                                           "jsonrpc": self.json_rpc}
        logger.info("SetupClass: Make the initial move on the chess board")
        result = self.move_obj.make_move(self.initial_state_of_the_board, self.url)
        (self.player_state, self.game_state, self.board_state) = self.move_obj.get_states_from_last_move(result)    

    @classmethod
    def tearDownClass(self):
        logger.info("\n\n ============================================ In SFCS TestSFCSFunctionalPawn TearDown Class ============================================")

    def test01_func_sfcs_pawn_movements_positive(self):
        """
            Test script to verify pawn movements. Single and double movements, killing a pawn and verify the pawn exists or not 

        """
        logger.info("\n\n test01_func_sfcs_pawn_movements_positive: Test script to verify pawn movements. Single and double movements, killing a pawn and verify the pawn exists or not  ")
        movement_list = ['g5', 'f4', 'b5', 'fxg5' , 'g5']
        self.next_move = {"method": self.method, "params":{}, "id": self.id, "jsonrpc": self.json_rpc}
        result = self.move_obj.make_iter_moves_for_game_action( (self.player_state, self.game_state, self.board_state), self.next_move,  movement_list, self.url, error_flag= False)
        self.assertTrue(result['error']['message'] == 'Move cannot be made.', msg= "Move shouldnt be made as coin does not exist on the board")
        logger.info('End of case test01_func_sfcs_pawn_movements_positive')
    
    def test02_func_sfcs_pawn_movements_illegal_negative_01(self):
        """
            Test script to verify illegal pawn movements - 3 steps forward
            
        """
        logger.info("\n\n test02_func_sfcs_pawn_movements_illegal_negative01: Test script to verify illegal pawn movements ")
        logger.info("Make initial move on the board")
        result = self.move_obj.make_move(self.initial_state_of_the_board, self.url)
        (self.player_state, self.game_state, self.board_state) = self.move_obj.get_states_from_last_move(result)
        movement_list = ['g3']
        self.next_move = {"method": self.method, "params":{}, "id": self.id, "jsonrpc": self.json_rpc}
        result = self.move_obj.make_iter_moves_for_game_action( (self.player_state, self.game_state, self.board_state), self.next_move,  movement_list, self.url, error_flag= False)
        self.assertTrue(result['error']['message'] == 'Move cannot be made.', msg= "Illegal move made by the pawn")
        logger.info('End of case test02_func_sfcs_pawn_movements_illegal_negative_01')
        
    def test03_func_sfcs_pawn_movements_illegal_negative_02(self):
        """
            Test script to verify illegal pawn movements - move backwards from initial position

        """
        logger.info("\n\n test03_func_sfcs_pawn_movements_illegal_negative_02: Test script to verify illegal pawn movements ")
        logger.info("Make initial move on the board")
        result = self.move_obj.make_move(self.initial_state_of_the_board, self.url)
        (self.player_state, self.game_state, self.board_state) = self.move_obj.get_states_from_last_move(result)
        movement_list = ['c8']
        self.next_move = {"method": self.method, "params":{}, "id": self.id, "jsonrpc": self.json_rpc}
        result = self.move_obj.make_iter_moves_for_game_action( (self.player_state, self.game_state, self.board_state), self.next_move,  movement_list, self.url, error_flag= False)
        self.assertTrue(result['error']['message'] == 'Move cannot be made.', msg= "Illegal move made by the pawn")
        logger.info('End of case test03_func_sfcs_pawn_movements_illegal_negative_02')
    
    def test04_func_sfcs_pawn_movements_illegal_negative_03(self):
        """
            Test script to verify illegal pawn movements -  move sideways

        """
        logger.info("\n\n test04_func_sfcs_pawn_movements_illegal_negative_03: Test script to verify illegal pawn movements ")
        logger.info("Make initial move on the board")
        result = self.move_obj.make_move(self.initial_state_of_the_board, self.url)
        (self.player_state, self.game_state, self.board_state) = self.move_obj.get_states_from_last_move(result)
        movement_list = ['a7']
        self.next_move = {"method": self.method, "params":{}, "id": self.id, "jsonrpc": self.json_rpc}
        result = self.move_obj.make_iter_moves_for_game_action( (self.player_state, self.game_state, self.board_state), self.next_move,  movement_list, self.url, error_flag= False)
        self.assertTrue(result['error']['message'] == 'Move cannot be made.', msg= "Illegal move made by the pawn")
        logger.info('End of case test04_func_sfcs_pawn_movements_illegal_negative_03')

    def test05_func_sfcs_pawn_movements_illegal_negative_04(self):
        """
            Test script to verify illegal pawn movements -  move diagonal backwards

        """
        logger.info("\n\n test05_func_sfcs_pawn_movements_illegal_negative_03: Test script to verify illegal pawn movements ")
        logger.info("Make initial move on the board")
        result = self.move_obj.make_move(self.initial_state_of_the_board, self.url)
        (self.player_state, self.game_state, self.board_state) = self.move_obj.get_states_from_last_move(result)
        movement_list = ['a8']
        self.next_move = {"method": self.method, "params":{}, "id": self.id, "jsonrpc": self.json_rpc}
        result = self.move_obj.make_iter_moves_for_game_action( (self.player_state, self.game_state, self.board_state), self.next_move,  movement_list, self.url, error_flag= False)
        self.assertTrue(result['error']['message'] == 'Move cannot be made.', msg= "Illegal move made by the pawn")
        logger.info('End of case test05_func_sfcs_pawn_movements_illegal_negative_03')
    
    
    def test06_func_sfcs_pawn_movements_illegal_negative_05(self):
        """
            Test script to verify illegal pawn movements - invalid location

        """
        logger.info("\n\n test06_func_sfcs_pawn_movements_illegal_negative_04: Test script to verify illegal pawn movements ")
        logger.info("Make initial move on the board")
        result = self.move_obj.make_move(self.initial_state_of_the_board, self.url)
        (self.player_state, self.game_state, self.board_state) = self.move_obj.get_states_from_last_move(result)
        movement_list = ['h9']
        self.next_move = {"method": self.method, "params":{}, "id": self.id, "jsonrpc": self.json_rpc}
        result = self.move_obj.make_iter_moves_for_game_action( (self.player_state, self.game_state, self.board_state), self.next_move,  movement_list, self.url, error_flag= False)
        self.assertTrue(result['error']['message'] == 'Invalid move string.', msg= "Illegal move made by the pawn")
        logger.info('End of case test06_func_sfcs_pawn_movements_illegal_negative_04')
        
    def test07_func_sfcs_pawn_movements_illegal_negative_06(self):
        """
            Test script to verify backward movement- move backwards from a different location

        """
        logger.info("\n\n test07_func_sfcs_pawn_movements_illegal_negative_05: Test script to verify illegal pawn movements ")
        logger.info("Make initial move on the board")
        movement_list = ['Nc3', 'f4', 'g4']
        self.next_move = {"method": self.method, "params":{}, "id": self.id, "jsonrpc": self.json_rpc}
        for i in range(len(movement_list)):
            print("Move #: %d" %i)
            params  =  initial_params
            state_of_the_board = {}
            params['playerState'] =   self.playerState
            params['move'] = movement_list[i]
            state_of_the_board = {"method": self.method,
                                           "params": params,
                                           "id": self.id,
                                           "jsonrpc": self.json_rpc}
            result =self.move_obj.make_move(state_of_the_board, self.url)
        (self.player_state, self.game_state, self.board_state) = self.move_obj.get_states_from_last_move(result)  
        movement_list = ['f2', 'g2']
        result = self.move_obj.make_iter_moves_for_game_action( (self.player_state, self.game_state, self.board_state), self.next_move,  movement_list, self.url, error_flag=False)
        self.assertTrue(result['error']['message'] == 'Move cannot be made.', msg= "Illegal backward  movement made by the pawn")
        logger.info('End of case test07_func_sfcs_pawn_movements_illegal_negative_05')

    def test08_func_sfcs_pawn_movements_illegal_negative_07(self):
        """
            Test script to verify illegal pawn movements - move 2 steps forward for the second time
            
        """
        logger.info("\n\n test08_func_sfcs_pawn_movements_illegal_negative_06: Test script to verify illegal pawn movements ")
        logger.info("Make initial move on the board")
        result = self.move_obj.make_move(self.initial_state_of_the_board, self.url)
        (self.player_state, self.game_state, self.board_state) = self.move_obj.get_states_from_last_move(result)
        movement_list = ['d5', 'h4', 'd3']
        self.next_move = {"method": self.method, "params":{}, "id": self.id, "jsonrpc": self.json_rpc}
        result = self.move_obj.make_iter_moves_for_game_action( (self.player_state, self.game_state, self.board_state), self.next_move,  movement_list, self.url, error_flag= False)
        self.assertTrue(result['error']['message'] == 'Move cannot be made.', msg= "Illegal move made by the pawn")
        logger.info('End of case test08_func_sfcs_pawn_movements_illegal_negative_06')
        

if __name__ == "__main":
    unittest.main()