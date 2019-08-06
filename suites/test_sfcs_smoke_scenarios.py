import unittest
from src.make_move import initial_params
from src.make_move import MakeMove 
from src.sfcs_logger import logger
from src.config_utils import ConfigUtil


class TestSFCSSmokeScenarios(unittest.TestCase):
    '''
        This suite covers the critical workflow of SFCS chess game related to different movements of the coins resulting in a game state
    '''
    @classmethod
    def setUpClass(self):
        logger.info("\n\n ============================================ In SFCS TestSFCSSmokeScenarios setup Class ============================================")
        self.move_obj = MakeMove()
        self.config = ConfigUtil().readConfigurationFile()
        self.url = self.config['TEST_URL']
        self.id = self.config['SESSION_ID']
        self.json_rpc = self.config['JSON_RPC']
        self.method = self.config['TEST_METHOD']
        self.playerState = self.config['PLAYER_STATE']
        self.move = "e3"
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
        logger.info("============================================ End of SFCS setup class ============================================")
    
    @classmethod
    def tearDownClass(self):
        logger.info("\n\n ============================================ In TestSFCSSmokeScenarios TearDown Class ============================================")

    def test01_smoke_sfcs_checkmate_end_to_end(self):
        """
            Test script to verify checkmate scenario by emulating multiple coin movements on a chess board

        """
        logger.info("\n\n test01_smoke_sfcs_checkmate_end_to_end: Test script to verify checkmate scenario by emulating multiple coin movements on a chess board")
        movement_list = ['e5', 'Ke2', 'd5', 'Kd3' , 'Qf6', 'Qe2', 'e4']
        self.next_move = {"method": self.method, "params":{}, "id": self.id, "jsonrpc": self.json_rpc}
        self.game_state = self.move_obj.make_iter_moves_for_game_action( (self.player_state, self.game_state, self.board_state), self.next_move,  movement_list, self.url)
        self.assertTrue(self.game_state=='checkmate', msg='Checkmate not achieved using selected moves')
        logger.info('End of case test01_smoke_sfcs_checkmate_end_to_end')

    def test02_smoke_scfs_stalemate_end_to_end(self):
        """
            Test script to verify stalemate scenario by emulating multiple coin movements on a chess board

        """
        logger.info("\n\n test02_smoke_scfs_stalemate_end_to_end: Test script to verify stalemate scenario by emulating multiple coin movements on a chess board")
        movement_list = ['a5', 'Qh5', 'Ra6' , 'Qxa5', 'h5', 'Qxc7', 'Rah6', 'h4', 'f6', 'Qxd7', 'Kf7', 'Qxb7', 'Qd3', 'Qxb8', 'Qh7', 'Qxc8', 'Kg6', 'Qe6']
        logger.info("Make initial move on the board")
        result = self.move_obj.make_move(self.initial_state_of_the_board, self.url)
        (self.player_state, self.game_state, self.board_state) = self.move_obj.get_states_from_last_move(result)
        
        self.next_move = {"method": self.method, "params":{}, "id": self.id, "jsonrpc": self.json_rpc}
        self.game_state = self.move_obj.make_iter_moves_for_game_action( (self.player_state, self.game_state, self.board_state), self.next_move,  movement_list, self.url)
        self.assertTrue(self.game_state=='stalemate', msg='Stalemate not achieved using selected moves')
        logger.info("End of case test02_smoke_scfs_stalemate_end_to_end")

    def test03_smoke_scfs_check_end_to_end(self):
        """
            Test script to verify a check scenario by emulating multiple coin movements on a chess board

        """
        logger.info("\n\n test03_smoke_scfs_check_end_to_end: Test script to verify a check scenario by emulating multiple coin movements on a chess board")
        movement_list = [ 'Nf6', 'Bb5', 'h5', 'Bxd7']
        logger.info("Make initial move on the board")
        result =  self.move_obj.make_move(self.initial_state_of_the_board, self.url)
        (self.player_state, self.game_state, self.board_state) = self.move_obj.get_states_from_last_move(result)
        self.next_move = {"method": self.method, "params":{}, "id": self.id, "jsonrpc": self.json_rpc}
        
        self.game_state = self.move_obj.make_iter_moves_for_game_action( (self.player_state, self.game_state, self.board_state), self.next_move,  movement_list, self.url)
        self.assertTrue(self.game_state=='check', msg='check not achieved using selected moves')
        logger.info("End of case test03_smoke_scfs_check_end_to_end")

    if __name__ == '__main__':
        unittest.main()