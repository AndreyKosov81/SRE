# diagram.py

# run pipenv shell

from diagrams  import Diagram
from diagrams.aws.compute import EC2
with Diagram (" SRE ", show=False ):
 EC2("Производственные операции") >> EC2("Начало производства") >> EC2("Тестирование") >> EC2("Разработка")
