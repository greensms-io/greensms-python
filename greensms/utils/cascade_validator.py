def cascade_validator(field, value, error):
    if not value or len(value) == 0:
        return

    split_arr = value.split(",")

    for cascade_str in split_arr:
        if cascade_str.lower() not in ['viber', 'sms', 'voice']:
            error(field, "Must be comma separated-value of voice, sms, voice")
