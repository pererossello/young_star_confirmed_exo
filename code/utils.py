import pyvo
import numpy as np

service = pyvo.dal.TAPService("http://voparis-tap-planeto.obspm.fr/tap")

def get_params(database='exoplanet.epn_core'):

    table_metadata = service.tables[database]
    parameters = {}
    for column in table_metadata.columns:
        parameters[column.name] = column.description

    return parameters
