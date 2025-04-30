from random import choice, randint

def get_response(user_input:str) -> str:
    lowered = user_input.lower()

    if lowered == '':
        return 'well you said nothing'
    elif lowered == 'hello':
        return 'hello there'
    elif lowered == 'roll':
        return str(randint(1,6))
    elif lowered == '!help':
        return '`This is a help message that you can modify`'
    elif lowered == '!about':
        return '`This is a about message that you can modify`'
    else:
        return choice9(['what?', 'i cannot understand', 'i dont know' ,'i dont understand' , 'actually i am not good at all' , 'please ask better questions next time'])