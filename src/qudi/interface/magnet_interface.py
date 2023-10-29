"""
Simple implementation of a magnet interface
"""

from abc import abstractmethod
from qudi.core.module import Base
from typing import Iterable, Mapping, Union, Optional, Tuple, Type, Dict

class MagnetConstraints:
    """ Data object holding the constraints for magnet control.
    """
    def __init__(self,
                 control_units: Optional[Mapping[str, str]] = None,
                 confirm_moves = None,
                 save_feedback_vals = None
                 ) -> None:
        """
        """

class ParameterFieldModel:
    """ Data object holding the parametrization of the magnet field.
    """
    def __init__(self) -> None:
        """
        """

    @property
    def control_param_to_field() -> None:
        """
        """

    @property
    def field_to_control_params({Bx:0, By:0, Bz:0}) -> None:
        """
        """

    @property
    def calibrate_model() -> None:
        """
        """

class MagnetInterface(Base):
    """ Abstract base class for all interfaces in this module
    """

    @property
    @abstractmethod
    def get_constraints(self) -> MagnetConstraints:
        """ Retrieve the hardware constrains from the magnet driving device.

                @return dict: dict with constraints for the magnet hardware. These
                              constraints will be passed via the logic to the GUI so
                              that proper display elements with boundary conditions
                              could be made.
        """
        pass

    @property
    @abstractmethod
    def get_model(self) -> ParameterFieldModel:
        """ Retrieve the model for a magnetic field parametrization.
        """
        pass

    @abstractmethod
    def get_status(self, param_list=None):
        """ Get the status of the magnet

        @param list param_list: optional, if a specific status of an axis
                                is desired, then the labels of the needed
                                axis should be passed in the param_list.
                                If nothing is passed, then from each axis the
                                status is asked.

        @return dict: with the axis label as key and the status number as item.
        """
        pass

    @abstractmethod
    def set_control(self, x:0, y:0, z:0, blocking=False):
        """ Sets magnet control in x,y,z

        @param dict param_dict: dictionary, which passes all the relevant
                                parameters, which should be changed. Usage:
                                 {'axis_label': <the-abs-pos-value>}.
                                 'axis_label' must correspond to a label given
                                 to one of the axis.

        @return int: error code (0:OK, -1:error)
        """
        pass

    @abstractmethod
    def get_control(self):
        """ Gets current control values of the magnet control

        @param list param_list: optional, if a specific position of an axis
                                is desired, then the labels of the needed
                                axis should be passed in the param_list.
                                If nothing is passed, then from each axis the
                                position is asked.

        @return dict: with keys being the axis labels and item the current
                      position.
        """
        pass

    def set_field(self, Bx:0, By:0, Bz:0, blocking=False):
        """ Sets Bfield in x,y,z

        @param dict param_dict: dictionary, which passes all the relevant
                                parameters, which should be changed. Usage:
                                 {'axis_label': <the-abs-pos-value>}.
                                 'axis_label' must correspond to a label given
                                 to one of the axis.

        @return int: error code (0:OK, -1:error)
        """
        pass

    @abstractmethod
    def get_field(self):
        """ Gets current Bfield components

        @param list param_list: optional, if a specific position of an axis
                                is desired, then the labels of the needed
                                axis should be passed in the param_list.
                                If nothing is passed, then from each axis the
                                position is asked.

        @return dict: with keys being the axis labels and item the current
                      position.
        """
        pass

    @abstractmethod
    def go_to_idle(self):
        """ goes to idle
        """
        pass

    @abstractmethod
    def stop(self):
        """ Stops magnet control

        @return int: error code (0:OK, -1:error)
        """
        pass

class ACurrentMagnet(MagnetInterface):

    @abstractmethod
    def set_ramp(self) -> None:
        """
        """
        pass

    @abstractmethod
    def coord_transform(self) -> None:
        """
        """
        pass


class AMotorMagnet(MagnetInterface):

    @abstractmethod
    def set_velocity(self) -> None:
        """
        """
        pass