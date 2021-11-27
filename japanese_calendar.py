from ask_sdk_core.skill_builder import SkillBuilder
from ask_sdk_core.dispatch_components import AbstractRequestHandler
from ask_sdk_core.dispatch_components import AbstractExceptionHandler
from ask_sdk_core.utils import is_request_type, is_intent_name

class LaunchRequestHandler(AbstractRequestHandler):
    
    def can_handle(self, handler_input) :
        return is_request_type("LaunchRequest")(handler_input)
    
    def handle(self, handler_input) :
        handler_input.response_builder.speak("welcome to the game of the Japanese zodiac, in this ability you will know your animal according to the Japanese calendar and you will know the personality with which that animal is related").set_should_end_session(False)
        return handler_input.response_builder. response


class CatchAllExceptionHandler(AbstractExceptionHandler):
    def can_handle(self, handler_input, exception) :
        return True
    def handle (self, handler_input, exception) :
        print(exception)
        handler_input. response_builder.speak("Ooops there is a problem here,pls try again !")
        return handler_input.response_builder. response




class JapaneseAnimalIntentHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        return is_intent_name("JapaneseAnimalIntent")(handler_input)

def handle(self, handler_input) :
    year = handler_input.request_envelope.request.intent. slots['year'].value
    speech_text="My custom Intent handler"
    handler_input.response_builder.speak(speech_text).set_should_end_session(False)
    return handler_input.response_builder.response



sb = SkillBuilder()
sb.add_request_handler(LaunchRequestHandler())
sb.add_exception_handler(CatchAllExceptionHandler())
sb.add_request_handler(JapaneseAnimalIntentHandler())

def handler (event, context):
    return sb. lambda_handler() (event, context)

        
def handler(event, context):

    
    return {"message": "Successfully executed"}
