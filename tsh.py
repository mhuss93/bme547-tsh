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


def get_diagnosis(tshlist):
    """Determines patient's diagnostic status.

    If any values exceed 4.0, this is considered hypothyroidism, If any are
    lower than 1.0, this is hyperthyroidism. Else normal thyroid function.

    Args:
        tshlist (list): List of TSH values

    Returns:
        string: diagnosis
    """

    if tshlist[0] < 1.0:
        return "hyperthyroidism"
    elif tshlist[-1] > 4.0:
        return "hypothyroidism"
    else:
        return "normal thyroid function"


def create_patient_dict(firstname, lastname, age, gender, diagnosis, tsh):
    """Generates a dictionary of patient attributes.

    Args:
        firstname (string): Patient firstname
        lastname (string): Patient lastname
        age (int): Age (years)
        gender (string): Patient gender
        diagnosis (string): Diagnosis based on TSH values
        tsh (list): List of TSH values

    Returns:
        dict: Patient dictionary.
    """

    patient_dict = {
        "First Name": firstname,
        "Last Name": lastname,
        "Age": age,
        "Gender": gender,
        "Diagnosis": diagnosis,
        "TSH": tsh,
    }
    return patient_dict


def write_patient_dict(patient_dict, dirName):
    """Write a patient dictionary to a json file in directory 'dirName'.

    Args:
        patient_dict (dict): Dictionary of patient information.
        dirName (string): Name of directory in which to save json.
    """

    import json

    firstname = patient_dict["First Name"]
    lastname = patient_dict["Last Name"]
    filename = dirName + '/' + firstname + '-' + lastname + '.json'
    with open(filename, 'w') as out:
        json.dump(patient_dict, out)
    return


def create_save_dir(dirName):
    """Creates the directory within the current working directory in which
    the patient profile jsons will be saved.

    Args:
        dirName (string): Name of directory.
    """

    import os
    if not os.path.exists(dirName):
        os.mkdir(dirName)
        print("Directory ", dirName,  " Created ")
    else:
        print("Directory ", dirName,  " already exists")
