import unittest
from src.make_move import initial_params
from src.make_move import MakeMove 
from src.sfcs_logger import logger
from src.config_utils import ConfigUtil

class TestSFCSFunctionalKnight(unittest.TestCase):
    '''
        This suite covers all the functional aspects of the coin Knight on the chess board. Movements, conditions & illegal actions
    '''
    @classmethod
    def setUpClass(self):
        logger.info("\n\n ============================================ In SFCS TestSFCSFunctionalKnight setup Class ============================================")
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
        logger.info("\n\n ============================================ In SFCS TestSFCSFunctionalKnight TearDown Class ============================================")

    def test01_func_sfcs_knight_movements_positive_01(self):
        """
            Test script to verify more than one knight movements (both black and white) and ultimately kill a black knight 

        """
        logger.info("\n\n test01_func_sfcs_knight_movements_positive: Test script to verify more than one knight movements (both black and white) and ultimately kill a black knight ")
        movement_list = ['Nc6', 'Na4', 'Nc4', 'Ne5' , 'Nxe5', 'Ng4']
        self.next_move = {"method": self.method, "params":{}, "id": self.id, "jsonrpc": self.json_rpc}
        result = self.move_obj.make_iter_moves_for_game_action( (self.player_state, self.game_state, self.board_state), self.next_move,  movement_list, self.url, error_flag= False)
        self.assertTrue(result['error']['message'] == 'Move cannot be made.', msg= "Move shouldn't be made as coin does not exist on the board")
        logger.info('End of case test01_func_sfcs_knight_movements_positive')

    def test02_func_sfcs_knight_movements_positive_02(self):
        """
            Test script to verify more than one knight movements (both black and white), issue a check

        """
        logger.info("\n\n test02_func_sfcs_knight_movements_positive: Test script to verify more than one knight movements (both black and white) and ultimately kill a black knight ")
        movement_list = ['b6', 'Nh3', 'Nh6', 'Nf4', 'Ng4' , 'Ng6', 'Nf2', 'Nxf8', 'Nd3']
        logger.info("Make initial move on the board")
        result = self.move_obj.make_move(self.initial_state_of_the_board, self.url)
        (self.player_state, self.game_state, self.board_state) = self.move_obj.get_states_from_last_move(result)
        
        self.next_move = {"method": self.method, "params":{}, "id": self.id, "jsonrpc": self.json_rpc}
        self.game_state = self.move_obj.make_iter_moves_for_game_action( (self.player_state, self.game_state, self.board_state), self.next_move,  movement_list, self.url, error_flag=False)
        self.assertTrue(self.game_state=='check', msg='check not achieved using selected moves')
        logger.info('End of case test02_func_sfcs_knight_movements_positive')

    
    def test03_func_sfcs_knight_back_movement_positive_03(self):
        """
            Test script to verify more than one knight movements (both black and white), issue backward movements

        """
        logger.info("\n\n test03_func_sfcs_knight_back_movement_positive: Test script to verify more than one knight movements (both black and white), issue backward movements")
        movement_list = ['b5', 'Nh6', 'b4', 'Nb1', 'f4' , 'Nf2', 'h6','Nf2']
        logger.info("Make initial move on the board")
        result = self.move_obj.make_move(self.initial_state_of_the_board, self.url)
        (self.player_state, self.game_state, self.board_state) = self.move_obj.get_states_from_last_move(result)
        
        self.next_move = {"method": self.method, "params":{}, "id": self.id, "jsonrpc": self.json_rpc}
        result = self.move_obj.make_iter_moves_for_game_action( (self.player_state, self.game_state, self.board_state), self.next_move,  movement_list, self.url, error_flag=False)
        self.assertTrue(result['error']['message']=='Move cannot be made.', msg='Knight Trying to move back to an already moved location')
        logger.info('End of case test02_func_sfcs_knight_movements_positive')
    
    def test04_func_sfcs_knight_illegal_movement_01(self):
        """
            Test script to verify illegal movements of a knight - set 1 (sideways, diagonal, Large L shape etc)

        """
        logger.info("\n\n test04_func_sfcs_knight_illegal_movement: Test script to verify illegal movements of a knight")
        movement_list = ['Nb2', 'Nf7', 'Nc2', 'Nf8', 'Na5', 'Nh4']        
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
            result = self.move_obj.make_move(state_of_the_board, self.url)
            logger.info("Result from TC: %s" %result)
            self.assertTrue(result['error']['message']=='Move cannot be made.', msg='Knight has made an illegal move. Possible bug')
        
        logger.info('End of case test04_func_sfcs_knight_illegal_movement')
  
    def test05_func_sfcs_knight_move_invalid_location_negative02(self):
        """
            Test script to verify movement to an invalid location

        """
        logger.info("\n\n test05_func_sfcs_knight_move_invalid_location_negative02: Test script to verify more than one knight movements (both black and white), issue backward movements")
        movement_list = ['Na9', 'Nh10', 'Na-1', 'nc3']
        
        self.next_move = {"method": self.method, "params":{}, "id": self.id, "jsonrpc": self.json_rpc}
        result = self.move_obj.make_iter_moves_for_game_action( (self.player_state, self.game_state, self.board_state), self.next_move,  movement_list, self.url, error_flag=False)
        self.assertTrue(result['error']['message']=="Invalid move string.", msg='Invalid move done on the chess board by Knight')
        logger.info('End of case test05_func_sfcs_knight_move_invalid_location_negative02')

    def test06_func_sfcs_knight_two_pieces_same_space_negative03(self):
        """
            Test script to verify two same Knight pieces are occupying same location

        """
        logger.info("\n\n test06_func_sfcs_knight_two_pieces_same_space_negative03: Test script to verify more than one knight movements (both black and white), issue backward movements")
        movement_list = ['b6', 'e3', 'b4', 'Ne2', 'h6' , 'Nc3']        
        self.next_move = {"method": self.method, "params":{}, "id": self.id, "jsonrpc": self.json_rpc}
        result = self.move_obj.make_iter_moves_for_game_action( (self.player_state, self.game_state, self.board_state), self.next_move,  movement_list, self.url, error_flag=False)
        self.assertTrue(result['error']['message']=='Move cannot be made.', msg='Knight occupying location of another knight of the same player')
        logger.info('End of case test06_func_sfcs_knight_two_pieces_same_space_negative03')


if __name__ == "__main":
    unittest.main()