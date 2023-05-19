# Tanto RFC como Clave_IMSS deben ser registro únicos.

# Ejemplo de CURP → TOFB700422MDFRLT09
# BEATRIZ ALEJANDRA TORRES FLORES
# (1 y 2 TOrres) (3 Flores) (4 Beatriz) , Luego la fecha de nacimiento (año 70 mes 04 día 22) 
# Luego sexo (Si es mujer es M o H hombre), Lugar de nacimiento - En el ejemplo, Distrito Federal y La clave RLT que forma parte de su nombre + 
# 09 dígitos aleatorios

class Client:
    def __init__(self, full_name,sur_name,birth_date,gender,birth_place,curp):
        self.full_name = full_name
        self.sur_name = sur_name
        self.birth_date = birth_date
        self.gender = gender
        self.birth_place = birth_place
        self.curp = curp

me = Client("Gian Marco", "Marelli Mesaglio", "23/11/1995", "H", "Capital Federal", "MAMG951123HCKLF10")

def firstLetterFirstSurNameExtractor(client):
    sur_name_splitter = client.sur_name.split(" ")
    first_sur_name = sur_name_splitter[0]
    sur_name_splitter = list(first_sur_name)
    first_letter = sur_name_splitter[0]
    return first_letter.upper()

def secondLetterFirstSurNameExtractor(client):
    sur_name_splitter = client.sur_name.split(" ")
    first_sur_name = sur_name_splitter[0]
    sur_name_splitter = list(first_sur_name)
    second_letter = sur_name_splitter[1]
    return second_letter.upper()

def firstLetterSecondSurnNameExtractor(client):
    sur_name_splitter = client.sur_name.split(" ")
    second_sur_name = sur_name_splitter[1]
    sur_name_splitter = list(second_sur_name)
    first_letter = sur_name_splitter[0]
    return first_letter.upper()

def firstLetterFirstNameExtractor(client):
    first_name = list(client.full_name)
    first_letter = first_name[0]
    return first_letter.upper()

def lastNumberYearExtractor(client):
    birth_splitter = client.birth_date.split("/")
    year = birth_splitter[2]
    year_splitter = list(year)
    last_number = year_splitter[3]
    return last_number
    
def thirdNumberYearExtractor(client):
    birth_splitter = client.birth_date.split("/")
    year = birth_splitter[2]
    year_splitter = list(year)
    third_number = year_splitter[2]
    return third_number

def lastNumberMonthExtractor(client):
    birth_splitter = client.birth_date.split("/")
    month = birth_splitter[1]
    month_splitter = list(month)
    last_number = month_splitter[1]
    return last_number

def firstNumberMonthExtractor(client):
    birth_splitter = client.birth_date.split("/")
    year = birth_splitter[1]
    year_splitter = list(year)
    first_number = year_splitter[0]
    return first_number

def lastNumberDayExtractor(client):
    birth_splitter = client.birth_date.split("/")
    day = birth_splitter[0]
    day_splitter = list(day)
    last_number = day_splitter[1]
    return last_number

def firstNumberDayExtractor(client):
    birth_splitter = client.birth_date.split("/")
    day = birth_splitter[0]
    day_splitter = list(day)
    first_number = day_splitter[0]
    return first_number

def genderExtractor(client):
    gender = client.gender
    return gender.upper()

def birthPlaceExtractor(client):
    birth_place = list(client.birth_place)
    birth_place_letter = birth_place[0]
    return birth_place_letter.upper()

def curpExtractor(client):
    curp_splitter = list(client.curp)
    if (curp_splitter[0] == firstLetterFirstSurNameExtractor(client) and curp_splitter[1] == secondLetterFirstSurNameExtractor(client) 
       and curp_splitter[2] == firstLetterSecondSurnNameExtractor(client) and curp_splitter[3] == firstLetterFirstNameExtractor(client) 
       and curp_splitter[4] == thirdNumberYearExtractor(client) and curp_splitter[5] == lastNumberYearExtractor(client) 
       and curp_splitter[6] == firstNumberMonthExtractor(client) and curp_splitter[7] == lastNumberMonthExtractor(client) and curp_splitter[8] == firstNumberDayExtractor(client)
       and curp_splitter[9] == lastNumberDayExtractor(client) and curp_splitter[10] == genderExtractor(client) and curp_splitter[11] == birthPlaceExtractor(client)):
        print("CURP validado")
    else: print("CUPR INVALIDO")

#vlaidador
curpExtractor(me)

# #primer apellido
# firstLetterFirstSurNameExtractor(me)
# secondLetterFirstSurNameExtractor(me)

# #segundo apellido
# firstLetterSecondSurnNameExtractor(me)

# #nombre
# firstLetterFirstNameExtractor(me)

# #anio
# lastNumberYearExtractor(me)
# thirdNumberYearExtractor(me)

# #mes
# lastNumberMonthExtractor(me)
# firstNumberMonthExtractor(me)

# #dias
# lastNumberDayExtractor(me)
# firstNumberDayExtractor(me)

# #sexo
# genderExtractor(me)

# #donde nacio
# birthPlaceExtractor(me)
