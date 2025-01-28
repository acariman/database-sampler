

def create_uri(settings):
    conn_settings = settings["connection"]

    if conn_settings["driver"].strip().lower() == "sqlite":    
        uri = f"sqlite://{conn_settings['file']}"
    else:
        uri = f"{conn_settings['driver']}://" \
            f"{conn_settings['username']}:{conn_settings['password']}" \
            f"@{conn_settings['host']}/{conn_settings['database']}"

    return uri
