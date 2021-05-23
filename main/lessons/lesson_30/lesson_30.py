# Упаковка данных. JSON, XML
import json
import xml.etree.ElementTree as ET


class A:
    def __init__(self):
        self.a = 1
        self.b = 1
        self.c = 1


def main():

    # --- XML ---

    # p = ET.Element('Employees')
    #
    # comment = ET.Comment('Comment 1')
    # p.append(comment)
    #
    # employee1 = ET.SubElement(p, 'Employee')
    # employee1_id = ET.SubElement(employee1, 'EmployeeID')
    # employee1_id.text = '1'
    # employee1_name = ET.SubElement(employee1, 'EmployeeName')
    # employee1_name.text = 'Mr. Smith'
    # employee1_department = ET.SubElement(employee1, 'Department')
    # employee1_department.text = 'Delivery'
    #
    # employee2 = ET.SubElement(p, 'Employee')
    # employee2_id = ET.SubElement(employee2, 'EmployeeID')
    # employee2_id.text = '2'
    # employee2_name = ET.SubElement(employee2, 'EmployeeName')
    # employee2_name.text = 'Mr. Brown'
    # employee2_department = ET.SubElement(employee2, 'Department')
    # employee2_department.text = 'Sales'
    #
    # employee3 = ET.SubElement(p, 'Employee')
    # employee3_id = ET.SubElement(employee3, 'EmployeeID')
    # employee3_id.text = '3'
    # employee3_name = ET.SubElement(employee3, 'EmployeeName')
    # employee3_name.text = 'Mr. Black'
    # employee3_department = ET.SubElement(employee3, 'Department')
    # employee3_department.text = 'Admin'
    #
    # # employee1 = root[0]
    # employee1.set('Money', '10000')
    #
    # ET.dump(p)
    # tree = ET.ElementTree(p)
    # tree.write('data.xml')

    # --- JSON ---

    # data = '{"name": "Vasya", "name": "Sasha"}'
    # print(json.dumps(data))
    #
    # print(json.loads(data))

    data = {
        "Employees": {
            "Employee1": {
                "EmployeeID": 1,
                "EmployeeName": "Sasha",
                "Department": "Sales"
            },
            "Employee2": {
                "EmployeeID": 2,
                "EmployeeName": "Ivan",
                "Department": "Delivery"
            },
            "Employee3": {
                "EmployeeID": 3,
                "EmployeeName": 'Андрей',
                "Department": "IT",
                "Admin": False,
                "Role": ["programmer", "smith"],
                "Additional": None
            },
        }
    }
    print(json.dumps(data))

    with open('json.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

    a = A()
    print(json.dumps(a.__dict__))


if __name__ == '__main__':
    main()
