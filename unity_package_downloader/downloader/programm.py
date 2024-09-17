def prompt_user_for_package():
    # Fragt den Benutzer nach dem Paketnamen
    package = input("Welches Paket möchtest du installieren? (z.B. com.unity.textmeshpro): ")
    
    # Fragt den Benutzer nach dem Installationsort
    location = input("Wo möchtest du das Paket installieren? (cache oder benutzerdefinierter Pfad): ")
    
    return package, location

