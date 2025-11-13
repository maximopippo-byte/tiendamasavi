import pytest

@pytest.mark.marca1(reason="no sirve xd")
def test_prueba():
    assert 2==2

#la marca la busca en el archivo pytest.ini y pone la razon
#en la consola ponemos pytest y nos salen los disntintos test 

@pytest.mark.marca1(reason="no sirve xd")
def test_prueba():
    assert 2==23

@pytest.fixture
def fixture_1():
    print("desde mi fixture")
    yield 3
    #retorna pero nos permite hacer un seguimiento el yield7
    print("desde mi fixture 2")


@pytest.mark.marca1(reason="no sirve xd")
def test_prueba(fixture_1):
    print("desde mi test1")
    variable = fixture_1
    assert variable==2