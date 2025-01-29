import sender_stand_request
import data

#Pruebas: crear una función que cambiará el contenido del cuerpo de solicitud
def get_kit_body(name):
    current_kit_body = data.kit_body.copy()
    current_kit_body['name'] = name
    return current_kit_body

#Prueba positiva
def positive_assert(kit_body):
    kit_body = get_kit_body(name)
    kit_response = sender_stand_request.post_new_client_kit(kit_body)

    assert kit_response.status_code == 201
    assert kit_response.json()['name'] == name

#Prueba negativa
def negative_assert_code_400(kit_body):
    kit_body = get_kit_body(name)
    kit_response = sender_stand_request.post_new_client_kit(kit_body)

    assert kit_response.status_code == 400

#Recibir el token
def get_new_user_token(kit_body):
    user_body = data.user_body
    response = sender_stand_request.post_create_new_user(user_body)
    return response.json()["authToken"]

#Test 1: El número permitido de caracteres (1):
def test_1_create_kit_1_letter_in_name_get_success_response():
    positive_assert(data.kit_body_name_test1)

def test_2_create_kit_511_letter_in_name_get_success_response():
    positive_assert(data.kit_body_name_test2)

def test_3_create_kit_0_letter_in_name_get_error_response():
    negative_assert(data.kit_body_name_test3)

def test_4_create_kit_512_letter_in_name_get_error_response():
    negative_assert(data.kit_body_name_test4)

def test_5_create_kit_has_special_symbol_in_name_get_success_response():
    positive_assert(data.kit_body_name_test5)

def test_6_create_kit_has_space_in_name_get_success_response():
    positive_assert(data.kit_body_name_test6)

def test_7_create_kit_has_numbers_in_name_get_success_response():
    positive_assert(data.kit_body_name_test7)

def negative_assert_no_kit_name(kit_body):
    response = sender_stand_request.post_new_client_kit(kit_body)
    assert response.status_code == 400
    assert response.json()["code"] == 400
    assert response.json()["message"] == "No se enviaron todos los parámetros requeridos"

def test_9_create_kit_number_type_in_name_get_error_response():
    negative_assert(data.kit_body_name_test9)
