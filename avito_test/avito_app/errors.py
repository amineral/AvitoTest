"""
Error codes with explanatios
"""

errors = {
    "code_1" : 
    {
        "error_text" : "QUERY PARAMS ERROR: Check query params", 
        "required_params" : "from=id, to=id, value=integer",
        "optional_params" : "currency=RUB(default)",
        "check_api_info" : "/api/help",
    },
    "code_2" :
    {
        "error_text" : "ID ERROR: Check clients ids", 
        "check_api_info" : "/api/help",
    },
    "code_3" :
    {
        "error_text" : "VALUE PARAM ERROR: You forgot value param or value less or equal 0",
        "check_api_info" : "/api/help",
    },
    "code_4" :
    {
        "error_text" : "CURRENCY ERROR: Wrong currency",
        "avaliable_currencys" : "Check here: https://openexchangerates.org/api/currencies.json",
        "check_api_info" : "/api/help",
    },
    "code_5":
    {
        "error_text": "BALANCE ERROR: Not enough balance"
    },
    "code_6":
    {
        "error_text": "WRONG METHOD: Only POST allowed"
    },
    "code_7":
    {
        "error_text": "SERIALIZER IS NOT VALID: check input data"
    }
}
