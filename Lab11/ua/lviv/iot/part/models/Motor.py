from ua.lviv.iot.part.models.Part import Part
from ua.lviv.iot.part.models.BrandName import BrandName
from ua.lviv.iot.part.models.ProducingCountry import ProducingCountry
from ua.lviv.iot.part.models.PartType import PartType
from ua.lviv.iot.part.models.Type import Type


class Motor(Part):

    def __init__(self,

                 price=0, serial_number="NoSerialNumber", producing_country=ProducingCountry, part_type=PartType,
                 brand_name=BrandName, type=Type.DIESEL

                 ):

        super(Motor, self).__init__(
            price, serial_number, producing_country, part_type, brand_name
       )

        self.type = type
