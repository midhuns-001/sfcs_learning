
import requests
import json
from src.sfcs_logger import logger

initial_params  =  {
        "boardState": [{"loc": "a8", "type": "r"}, {"loc": "b8", "type": "n"}, {"loc": "c8", "type": "b"},
                       {"loc": "d8", "type": "q"}, {"loc": "e8", "type": "k"}, {"loc": "f8", "type": "b"}, {"loc": "g8", "type":
                        "n"}, {"loc": "h8", "type": "r"}, {"loc": "a7", "type": "p"}, {"loc": "b7", "type": "p"}, {"loc": "c7",
                        "type": "p"}, {"loc": "d7", "type": "p"}, {"loc": "e7", "type": "p"}, {"loc": "f7", "type": "p"}, {"loc":
                        "g7", "type": "p"}, {"loc": "h7", "type": "p"}, {"loc": "a1", "type": "R"}, {"loc": "b1", "type": "N"},
                        {"loc": "c1", "type": "B"}, {"loc": "d1", "type": "Q"}, {"loc": "f1", "type": "B"}, {"loc": "g1", "type":
                        "N"}, {"loc": "h1", "type": "R"}, {"loc": "a2", "type": "P"}, {"loc": "b2", "type": "P"}, {"loc": "c2",
                        "type": "P"}, {"loc": "d2", "type": "P"}, {"loc": "e2", "type": "P"}, {"loc": "f2", "type": "P"}, {"loc":
                        "g2", "type": "P"}, {"loc": "e1", "type": "K"}, {"loc": "h2", "type": "P"}] }

class MakeMove():

    def get_states_from_last_move(self, response):
        """
            This method takes the actual response dictionary returned by make_move method
            
        Parameters:
        response (dict): Response dictionary obtained from makeMove method call
        Returns:
        returns a tuple of next player state, game state(if any) and present board state
        
        """
        logger.debug("Calling method get_states_from_last_move, Getting states of last move")
        player_state  = response['result']['playerState']
        game_state = response['result']['gameState']
        board_state = response['result']['boardState']
        return(player_state, game_state, board_state)


    def make_move(self, state_of_the_board, url):
        """
            This method invokes a REST API POST request call to the url
    
        Parameters:
        state_of_the_board (dict): Present state of the chess board in dictionary format
        url (str)                : Endpoint to access 
        Returns:
        response the board state in a dictionary format. returns None if nothing is executed
        
        """
        logger.debug("Calling method make_move, invokes a REST API POST request call to the url")
        headers = json.dumps({'content-type': 'application/json'})
        state_of_the_board = json.dumps(state_of_the_board)
        headers = json.loads(headers)
        logger.debug("URL is : %s\n\n" % (url))        
        logger.debug("PAYLOAD is : %s\n\n" %state_of_the_board)

        try:
            resp = requests.post(url=url,  headers=headers, data=state_of_the_board)
            
            if 'error' in resp.json():
                response = resp.json()
                logger.info ("\n\n Error in response: %s" %response)
                return response
            elif 'result' in resp.json():
                response = resp.json()
                status = resp.status_code
                logger.info("\n\n Status Obtained : %s" %status)
                logger.info("\n\n Response : %s" %response)
                logger.info("\n\n")
                return response
            else:
                return None
                    
        except Exception as e:
            logger.error(e)
            return e
            
    def make_iter_moves_for_game_action(self, state, move, movement_list, url, error_flag = True):
        """
            This is a helper method to invoke multiple calls  to emulate chess moves by iterating make_move() method 
    
        Parameters:
        state (tuple)                :    a tuple of next player state, game state(if any) and present board state
        state_of_the_board (dict)    : state of the board
        movement_list (list)        : list which contains the chess coin movements
        url (str)                    : Endpoint to access
        error_flag(boolean)        : Set/unset the error flag if the error has to be returned to capture negative scenarios. Else it will assert a failure
        Returns:
        should return the game state. 
        
        """
        (player_state, game_state, board_state) =  state
        logger.debug("player state: %s" %player_state)
        for i in range (len(movement_list)):
            logger.debug("%s Moving to :%s"%(player_state, movement_list[i]))
            b_state = {}
            b_state['boardState'] = board_state
            b_state['move'] = movement_list[i]
            b_state['playerState'] = player_state           
            move['params'] = b_state
            result = self.make_move(move, url)
            if 'error' in result:
                logger.error ("Found error in MakeMove: %s" %result)
                if not error_flag:
                    return result
                else:
                    assert(False)
            else:
                (player_state, game_state, board_state)=  self.get_states_from_last_move(result)
                if game_state != '':
                    logger.info("Found a game state: %s" %game_state)
    
        return game_state
    
    

### Sample Unit test
if __name__ == '__main__':
    url = "http://chesstest.solidfire.net:8080/json-rpc"
    state_of_the_board = {
   "method": "MakeMove",
    "params": {
        "boardState": [{"loc": "a8", "type": "r"}, {"loc": "b8", "type": "n"}, {"loc": "c8", "type": "b"},
{"loc": "d8", "type": "q"}, {"loc": "e8", "type": "k"}, {"loc": "f8", "type": "b"}, {"loc": "g8", "type":
"n"}, {"loc": "h8", "type": "r"}, {"loc": "a7", "type": "p"}, {"loc": "b7", "type": "p"}, {"loc": "c7",
"type": "p"}, {"loc": "d7", "type": "p"}, {"loc": "e7", "type": "p"}, {"loc": "f7", "type": "p"}, {"loc":
"g7", "type": "p"}, {"loc": "h7", "type": "p"}, {"loc": "a1", "type": "R"}, {"loc": "b1", "type": "N"},
{"loc": "c1", "type": "B"}, {"loc": "d1", "type": "Q"}, {"loc": "f1", "type": "B"}, {"loc": "g1", "type":
"N"}, {"loc": "h1", "type": "R"}, {"loc": "a2", "type": "P"}, {"loc": "b2", "type": "P"}, {"loc": "c2",
"type": "P"}, {"loc": "d2", "type": "P"}, {"loc": "e2", "type": "P"}, {"loc": "f2", "type": "P"}, {"loc":
"g2", "type": "P"}, {"loc": "e1", "type": "K"}, {"loc": "h2", "type": "P"}],
        "move": "Nc3",
        "playerState": "w"
    },
"id": 1,
    "jsonrpc": "2.0"
}

    #ab = make_move(state_of_the_board, url)