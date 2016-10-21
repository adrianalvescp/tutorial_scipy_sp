
# lista_encontros.py 
def encontro_scipy_sp(id=4, date="21/10/2016", presentes="Mauricio Vieira"):
    print("SciPy-SP #{id}: {date}, apresentado por {presentes}".format(
        id=id, 
        date=date, 
        presentes=presentes
        )
    )

encontro_scipy_sp(id=1, date="19/09/2016",presentes="Vinícius")
encontro_scipy_sp()
