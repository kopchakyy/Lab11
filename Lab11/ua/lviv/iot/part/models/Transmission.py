from ua.lviv.iot.part.models.Part import Part
from ua.lviv.iot.part.models.BrandName import BrandName
from ua.lviv.iot.part.models.ProducingCountry import ProducingCountry
from ua.lviv.iot.part.models.PartType import PartType
from ua.lviv.iot.part.models.TransmissionType import TransmissionType


class Transmission(Part):

    def __init__(self,

                 price=0, serial_number="NoSerialNumber", producing_country=ProducingCountry.CHINA, part_type=PartType.TRANSMISSION,
                 brand_name=BrandName.HONDA, number_of_gears=0, transmissionType=TransmissionType.MECHANICAL

                 ):

        super(Transmission, self).__init__(
            price, serial_number, producing_country, part_type, brand_name
       )

        self.number_of_gears = number_of_gears
        self.transmissionType = transmissionType
