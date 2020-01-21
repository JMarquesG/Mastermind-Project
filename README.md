# Mastermind Project
    This is a Mastermind Api, write in Python with the framework Django and MongDb as data base

## Requeriments
    Python3 (3.7.3)
    MongoDB (3.6.8)

### All dependencies on requeriments.txt
    pip install -r requirements.txt

## Description

    After runing the django -> python3 manage.py runserve
    The api will be deployed in localhost:8000/

    Request:

        ['GET'] /create_game
            
            - Check all game that exists in the DB, returning the id and the name
        
        ['POST'] /create_game
            {
                "name" : string,
                "c1" : COLOR,
                "c2" : COLOR,
                "c3" : COLOR,
                "c4" : COLOR,
            }
        *there are 6 color options -> COLOR = ['RED','GREEN','BLUE','PURPLE','YELLOW','ORANGE']    
            - Creates a new game

        ['POST'] /code
            {
                "game": game_id
                "c1" : COLOR,
                "c2" : COLOR,
                "c3" : COLOR,
                "c4" : COLOR,
            }

            - Creates a new check and returns feedback as a sequence of pegs, BLACK if color and order correct, WHITE if just contains de color,  nothing if neither of both 
        
        ['GET'] /code_history
            {
                "id" : number
            }
            *paremeter is required

            - Show all history of feedbacks for a game

## Author
    Jordi Marques Godo