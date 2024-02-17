"""Support for controlling a Tuya IR AC device."""
import logging
import requests
import json
from homeassistant.const import (
    ATTR_ENTITY_ID,
    SERVICE_TURN_ON,
    SERVICE_TURN_OFF
)
from homeassistant.helpers import config_validation as cv
from homeassistant.helpers.entity import ToggleEntity

_LOGGER = logging.getLogger(__name__)

DOMAIN = "tuya_ir_ac"

SERVICE_SEND_COMMAND = "send_command"

ATTR_COMMAND = "command"

COMMAND_SCHEMA = cv.string

TUYA_API_ENDPOINT = "https://openapi.tuyain.com/v2.0/infrareds/{d79634ca31ef0ae8807vlh}/air-conditioners/{d7af1190782799d1a6fu9u}/scenes/command"

def setup(hass, config):
    """Set up the Tuya IR AC platform."""
    hass.services.register(DOMAIN, SERVICE_SEND_COMMAND, lambda service: handle_send_command(hass, service))

    return True

def handle_send_command(hass, service):
    """Handle sending commands."""
    entity_id = service.data.get(ATTR_ENTITY_ID)
    command = service.data.get(ATTR_COMMAND)

    if entity_id:
        entity = hass.states.get(entity_id)
        if entity:
            device_id = entity.attributes.get("device_id")
            if command:
                send_tuya_command(hass, device_id, command)
            else:
                _LOGGER.error("No command provided for entity %s", entity_id)
        else:
            _LOGGER.error("Entity not found: %s", entity_id)
    else:
        _LOGGER.error("No entity_id provided for command")

def send_tuya_command(hass, device_id, command):
    """Send command to Tuya device."""
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer d68c08a3d309eb136dc2b965c4e61fd5"  # Replace with your Tuya API access token
    }

    data = {
        "commands": [{
            "code": command,
            "value": True
        }]
    }

    response = requests.post(TUYA_API_ENDPOINT.format(device_id), headers=headers, data=json.dumps(data))

    if response.status_code == 200:
        _LOGGER.info("Command sent successfully")
    else:
        _LOGGER.error("Failed to send command. Error: %s", response.text)
