def read_data(fileobject):
    """Reads 4 consecutive lines of the patient data file and returns
    data to be used in constructing a patient dictionary.

    Args:
        fileobject (I/O object): I/O object with test_data.txt file open.

    Returns:
        string: patient firstname
        string: patient lastname
        int: patient age (in years)
        string: patient gender
        list: list of patient tsh values (ordered)
    """

    lines = []
    for _ in range(4):
        lines.append(fileobject.readline())
    firstname, lastname = get_names(lines[0])
    age = int(lines[1])
    gender = lines[2].rstrip()
    tsh = get_tsh_list(lines[3])
    return firstname, lastname, age, gender, tsh


def get_names(namestring):
    """Generate firstname and lastname as separate strings.

    Args:
        namestring (string): String of form "FirstName LastName"

    Returns:
        string: Patient firstname.
        string: Patient lastname.
    """

    names = namestring.split()
    return names[0], names[1]


def get_tsh_list(tshstring):
    """Generates ordered list of tsh values from string of
    text in test_data.txt.

    Args:
        tshstring (string): Line from test_data of form "TSH,value1,value2,..."

    Returns:
        list: Ordered low to high list of tsh values.
    """

    lst = tshstring.split(',')
    tsh_list = [float(i) for i in lst[1:]]
    tsh_list.sort()
    return tsh_list
