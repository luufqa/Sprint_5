first_login_button = ".//*[contains(text(), 'Войти в аккаунт')]"
second_login_button = ".//p[contains(text(), 'Личный Кабинет')]"
field_email = ".//input[@name='name']"
field_password = ".//input[@name='Пароль']"
enter_profile_button = ".//*[contains(@class, 'Auth_link__') and text()='Войти']"
enter_profile_button_second = ".//button[contains(text(), 'Войти')]"
get_order_button = ".//*[contains(text(), 'Оформить заказ')]"
register_button = ".//*[contains(@class, 'Auth_link__') and text()='Зарегистрироваться']"
register_button_second = ".//*[contains(@class, 'button_button__33qZ0 button') and text()='Зарегистрироваться']"
restore_button = ".//*[contains(@class, 'Auth_link__') and text()='Восстановить пароль']"
logout_button = ".//button[contains(text(), 'Выход')]"
logo = ".//*[name()='svg' and @viewBox='0 0 290 50']"
constructor_element = ".//p[contains(text(), 'Конструктор')]"
sauces_element = ".//span[contains(text(), 'Соусы')]"
fillings_element = ".//span[contains(text(), 'Начинки')]"
breads_element = ".//span[contains(text(), 'Булки')]"
field_register_login = "//label[contains(text(), 'Имя')]/..//input"
field_register_email = "//label[contains(text(), 'Email')]/..//input"
field_register_password = "//label[contains(text(), 'Пароль')]/..//input"
tooltip_message_user = ".//*[contains(@class, 'input__error text_type_main-default') and text()='Такой пользователь уже существует']"
tooltip_message_pass = ".//*[contains(@class, 'input__error text_type_main-default') and text()='Некорректный пароль']"
sauces_after_click = "//div[contains(@class, 'tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect')]/..//span[text()='Соусы']"
fillings_after_click = "//div[contains(@class, 'tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect')]/..//span[text()='Начинки']"
breads_after_click = "//div[contains(@class, 'tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect')]/..//span[text()='Булки']"