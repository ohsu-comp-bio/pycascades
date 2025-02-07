import requests 
import json
import pandas as pd 

def identifiers(ids='EGF,EGFR', interactors=False, page_size='1', page='1', species='Homo Sapiens',
                sort_by='ENTITIES_FDR', order='ASC', resource='TOTAL', p_value='1', include_disease=True,
                min_entities=None, max_entities=None, projection=False, importable_only=False):
    """
    Given a list of protein, gene, or small molecule identifiers conducts reactome pathway enrichment analysis.

    :param ids: comma seperated list of proteins, genes or small molecules identifiers symbol in string format ex. 'EGF,EGFR'
    :param interactors: boolean value indicating include interations
    :param page_size: page size
    :param page: number of pages
    :param species: list of species to filter the result (accepts taxonomy ids, species names and dbId)
    :param sort_by: how to sort the result. Available filters: TOTAL_ENTITIES, TOTAL_REACTIONS, TOTAL_INTERACTIONS,
        FOUND_ENTITIES, FOUND_INTERACTIONS, FOUND_REACTIONS, ENTITIES_RATIO, ENTITIES_PVALUE, ENTITIES_FDR, REACTIONS_RATIO
    :param order: order ASC or DESC
    :param resource: the resource to sort TOTAL, UNIPORT, ENSEMBLE, CHEMBI, IUPHAR, MIRBASE, NCBI_PROTEIN, EMBL, COMPOUND, PUBCEM_COMPOUND
    :param p_value: defines the pValue threshold. Only hit pathway with pValue equals or below the threshold will be returned
    :param include_disease: set to ‘false’ to exclude the disease pathways from the result (it does not alter the statistics)
    :param projection: if true, projects the identifiers to human and only shows the result in this species
    :param max_entities: maximum number of contained entities per pathway (takes into account the resource)
    :param min_entities: minimum number of contained entities per pathway (takes into account the resource)
    :return: Json dictionary object
    """
    if isinstance(page_size, NumberTypes):
        page_size = str(page_size)

    if isinstance(page, NumberTypes):
        page = str(page)

    if isinstance(p_value, NumberTypes):
        p_value = str(p_value)

    if isinstance(min_entities, NumberTypes):
        min_entities = str(min_entities)

    if isinstance(max_entities, NumberTypes):
        max_entities = str(max_entities)

    if interactors:
        interactors = 'true'
    else:
        interactors = 'false'

    if include_disease:
        include_disease = 'true'
    else:
        include_disease = 'false'

    headers = {
        'accept': 'application/json',
        'content-type': 'text/plain',
    }

    params = (
        ('interactors', interactors),
        ('pageSize', page_size),
        ('page', page),
        ('sortBy', sort_by),
        ('order', order),
        ('species',  species),
        ('resource', resource),
        ('pValue', p_value),
        ('includeDisease', include_disease),
        ('min', min_entities),
        ('max', max_entities),
        ('importableOnly', importable_only)
    )

    if projection:
        url = 'https://reactome.org/AnalysisService/identifiers/projection'
    else:
        url = 'https://reactome.org/AnalysisService/identifiers/'

    data = ids

    try:
        response = requests.post(url=url, headers=headers, params=params, data=data)
    except ConnectionError as e:
        print(e)

    if response.status_code == 200:
        return response.json()
    else:
        print('Status code returned a value of %s' % response.status_code)

def token(token, species='Homo sapiens', page_size='1', page='1', sort_by='ENTITIES_FDR', order='ASC', resource='TOTAL',
          p_value='1', include_disease=True, min_entities=None, max_entities=None):
    """
    Returns the result associated with token.
    Use page and pageSize to reduce the amount of data retrieved. Use sortBy and order to sort the result by your preferred option.
    The resource field will filter the results to show only those corresponding to the preferred molecule type (TOTAL includes all the different molecules type)

    :param token: The token associated with the data result - analysis Web-Service is token based, so for every analysis
        request a TOKEN is associated to the result
    :param species: List of species to filter the result (accepts taxonomy ids, species names and reactome dbId)
    :param page_size: Page size
    :param page: Page number
    :param sort_by: How to sort the result. Available filters: TOTAL_ENTITIES, TOTAL_REACTIONS, TOTAL_INTERACTIONS,
        FOUND_ENTITIES, FOUND_INTERACTIONS, FOUND_REACTIONS, ENTITIES_RATIO, ENTITIES_PVALUE, ENTITIES_FDR, REACTIONS_RATIO
    :param order: Order ASC or DESC
    :param resource: The resource to sort TOTAL, UNIPORT, ENSEMBLE, CHEMBI, IUPHAR, MIRBASE, NCBI_PROTEIN, EMBL, COMPOUND, PUBCEM_COMPOUND
    :param p_value: Defines the pValue threshold. Only hit pathway with pValue equals or below the threshold will be returned
    :param include_disease: Set to ‘false’ to exclude the disease pathways from the result (it does not alter the statistics)
    :param min_entities: Minimum number of contained entities per pathway (takes into account the resource)
    :param max_entities: Maximum number of contained entities per pathway (takes into account the resource)
    :return: Json dictionary object
    """
    if isinstance(page_size, NumberTypes):
        page_size = str(page_size)

    if isinstance(page, NumberTypes):
        page = str(page)

    if isinstance(p_value, NumberTypes):
        p_value = str(p_value)

    if isinstance(min_entities, NumberTypes):
        min_entities = str(min_entities)

    if isinstance(max_entities, NumberTypes):
        max_entities = str(max_entities)

    if include_disease:
        include_disease = 'true'
    else:
        include_disease = 'false'

    headers = {
        'accept': 'application/json',
    }

    params = (
        ('pageSize', page_size),
        ('page', page),
        ('sortBy', sort_by),
        ('order', order),
        ('species',  species),
        ('resource', resource),
        ('pValue', p_value),
        ('includeDisease', include_disease),
        ('min', min_entities),
        ('max', max_entities),
    )

    url = 'https://reactome.org/AnalysisService/token/%s' % token

    try:
        response = requests.get(url=url, headers=headers, params=params)
    except ConnectionError as e:
        print(e)

    if response.status_code == 200:
        return response.json()
    else:
        print('Status code returned a value of %s' % response.status_code)


NumberTypes = (int, float, complex)
