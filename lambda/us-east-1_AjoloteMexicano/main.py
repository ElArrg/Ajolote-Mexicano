# -*- coding: utf-8 -*-
import random
import logging

from ask_sdk_core.skill_builder import SkillBuilder
from ask_sdk_core.utils import is_request_type, is_intent_name
from ask_sdk_core.handler_input import HandlerInput

from ask_sdk_model.ui import SimpleCard
from ask_sdk_model import Response

skill = SkillBuilder()

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

SKILL_NAME = "Ajolote Mexicano"
HELP_MESSAGE = "Puedes pedirme un dato sobre el Ajolote Mexicano."
datos = [
    "Los ajolotes o axolotes son anfibios endémicos de México.",
    "Los anfibios generalmente pasan del estado larvario a la adultez. Pero el axolote permanece en su forma larvaria durante toda su vida. Si creciera hasta la edad adulta, el ajolote se vería igual que su pariente más cercano, la salamandra mexicana.",
    "Los ajolotes pertenecen a la familia de los ambistomátidos o tilapias tigre que provienen de México.",
    "Las salamandras viven en la tierra, pero los ajolotes son completamente acuáticos. Tienen pulmones, pero respiran a través de sus branquias y de su piel.",
    "El axolote sólo necesita ser alimentado cada dos o tres días.",
    "Se alimenta de renacuajos, insectos blandos, gusanos e incluso pequeños peces, pero también puede ser alimentados con pequeñas porciones de carne cruda.",
    "Dos especies distintas son conocidas como axolotes, Ambystoma mexicanum y Ambystoma bombypellum.",
    "Un acuario de ajolotes debe tener agua por lo menos a unos 15 a 20 cm de profundidad y entre 14 a 20 grados centígrados. No se recomienda colocar otros peces en el mismo tanque.",
    "Los axolotes son famosos por sus habilidades de regenerar casi cualquier parte de su cuerpo, desde las extremidades, hasta órganos como el corazón, el hígado y pulmones.",
    "Los colores más comunes de los ajolotes son el gris y el marrón, pero también hay albinos dorados, albinos blancos, negros y algunas variedades con manchas.",
    "El ajolote puede llegar a crecer unos 20 a 40 cm de largo y vivir unos 10 a 15 años.",
    "A los 12 meses, un ajolote está listo para aparearse.",
    "El proceso de apareamiento del ajolote, es fuertemente influenciado por la temperatura del agua.",
    "Una hembra puede poner entre 300 y 1000 huevecillos por apareamiento, estos huevecillos son gelatinosos y translúcidos.",
    "Está especie está en peligro crítico de extinción debido a la caza ilegal y a la contaminación de su habitat.",
    "El ajolote habita en Xochimilco"
    ]


@skill.request_handler(can_handle_func = is_request_type("LaunchRequest"))
def launch_request_handler(handler_input):
    speech_text = "¡Bienvenido!, es bueno que quieras saber más de este fantástico animal." + ' ' + HELP_MESSAGE

    return handler_input.response_builder.speak(speech_text).set_card(
        SimpleCard(SKILL_NAME, speech_text)).set_should_end_session(False).response


@skill.request_handler(can_handle_func = is_intent_name("DatoCuriosoIntent"))
def dato_curioso_intent_handler(handler_input):
    speech_text = random.choice(datos)
    
    return handler_input.response_builder.speak(speech_text).set_card(
                SimpleCard(SKILL_NAME, speech_text)).response


@skill.request_handler(can_handle_func=is_intent_name("AMAZON.HelpIntent"))
def help_intent_handler(handler_input):

    return handler_input.response_builder.speak(HELP_MESSAGE).ask(
        HELP_MESSAGE).set_card(SimpleCard(SKILL_NAME, HELP_MESSAGE)).response


@skill.request_handler(
    can_handle_func=lambda handler_input:
        is_intent_name("AMAZON.CancelIntent")(handler_input) or
        is_intent_name("AMAZON.StopIntent")(handler_input))
def cancel_and_stop_intent_handler(handler_input):
    speech_text = "Adiós"

    return handler_input.response_builder.speak(speech_text).set_card(
        SimpleCard(SKILL_NAME, speech_text)).response


@skill.request_handler(can_handle_func=is_request_type("SessionEndedRequest"))
def session_ended_request_handler(handler_input):

    return handler_input.response_builder.response


@skill.exception_handler(can_handle_func=lambda i, e: True)
def all_exception_handler(handler_input, exception):
    logger.error(exception, exc_info=True)

    speech = "<say-as interpret-as='interjection'>achís achís, no sé que pasó</say-as>"
    handler_input.response_builder.speak(speech)

    return handler_input.response_builder.response


lambda_handler = skill.lambda_handler()