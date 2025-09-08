def AutocompleteFields(
        AddressForm,
        ConnectionDatabase,
    ) -> None:
    """
    Function for filling the missing 
    fields with queried data using 
    the known data
    """

    DataAddress = {
        'PostalCode': AddressForm.PostalCode.data.strip() if AddressForm.PostalCode.data else '',
        'LocationName': AddressForm.Location.data.strip() if AddressForm.Location.data else '',
        'CityName': AddressForm.City.data.strip() if AddressForm.City.data else '',
        'DistrictName': AddressForm.District.data.strip() if AddressForm.District.data else '',
        'StateName': AddressForm.State.data.strip() if AddressForm.State.data else '',
    }

    if any(DataAddress.values()):
        PartialDataAddress = []
        KnownValuesAddress = []
        for fact_address , value in DataAddress.items():
            if value:
                PartialDataAddress.append(f'{fact_address} = %s')
                KnownValuesAddress.append(value)

        Query = """
        SELECT PostalCode , LocationName , CityName , DistrictName , StateName 
        FROM PostalCodes 
        WHERE """ + ' AND '.join(PartialDataAddress) + ' LIMIT 1'
        QueryResult = ConnectionDatabase(Query,KnownValuesAddress)

        if not AddressForm.PostalCode.data:
            AddressForm.PostalCode.data = QueryResult['PostalCode']
        if not AddressForm.Location.data:
            AddressForm.Location.data = QueryResult['LocationName']
        if not AddressForm.City.data:
            AddressForm.City.data = QueryResult['CityName']
        if not AddressForm.District.data:
            AddressForm.District.data = QueryResult['DistrictName']
        if not AddressForm.State.data:
            AddressForm.State.data = QueryResult['StateName']