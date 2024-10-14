def total_salary(path) -> tuple:
    total_salary = 0
    average_salary = 0
    employee_data = []

    try:
        with open(path, 'r', encoding='utf-8') as fh:
            lines = [line.strip() for line in fh.readlines()]
        
        for line in lines:
            full_name, salary = line.split(',')
            employee_data.append([full_name.strip(), float(salary)])

        total_salary = sum(employee[1] for employee in employee_data)
        average_salary = sum(employee[1] for employee in employee_data) / len(employee_data) if employee_data else 0
    except FileNotFoundError:
        print(f"File was not found: {path}")
    except ValueError:
        print("Data conversion error. Please check the file format.")
    except Exception as e:
        print(f"An error occurred: {e}")
    
    return (total_salary, average_salary)

total, average = total_salary("salary_data.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")