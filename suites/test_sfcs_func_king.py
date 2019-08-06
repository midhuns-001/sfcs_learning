import unittest
from src.make_move import initial_params
from src.make_move import MakeMove 
from src.sfcs_logger import logger
from src.config_utils import ConfigUtil

class TestSFCSFunctionalKing(unittest.TestCase):
    '''
        This suite covers all the functional aspects of the coin King on the chessboard. Movements, conditions & illegal actions
    '''
    @classmethod
    def setUpClass(self):
        logger.info("\n\n ============================================ In SFCS TestSFCSFunctionalKing setup Class ============================================")
        
        self.config = ConfigUtil().readConfigurationFile()
        self.move_obj = MakeMove()
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
        logger.info("\n\n ============================================ In SFCS TestSFCSFunctionalKing TearDown Class ============================================")
    
    def test01_func_sfcs_king_movements_positive(self):
        """
            Test script to verify king movements.- Move the king in all directions one step

        """
        logger.info("\n\n test01_func_sfcs_pawn_movements_positive: Move the king in all directions one step  ")
        movement_list = ['Nf6', 'f4','c5', 'd4', 'd6', 'Nb5', 'Nc6', 'c4', 'Bf5', 'e4', 'Bg6', 'g4', 'h6', 'Qa4', 'Bxe4', 'Bh3', 'a6', 'Ke2', 'axb5', 'Ke1', 'bxa4', 'Kf1', 'Bxh1', 'Ke1',
                         'Nxd4', 'Kd2', 'Qd7', 'Kc1']
        self.next_move = {"method": self.method, "params":{}, "id": self.id, "jsonrpc": self.json_rpc}
        result = self.move_obj.make_iter_moves_for_game_action( (self.player_state, self.game_state, self.board_state), self.next_move,  movement_list, self.url, error_flag = False)
        self.assertTrue(result['error']['message'] == 'Move cannot be made.', msg= "Move shouldnt be made as coin does not exist on the board")
        logger.info('End of case test01_func_sfcs_pawn_movements_positive')
    
    def test02_func_sfcs_king_movements_positive(self):
        """
            Test script to verify king movements.- Move the coins until a check is called by the opponent

        """
        logger.info("\n\n test02_func_sfcs_king_movements_positive: Test script to verify king movements.- Move the coins until a check is called by the opponent ")
        logger.info("SetupClass: Make the initial move on the chess board")
        result = self.move_obj.make_move(self.initial_state_of_the_board, self.url)
        (self.player_state, self.game_state, self.board_state) = self.move_obj.get_states_from_last_move(result)    
        
        movement_list = [ 'e5', 'd4', 'e4', 'Qd2', 'Qe7', 'Nxe4', 'Qxe4', 'f3', 'Qg6', 'Qc3', 'Qc6', 'Kd2', 'd6', 'Kd3', 'Ne7', 'd5', 'Nxd5', 'Qd4', 'f5', 'Qxd5', 'Qxd5']
        self.next_move = {"method": self.method, "params":{}, "id": self.id, "jsonrpc": self.json_rpc}
        result = self.move_obj.make_iter_moves_for_game_action( (self.player_state, self.game_state, self.board_state), self.next_move,  movement_list, self.url, error_flag = False)
        self.assertTrue(result == 'check', msg= "Check call not found on the king")
        logger.info('End of case test02_func_sfcs_king_movements_positive')
    
    def test03_func_sfcs_kill_using_king_positive(self):
        """
            Test script to verify king movements.- Kill a coin using king

        """
        logger.info("\n\n test03_func_sfcs_kill_using_king_positive: Test script to verify king movements.-  Kill a coin using king")
        logger.info("SetupClass: Make the initial move on the chess board")
        result = self.move_obj.make_move(self.initial_state_of_the_board, self.url)
        (self.player_state, self.game_state, self.board_state) = self.move_obj.get_states_from_last_move(result)    
        
        movement_list = [ 'a6', 'f4', 'Nc6', 'f5', 'g6', 'f6', 'd6', 'fxe7', 'Kxe7']
        self.next_move = {"method": self.method, "params":{}, "id": self.id, "jsonrpc": self.json_rpc}
        self.move_obj.make_iter_moves_for_game_action( (self.player_state, self.game_state, self.board_state), self.next_move,  movement_list, self.url)
        logger.info('End of case test03_func_sfcs_kill_using_king_positive')

    
    def test04_func_sfcs_king_illegal_moves_negative_01(self):
        """
            Test script to verify illegal king movements - forward

        """
        logger.info("\n\n test04_func_sfcs_king_illegal_moves_negative_01: Test script to verify illegal king movements ")
        logger.info("SetupClass: Make the initial move on the chess board")
        result = self.move_obj.make_move(self.initial_state_of_the_board, self.url)
        (self.player_state, self.game_state, self.board_state) = self.move_obj.get_states_from_last_move(result)    
        
        movement_list = [ 'Ke7']
        self.next_move = {"method": self.method, "params":{}, "id": self.id, "jsonrpc": self.json_rpc}
        result = self.move_obj.make_iter_moves_for_game_action( (self.player_state, self.game_state, self.board_state), self.next_move,  movement_list, self.url, error_flag = False)
        self.assertTrue(result['error']['message'] == 'Move cannot be made.', msg= "Illegal move made by the pawn")
        logger.info('End of case test04_func_sfcs_king_illegal_moves_negative_01')

    def test05_func_sfcs_king_illegal_moves_negative_02(self):
        """
            Test script to verify illegal king movements - diagonal

        """
        logger.info("\n\n test05_func_sfcs_king_illegal_moves_negative_02: Test script to verify illegal king movements ")
        logger.info("SetupClass: Make the initial move on the chess board")
        result = self.move_obj.make_move(self.initial_state_of_the_board, self.url)
        (self.player_state, self.game_state, self.board_state) = self.move_obj.get_states_from_last_move(result)    
        
        movement_list = [ 'Kf7']
        self.next_move = {"method": self.method, "params":{}, "id": self.id, "jsonrpc": self.json_rpc}
        result = self.move_obj.make_iter_moves_for_game_action( (self.player_state, self.game_state, self.board_state), self.next_move,  movement_list, self.url, error_flag = False)
        self.assertTrue(result['error']['message'] == 'Move cannot be made.', msg= "Illegal move made by the pawn")
        logger.info('End of case test05_func_sfcs_king_illegal_moves_negative_02')

    def test06_func_sfcs_king_illegal_moves_negative_03(self):
        """
            Test script to verify illegal king movements - sideways

        """
        logger.info("\n\n test06_func_sfcs_king_illegal_moves_negative_03: Test script to verify illegal king movements ")
        logger.info("SetupClass: Make the initial move on the chess board")
        result = self.move_obj.make_move(self.initial_state_of_the_board, self.url)
        (self.player_state, self.game_state, self.board_state) = self.move_obj.get_states_from_last_move(result)    
        
        movement_list = [ 'Kf7']
        self.next_move = {"method": self.method, "params":{}, "id": self.id, "jsonrpc": self.json_rpc}
        result = self.move_obj.make_iter_moves_for_game_action( (self.player_state, self.game_state, self.board_state), self.next_move,  movement_list, self.url, error_flag = False)
        self.assertTrue(result['error']['message'] == 'Move cannot be made.', msg= "Illegal move made by the pawn")
        logger.info('End of case test06_func_sfcs_king_illegal_moves_negative_03')

    def test07_func_sfcs_king_illegal_moves_negative_04(self):
        """
            Test script to verify illegal king movements - invalid location

        """
        logger.info("\n\n test07_func_sfcs_king_illegal_moves_negative_04: Test script to verify illegal king movements ")
        logger.info("SetupClass: Make the initial move on the chess board")
        result = self.move_obj.make_move(self.initial_state_of_the_board, self.url)
        (self.player_state, self.game_state, self.board_state) = self.move_obj.get_states_from_last_move(result)    
        
        movement_list = [ 'Kh10']
        self.next_move = {"method": self.method, "params":{}, "id": self.id, "jsonrpc": self.json_rpc}
        result = self.move_obj.make_iter_moves_for_game_action( (self.player_state, self.game_state, self.board_state), self.next_move,  movement_list, self.url, error_flag = False)
        self.assertTrue(result['error']['message'] == 'Invalid move string.', msg= "Illegal move made by the pawn")
        logger.info('End of case test07_func_sfcs_king_illegal_moves_negative_04')

    def test08_func_sfcs_king_illegal_moves_negative_05(self):
        """
            Test script to verify illegal king movements - L shape

        """
        logger.info("\n\n test08_func_sfcs_king_illegal_moves_negative_05: Test script to verify illegal king movements ")
        logger.info("SetupClass: Make the initial move on the chess board")
        result = self.move_obj.make_move(self.initial_state_of_the_board, self.url)
        (self.player_state, self.game_state, self.board_state) = self.move_obj.get_states_from_last_move(result)    
        
        movement_list = [ 'Kd6']
        self.next_move = {"method": self.method, "params":{}, "id": self.id, "jsonrpc": self.json_rpc}
        result = self.move_obj.make_iter_moves_for_game_action( (self.player_state, self.game_state, self.board_state), self.next_move,  movement_list, self.url, error_flag = False)
        self.assertTrue(result['error']['message'] == 'Move cannot be made.', msg= "Illegal move made by the pawn")
        logger.info('End of case test08_func_sfcs_king_illegal_moves_negative_05')

    def test09_func_sfcs_king_illegal_moves_negative_06(self):
        """
            Test script to verify illegal king movements - invalid location backwards

        """
        logger.info("\n\n test09_func_sfcs_king_illegal_moves_negative_06: Test script to verify illegal king movements ")
        logger.info("SetupClass: Make the initial move on the chess board")
        result = self.move_obj.make_move(self.initial_state_of_the_board, self.url)
        (self.player_state, self.game_state, self.board_state) = self.move_obj.get_states_from_last_move(result)    
        
        movement_list = [ 'Ke9']
        self.next_move = {"method": self.method, "params":{}, "id": self.id, "jsonrpc": self.json_rpc}
        result = self.move_obj.make_iter_moves_for_game_action( (self.player_state, self.game_state, self.board_state), self.next_move,  movement_list, self.url, error_flag = False)
        self.assertTrue(result['error']['message'] == 'Invalid move string.', msg= "Illegal move made by the pawn")
        logger.info('End of case test09_func_sfcs_king_illegal_moves_negative_06')