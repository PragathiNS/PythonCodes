import pandas
import pandasql

def select_first_50(filename):
    aadhaar_data = pandas.read_csv(filename)
    aadhaar_data.rename(columns = lambda x:x.replace(' ', '_').lower(), inplace=True)
    query = """select registrar, enrolment_agency from aadhaar_data limit 50"""

    # Executing the SQL command on the pandas dataframe
    aadhaar_solution = pandasql.sqldf(query.lower(), locals())
    return aadhaar_solution

select_first_50("../aadhaar_data.csv")
