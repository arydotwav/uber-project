# Uber-like Console Application

This is a console-based application simulating a simplified Uber-like service. It allows users to interact with the system as either passengers or drivers, facilitating basic trip requests, confirmations, and user management.

## Team Members

*   Agustin Scklink
*   Ariana Ruiz
*   Aldana Velazquez
*   Sebastian Di Pietro

## Project Structure

The project is organized into several modules, each responsible for a specific part of the application's functionality:

```
uber_project/
├── auth/
│   ├── __init__.py
│   ├── auth_manager.py   # Handles user authentication (login, registration)
│   └── user.py           # Defines User, Passenger, and Driver classes
├── core/
│   ├── __init__.py
│   ├── controller.py     # Provides an interface for trip options and management
│   ├── trip_manager.py   # Manages trip-related logic (finding drivers/passengers, confirming trips)
│   └── trip_options.py   # Provides trip-related options like addresses and pricing
├── models/
│   ├── __init__.py
│   ├── addresses_list.py # Manages a list of saved addresses
│   └── trip.py           # Defines the Trip class
├── ui/
│   ├── __init__.py
│   ├── calification.py   # Handles trip calification (rating)
│   ├── follow_up.py      # Manages post-trip follow-up (e.g., showing trip info, prompting for calification)
│   └── trip_ui.py        # The main user interface logic for interacting with the system
├── test/
│   ├── __init__.py
│   └── user.py           # Contains test-related user definitions
├── __init__.py           # Makes 'uber_project' a Python package
└── __main__.py           # The main entry point for running the application as a module
```

## Features

*   **User Authentication:** Login and registration for both passengers and drivers.
*   **Role-Based Access:** Different functionalities for passengers (requesting trips) and drivers (accepting trips, showing as active).
*   **Trip Management:** Basic trip confirmation and driver/passenger matching.
*   **Address Management:** Passengers can manage a list of saved addresses.
*   **Trip Calification:** Users can calificate (rate) their trips.

## How to Run

To run this application, navigate to the directory *containing* the `uber_project` folder (e.g., `/home/agustin/Documentos/`) and execute the following command:

```bash
python -m uber_project
```

This command tells Python to run the `uber_project` package as a module, executing the code found in `uber_project/__main__.py`.

---

# Aplicación de Consola Tipo Uber

Esta es una aplicación de consola que simula un servicio simplificado tipo Uber. Permite a los usuarios interactuar con el sistema como pasajeros o conductores, facilitando solicitudes básicas de viajes, confirmaciones y gestión de usuarios.

## Miembros del Equipo

*   Agustin Scklink
*   Ariana Ruiz
*   Aldana Velazquez
*   Sebastian Di Pietro

## Estructura del Proyecto

El proyecto está organizado en varios módulos, cada uno responsable de una parte específica de la funcionalidad de la aplicación:

```
uber_project/
├── auth/
│   ├── __init__.py
│   ├── auth_manager.py   # Maneja la autenticación de usuarios (inicio de sesión, registro)
│   └── user.py           # Define las clases User, Passenger y Driver
├── core/
│   ├── __init__.py
│   ├── controller.py     # Proporciona una interfaz para opciones y gestión de viajes
│   ├── trip_manager.py   # Gestiona la lógica relacionada con los viajes (encontrar conductores/pasajeros, confirmar viajes)
│   └── trip_options.py   # Proporciona opciones relacionadas con los viajes, como direcciones y precios
├── models/
│   ├── __init__.py
│   ├── addresses_list.py # Gestiona una lista de direcciones guardadas
│   └── trip.py           # Define la clase Trip
├── ui/
│   ├── __init__.py
│   ├── calification.py   # Maneja la calificación de viajes
│   ├── follow_up.py      # Gestiona el seguimiento post-viaje (ej., mostrar información del viaje, solicitar calificación)
│   └── trip_ui.py        # La lógica principal de la interfaz de usuario para interactuar con el sistema
├── test/
│   ├── __init__.py
│   └── user.py           # Contiene definiciones de usuario relacionadas con pruebas
├── __init__.py           # Convierte 'uber_project' en un paquete de Python
└── __main__.py           # El punto de entrada principal para ejecutar la aplicación como un módulo
```

## Características

*   **Autenticación de Usuarios:** Inicio de sesión y registro para pasajeros y conductores.
*   **Acceso Basado en Roles:** Diferentes funcionalidades para pasajeros (solicitar viajes) y conductores (aceptar viajes, mostrarse como activos).
*   **Gestión de Viajes:** Confirmación básica de viajes y emparejamiento conductor/pasajero.
*   **Gestión de Direcciones:** Los pasajeros pueden gestionar una lista de direcciones guardadas.
*   **Calificación de Viajes:** Los usuarios pueden calificar sus viajes.

## Cómo Ejecutar

Para ejecutar esta aplicación, navega al directorio que *contiene* la carpeta `uber_project` (por ejemplo, `/home/agustin/Documentos/`) y ejecuta el siguiente comando:

```bash
python -m uber_project
```

Este comando le indica a Python que ejecute el paquete `uber_project` como un módulo, ejecutando el código que se encuentra en `uber_project/__main__.py`.