import xml.etree.cElementTree as ET
import sys


def main():
    tree = ET.parse('data.xml')
    root = tree.getroot()

    # employee1 = root[0]
    # employee1.set('Money', '10000')

    # root.remove(employee1)
    # ET.dump(root)

    # events = ['start', 'end']
    # for event, elem in ET.iterparse('data.xml', events=events):
    #     # ET.dump(elem)
    #     if elem.tag == 'EmployeeID' and event == 'end':
    #         print(elem.text)

    # for child in root:
    #     print(child.tag, child.attrib)

    # print(root[0][0].text)
    # print(root.findall('Employee'))

    # XPath
    # print(tree.findall('Employee/Department'))
    #
    # print(tree.findall('Employee[Department="Sales"]'))
    #
    # print(tree.find('Employee[@Money="10000"]'))
    #
    # print(tree.findall('Employee[Department="Sales"]/EmployeeName'))

    print(sys.getsizeof(ET.iterparse('data.xml')))
    print(sys.getsizeof(tree.getroot()))
    print(sys.getsizeof(ET.parse('data.xml')))


if __name__ == '__main__':
    main()
