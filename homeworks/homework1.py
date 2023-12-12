class Home:
    def new(self, value):
        try:
            int_value = int(value)
            print(f"Введенное значение {int_value} является целым числом.")
        except ValueError:
            print(f"Ошибка: Введенное значение '{value}' не является целым числом.")

home_instance = Home()

home_instance.new(42)

home_instance.new("abc")