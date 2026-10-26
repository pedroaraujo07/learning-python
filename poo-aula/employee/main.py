from employee import Employee, FulltimeEmployee, HourlyEmployee


# não é possível criar um objeto da classe Employee por ser uma classe abstrata


employee1 = FulltimeEmployee("Carlos", "Romão", 2000, 200)

print(f"\n{employee1.full_name()} \n-Salário Total: R${employee1.compute_salary():.2f} \n-Salário Base: R${employee1.get_base_salary():.2f} \n-Bônus: R${employee1.get_bonus():.2f} \n")


employee2 = FulltimeEmployee("Vinícius", "Gomes", 10000)

print(f"{employee2.get_first_name()} {employee2.get_last_name()} \n-Salário Total: R${employee2.compute_salary():.2f} \n-Salário Base: R${employee2.get_base_salary():.2f} \n-Bônus: R${employee2.get_bonus():.2f} \n")


employee1.set_first_name("Pedro")
employee1.set_last_name("Araújo")
employee1.set_base_salary(15000)
employee1.set_bonus(500)

print(f"{employee1.full_name()} \n-Salário Total: R${employee1.compute_salary():.2f} \n-Salário Base: R${employee1.get_base_salary():.2f} \n-Bônus: R${employee1.get_bonus():.2f} \n")


employee3 = HourlyEmployee("Yan", "Souza", 100, 40)

print(f"{employee3.full_name()} \n-Salário Total: R${employee3.compute_salary():.2f} \n-Horas trabalhadas: {employee3.get_worked_hours()} \n-Valor da Hora: R${employee3.get_value_hour():.2f} \n")

employee4 = HourlyEmployee("Arthur", "Carvalho", 120)

print(f"{employee4.full_name()} \n-Salário Total: R${employee4.compute_salary():.2f} \n-Horas trabalhadas: {employee4.get_worked_hours()} \n-Valor da Hora: R${employee4.get_value_hour():.2f} \n")


employee3.set_worked_hours(110)
employee3.set_value_hour(55)

print(f"{employee3.full_name()} \n-Salário Total: R${employee3.compute_salary():.2f} \n-Horas trabalhadas: {employee3.get_worked_hours()} \n-Valor da Hora: R${employee3.get_value_hour():.2f} \n")

print(f"Total de funcionários: {Employee.get_count()}\n")