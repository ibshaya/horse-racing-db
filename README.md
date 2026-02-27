# Horse Racing Database System

A comprehensive database management system for horse racing operations, featuring a GUI application for managing races, horses, owners, and stables.

## Project Overview

This project provides a complete solution for managing horse racing data with both administrative and guest access levels. It includes a MySQL database backend, Python GUI application, and SQL procedures for efficient data management.

## Features

- **Admin Panel**: Full access to manage races, horses, owners, and stables
- **Guest Panel**: Read-only access to view racing information
- **Database Management**: MySQL database with normalized schema
- **User-Friendly GUI**: Built with Tkinter for easy interaction
- **Stored Procedures**: SQL functions for common operations
- **Secure Access**: Role-based access control (Admin/Guest)

## Project Structure

```
HorseRacingDB/
├── horse_racing_gui.py      # Main GUI application with Tkinter
├── db_connection.py          # Database connection module
├── ddl_dml.sql               # Database schema and initialization
├── admin_functions.sql       # Admin-level stored procedures
├── guest_functions.sql       # Guest-level stored procedures
└── README.md                 # This file
```

## Technology Stack

- **Backend**: Python 3.x
- **GUI**: Tkinter
- **Database**: MySQL


## Prerequisites

- Python 3.x installed
- MySQL Server running
- mysql-connector-python library


## Usage

Run the application:
```bash
python horse_racing_gui.py
```

### Welcome Screen
- Click **Admin** to access admin features
- Click **Guest** to access guest features

### Admin Functions
- Add new races and results
- Manage horses and owners
- Manage stables
- View detailed racing statistics

### Guest Functions
- View available races
- View horse information
- View race results and statistics

## Database Schema

### Main Tables
- **Stable**: Store stable information (ID, name, location, colors)
- **Horse**: Horse details (ID, name, age, gender, registration, stable reference)
- **Owner**: Owner information (ID, first name, last name)
- **Owns**: Junction table for owner-horse relationships
- **Race**: Race information (ID, name, track, date, time)
- **Results**: Race results (race ID, horse ID, placement, prize money)

## File Descriptions

- **horse_racing_gui.py**: Main GUI application using Tkinter framework with admin and guest panels
- **db_connection.py**: Handles MySQL database connections
- **ddl_dml.sql**: Contains CREATE TABLE statements and initial data
- **admin_functions.sql**: Admin-level stored procedures and functions
- **guest_functions.sql**: Guest-level read-only procedures and views

### By Ibrahim Alshayea

