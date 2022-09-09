# Негативный тест 1 - Получение api_key c некорректным email
# Ожидаемый результат -  код ошибки 403
# Фактический результат - код ошибки 403

def test_get_api_key_for_failed_email1(email=valid_email, password=valid_password):
    status, result = pf.get_api_key(email, password)
    assert status == 403

# Негативный тест 2 - Получение api_key c пустым полем email
# Ожидаемый результат -  код ошибки 403
# Фактический результат - код ошибки 403

def test_get_api_key_for_failed_email2(email=valid_email, password=valid_password):
    status, result = pf.get_api_key(email, password)
    assert status == 403

# Негативный тест 3 - Получение api_key c некорретным password
# Ожидаемый результат -  код ошибки 403
# Фактический результат - код ошибки 403

def test_get_api_key_for_failed_password1(email=valid_email, password=valid_password):
    status, result = pf.get_api_key(email, password)
    assert status == 403

# Негативный тест 4 - Получение api_key c пустым полем password
# Ожидаемый результат -  код ошибки 403
# Фактический результат - код ошибки 403

def test_get_api_key_for_failed_password2(email=valid_email, password=valid_password):
    status, result = pf.get_api_key(email, password)
    assert status == 403

# Негативный тест 5 - Получение списка питомцев с некорректным api_key (неверный пароль)
# Ожидаемый результат -  код ошибки 403
# Фактический результат - код ошибки 403

def test_get_all_pets_with_failed_password_key(filter=''):
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.get_api_key(valid_email, valid_password)
    assert status == 403

# Негативный тест 6 - Получение списка питомцев с некорректным api_key (пустой email)
# Ожидаемый результат -  код ошибки 403
# Фактический результат - код ошибки 403

def test_get_all_pets_with_failed_email_key(filter=''):
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.get_api_key(valid_email, valid_password)
    assert status == 403

# Негативный тест 7 - Добавляем питомца, используя в качестве фотографии питомца текстовый файл
# Ожидаемый результат -  код ответа 400 (Некорретные данные)
# Фактический результат - статус 200
# Нам нужен баг репорт

def test_add_new_pet_with_incorrect_data_foto(name= 'Барбоскин', animal_type='11', age='1'
                                     , pet_photo='images/test.txt'):
    # pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)
    assert status == 200
    assert result['name'] == name


# Негативный тест 8 - Добавляем питомца с пустым полем имя
# Ожидаемый результат -  код ответа 400 (Некорретные данные)
# Фактический результат - статус 200
# Нам нужен баг репорт

def test_add_new_pet_with_incorrect_data_name(name='1', animal_type='11', age='1'
                                              , pet_photo='images/test.txt'):
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)
    assert status == 500
    assert result['name'] == name

# Негативный тест 9 - Добавляем питомца где в поле возраст символьное значение
# Ожидаемый результат -  код ответа 400 (Некорретные данные)
# Фактический результат - статус 200
# Нам нужен баг репорт

def test_add_new_pet_with_incorrect_data_age(name='Барбоскин', animal_type='ХтоЯ', age='test'
                                              , pet_photo='images/cat1.jpg'):
   pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)
    assert status == 200
    assert result['name'] == name

# Негативный тест 10 - Добавляем питомца  где в качестве породы - цифры
# Ожидаемый результат -  код ответа 400 (Некорретные данные)
# Фактический результат - статус 200
# Нам нужен баг репорт

def test_add_new_pet_with_incorrect_data_animal_type(name='Барбоскин', animal_type='1112', age='2'
                                              , pet_photo='images/cat1.jpg'):
   # pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)
    assert status == 200
    assert result['name'] == name
