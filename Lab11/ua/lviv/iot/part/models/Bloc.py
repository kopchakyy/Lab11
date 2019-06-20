from ua.lviv.iot.part.models.Part import Part
from ua.lviv.iot.part.models.BrandName import BrandName
from ua.lviv.iot.part.models.ProducingCountry import ProducingCountry
from ua.lviv.iot.part.models.PartType import PartType


class Bloc(Part):

    def __init__(self,

                 price=0, serial_number="NoSerialNumber", producing_country=ProducingCountry.CHINA, part_type=PartType.TRANSMISSION,
                 brand_name=BrandName.HONDA, field="NoField"

                 ):

        super(Bloc, self).__init__(
            price, serial_number, producing_country, part_type, brand_name
       )

        self.field = field
