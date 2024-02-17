"""Support for controlling a Tuya IR AC device."""
import logging
from homeassistant.components.climate import ClimateEntity
from homeassistant.const import (
    ATTR_TEMPERATURE,
    TEMP_CELSIUS
)

_LOGGER = logging.getLogger(__name__)

class TuyaIRAC(ClimateEntity):
    """Representation of a Tuya IR AC."""

    def __init__(self, name, device_id):
        """Initialize the AC."""
        self._name = name
        self._device_id = device_id
        self._current_temperature = None
        self._target_temperature = 23
        self._target_temperature_step = 1
        self._operation_mode = "off"
        self._fan_mode = "auto"
        self._supported_features = 0

    @property
    def supported_features(self):
        """Return the supported features."""
        return self._supported_features

    @property
    def name(self):
        """Return the name of the AC."""
        return self._name

    @property
    def unique_id(self):
        """Return a unique ID."""
        return self._device_id

    @property
    def current_temperature(self):
        """Return the current temperature."""
        return self._current_temperature

    @property
    def target_temperature(self):
        """Return the temperature we try to reach."""
        return self._target_temperature

    @property
    def target_temperature_step(self):
        """Return the supported step of target temperature."""
        return self._target_temperature_step

    @property
    def temperature_unit(self):
        """Return the unit of measurement."""
        return TEMP_CELSIUS

    @property
    def hvac_mode(self):
        """Return current operation ie. heat, cool, idle."""
        return self._operation_mode

    @property
    def hvac_modes(self):
        """Return the list of available operation modes."""
        return ["off", "heat", "cool", "auto"]

    @property
    def fan_mode(self):
        """Return the fan setting."""
        return self._fan_mode

    @property
    def fan_modes(self):
        """Return the list of available fan modes."""
        return ["auto", "low", "medium", "high"]

    def set_temperature(self, **kwargs):
        """Set new target temperature."""
        temperature = kwargs.get(ATTR_TEMPERATURE)
        if temperature is not None:
            self._target_temperature = temperature

    def set_hvac_mode(self, hvac_mode):
        """Set new operation mode."""
        self._operation_mode = hvac_mode

    def set_fan_mode(self, fan_mode):
        """Set new fan mode."""
        self._fan_mode = fan_mode

    def turn_on(self):
        """Turn the climate entity on."""
        self.set_hvac_mode("auto")

    def turn_off(self):
        """Turn the climate entity off."""
        self.set_hvac_mode("off")

    def update(self):
        """Get the latest data from the Tuya IR AC device."""
        # Update the state of the climate entity here
